"""Standalone computations for the stated symmetric-ball-lens covariance theorem.

Requirements: Python 3.10+ and mpmath >= 1.3.0. Run: python verify.py.
The theorem relies on its analytic proof; these are reproducibility checks.
"""
import math
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 65
COUNT = 0

def check(ok, label):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(label)

def near(x, y, tol=mp.mpf('1e-35')):
    return abs(x-y) < tol*max(1, abs(x), abs(y))

def moments(n, a):
    a=mp.mpf(a); k=mp.mpf(n-1)/2; delta=1-a
    def w(s): return (1-s)**k*(1+a+delta*s)**k
    b=[mp.quad(lambda s,j=j: s**j*w(s), [0,1]) for j in range(4)]
    para=delta**2*b[2]/b[0]
    perp=para+a*delta*b[1]/b[0]
    return para,perp,b,w

for n in [2,3,4,5,7,10,20,40]:
    k=mp.mpf(n-1)/2
    lo=mp.gamma(k+mp.mpf(5)/2)/(mp.gamma(mp.mpf(3)/2)*mp.gamma(k+2))
    hi=mp.mpf(n+5)/4
    prev=mp.mpf(1)
    for astr in ['0.00001','.05','.15','.35','.55','.75','.9','.99']:
        a=mp.mpf(astr); delta=1-a
        para,perp,b,w=moments(n,a)
        r=perp/para
        q=(r-1)*delta/a
        check(lo < q < hi, f'sharp bounds n={n}, a={a}')
        check(r>prev, f'monotonicity n={n}, a={a}')
        check(near(perp-para, a*delta*b[1]/b[0]),'moment identity')
        check(near(q,b[1]/b[2]),'rescaled exact representation')
        g=lambda s:k*(1-s)/(1+a+delta*s)
        j1=mp.quad(lambda s:s*w(s)*g(s),[0,1]);j2=mp.quad(lambda s:s*s*w(s)*g(s),[0,1])
        covariance=j2/b[1]-(b[2]/b[1])*(j1/b[1])
        check(covariance<0, f'strict size-biased antitonicity n={n}')
        prev=r
    # Endpoint constants of the scale-free profile, independently integrated.
    for a, expected in [(mp.mpf(0),lo),(mp.mpf(1),hi)]:
        _,_,b,_=moments(n,a)
        check(near(b[1]/b[2],expected),'endpoint moment ratio')
    # Thin-lens sharp eigenvalue asymptotics.
    a=mp.mpf('0.9999999'); delta=1-a
    para,perp,b,_=moments(n,a)
    expected_para=2*delta**2/((k+2)*(k+3))
    expected_perp=delta/(k+2)
    check(abs(para/expected_para-1)<mp.mpf('1e-6'),'thin axial rate')
    check(abs(perp/expected_perp-1)<mp.mpf('1e-6'),'thin transverse rate')

# Separate exact-rational 3-dimensional polynomial integration.
for a in [F(0),F(1,7),F(1,3),F(1,2),F(4,5),F(9,10)]:
    m=lambda j:(1+a)/F(j+1)-2*a/F(j+2)-(1-a)/F(j+3)
    check(m(0)==(2+a)/3,'three-dimensional M0')
    check(m(1)==(3+a)/12,'three-dimensional M1')
    check(m(2)==(4+a)/30,'three-dimensional M2')
    if a<1:
        para=(1-a)**2*m(2)/m(0)
        perp=para+a*(1-a)*m(1)/m(0)
        check(para==(1-a)**2*(4+a)/(10*(2+a)),'3D axial exact')
        check(perp==(1-a)*(8+9*a+3*a*a)/(20*(2+a)),'3D transverse exact')
        check(perp/para==1+5*a*(3+a)/(2*(1-a)*(4+a)),'3D rational anisotropy')

# Independent geometric cross-section check: integrate the transverse second moment
# with the (n-1)-ball cross section, rather than the integrated-by-parts formula.
for n in (2,3,5,11):
    for astr in ('.08','.43','.78'):
        a=mp.mpf(astr); delta=1-a; k=mp.mpf(n-1)/2
        para,perp,_,_=moments(n,a)
        base=mp.quad(lambda s:(1-s)**k*(1+a+delta*s)**k,[0,1])
        cross=delta/(n+1)*mp.quad(lambda s:(1-s)**(k+1)*(1+a+delta*s)**(k+1),[0,1])/base
        axial=delta**2*mp.quad(lambda s:s*s*(1-s)**k*(1+a+delta*s)**k,[0,1])/base
        check(near(cross,perp),'independent transverse section integration')
        check(near(axial,para),'independent axial section integration')

print(f'PASS: {COUNT} exact-fraction and high-precision analytic-quadrature checks.')
