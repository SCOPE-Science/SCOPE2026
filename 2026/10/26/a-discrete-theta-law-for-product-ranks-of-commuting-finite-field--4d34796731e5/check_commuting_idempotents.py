"""Exhaustive small-field verification of rank-stratified commuting idempotents.

Pure Python 3; no external dependencies.
"""
from collections import Counter, defaultdict
from itertools import product
from math import prod


def multiply(a, b, n, q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n)) % q
                 for i in range(n) for j in range(n))


def rank_mod(a, n, q):
    rows = [list(a[i*n:(i+1)*n]) for i in range(n)]
    piv = 0
    for j in range(n):
        sel = next((i for i in range(piv, n) if rows[i][j] % q), None)
        if sel is None:
            continue
        rows[piv], rows[sel] = rows[sel], rows[piv]
        inv = pow(rows[piv][j], -1, q)  # this checker tests prime fields only
        rows[piv] = [(v*inv) % q for v in rows[piv]]
        for i in range(piv+1, n):
            factor = rows[i][j]
            if factor:
                rows[i] = [(u-factor*v) % q for u, v in zip(rows[i], rows[piv])]
        piv += 1
    return piv


def gl(n, q):
    return prod(q**n-q**j for j in range(n))


def profile(n, q, r, s):
    values = Counter()
    G = gl(n, q)
    for t in range(max(0, r+s-n), min(r, s)+1):
        dims = [t, r-t, s-t, n-r-s+t]
        values[t] = G//prod(gl(d, q) for d in dims)
        assert values[t]*prod(gl(d, q) for d in dims) == G
    return values


def enumerate_case(n, q, requested_pairs=None):
    mats = defaultdict(list)
    for a in product(range(q), repeat=n*n):
        if multiply(a, a, n, q) == a:
            mats[rank_mod(a, n, q)].append(a)
    target = requested_pairs if requested_pairs is not None else [(r,s) for r in range(n+1) for s in range(n+1)]
    total_pairs = 0
    total_commuting = 0
    summaries=[]
    for r,s in target:
        obs=Counter()
        for a in mats[r]:
            for b in mats[s]:
                ab = multiply(a, b, n, q)
                if ab == multiply(b, a, n, q):
                    obs[rank_mod(ab, n, q)] += 1
        want=profile(n,q,r,s)
        assert obs == want, (n,q,r,s,obs,want)
        total_pairs+=len(mats[r])*len(mats[s])
        total_commuting+=sum(obs.values())
        summaries.append((r,s,dict(sorted(obs.items()))))
    return dict(n=n,q=q,idempotents=sum(map(len,mats.values())),pairs=total_pairs,
                commuting=total_commuting, profiles=summaries)


def main():
    cases=[(2,2,None),(3,2,None),(4,2,[(2,2)]),(2,3,None),(3,3,None)]
    for n,q,pairs in cases:
        out=enumerate_case(n,q,pairs)
        print(f"n={n} q={q} idempotents={out['idempotents']} pairs={out['pairs']} commuting={out['commuting']} profile_count={len(out['profiles'])}")
        print('rank profiles:',out['profiles'])
    print('ALL_COMMUTING_IDEMPOTENT_RANK_CHECKS_PASSED')


if __name__=='__main__':
    main()
