"""Independent algebraic and transform checks for gated-diffusion translocations.
Requires Python >=3.9 and SymPy; no external data or network access.
"""
import sympy as S
from math import exp,sqrt,pi,erfc
p,k,a,e,X=S.symbols('p k a e X', positive=True)
I=S.eye(2); one=S.ones(2,1)
P=S.Matrix([[p,1-p],[p,1-p]])
R=S.diag(S.Rational(1,2),1)
b=S.Matrix([S.Rational(1,2),0])
K=lambda h: h*I+(1-h)*P
assert all(S.simplify(v)==0 for v in K(k)*one-one)
assert S.simplify((I-K(k)*R).det()-p*(1-k)/2)==0
assert S.simplify((I-R*K(k)).det()-p*(1-k)/2)==0
g=(I-K(k)*R).inv()*e*one
C=X*one+K(a)*R*g
expected=S.Matrix([
 X+e*(2-p-k-(1-p)*a)/(p*(1-k)),
 X+e*(2-p-k+p*a)/(p*(1-k))])
assert all(S.simplify(C[i]-expected[i])==0 for i in range(2))
assert S.simplify(C[1]-C[0]-e*a/(p*(1-k)))==0
# For gate hitting after each excursion the Markov renewal stationary open weight is p.
assert all(S.simplify(v)==0 for v in P*K(k)-P)
assert all(S.simplify(v)==0 for v in P*b-S.Matrix([[p/2],[p/2]]))
# Row-stochastic matrices and half-normal moment constants.
assert S.simplify(S.sqrt(2)*S.sqrt(2/S.pi)-2/S.sqrt(S.pi))==0
assert S.simplify((p*p/4)*(2-4/S.pi)/(p*p/S.pi)-(S.pi/2-1))==0
import mpmath as mp
mp.mp.dps=75
checks=8
for D,alpha,beta,eps,x in [(1,2,3,0.8,2.1),(2.5,0.4,4.1,1.3,0.2),(0.8,5.1,0.8,0.45,0.47),(1,0.05,0.09,1.7,0.6)]:
    D,alpha,beta,eps,x=map(mp.mpf,(D,alpha,beta,eps,x))
    lam=alpha+beta; pp=beta/lam
    Pi=mp.matrix([[pp,1-pp],[pp,1-pp]])
    Id=mp.eye(2); unity=mp.matrix([1,1]); rr=mp.diag([mp.mpf('.5'),1]); bb=mp.matrix([mp.mpf('.5'),0])
    def kern(dist,s):
        u=mp.exp(-dist*mp.sqrt(s/D))
        v=mp.exp(-dist*mp.sqrt((s+lam)/D))
        return u*Pi+v*(Id-Pi)
    ar=mp.exp(-x*mp.sqrt(lam/D)); kr=mp.exp(-eps*mp.sqrt(lam/D))
    exact=mp.matrix([x/mp.sqrt(D)+eps*(2-pp-kr-(1-pp)*ar)/(pp*(1-kr)*mp.sqrt(D)),
                     x/mp.sqrt(D)+eps*(2-pp-kr+pp*ar)/(pp*(1-kr)*mp.sqrt(D))])
    for z in [mp.mpf(0),mp.mpf('.3'),mp.mpf('.93'),mp.mpf(1)]:
        s=mp.mpf('.61'); M=mp.diag([(1+z)/2,1]); kx=kern(x,s); ke=kern(eps,s)
        sx=(1-mp.exp(-x*mp.sqrt(s/D)))/s
        se=(1-mp.exp(-eps*mp.sqrt(s/D)))/s
        gg=sx*unity+kx*M*mp.inverse(Id-ke*M)*(se*unity)
        if z==1: assert max(abs(gg[i]-1/s) for i in range(2))<mp.mpf('1e-65')
        if z==0:
            phi=kx*(bb+rr*mp.inverse(Id-ke*rr)*ke*bb)
            assert max(abs(gg[i]-(1-phi[i])/s) for i in range(2))<mp.mpf('1e-65')
        checks+=2
    for sval in ['1e-8','1e-12','1e-16']:
        s=mp.mpf(sval);kx=kern(x,s);ke=kern(eps,s)
        phi=kx*(bb+rr*mp.inverse(Id-ke*rr)*ke*bb)
        err=max(abs((1-phi[i])/mp.sqrt(s)-exact[i]) for i in range(2))
        assert err < 2*mp.sqrt(s)*max(1,abs(exact[0]),abs(exact[1]))**3
        checks+=2
print(f'PASS {checks} independent algebra/normalization/small-s checks')
