#!/usr/bin/env python3
"""Exact checks for parity and correlations of antiprism Ising ground states.

Only Python 3 standard library is required. This is finite verification;
the complete all-size argument appears separately in RESULT.md.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def edges(n):
    """Vertices a_i=2*i, b_i=2*i+1, with indices reduced modulo n."""
    e = []
    for i in range(n):
        j = (i + 1) % n
        e.extend(((2*i, 2*j), (2*i+1, 2*j+1),
                  (2*i, 2*i+1), (2*j, 2*i+1)))
    assert len(e) == len(set(tuple(sorted(q)) for q in e)) == 4*n
    return e


def ground_construction(n):
    if n % 2 == 0:
        for sign_a in (-1, 1):
            for sign_b in (-1, 1):
                yield tuple(v for i in range(n)
                            for v in (sign_a*(-1)**i, sign_b*(-1)**i))
    else:
        for ia in range(n):
            for ib in range(n):
                for sign_a in (-1, 1):
                    a = [sign_a]
                    for i in range(n-1):
                        a.append(a[-1] if i == ia else -a[-1])
                    b0 = -a[ia] * (-1)**ia * (-1 if ib < ia else 1)
                    b = [b0]
                    for i in range(n-1):
                        b.append(b[-1] if i == ib else -b[-1])
                    yield tuple(v for i in range(n) for v in (a[i],b[i]))


def predicted_count(n):
    if n % 2 == 0:
        return {0: 4}
    return {-2:n*(n-1)//2, 0:n*(n+1), 2:n*(n-1)//2}


def frustrated(spins, ee):
    return sum(spins[u] == spins[v] for u, v in ee)


def exhaustive(n):
    ee = edges(n)
    best = 10**8
    counts = Counter()
    cc_a, cc_ab = [0]*n, [0]*n
    for s in product((-1,1), repeat=2*n):
        f=frustrated(s,ee)
        if f<best:
            best=f
            counts.clear()
            cc_a=[0]*n
            cc_ab=[0]*n
        if f==best:
            counts[sum(s)] += 1
            for r in range(n):
                cc_a[r] += s[0]*s[2*r]
                cc_ab[r] += s[0]*s[2*r+1]
    return best, counts, cc_a, cc_ab


def predicted_corr(n,r):
    if n % 2 == 0:
        return Fraction((-1)**r),Fraction(0)
    return (Fraction((-1)**r*(n-2*r),n),
            Fraction(-(-1)**r*(n+2*r*(n-r-1)),n*n))


def transfer_counts(n):
    """Independent four-state zero-field max-cut transfer with magnetization."""
    pairs=list(product((-1,1),repeat=2))
    final=defaultdict(int)
    global_best=10**9
    for first in pairs:
        dp={(first,sum(first)):(0,1)}
        for t in range(n):
            nxt={}
            for (old,m),(f,num) in dp.items():
                for new in pairs:
                    # Closing step n-1 -> n uses new==first.
                    if t == n-1 and new != first:
                        continue
                    ff=(old[0]==new[0])+(old[1]==new[1])+(old[0]==old[1])+(new[0]==old[1])
                    mm=m+(sum(new) if t<n-1 else 0)
                    key=(new,mm)
                    if key not in nxt or f+ff<nxt[key][0]:
                        nxt[key]=(f+ff,num)
                    elif f+ff==nxt[key][0]:
                        nxt[key]=(f+ff,nxt[key][1]+num)
            dp=nxt
        for (last,m),(f,num) in dp.items():
            if f<global_best:
                global_best=f
                final.clear()
            if f==global_best:
                final[m]+=num
    return global_best,dict(final)


def verify():
    brute=0
    for n in range(3,10):
        got, cnt, ca,cab=exhaustive(n)
        expected_f=n+(n%2)
        assert got==expected_f,('min',n,got,expected_f)
        assert dict(cnt)==predicted_count(n),('mag',n,cnt)
        config=list(ground_construction(n))
        assert len(set(config))==len(config)==sum(cnt.values())
        assert all(frustrated(s,edges(n))==got for s in config)
        for r in range(n):
            x,y=predicted_corr(n,r)
            assert Fraction(ca[r],sum(cnt.values()))==x,('aa',n,r)
            assert Fraction(cab[r],sum(cnt.values()))==y,('ab',n,r)
        brute+=1
    transfer=0
    for n in range(3,35):
        f,c=transfer_counts(n)
        assert f==n+(n%2)
        assert c==predicted_count(n),(n,c)
        transfer+=1
    constructive=0
    for n in range(3,52):
        configs=list(ground_construction(n))
        assert len(configs)==sum(predicted_count(n).values())
        ee=edges(n)
        assert all(frustrated(s,ee)==n+(n%2) for s in configs)
        counts=Counter(sum(s) for s in configs)
        assert dict(counts)==predicted_count(n)
        for r in range(n):
            x,y=predicted_corr(n,r)
            assert Fraction(sum(s[0]*s[2*r] for s in configs),len(configs))==x
            assert Fraction(sum(s[0]*s[2*r+1] for s in configs),len(configs))==y
        constructive+=1
    print(f'VERIFY_OK brute_n={brute} transfer_n={transfer} constructive_n={constructive}')

if __name__=='__main__':
    verify()
