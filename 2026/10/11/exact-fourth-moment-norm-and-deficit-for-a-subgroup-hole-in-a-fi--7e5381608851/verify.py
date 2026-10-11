from fractions import Fraction
from math import pi
import cmath, random

def alpha(m):
    return Fraction(m*m-3*m+3, m*(m-1))

def k4four(N,k):
    m=N//k
    return Fraction(k*(m*m-3*m+3), m-1)

# Exact algebra behind the simplex-frame local bound.
for m in range(2,41):
    d=m-1
    lam0=Fraction(m-1,m)
    lam1=Fraction(m-2,m)
    rhs=lam0*Fraction(1,d)+lam1*Fraction(m-2,m-1)
    assert rhs == alpha(m)

random.seed(27049)
checks=0
extremizers=0
for N in range(4,33):
    for k in range(1,N):
        if N%k or k==N:
            continue
        m=N//k
        K={ (j*m)%N for j in range(k) }
        Lam=[j for j in range(N) if j not in K]
        target=float(k4four(N,k))
        for _ in range(24):
            a={j: complex(random.uniform(-1,1),random.uniform(-1,1)) for j in Lam}
            s2=sum(abs(v)**2 for v in a.values())
            vals=[sum(a[j]*cmath.exp(2j*pi*j*x/N) for j in Lam) for x in range(N)]
            ratio=(sum(abs(v)**4 for v in vals)/N)/(s2*s2)
            assert ratio <= target + 2e-10
            checks += 1
        y=(N//3)%N
        a={j: cmath.exp(-2j*pi*j*y/N) for j in Lam}
        s2=sum(abs(v)**2 for v in a.values())
        vals=[sum(a[j]*cmath.exp(2j*pi*j*x/N) for j in Lam) for x in range(N)]
        ratio=(sum(abs(v)**4 for v in vals)/N)/(s2*s2)
        assert abs(ratio-target) < 2e-10, (N,k,ratio,target)
        extremizers += 1
print(f"VERIFY_OK exact_m=2..40 random_checks={checks} cyclic_extremizers={extremizers}")
