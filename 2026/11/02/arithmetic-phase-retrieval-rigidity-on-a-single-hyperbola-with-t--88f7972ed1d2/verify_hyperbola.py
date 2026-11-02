"""Exact symbolic sanity checks for hyperbolic conic phase magnitudes.
Requires Python 3 and SymPy. The general proof is algebraic, not an enumeration.
"""
import sympy as S
z = S.Symbol('z')
w = S.Symbol('w', positive=True)
I = S.I

def dickson(k, s):
    d0, d1 = S.Integer(2), z
    if k == 0: return d0
    for j in range(2, k+1):
        d0, d1 = d1, S.expand(z*d1 - s*d0)
    return d1

def check(a,b,m,eps):
    a,b = S.sympify(a),S.sympify(b)
    c=(a+I*b)/2
    d=S.conjugate(c)
    s=S.expand(c*d)
    r=d/c
    assert S.simplify(r**(2*m)-1)==0
    assert all(S.simplify(r**(2*j)-1)!=0 for j in range(1,m))
    assert S.simplify(r**m-eps)==0
    D=dickson(m,s)
    # Dickson polynomial recurrence is an exact Laurent identity.
    Z=c*w+d/w
    U=S.expand(D.subs(z,Z))
    expected=c**m*w**m+d**m/w**m
    assert S.simplify(U-expected)==0
    T=S.expand((-I if eps==-1 else 1)*D)
    V=S.simplify(T.subs(z,Z))
    assert S.simplify(V-S.conjugate(V))==0
    # Nontrivial degree-m pair, checked for every real parameter w.
    P=S.expand(T+I); Q=S.expand(T-I)
    delta=S.simplify(S.expand(P.subs(z,Z)*S.conjugate(P.subs(z,Z))-
                              Q.subs(z,Z)*S.conjugate(Q.subs(z,Z))))
    assert delta==0
    assert S.simplify(P-I*Q)!=0
    return {'m':m,'D_m':str(D),'T':str(T),'tested_w': [str(S.simplify(V.subs(w,v))) for v in [1,2,3]]}

cases=[(1,1,2,-1),(S.sqrt(3),1,3,-1),(1+S.sqrt(2),1,4,-1),(1,S.sqrt(3),3,1)]
for data in cases:
    print('RATIONAL',check(*data))
# Irrational angle sample: r=(1-2i)/(1+2i)=(-3-4i)/5.
# A root of unity in Q(i) must be one of 1,-1,i,-i, which this is not.
r=S.simplify((1-2*I)/(1+2*I))
assert S.simplify(r-(-3-4*I)/5)==0
assert r not in (1,-1,I,-I)
print('IRRATIONAL_SAMPLE',str(r))
# For degree n, parameterizing an |P|^2-|Q|^2 difference gives
# exponents at most +/-2n and after multiplication by w^(2n)
# an ordinary polynomial of degree at most 4n.
for n in range(1,6):
    P=sum((j+1+I*(j%2))*z**j for j in range(n+1))
    Q=sum((2*j+3-I*(j%3))*z**j for j in range(n+1))
    Z=(1+I)*w/2+(1-I)/(2*w)
    F=S.expand(P.subs(z,Z)*S.conjugate(P.subs(z,Z))-
               Q.subs(z,Z)*S.conjugate(Q.subs(z,Z)))
    poly=S.Poly(S.expand(F*w**(2*n)),w)
    assert poly.degree()<=4*n
    assert poly.LC()!=0
    print('SAMPLING_DEGREE',n,poly.degree())
print('ALL_CHECKS_PASS')
