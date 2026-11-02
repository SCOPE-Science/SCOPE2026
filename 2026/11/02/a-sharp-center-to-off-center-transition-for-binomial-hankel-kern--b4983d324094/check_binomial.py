"""Standalone finite consistency tests for binomial Hardy Hankel kernel norms.

Run: python3 check_binomial.py
Uses only the Python standard library. Its finite checks do not establish
continuum optimization or asymptotic claims.
"""
from fractions import Fraction
from math import cos, pi, ceil, sqrt, isclose

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def radial(m, n, c, r):
    return 1+c*c-r**(2*m)-(c*c)*r**(2*n) + 2*c*r**(m-n)*(1-r**(2*n))

def threshold(m,n):
    if m<3*n:
        return float('inf')
    if m==3*n:
        return 2.0
    p=(m-3*n)/(2*n)
    return 2**(-p-1)*(p/(p+1))**p*((p+2)/(p+1))**(p+2)

def max_grid(m,n,c,num=2000):
    return max((radial(m,n,c,j/num),j/num) for j in range(num+1))

# The two exact tangencies: m=5,n=1 and m=3,n=1.
c=Fraction(27,64); x=Fraction(3,8)
# For m=5,n=1 the transition radius has r^2=x,
# with B/r^2 = -x^4 - c^2 + 2*c*x*(1-x).
q = -x**4-c*c+2*c*x*(1-x)
dq= -4*x**3+2*c*(1-2*x)
check(q==0,'5,1 exact contact')
check(dq==0,'5,1 stationary contact')
check(threshold(5,1)==float(c),'5,1 exact threshold')
for x in [Fraction(j,100) for j in range(1,100)]:
    # The quadratic has no positive value above the threshold.
    b=-(x**5)-c*c*x+2*c*x*x*(1-x)
    check(b<=0,'5,1 all sampled radii below center at threshold')
for cc in [Fraction(2,1),Fraction(3,1)]:
    for x in [Fraction(j,100) for j in range(1,101)]:
        # m=3,n=1: B=x[(2c-c^2)-2cx-x^2].
        b=x*((2*cc-cc*cc)-2*cc*x-x*x)
        check(b<=0,'3,1 center optimal above threshold')

# Independent finite matrix/kernel calculation of the Poisson variance:
# the truncated Hardy kernel has coefficient vector sqrt(1-r^2)*(1,r,...).
for m in range(2,10):
    for n in range(1,m):
        for cc in [Fraction(1,3), Fraction(2,5), Fraction(2,1)]:
            for rr in [Fraction(1,3),Fraction(1,2),Fraction(3,4)]:
                outputs=[]
                for i in range(m):
                    v=sum((int(i+j==m-1)+cc*int(i+j==n-1))*rr**j for j in range(m))
                    outputs.append(v)
                squared=(1-rr*rr)*sum(v*v for v in outputs)
                check(squared==radial(m,n,cc,rr),'independent finite Hardy-kernel variance')

# Explicit finite Hankel matrices and the exact first-order path operator.
def reverse(m):
    return [[int(i+j==m-1) for j in range(m)] for i in range(m)]
for m in range(2,14):
    for n in range(1,m):
        d=m-n
        Jm=reverse(m)
        Jn=[[int(i<n and j<n and i+j==n-1) for j in range(m)] for i in range(m)]
        A=[[sum(Jm[k][i]*Jn[k][j]+Jn[k][i]*Jm[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                check(A[i][j]==int(abs(i-j)==d),'linear Gram path matrix')
        check(ceil(m/d)>=2,'path has at least two vertices')
        check(2*cos(pi/(ceil(m/d)+1))>0,'positive first derivative')

# Check a few off-center/center transitions, avoiding near-critical grid ambiguity.
for m,n in [(2,1),(3,1),(4,1),(5,1),(7,2),(8,2),(10,3)]:
    t=threshold(m,n)
    vals=[0.1,0.8,10.] if t==float('inf') else [0.45*t,1.5*t]
    for cc in vals:
        best,r=max_grid(m,n,cc)
        if t==float('inf') or cc<t:
            check(best>1+cc*cc+1e-8,'off-center advantage')
            check(r>0,'off-center maximizer')
        else:
            check(abs(best-(1+cc*cc))<1e-10,'center wins')
            check(r<1/50,'center maximizer within grid precision')

# Evaluate the small-coefficient max without using scipy and check the
# asymptotic universal scaling at sufficient grid resolution.
for m,n in [(2,1),(3,1),(4,1),(5,2),(7,1)]:
    d=m-n;M=m+n; alpha=2*m/M
    K=M/m*(d/m)**(d/M)
    s=(d/m)**(1/M)
    for cc in [1e-5,1e-6]:
        r=s*cc**(1/M)
        ratio=(radial(m,n,cc,r)-1)/cc**alpha
        check(abs(ratio-K)<0.13,'fractional-power asymptotic test')

print('PASS:',checks,'finite assertions')
