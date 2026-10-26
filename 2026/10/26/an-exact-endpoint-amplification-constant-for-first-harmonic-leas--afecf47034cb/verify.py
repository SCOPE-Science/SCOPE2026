"""Standalone reproducibility checks for the semicircular affine projector.
Run: python verify.py  (requires mpmath; no external data).
These computations supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=75
nchecks=0
def ck(condition, name):
    global nchecks
    assert condition, name
    nchecks+=1
p_lo,p_hi=F(314159,100000),F(314160,100000)
s_lo,s_hi=F(173205,100000),F(173206,100000)
# Rational endpoint inequalities, assuming the standard exact enclosures
# 3.14159 < pi < 3.14160 and 1.73205 < sqrt(3) < 1.73206.
m_lo,m_hi=2/p_hi,2/p_lo
v_lo=F(1,2)-m_hi*m_hi
ck(m_lo>F(5,8),"zero-crossing cut lies above one third")
ck(m_hi*m_hi<F(23,32),"paired-arc dominance at m")
ck(F(25,9)+(m_hi-F(1,3))**2/v_lo<4,"Cauchy bound at one third")
ck(1+(1-m_lo)**2/v_lo<4,"Cauchy bound at one")
# A rational upper bound for the exact integral over [pi/3,5*pi/6].
# Its negativity proves the sharp norm is strictly greater than two.
witness_upper=(p_hi**3+p_lo**2*(1-s_lo)
               -(6+2*s_lo)*p_lo+8*(s_hi-1))
ck(witness_upper<0,"integral witness strictly exceeds two")
pi=mp.pi;m=2/pi;v=mp.mpf('.5')-m*m;D=pi*pi-8
R=2*mp.sqrt(D*D+4*pi*pi)
beta=mp.acos(pi*pi/R)
Lam=1+4*(mp.sqrt(R*R-pi**4)-pi*pi*beta)/(pi*D)
ck(mp.mpf('2.04809')<Lam<mp.mpf('2.04811'),"sharp constant enclosure")
ck(0<beta<pi/2,"nonempty negative arc")
angle=mp.atan(2*pi/D)
root1,root2=pi-angle-beta,pi-angle+beta
ck(0<root1<pi/2<root2<pi,"both roots interior")
def kernel(theta,phi):
    return 1+2*mp.cos(theta)*mp.cos(phi)+(mp.sin(theta)-m)*(mp.sin(phi)-m)/v
ck(abs(kernel(0,root1))<mp.mpf('1e-60'),"first zero")
ck(abs(kernel(0,root2))<mp.mpf('1e-60'),"second zero")
ck(kernel(0,pi/2)<0 and kernel(0,0)>0 and kernel(0,pi)>0,"sign pattern")
# Exact signed split quadrature at the two analytic roots.
integrated=mp.quad(lambda z:kernel(0,z),[0,root1])\
          -mp.quad(lambda z:kernel(0,z),[root1,root2])\
          +mp.quad(lambda z:kernel(0,z),[root2,pi])
ck(abs(integrated/pi-Lam)<mp.mpf('1e-57'),"signed exact integral")
ck(abs(mp.quad(lambda z:kernel(0,z),[0,pi])/pi-1)<mp.mpf('1e-65'),"reproducing constants")
# Independent numerical quadrature at interior evaluation points: not a global proof.
for j in range(1,36):
    theta=pi*j/36
    fine=mp.quad(lambda z:abs(kernel(theta,z)),[0,pi/4,pi/2,3*pi/4,pi])/pi
    ck(fine < Lam-mp.mpf('1e-8'),f"interior comparison {j}")
print(f"PASS {nchecks} checks; lambda={mp.nstr(Lam,32)}")
