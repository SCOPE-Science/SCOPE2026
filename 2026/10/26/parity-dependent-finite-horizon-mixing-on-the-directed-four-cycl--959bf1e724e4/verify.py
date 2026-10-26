"""Exact finite-state verification of cyclic walk total-variation formulas."""
from fractions import Fraction
from math import comb, sqrt, tan, pi, cos, sin

def matrix_distribution(h, p):
    v = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    for _ in range(h):
        w = [Fraction(0)] * 4
        for j in range(4):
            w[j] += (1-p)*v[j]
            w[(j+1)%4] += p*v[j]
        v = w
    return v

def derived_distribution(h,p):
    # (a+ib)^h by exact rational integer arithmetic.
    a,b=Fraction(1),Fraction(0)
    for _ in range(h):a,b=a*(1-p)-b*p,a*p+b*(1-p)
    B=(1-2*p)**h
    return [(1+B+2*a)/4,(1-B+2*b)/4,(1+B-2*a)/4,(1-B-2*b)/4]

def tv(v):return sum(abs(x-Fraction(1,4)) for x in v)/2

n=0
for h in range(1,31):
    for j in range(0,61):
        p=Fraction(j,60)
        v=matrix_distribution(h,p)
        w=derived_distribution(h,p)
        assert v==w,(h,p,v,w)
        assert tv(v)>=0
        if h>=2 and h%2==0:
            assert tv(v)>=Fraction(1,2)*Fraction(1,2)**(h//2)
        n+=1
for h in range(2,100,2):
    assert abs(float(tv(matrix_distribution(h,Fraction(1,2))))-2**(-h/2-1))<1e-14
for h in range(3,32,2):
    dmid=float(tv(matrix_distribution(h,Fraction(1,2))))
    assert float(tv(matrix_distribution(h,Fraction(1,2)+Fraction(1,10000*h))))<dmid
for h in range(3,100,2):
    eps=pi/(4*h)
    p=.5+.5*tan(eps)
    r=sqrt((1-p)**2+p*p)
    B=abs(1-2*p)**h
    analytic=(r**h)/2+B/4
    assert B<2*r**h
    ratio=(analytic)/(2**(-h/2-1))
    assert ratio>=1
    if h>=51:assert ratio<1.03,(h,ratio)
print('PASSED',n,'exact rational Fourier/convolution comparisons, parity bounds, odd improvement and asymptotic witness checks')
