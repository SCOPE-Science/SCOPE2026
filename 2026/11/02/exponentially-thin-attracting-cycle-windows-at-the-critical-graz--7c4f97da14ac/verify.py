"""Reproduce algebraic identities and numerical checks for the critical-slope grazing-map theorem.

Requires sympy and mpmath. The proof is analytical; numerical tests are consistency checks.
"""
from fractions import Fraction
import mpmath as mp
import sympy as S

mp.mp.dps = 80
E, g = S.symbols('E g', positive=True)
v = 1/(1+g)
zstar = (1+E)/(1+g+(1-g)*E)
# Exact defining multiplier identity at the threshold.
mstar = S.factor(E-g*(1-E)*zstar/(1-zstar))
assert S.simplify(mstar+1) == 0
# The parameter formula must satisfy both the return-map fixed equation
# and the prescribed derivative -1.
Linv = E+(1-E)*(zstar/v)*((1-v)/(1-zstar))**g
Lseries = S.series(S.log(Linv),E,0,2).removeO()
assert S.simplify(S.diff(Lseries,E).subs(E,0)-4*g/(1+g)) == 0
# S(G)>0 for the limiting fractional power, so the flip is subcritical.
Szero = (1-g**2)/(2*(1-v)**2)
assert S.simplify(Szero-(1-g**2)/(2*(g*v)**2)) == 0
P2=(g-1)*(1+E)/(1-zstar)
P3=-(g-1)*(g-2)*(1+E)/(1-zstar)**2
Scross=S.factor(-P3-S.Rational(3,2)*P2**2)
Sexact=(1-g)*(1+E)*(1+g-3*(1-g)*E)/(2*(1-zstar)**2)
assert S.simplify(Scross-Sexact)==0

checks = 0
for p,q in [(2,1),(3,1),(5,2),(7,3)]:
    gamma=mp.mpf(q)/p
    nu=1/(1+gamma)
    for M in [6,8,12,40]:
        eps=nu**M
        zcrit=(1+eps)/(1+gamma+(1-gamma)*eps)
        Linv=eps+(1-eps)*(zcrit/nu)*((1-nu)/(1-zcrit))**gamma
        lamcrit=Linv**(-1/gamma)
        assert nu**(1/gamma)<lamcrit<1
        def param_mu(lam):
            return (nu**(M-2)*(1-nu)**gamma/(lam**(-gamma)-eps))**(1/(1-gamma))
        def return_map(z,lam):
            return eps*z+nu*(lam**(-gamma)-eps)*((1-z)/(1-nu))**gamma
        def root(lam):
            low,high=nu,mp.mpf(1)
            for _ in range(300):
                mid=(low+high)/2
                if return_map(mid,lam)>mid:low=mid
                else:high=mid
            return (low+high)/2
        for lam in [lamcrit+(1-lamcrit)/4,lamcrit+(1-lamcrit)/2,lamcrit,lamcrit-(lamcrit-nu**(1/gamma))/10]:
            z=root(lam)
            mu=param_mu(lam)
            der=eps-gamma*(1-eps)*z/(1-z)
            assert abs(return_map(z,lam)-z)<mp.mpf('1e-70')
            # A true primitive M-cycle has one nonlinear iterate and M-1 linear ones.
            x=z*mu
            orbit=[]
            for j in range(M):
                orbit.append(x)
                if j==0:
                    assert nu*mu < x < mu
                    x=nu*x+(mu-x)**gamma
                else:
                    assert x>mu
                    x=nu*x
            assert abs(x-z*mu)<mp.mpf('1e-65')
            if lam>lamcrit:
                assert -1<der<1
            elif lam<lamcrit:
                assert der<-1
            else:
                assert abs(der+1)<mp.mpf('1e-65')
            checks+=1
        # The exact boundary-layer asymptotics hold at large M.
        if M==40:
            assert abs((1-lamcrit)/eps-4*nu)<mp.mpf('0.004')
            muplus=param_mu(mp.mpf(1))
            mumin=param_mu(lamcrit)
            coeff=(muplus-mumin)/muplus/eps
            assert abs(coeff-4*gamma*nu/(1-gamma))<mp.mpf('0.015')
print(f'PASS: symbolic multiplier, threshold and Schwarzian identities; {checks} high-precision period checks')
# Representative verification of a local repelling 2M orbit on the stable side.
gamma=mp.mpf(1)/2
nu=1/(1+gamma)
M=8
eps=nu**M
zcrit=(1+eps)/(1+gamma+(1-gamma)*eps)
lamcrit=(eps+(1-eps)*(zcrit/nu)*((1-nu)/(1-zcrit))**gamma)**(-1/gamma)
lam=lamcrit+mp.mpf('0.000001')
P=lambda z: eps*z+nu*(lam**(-gamma)-eps)*((1-z)/(1-nu))**gamma
Pprime=lambda z:eps-gamma*nu*(lam**(-gamma)-eps)/(1-nu)*((1-z)/(1-nu))**(gamma-1)
L=mp.findroot(lambda z:P(P(z))-z,(zcrit-mp.mpf('0.002'),zcrit-mp.mpf('0.001')))
R=P(L)
assert nu<L<R<1
assert abs(P(R)-L)<mp.mpf('1e-60')
assert Pprime(L)*Pprime(R)>1
print('PASS: one repelling doubled-period pair in the strict one-nonlinear-step return cell')
