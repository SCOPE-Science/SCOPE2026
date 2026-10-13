"""Independent direct-subset checks for minimal defensive alliances on balanced multipartite graphs.

Pure Python 3, no third-party dependencies. Run: python verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def threshold(r, n):
    return ((r - 1) * n) // 2  # ceil(((r-1)n-1)/2)


def is_alliance(mask, neighbor_masks):
    if mask == 0:
        return False
    for v, nv in enumerate(neighbor_masks):
        if mask & (1 << v):
            internal = (nv & mask).bit_count()
            external = (nv & ~mask).bit_count()
            if internal + 1 < external:
                return False
    return True


def exact_polynomial(r, n):
    vertex_count = r * n
    parts = [((1 << n) - 1) << (n * j) for j in range(r)]
    all_vertices = (1 << vertex_count) - 1
    neighbors = [all_vertices ^ parts[v // n] for v in range(vertex_count)]
    eligible = bytearray(1 << vertex_count)
    strict_suballiance = bytearray(1 << vertex_count)
    output = Counter()
    for mask in range(1, 1 << vertex_count):
        eligible[mask] = is_alliance(mask, neighbors)
        sub = mask
        any_proper = False
        while sub:
            lsb = sub & -sub
            child = mask ^ lsb
            if eligible[child] or strict_suballiance[child]:
                any_proper = True
                break
            sub ^= lsb
        strict_suballiance[mask] = any_proper
        if eligible[mask] and not any_proper:
            output[mask.bit_count()] += 1
    return output


def formula_polynomial(r, n):
    t = threshold(r, n)
    out = Counter()
    # Occupancy vector (s_1,...,s_r) with 0 <= s_i <= n.
    # Each vertex selection contributes binomial(n,s_i).
    def walk(i, total, mx, multiplicity, ways):
        if i == r:
            if total > 0 and total-mx == t and multiplicity >= 2:
                out[total] += ways
            return
        for count in range(n + 1):
            if count > mx:
                walk(i+1, total+count, count, 1, ways*comb(n,count))
            elif count == mx:
                walk(i+1, total+count, mx, multiplicity+1, ways*comb(n,count))
            else:
                walk(i+1, total+count, mx, multiplicity, ways*comb(n,count))
    walk(0,0,0,0,1)
    return out


def coefficient_formula(r, n):
    t = threshold(r, n)
    out = Counter()
    for a in range(1, n + 1):
        # f_a(z) = sum_{j=0}^a binom(n,j) z^j
        coeff = [comb(n,j) for j in range(a+1)]
        by_k = {0:[1]}
        for power in range(1,r+1):
            last=by_k[power-1]
            nxt=[0]*(len(last)+a)
            for j,v in enumerate(last):
                for u,w in enumerate(coeff):
                    nxt[j+u]+=v*w
            by_k[power]=nxt
        ct=0
        for k in range(2,r+1):
            wanted = t - (k-1)*a
            arr = by_k[r-k]
            if 0 <= wanted < len(arr):
                ct += (-1)**(k-2)*(k-1)*comb(r,k)*comb(n,a)**k*arr[wanted]
        if ct:
            out[t+a] += ct
    return out


def maximum_multiplicity(r, n):
    t=threshold(r,n)
    return sum((-1)**(k-2)*(k-1)*comb(r,k)*comb((r-k)*n,t-(k-1)*n)
               for k in range(2,r+1) if 0<=t-(k-1)*n<=(r-k)*n)


def main():
    checked=0
    direct_masks=0
    tests=[(r,n) for r in range(3,7) for n in range(2,6) if r*n<=17]
    for r,n in tests:
        from_masks=exact_polynomial(r,n)
        by_profiles=formula_polynomial(r,n)
        by_ie=coefficient_formula(r,n)
        assert from_masks==by_profiles==by_ie,(r,n,from_masks,by_profiles,by_ie)
        t=threshold(r,n)
        assert max(from_masks)==n+t
        assert from_masks[n+t]==maximum_multiplicity(r,n)
        checked+=1
        direct_masks += (1<<(r*n))-1
        print('PASS',r,n,'t=',t,'coefficients=',sorted(from_masks.items()),'maximum_count=',maximum_multiplicity(r,n))
    # Larger symbolic checks avoid exponential vertex-subset traversal.
    large_tests=0
    for r in range(3,7):
        for n in range(2,7):
            if r*n<=17: continue
            assert formula_polynomial(r,n)==coefficient_formula(r,n),(r,n)
            p=formula_polynomial(r,n)
            assert max(p)==threshold(r,n)+n
            assert p[max(p)]==maximum_multiplicity(r,n)
            large_tests+=1
    print('ALL_PASS direct_graphs=',checked,'direct_candidate_masks=',direct_masks,'larger_profile_checks=',large_tests)


if __name__=='__main__':
    main()
