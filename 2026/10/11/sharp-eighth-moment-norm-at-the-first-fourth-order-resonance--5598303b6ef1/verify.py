from sympy import symbols, Poly, Rational, factor, resultant, subresultants, diff, simplify, nsolve, N, oo
from math import factorial

x,r=symbols('x r', positive=True)
Q=(r**8*x**4+16*r**6*x**4+16*r**6*x**3+36*r**4*x**4+144*r**4*x**3+36*r**4*x**2+16*r**2*x**4+144*r**2*x**3+144*r**2*x**2+16*r**2*x+8*r*x**2+x**4+16*x**3+36*x**2+16*x+1)
D=1+x*(1+r**2)
Phi=Q/D**4
F1=factor(-diff(Phi,x)*D**5/4)
F2=factor(-diff(Phi,r)*D**5/(8*x))
assert Poly(F1,x,r).total_degree() <= 11
assert Poly(F2,x,r).total_degree() <= 11

# Reconstruct the degree-four collision pattern for frequencies 0,1,4.
groups={}
for u0 in range(5):
    for u1 in range(5-u0):
        u2=4-u0-u1
        s=u1+4*u2
        coeff=factorial(4)//(factorial(u0)*factorial(u1)*factorial(u2))
        groups.setdefault(s,[]).append((u0,u1,u2,coeff))
collisions=[v for v in groups.values() if len(v)>1]
assert collisions == [[(0,4,0,1),(3,0,1,4)]]

R=factor(resultant(F1,F2,x))
H=3*r**8+6*r**6+4*r**5+9*r**4+8*r**3+6*r**2+4*r+3
P=Poly(30375*r**21+8100*r**20+294840*r**19+68499*r**18+7884*r**17-60237*r**16-759429*r**15-321336*r**14-325152*r**13+155736*r**12+323484*r**11+248886*r**10+742505*r**9+97182*r**8+20062*r**7-162720*r**6-303994*r**5-36804*r**4-30665*r**3-2709*r**2+90*r+3,r)
assert simplify(R/(18*H*P.as_expr())) == 1
assert P.count_roots(0,oo) == 4
intervals=[(Rational(406,10000),Rational(407,10000)),(Rational(9336,10000),Rational(9337,10000)),(Rational(98759,100000),Rational(98761,100000)),(Rational(11470,10000),Rational(11471,10000))]
assert [P.count_roots(a,b) for a,b in intervals] == [1,1,1,1]

subs=subresultants(F1,F2,x)
L=Poly(subs[-2],x)
Ac=Poly(L.coeff_monomial(x),r)
Bc=Poly(L.coeff_monomial(1),r)
sgn=[]
for a,b in intervals:
    assert Ac.count_roots(a,b)==0 and Bc.count_roots(a,b)==0
    m=(a+b)/2
    av=Ac.eval(m); bv=Bc.eval(m)
    sgn.append(1 if (-bv/av)>0 else -1)
assert sgn == [-1,-1,1,-1]

# Boundary two-frequency value and a strict interior witness.
assert Rational(1,16)*70 == Rational(35,8)
assert Rational(647,81) > Rational(35,8)

sol=nsolve([F1,F2],[x,r],[Rational(988,1000),Rational(988,1000)],tol=1e-50,maxsteps=100,prec=70)
xs,rs=sol
assert Rational(98759,100000) < rs < Rational(98761,100000)
ks8=N(Phi.subs({x:xs,r:rs}),50)
k=N(ks8**Rational(1,8),50)
print('VERIFY_OK collision=1 positive_stationary=1 r=%s x=%s K8pow=%s K=%s' % (N(rs,20),N(xs,20),ks8,k))
