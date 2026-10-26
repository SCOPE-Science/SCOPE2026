"""Independent exhaustive relation enumeration for finite flat meet-semilattices.
Run: python3 verify.py (Python 3.9+, standard library)."""
from math import comb


def meet(i,j):
    return i if i==j else 0


def formula(m):
    d=0
    sym=0
    for L in range(1<<m):
        for R in range(1<<m):
            d += 1 << (L.bit_count()*R.bit_count()-(L&R).bit_count())
    for k in range(m+1):
        sym += comb(m,k) * (1 << (k*(k-1)//2))
    return d,sym,1<<m


def checks(m):
    n=m+1
    off=[(i,j) for i in range(n) for j in range(n) if i!=j]
    diagonal={(i,i) for i in range(n)}
    totals=[0,0,0]
    for bitmask in range(1<<len(off)):
        rel=diagonal | {v for k,v in enumerate(off) if bitmask & (1<<k)}
        if any((meet(a,c),meet(b,d)) not in rel for a,b in rel for c,d in rel):
            continue
        totals[0]+=1
        L={i for i in range(1,n) if (i,0) in rel}
        R={j for j in range(1,n) if (0,j) in rel}
        E={(i,j) for i,j in rel if i and j and i!=j}
        assert E<= {(i,j) for i in L for j in R if i!=j}
        assert rel == diagonal | {(i,0) for i in L} | {(0,j) for j in R} | E
        symmetric=all((b,a) in rel for a,b in rel)
        transitive=all((a,c) in rel for a,b in rel for d,c in rel if b==d)
        totals[1]+=int(symmetric)
        totals[2]+=int(symmetric and transitive)
    assert tuple(totals)==formula(m), (m,totals,formula(m))
    print('m=',m,'direct=',totals)

for m in range(0,4):
    checks(m)
for m in range(4,8):
    print('m=',m,'formula=',formula(m))
print('VERIFY_OK')
