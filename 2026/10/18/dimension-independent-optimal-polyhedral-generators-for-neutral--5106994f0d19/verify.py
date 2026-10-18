"""Finite exact-rational diagnostics for the polygonal toral generator.

The entropy and almost-everywhere generation assertions require the proof,
not these finite tests. Python 3, standard library only.
"""
from fractions import Fraction as F
from random import Random


def windows(m, q):
    return [(F(2*i-1, m*(2*q+1)), F(2*i, m*(2*q+1)))
            for i in range(1, q+1)]


def symbol(m, theta, y):
    d = int(m*y)
    if d:
        return d
    for (a, b), x in zip(windows(m, len(theta)), theta):
        if a <= y < a + (b-a)*x:
            return -1  # the single special cell
    return 0


def test_exact():
    rng=Random(20261001)
    checked=0
    for m in range(2, 9):
        for q in range(2, 10):
            w=windows(m,q)
            assert all(F(0)<=a<b<F(1,m) for a,b in w)
            assert all(w[i][1] < w[i+1][0] for i in range(q-1))
            theta=[F(rng.randrange(1, 43),43) for _ in range(q)]
            # Every admissible symbol has an exact rational witness.
            assert symbol(m,theta,(w[-1][1]+F(1,m))/2) == 0
            for j in range(1,m):
                assert symbol(m,theta,F(2*j+1,2*m)) == j
            for (a,b),x in zip(w,theta):
                assert symbol(m,theta,a+(b-a)*x/2) == -1
            for _ in range(45):
                y=F(rng.randrange(0,100000),100000)
                first=symbol(m,theta,y)
                assert first in {-1,0,*range(1,m)}
                assert (first in (-1,0)) == (int(m*y) == 0)
                names=[]
                z=y
                for n in range(14):
                    name=symbol(m,theta,z)
                    names.append(0 if name in (-1,0) else name)
                    assert names[-1]==int(m*z)
                    z=(m*z)%1
                p=sum(F(d,m**(i+1)) for i,d in enumerate(names))
                assert p<=y<p+F(1,m**len(names))
                checked+=1
    return checked


def test_frequency():
    # Finite approximation to a single base-m orbit, not an infinite proof.
    rng=Random(197510)
    m=2; q=3; N=120000; K=35
    digits=[rng.randrange(m) for _ in range(N+K)]
    # n-th base-m state from its first K digits; truncation < m^-K.
    w=windows(m,q)
    theta=[F(1,5),F(1,2),F(4,5)]
    counts=[0]*q
    # Recurrence computes sliding binary windows exactly without big integers.
    radix=m**K
    state=0
    for d in digits[:K]: state=state*m+d
    for n in range(N):
        y=F(state,radix)
        for i,((a,b),x) in enumerate(zip(w,theta)):
            if a <= y < a+(b-a)*x: counts[i]+=1
        state=(state*m+digits[n+K])%radix
    recovered=[F(counts[i],N)/(b-a) for i,(a,b) in enumerate(w)]
    return [float(x) for x in recovered], [float(x) for x in theta]


if __name__=='__main__':
    total=test_exact()
    obs, target=test_frequency()
    assert max(abs(a-b) for a,b in zip(obs,target)) < 0.05
    print('PASS exact rational cases:',total,' ; finite frequency diagnostic:',obs,'targets:',target)
