"""Reproducibility checks for faithful representation dimensions of mixed extraspecial-by-abelian groups.
Only Python's standard library is required.
"""
from itertools import combinations, product
from math import prod


def predicted(weights, extra_ranks):
    # weights are (prime, irreducible-degree), one extraspecial factor per prime
    ps = {p for p, _ in weights}
    t = len(weights)
    assert t >= 1 and len(ps) == t
    rank = max([1 + extra_ranks.get(p, 0) for p in ps]
               + [r for p, r in extra_ranks.items() if p not in ps]
               + [1])
    return sum(w for _, w in weights) + max(0, rank - t)


def direct_discrete_optimization(weights, extra_ranks):
    """Independent finite weighted-cover optimization of permitted irreducible row types.
    A row tensoring the nonlinear irreducibles indexed by mask has cost
    product of their degrees. Other factors can act via linear characters.
    Since A is arbitrary abelian, sufficient central rank is available iff
    N>=R and every extraspecial center occurs in some row.
    """
    t = len(weights)
    full = (1 << t) - 1
    primes = {p for p, _ in weights}
    R = max([1 + extra_ranks.get(p, 0) for p in primes]
            + [r for p, r in extra_ranks.items() if p not in primes]
            + [1])
    cutoff = sum(w for _, w in weights) + max(0, R - t)
    # shortest path in (covered-mask, num-rows), with positive integer costs
    dp = {0: 0}
    best = float('inf')
    for rows in range(1, cutoff + 1):
        nx = {}
        for covered, c in dp.items():
            for mask in range(1 << t):
                co = prod(weights[i][1] for i in range(t) if mask >> i & 1)
                newmask = covered | mask
                val = c + co
                if val < nx.get(newmask, float('inf')):
                    nx[newmask] = val
        if rows >= R:
            best = min(best, nx.get(full, float('inf')))
        dp = {mask: c for mask, c in nx.items() if c < best and c <= cutoff}
        if not dp:
            break
    return best


def d8_matrices():
    def mm(a,b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    I=((1,0),(0,1)); r=((0,-1),(1,0)); s=((1,0),(0,-1))
    out=[]; rk=I
    for k in range(4):
        out.extend((rk,mm(rk,s)))
        rk=mm(rk,r)
    assert len(set(out))==8
    return out


def exact_matrix_rep_check():
    # Element r^i s^j of D8 represented by integer matrices; C3 uses omega.
    # In Q(omega), omega^2=-1-omega. Each entry is represented exactly as (a,b).
    wcoeff=((1,0),(0,1),(-1,-1))
    seen=set()
    for mat,k in product(d8_matrices(),range(3)):
        a,b=wcoeff[k]
        matrix=tuple((a*x,b*x) for row in mat for x in row)
        assert matrix not in seen
        seen.add(matrix)
    assert len(seen)==24
    # D8 times C3^2: pair the 2D char of D8 with first C3 char,
    # and an independent 1D character with the second C3 factor.
    seen=set()
    for mat,k,l in product(d8_matrices(),range(3),range(3)):
        a,b=wcoeff[k]
        first=tuple((a*x,b*x) for row in mat for x in row)
        rep=(first,wcoeff[l])
        assert rep not in seen
        seen.add(rep)
    assert len(seen)==72
    return len(seen)


def main():
    cases=0
    for t in (1,2,3):
        # The primes are distinct, so all weights are powers of distinct primes.
        ps=(2,3,5)[:t]
        for ns in product((1,2),repeat=t):
            weights=list(zip(ps,(p**n for p,n in zip(ps,ns))))
            for rp in product(range(4), repeat=3):
                extra_ranks=dict(zip((2,3,7),rp))
                x=predicted(weights,extra_ranks)
                y=direct_discrete_optimization(weights,extra_ranks)
                assert x == y, (weights, extra_ranks, x, y)
                cases+=1
    assert predicted([(2,2)],{3:1})==2
    assert predicted([(2,2)],{3:2})==3
    assert predicted([(2,2),(3,3)],{})==5
    assert predicted([(2,2),(3,3)],{2:2,3:3,7:4})==7
    group_elements=exact_matrix_rep_check()
    print('OPTIMIZATION_CASES',cases,'EXACT_D8_x_C3^2_ELEMENTS',group_elements,'VERIFY_OK')

if __name__=='__main__':
    main()
