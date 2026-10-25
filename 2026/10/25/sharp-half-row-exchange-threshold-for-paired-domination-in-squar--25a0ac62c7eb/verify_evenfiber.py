"""Independent parity-fiber enumeration for square rook graphs of sizes 4 and 6.
Run: python3 verify_evenfiber.py
Only the Python standard library is required.
"""
from itertools import product
from collections import deque,Counter
from math import factorial


def even_functions(n):
    out=set()
    for f in product(range(n),repeat=n):
        if all(f.count(c)%2==0 for c in range(n)):
            out.add(f)
    return out


def coeff_even(n):
    # Coefficient of z^n in (sum_j z^(2j)/(2j)!)^n, multiplied by n!, computed without fractions.
    # DP counts choices for sequential input rows, tracking occupancy-parity target via convolution.
    a=[1]+[0]*n
    for col in range(n):
        nxt=[0]*(n+1)
        for used in range(n+1):
            for t in range(0,n-used+1,2):
                from math import comb
                nxt[used+t]+=a[used]*comb(used+t,t)
        a=nxt
    return a[n]

for n in (4,6):
    F=even_functions(n)
    assert len(F)==coeff_even(n), (n,len(F),coeff_even(n))
    assert len(F)==({4:40,6:2256}[n])
    # Move any two rows in the same column to another column; each is a batch-two swap.
    start=(0,)*n
    seen={start}; stack=deque([start])
    while stack:
        f=stack.popleft()
        for i in range(n):
            for j in range(i+1,n):
                if f[i]!=f[j]: continue
                for c in range(n):
                    if c==f[i]: continue
                    g=list(f);g[i]=g[j]=c;g=tuple(g)
                    assert g in F
                    if g not in seen:
                        seen.add(g);stack.append(g)
    assert seen==F,(n,len(seen),len(F))
    h=n//2
    S={(2*j,j) for j in range(h)}|{(2*j+1,j) for j in range(h)}
    T={(2*j,j) for j in range(h)}|{(2*j,j+h) for j in range(h)}
    assert len(S)==len(T)==n
    assert len(S&T)==h and len(S-T)==h
    # S has even column multiplicity; T has even row multiplicity.
    assert all(sum(c==j for i,c in S)%2==0 for j in range(n))
    assert all(sum(i==j for i,c in T)%2==0 for j in range(n))
    print(f'n={n}: even-fiber functions {len(F)} per orientation; {2*len(F)} minima; all parity states connected by batch-two moves; cross threshold {h}')
print('coefficient sequence (n=4,6,8):', [coeff_even(n)*2 for n in (4,6,8)])
assert coeff_even(8)*2==500992
print('ALL ASSERTIONS PASSED')
