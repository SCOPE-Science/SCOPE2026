from fractions import Fraction
from math import sqrt


def exact_case(e):
    n=len(e)
    tails=[Fraction(0) for _ in range(n+1)]
    for j in range(n-1,-1,-1):
        tails[j]=tails[j+1]+e[j]
    S=sum(t*t for t in tails[:-1])
    W=sum(Fraction((j+1)**2)*e[j]*e[j] for j in range(n))
    rhs=sum(Fraction(j+1)*e[j]*(tails[j]+tails[j+1]) for j in range(n))
    assert S==rhs
    assert S<=4*W
    return S,W

cases=[
    [Fraction(1,j+1) for j in range(8)],
    [Fraction(1,(j+1)**2) for j in range(10)],
    [Fraction(3,2*(j+1)+1) for j in range(12)],
]
for e in cases:
    S,W=exact_case(e)
    assert W<=S  # all listed cases are decreasing

# A few arbitrary nonnegative sequences test that monotonicity is not needed above.
for e in [
    [Fraction(1,3),Fraction(4,5),Fraction(1,7),Fraction(2,9)],
    [Fraction(0),Fraction(5,4),Fraction(1,100),Fraction(7,8),Fraction(0)],
]:
    exact_case(e)


def sharp_ratio(N):
    tail=0.0
    S=0.0
    W=0.0
    for n in range(N,0,-1):
        a=n**(-1.5)
        tail+=a
        S+=tail*tail
        W+=1.0/n
    return S/W

Ns=[1000,10000,100000,1000000]
ratios=[sharp_ratio(N) for N in Ns]
assert all(a<b for a,b in zip(ratios,ratios[1:]))
assert ratios[-1]>3.45 and ratios[-1]<4.0
print('VERIFY_OK exact_cases=5 sharp_N=%d sharp_ratio=%.12f' % (Ns[-1],ratios[-1]))
