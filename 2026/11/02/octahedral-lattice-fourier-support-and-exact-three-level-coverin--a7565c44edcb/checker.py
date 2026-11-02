"""Exact arithmetic and independent integer-placement checks for the octahedral Fourier/covering identity."""
from fractions import Fraction
from itertools import product
from math import gcd


def symbol(k):
    """Returns the rational q such that Fourier(1_{l1-ball})(k)=q/pi**2, or volume at zero."""
    a=sorted(map(abs,k))
    if a==[0,0,0]: return 'volume',Fraction(4,3)
    if a[0]==0 and a[1]==0: return 'pi^-2',Fraction(2,a[2]**2)
    if a[0]==a[1]==a[2]: return 'pi^-2',Fraction(-1,4*a[0]**2)
    if a[0]==a[1] and a[0]>0: return 'pi^-2',Fraction(1,a[2]**2-a[0]**2)
    if a[1]==a[2] and a[1]>0: return 'pi^-2',Fraction(1,a[0]**2-a[1]**2)
    return 'pi^-2',Fraction(0)


def count(x,m):
    return sum(sum(abs(z-y) for z,y in zip(n,x)) < m for n in product(range(-m, m+2),repeat=3))

for N in range(1,9):
    pts=list(product(range(-N,N+1), repeat=3))
    nonzero=sum(symbol(k)[1]!=0 for k in pts)
    assert nonzero==24*N*N+2*N+1, (N,nonzero)
    for k in pts:
        if k==(0,0,0):continue
        is_support=any(abs(k[i])==abs(k[j]) for i in range(3) for j in range(i+1,3))
        assert (symbol(k)[1]!=0)==is_support,k
        for m in (2,3,4):
            at_scale=symbol(tuple(m*x for x in k))[1]
            assert at_scale*m*m==symbol(k)[1],k

R=[(Fraction(1,10),Fraction(1,7),Fraction(2,9)),
   (Fraction(7,20),Fraction(1,4),Fraction(1,6)),
   (Fraction(49,100),Fraction(12,25),Fraction(23,50)),
   (Fraction(3,11),Fraction(2,7),Fraction(4,9)),
   (Fraction(13,20),Fraction(11,20),Fraction(9,20))]
for u in R:
    a=count(u,1)
    assert a in (0,1,2)
    for m in range(1,8):
        assert count(u,m)==Fraction(4,3)*(m**3-m)+m*a,(u,m,count(u,m),a)

# An independent geometric overlap calculation:
# intersection of B_1(0) and B_1(e1) has x-section length (1-2r)_+
# for r=|y|+|z|; L1 planar radial shell element is 4r dr.
assert 4*(Fraction(1,8)-Fraction(1,12))==Fraction(1,6)
# Mean octahedral occupancy = 4/3; mean binomial(N1,2)=3*(1/6)=1/2.
p2=Fraction(1,2);p1=Fraction(4,3)-2*p2;p0=1-p1-p2
assert (p0,p1,p2)==(Fraction(1,6),Fraction(1,3),Fraction(1,2))
print('PASS: exact supports/cutoff counts/scaling N<=8, m<=4; translated placements m<=7; overlap and fractions')

# Independent analytic-octant numerical quadrature (not used to prove all-frequency statements).
try:
    from scipy.integrate import dblquad
    from math import sin,cos,pi
    for k in [(1,0,0),(1,1,0),(1,1,1),(1,1,2),(1,2,0),(1,2,3),(0,2,2)]:
        def reduced(y,x):
            zint=1-x-y if k[2]==0 else sin(2*pi*k[2]*(1-x-y))/(2*pi*k[2])
            return 8*cos(2*pi*k[0]*x)*cos(2*pi*k[1]*y)*zint
        approx,_=dblquad(reduced,0,1,lambda x:0,lambda x:1-x,epsabs=1e-9)
        exact=float(symbol(k)[1])/pi**2
        assert abs(approx-exact)<2e-8,(k,approx,exact)
    print('PASS: independent octant quadrature')
except ImportError:
    print('SKIP: scipy not installed; exact checks above passed')
