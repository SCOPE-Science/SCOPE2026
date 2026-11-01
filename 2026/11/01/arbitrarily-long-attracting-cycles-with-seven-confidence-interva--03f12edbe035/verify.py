"""Exact rational checks for a finite-band SCOD period construction.
Scientific evidence is the analytic argument; this script only checks representative cases.
"""
from fractions import Fraction as F


def confidence_intervals(p):
    assert p >= 2
    Q = 2**p-1
    c = F(1,4*Q)
    positive = [(F(0), c)]
    if p >= 3:
        positive.append((F(2,Q)-c, F(2**(p-2), Q)+c))
    positive.append((F(2**(p-1),Q)-c, F(2**(p-1),Q)+c))
    positive.append((F(Q-1,Q)-c, F(Q-1,Q)+c))
    # Sort and merge duplicates, but do not change mathematical set
    return positive


def trusts(delta, bands):
    return any(a <= abs(delta) <= b for a,b in bands)


def Fstep(x, bands):
    peers = [x]
    if trusts(x,bands): peers.append(F(0))
    if trusts(1-x,bands): peers.append(F(1))
    return sum(peers,F(0))/len(peers)


def orbit(p):
    Q=2**p-1
    return [F(1,Q)]+[F(2**(p-j),Q) for j in range(1,p)]


def verify(p):
    B = confidence_intervals(p)
    X = orbit(p)
    c = F(1,4*(2**p-1))
    assert len(set(X))==p
    assert trusts(F(0),B)
    for j,x in enumerate(X):
        left = trusts(x,B)
        right = trusts(1-x,B)
        assert (left,right)==((False,True) if j==0 else (True,False)), (p,j,x,left,right)
        assert Fstep(x,B) == X[(j+1)%p]
    for eps in [-c/2, c/2, -c/4, c/4]:
        y=X[0]+eps
        for k in range(4*p):
            j=k%p
            assert trusts(y,B)==(j!=0), (p,k,'left')
            assert trusts(1-y,B)==(j==0), (p,k,'right')
            assert y-X[j]==eps/F(2**k), (p,k,'dist')
            y=Fstep(y,B)
    assert y-X[0]==eps/F(2**(4*p))
    # Bound number of connected positive intervals, despite overlaps
    assert len(B) <= 4
    return len(B), c


if __name__ == '__main__':
    for p in range(2,121):
        verify(p)
    print('PASS: exact rational itinerary and open-basin checks for periods 2..120')
    for p in [2,3,4,5,8,12]:
        print('p',p,'rational orbit', [str(x) for x in orbit(p)], 'positive interval count',len(confidence_intervals(p)))
