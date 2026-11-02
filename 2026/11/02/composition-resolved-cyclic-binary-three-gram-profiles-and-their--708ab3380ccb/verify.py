#!/usr/bin/env python3
"""Independent integer checks for cyclic binary ordered three-gram profile counts.
Standalone mathematical verification program. Standard library only.
"""
from collections import defaultdict


def connected(a, b, d, f, h):
    # The remaining balanced entries are N010=b+f-d, N100=b, N110=d.
    if b + f < d:
        return False
    if b > 0 and d > 0:
        return True
    if b > 0:
        return h == 0
    if d > 0:
        return a == 0
    if f > 0:
        return a == 0 and h == 0
    return (a > 0) != (h > 0)


def parameter_count(n, chosen_weight=None):
    """Enumerate *all* balanced profiles via five independent integers."""
    weight_counts = defaultdict(int)
    for b in range(n // 3 + 1):
        for d in range(n + 1):
            for f in range(n // 2 + 1):
                base = 3*b + d + 2*f
                if base > n or b + f < d:
                    continue
                if chosen_weight is None:
                    for h in range(n-base+1):
                        a = n-base-h
                        if connected(a,b,d,f,h):
                            weight_counts[b+d+f+h] += 1
                else:
                    h = chosen_weight-b-d-f
                    a = n-base-h
                    if a >= 0 and h >= 0 and connected(a,b,d,f,h):
                        weight_counts[chosen_weight] += 1
    if chosen_weight is not None:
        return weight_counts[chosen_weight]
    return dict(weight_counts)


def direct_counts(n):
    """Independent word-level enumeration, with no flow parameters."""
    by_weight = defaultdict(set)
    for mask in range(1 << n):
        profile = [0]*8
        for k in range(n):
            a = (mask >> k) & 1
            b = (mask >> ((k+1) % n)) & 1
            c = (mask >> ((k+2) % n)) & 1
            profile[4*a+2*b+c] += 1
        by_weight[mask.bit_count()].add(tuple(profile))
    return {w:len(p) for w,p in by_weight.items()}


def mul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C


def rational_coefficients(N):
    """Formal-series expansion of independently derived reduced rational GF."""
    den=[1]
    for _ in range(5):den=mul(den,[1,-1])
    for factor in [[1,1],[1,0,1],[1,1,1]]:den=mul(den,factor)
    num={1:2,2:-3,3:1,4:-1,6:5,7:-5,8:6,9:-7,10:3}
    out=[0]*(N+1)
    for n in range(N+1):
        out[n]=num.get(n,0)-sum(den[j]*out[n-j] for j in range(1,min(len(den)-1,n)+1))
    return out


def stabilized_count(w):
    if w==0:return 1
    return (w**3+(8 if w%2==0 else 7)*w)//8


def main():
    counts=rational_coefficients(100)
    assert counts[0]==0
    assert counts[1:17]==[2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271]
    checked=0
    # Full source enumeration for all 1<=n<=16.
    for n in range(1,17):
        direct=direct_counts(n)
        param=parameter_count(n)
        assert direct==param,(n,direct,param)
        assert sum(direct.values())==counts[n]
        checked+=(1<<n)
    # Test rational formula against direct flow-vector enumeration beyond word-exhaustible lengths.
    for n in range(17,43):
        param=parameter_count(n)
        assert sum(param.values())==counts[n],(n,sum(param.values()),counts[n])
        for w,v in param.items():
            assert v==param.get(n-w,0),(n,w,v,param.get(n-w))
    # Exact threshold and sharp one-step-before discrepancy at each fixed weight.
    for w in range(2,25):
        assert parameter_count(3*w,w)==stabilized_count(w),(w,'threshold')
        assert parameter_count(3*w-1,w)==stabilized_count(w)-1,(w,'below')
        assert parameter_count(3*w+1,w)==stabilized_count(w),(w,'above')
    assert all(parameter_count(n,1)==1 for n in range(1,81))
    # Leading coefficient and poles are proved symbolically in RESULT.md, not inferred from testing.
    print('VERIFIED: source instances =',checked)
    print('VERIFIED: complete word-level weighted profiles for n=1..16')
    print('VERIFIED: independent balanced-flow counts for n=17..42')
    print('VERIFIED: sharp stabilization for weights 2..24')
    print('VERIFIED: exact rational coefficients n=1..42')

if __name__=='__main__':main()
