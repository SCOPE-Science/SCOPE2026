#!/usr/bin/env python3
"""Exact checks for the elliptic-fiber discriminant in Suluyer's cubic pencil.
Requires sympy; no external files or network.
"""
import sympy as S
x,y,z,t,a=S.symbols('x y z t a')
A=x-a*y
B=x-y
L=A+t*B
G=S.expand(A*(x*x+y*y)+t*B*(x*x-x*y+y*y))
H=S.Poly(S.expand((L*G).subs(y,1)),x)
alpha,b,c,d,e=H.all_coeffs()
I=S.expand(12*alpha*e-3*b*d+c*c)
J=S.expand(72*alpha*c*e+9*b*c*d-27*alpha*d*d-27*b*b*e-2*c**3)
Q=3*t**4+10*(a+1)*t**3+(59*a*a-70*a+59)*t*t+4*(7*a**3-a*a-a+7)*t+4*(a*a+1)**2
Delta=S.expand(4*I**3-J**2)
print('built polynomials', flush=True)
def eq(u,v):
    assert S.expand(u-v)==0

eq(Delta,-27*(a-1)**2*t**2*(t+1)**2*(t+a)**2*Q)
print('Delta identity',flush=True)
eq(S.discriminant(Q,t),512*(a-1)**4*(a*a-a+1)*(71*a*a-196*a+71)**3)
print('Q discriminant',flush=True)
eq(Q.subs(t,0),4*(a*a+1)**2)
eq(Q.subs(t,-1),(a-2)**2*(4*a*a-12*a+7))
eq(Q.subs(t,-a),(2*a-1)**2*(7*a*a-12*a+4))
eq(I.subs(t,0),(a*a+1)**2)
eq(I.subs(t,-1),(a-2)**2*(a-1)**2)
eq(I.subs(t,-a),(a-1)**2*(2*a-1)**2)
# The discriminant has degree ten in t; its homogeneous degree-twelve extension
# has a zero of order exactly two at [lambda:mu]=[0:1].
assert S.degree(Delta,t)==10
assert S.Poly(I,t).degree()==4 and S.Poly(J,t).degree()==6
assert S.Poly(I,t).LC()==1 and S.Poly(J,t).LC()==-2

# Exact parameter-ideal valuations: reduce coefficients modulo the polynomial
# defining an exceptional a, rather than approximating individual roots.
def reduced(poly, f, T):
    u=S.Poly(S.expand(poly.subs(t,T)),a,domain=S.QQ)
    return u.rem(S.Poly(f,a,domain=S.QQ)).as_expr()
def local_order(poly,f,T):
    for i in range(7):
        if S.expand(reduced(S.diff(poly,t,i),f,T))!=0:
            return i
    raise AssertionError('unexpected high valuation')
def group(f,T,iv,jv,qv,base2):
    assert S.discriminant(f,a)!=0 if S.degree(f,a)>1 else True
    assert local_order(I,f,T)==iv,(f,'I')
    assert local_order(J,f,T)==jv,(f,'J')
    assert local_order(Q,f,T)==qv,(f,'Q')
    # The four fixed factors 0, -1, -a, infinity are always distinct.
    assert (2 if base2 else 0)+qv in (2,3)
    print('case',str(f),'t=',T,'ord(I,J,Q)=',iv,jv,qv,flush=True)

group(a-2,S.Integer(-1),1,2,1,True)                # III
group(2*a-1,-a,1,2,1,True)                        # III
group(a*a+1,S.Integer(0),1,2,1,True)               # III
group(4*a*a-12*a+7,S.Integer(-1),0,0,1,True)      # I_3
group(7*a*a-12*a+4,-a,0,0,1,True)                 # I_3
group(a*a-a+1,(a+1)/3,0,0,2,False)                # I_2
group(71*a*a-196*a+71,-4*(a+1)/13,1,1,2,False) # II

# Generic a=3: Q has four simple roots disjoint from fixed loci and I=0.
assert S.gcd(Q.subs(a,3),S.diff(Q,t).subs(a,3))==1
assert S.gcd(Q.subs(a,3),I.subs(a,3))==1
for tt in (0,-1,-3):
    assert I.subs({a:3,t:tt})!=0

# Base scheme: for a^2-a+1=0, one pair of base points becomes
# infinitesimally near at [a:1:0]; the cubic at t=(a+1)/3 is nodal there.
F=S.expand(G-z*z*L)
f=a*a-a+1
T=(a+1)/3
for P in (F,S.diff(F,x),S.diff(F,y),S.diff(F,z)):
    assert S.expand(S.Poly(S.expand(P.subs({x:a,y:1,z:0,t:T})),a).rem(S.Poly(f,a)).as_expr())==0
for P in (S.diff(F,x,2),S.diff(F,z,2)):
    assert S.expand(S.Poly(S.expand(P.subs({x:a,y:1,z:0,t:T})),a).rem(S.Poly(f,a)).as_expr())!=0

# Distinct exceptional groups, excluding a=0,1; their factors are pairwise coprime.
labels=[a-2,2*a-1,a*a+1,4*a*a-12*a+7,7*a*a-12*a+4,a*a-a+1,71*a*a-196*a+71]
for i,p in enumerate(labels):
    for q in labels[i+1:]:
        assert S.gcd(p,q)==1,(p,q)
print('VERIFY_OK exact discriminant, all exceptional valuations, nodal basepoint')
