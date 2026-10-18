"""Reproduce finite checks for the negative-tense chain completion theorem.

No external dependencies: Python 3.10+. These finite tests support, not replace,
the proofs for arbitrary positive chain lengths.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, product
from math import comb


def permitted_pairs(n):
    yield (None, None)
    for asc in combinations_with_replacement(range(n), n-1):
        a = tuple(reversed(asc)) + (0,)
        for des in combinations_with_replacement(range(n), n-1):
            b = (n-1,) + tuple(reversed(des))
            if all(a[i] <= b[i] for i in range(n)) and all(
                b[i+1] >= a[i]-1 for i in range(n-1)
            ):
                yield a, b


def test_s_conditions(a, b, n):
    if a is None:
        rows = tuple(() for _ in range(n))
    else:
        rows = tuple(tuple(range(a[i],b[i]+1)) for i in range(n))
    cols = tuple(tuple(i for i,row in enumerate(rows) if j in row) for j in range(n))
    for fibers in (rows, cols):
        for s in fibers:
            assert not s or s == tuple(range(s[0],s[-1]+1))
        for k in range(n+1):
            outside = set(range(k))
            g = {i for i,s in enumerate(fibers) if any(j in outside for j in s)}
            f = {i for i,s in enumerate(fibers) if all(j in outside for j in s)}
            assert all(i in g for i in range(min(g),n)) if g else True
            assert all(i in f for i in range(min(f),n)) if f else True


def all_admissible_direct(n):
    intervals=[tuple(range(i,j+1)) for i in range(n) for j in range(i,n)]+[()]
    def consecutive(s):
        return not s or s==tuple(range(s[0],s[-1]+1))
    for rows in product(intervals, repeat=n):
        cols=tuple(tuple(i for i,r in enumerate(rows) if j in r) for j in range(n))
        if not all(consecutive(s) for s in cols):
            continue
        ok=True
        for fibers in (rows, cols):
            for k in range(n+1):
                outside=set(range(k))
                g=[i for i,s in enumerate(fibers) if any(j in outside for j in s)]
                f=[i for i,s in enumerate(fibers) if all(j in outside for j in s)]
                if (g and g!=list(range(g[0],n))) or (f and f!=list(range(f[0],n))):
                    ok=False; break
            if not ok: break
        if ok:
            yield rows


def check_axioms_direct(points):
    vals=[tuple(reversed(z)) for z in combinations_with_replacement(range(points), points)]
    GH=[z for z in vals if z[-1]==0]
    FP=[z for z in vals if z[0]==points-1]
    count=0
    g_profiles=defaultdict(int)
    for g,h in product(GH,repeat=2):
        if not all(g[h[x]]<=x and h[g[x]]<=x for x in range(points)):
            continue
        for f,p in product(FP,repeat=2):
            if not all(x<=p[f[x]] and x<=f[p[x]] for x in range(points)):
                continue
            if not all(
                min(g[x],f[y])<=g[max(x,y)]
                and min(h[x],p[y])<=h[max(x,y)]
                and f[min(x,y)]<=max(f[x],g[y])
                and p[min(x,y)]<=max(p[x],h[y])
                for x in range(points) for y in range(points)
            ):
                continue
            count+=1
            g_profiles[g]+=1
    return count, sorted(g_profiles.values())


def main():
    totals=[2,5,30,267,2763]
    reducts=[2,3,7,21,71]
    for n in range(1,6):
        pairs=list(permitted_pairs(n))
        assert len(pairs)==totals[n-1]
        f=defaultdict(int)
        for a,b in pairs:
            test_s_conditions(a,b,n)
            if a is not None:
                f[a]+=1
        assert len(f)+1==reducts[n-1]==1+comb(2*n-2,n-1)
        assert max(f.values())==comb(2*n-2,n-1)
        assert min(f.values())==(1 if n==1 else 2)
        print('DUAL',n,'full',len(pairs),'g_reducts',len(f)+1,'fiber_minmax',min(f.values()),max(f.values()))
    for n in range(1,5):
        rows_from_formula={tuple(tuple(range(a[i],b[i]+1)) for i in range(n)) if a is not None else tuple(() for _ in range(n)) for a,b in permitted_pairs(n)}
        rows_from_axioms=set(all_admissible_direct(n))
        assert rows_from_formula==rows_from_axioms
        print('RELATION_DIRECT',n,len(rows_from_axioms))
    for points in range(2,5):
        count,profile=check_axioms_direct(points)
        dual_n=points-1
        f=defaultdict(int)
        for a,b in permitted_pairs(dual_n):
            f[a]+=1
        assert count==totals[dual_n-1]
        assert profile==sorted(f.values())
        print('AXIOMS_DIRECT',points,'quadruples',count,'g_fibers',profile)
    print('VERIFY_OK')

if __name__=='__main__':main()
