"""Independent finite checks for cyclic closure of bounded-jump 123-avoiders.

No third-party packages. Usage: python3 verify.py
Finite tests corroborate, but do not replace, the all-parameter proof.
"""
import itertools
from functools import lru_cache


def avoids_123(p):
    return not any(p[i] < p[j] < p[k]
                   for i in range(len(p))
                   for j in range(i + 1, len(p))
                   for k in range(j + 1, len(p)))


def cyclic_jumps_ok(p, m):
    return all(abs(p[i] - p[(i+1) % len(p)]) <= m
               for i in range(len(p)))


def witness(m):
    assert m >= 2
    return tuple([2*m+1]
                 + list(range(3*m+1, 2*m+1, -1))
                 + list(range(2*m, m+1, -1))
                 + list(range(m, 0, -1))
                 + [m+1])


def count_dynamic(n, m):
    """Exact count with independent combinatorial pruning.

    State 'tail' is the minimum second member of an increasing pair
    already present; appending x makes 123 iff x>tail.
    """
    full = (1 << n) - 1
    @lru_cache(None)
    def search(first, last, remaining, tail):
        if not remaining:
            return int(abs(last-first) <= m)
        total = 0
        used = full ^ remaining
        for x in range(max(1,last-m), min(n,last+m)+1):
            bit = 1 << (x-1)
            if not (remaining & bit) or x > tail:
                continue
            newtail = min(tail,x) if (used & (bit-1)) else tail
            total += search(first, x, remaining ^ bit, newtail)
        return total
    return sum(search(a,a,full ^ (1 << (a-1)),n+1) for a in range(1,n+1))


def main():
    direct_cases = 0
    for n in range(3,9):
        for m in range(1,5):
            direct = 0
            for p in itertools.permutations(range(1,n+1)):
                if avoids_123(p) and cyclic_jumps_ok(p,m):
                    direct += 1
                    assert m >= 2 and n <= 3*m+1
                    if n == 3*m+1:
                        assert (p[0], p[1], p[-2], p[-1]) == (2*m+1, n, 1, m+1)
            assert direct == count_dynamic(n,m), (n,m,direct,count_dynamic(n,m))
            direct_cases += 1
    print('direct_permutation_and_dynamic_counts: 24 cases PASS')
    upper_cases = 0
    expected = {(2,7):1,(2,8):0,(3,10):4,(3,11):0,
                (4,13):35,(4,14):0,(5,16):338,(5,17):0}
    for (m,n),target in expected.items():
        x = count_dynamic(n,m)
        assert x == target,(m,n,x,target)
        upper_cases += 1
    print('independent_extremal_counts: 8 cases PASS')
    for m in range(2,41):
        w=witness(m)
        n=3*m+1
        assert sorted(w) == list(range(1,n+1))
        assert cyclic_jumps_ok(w,m)
        assert avoids_123(w)
        assert (w[0],w[1],w[-2],w[-1]) == (2*m+1,n,1,m+1)
        for deleted in range(3):
            p=tuple(v for v in w if v <= n-deleted)
            assert len(p)==n-deleted
            assert cyclic_jumps_ok(p,m) and avoids_123(p)
    print('explicit_all_residue_constructions: 39 parameters, 117 cases PASS')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
