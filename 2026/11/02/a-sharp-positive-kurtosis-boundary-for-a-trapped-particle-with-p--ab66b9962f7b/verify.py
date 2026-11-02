"""Recompute exact stationary moments and the directional-turning phase boundary.

Run: python3 verify.py. All algebraic checks use Python's exact Fractions.
"""
from fractions import Fraction as F
from itertools import product


def moments(kappa, v, alpha, m1, m2, D):
    A, B = alpha*(1-m1), alpha*(1-m2)
    assert kappa>0 and v>0 and alpha>0 and A>0 and B>=0 and D>=0
    # Stationary co-rotating complex-moment generator hierarchy.
    m10 = v/(kappa+A)
    m20 = 2*v*m10/(2*kappa+B)
    m11 = v*m10/kappa
    m21 = v*(2*m11+m20)/(3*kappa+A)
    m22 = v*m21/kappa
    # Independent ordered four-time angular-correlation integration.
    four_integral = (4*v**4/(4*kappa*(3*kappa+A)*(kappa+A))
                     * (2/(2*kappa+B)+4/(2*kappa)))
    # Closed expressions, independently derived from hierarchy.
    sactive = v*v/(kappa*(kappa+A))
    fourthactive = 2*v**4*(3*kappa+B)/(kappa**2*(kappa+A)*(2*kappa+B)*(3*kappa+A))
    assert m11==sactive and m22==fourthactive==four_integral
    sgauss = 2*D/kappa
    s = sactive+sgauss
    fourth = fourthactive+4*sactive*sgauss+2*sgauss*sgauss
    K=fourth/(2*s*s)-1
    Kformula=(kappa*(A-2*B-3*kappa)/((2*kappa+B)*(3*kappa+A))
              *(sactive/s)**2)
    assert K==Kformula
    assert (K>0)==(A>2*B+3*kappa)
    assert (K<0)==(A<2*B+3*kappa)
    assert (K==0)==(A==2*B+3*kappa)
    # Inversion from only one Cartesian position component's moments.
    V2=s/2
    V4=3*fourth/8
    u=V2-D/kappa
    Arec=v*v/(2*kappa*u)-kappa
    Kcart=V4/(3*V2*V2)-1
    Ka=Kcart*(V2/u)**2
    c=(1+Ka)*(3*kappa+Arec)/(kappa+Arec)
    Brec=kappa*(3-2*c)/(c-1)
    assert Arec==A and Brec==B and Kcart==K
    return A,B,K

checks=0
phis=[(F(1),F(1)), (F(1,2),F(-1,2)), (F(0),F(-1)),
      (F(-1,2),F(-1,2)), (F(-1),F(1))]
for (k,v,alpha,D,p,(c1,c2)) in product(
        [F(1,2),F(1),F(7,4)], [F(3,4),F(2)],
        [F(1),F(3),F(8),F(20)], [F(0),F(1,5),F(2)],
        [F(0),F(1,4),F(1,2),F(3,4)], phis):
    A,B,K=moments(k,v,alpha,p*c1,p*c2,D)
    assert 0<=B<=2*alpha and 0<A<=2*alpha
    checks+=1

# Exact mixed pi-turn/uniform reorientation threshold and recovery.
for p,alpha,k in product([F(0),F(1,10),F(1,3),F(1,2),F(3,4),F(9,10)],
                         [F(1),F(3),F(5),F(8),F(20)], [F(1,2),F(1),F(2)]):
    A,B,K=moments(k,F(1),alpha,-p,p,F(1,3))
    assert (K>0)==(p>F(1,3) and alpha*(3*p-1)>3*k)
    assert (A+B)/2==alpha and (A-B)/(A+B)==p
    checks+=1

# A positive and a negative benchmark, independently evaluated.
_,_,kp=moments(F(1),F(1),F(8),-F(3,4),F(3,4),F(0))
_,_,kn=moments(F(1),F(1),F(8),-F(1,10),F(1,10),F(0))
assert kp==F(7,68) and kn<0
checks+=2
print('PASS: %d exact-rational model and inversion cases' % checks)
print('Positive-kurtosis benchmark:', kp, '; negative benchmark:', kn)
