"""Finite reproducibility checks for crown-graph acyclic orientation sink formulas.

No external packages are required. The theorem is proved symbolically in RESULT.md;
this script compares its formulas with direct finite colorings and orientations.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, factorial


@lru_cache(None)
def ordinary_stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k <= 0 or k > n:
        return 0
    return k * ordinary_stirling(n - 1, k) + ordinary_stirling(n - 1, k - 1)


@lru_cache(None)
def nonsingleton_stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k <= 0 or k > n:
        return 0
    return sum((-1)**j * comb(n, j) * ordinary_stirling(n-j, k-j)
               for j in range(min(n, k) + 1))


def chromatic_formula(m, n, q):
    total = 0
    for p in range(m + 1):
        falling = 1
        for j in range(p):
            falling *= q-j
        for k in range(p + 1):
            ways = comb(m, k) * nonsingleton_stirling(m-k, p-k)
            if ways:
                total += ways * falling * (q-p)**(n-k) * (q-p+1)**k
    return total


@lru_cache(None)
def acyclic_formula(m, n):
    return (-1)**(m+n) * chromatic_formula(m, n, -1)


def sink_formula(n):
    # Formula in RESULT.md. Coefficients are indexed by the number of sinks.
    s = [0]*(n+1)
    cn = acyclic_formula(n, n)
    for k in range(n+1):
        multiplicity = comb(n,k)
        for j in range(k+1):
            s[j] += 2*multiplicity*comb(k,j)*(-1)**(k-j)*acyclic_formula(n-k,n)
    s[0] -= cn
    a = acyclic_formula(n-1,n-1)
    s[0] += n*a
    s[1] -= 2*n*a
    s[2] += n*a
    return s


def brute_chromatic(m, n, q):
    e = [(i, m+j) for i in range(m) for j in range(n) if i != j]
    return sum(all(c[u] != c[v] for u,v in e)
               for c in product(range(q), repeat=m+n))


def direct_orientation_census(n):
    # Explicitly orient each edge; independently reject directed cycles by
    # Kahn's topological deletion algorithm; then count zero-outdegree vertices.
    e = [(i,n+j) for i in range(n) for j in range(n) if i != j]
    seen=Counter()
    accepted=0
    for mask in range(1<<len(e)):
        out=[[] for _ in range(2*n)]
        indeg=[0]*(2*n)
        for k,(u,v) in enumerate(e):
            if (mask>>k)&1: u,v=v,u
            out[u].append(v); indeg[v]+=1
        queue=[i for i,d in enumerate(indeg) if d==0]
        h=0
        while h<len(queue):
            v=queue[h];h+=1
            for w in out[v]:
                indeg[w]-=1
                if indeg[w]==0:queue.append(w)
        if len(queue)!=2*n:continue
        accepted+=1
        sinks=tuple(i for i in range(2*n) if not out[i])
        seen[sinks]+=1
    return seen,accepted


def eval_multivar_from_formula(n, xs, ys):
    # The full multivariate expression in the theorem (integer substitutions).
    ans = -acyclic_formula(n,n)
    for values in [xs,ys]:
        for mask in range(1<<n):
            v=acyclic_formula(n-mask.bit_count(),n)
            for i in range(n):
                if mask>>i&1:v*=values[i]-1
            ans+=v
    a=acyclic_formula(n-1,n-1)
    for i in range(n):ans+=a*(xs[i]-1)*(ys[i]-1)
    return ans


def main():
    color_checks=0;orientation_checks=0;multivar_checks=0
    for m in range(0,5):
        for n in range(max(1,m),6):
            if m+n>8: continue
            for q in range(1,5):
                assert chromatic_formula(m,n,q)==brute_chromatic(m,n,q),(m,n,q)
                color_checks+=1
    for n in (2,3,4):
        seen,total=direct_orientation_census(n)
        expected=sink_formula(n)
        assert total==acyclic_formula(n,n)==sum(expected),(n,total,expected)
        actual=[0]*(n+1)
        for subset,c in seen.items():
            actual[len(subset)]+=c
        assert actual==expected,(n,expected,actual)
        orientation_checks+=1<<n*(n-1)
        # Test the whole multivariate polynomial at two independent assignments.
        for shift in (0,1):
            xs=[2+i+shift for i in range(n)]
            ys=[3+2*i+shift for i in range(n)]
            direct=sum(c*__import__('math').prod(
                       xs[v] if v<n else ys[v-n] for v in subset)
                       for subset,c in seen.items())
            assert eval_multivar_from_formula(n,xs,ys)==direct,(n,shift)
            multivar_checks+=1
    assert sink_formula(3)==[0,30,30,2]
    assert sink_formula(4)==[0,1064,740,56,2]
    assert sink_formula(5)==[0,52770,32250,3060,150,2]
    assert sink_formula(6)==[0,3747852,2094402,234360,15630,372,2]
    # The cubic P(z)=z^3+28*z^2+370*z+532 has discriminant < 0.
    a,b,c,d=1,28,370,532
    discriminant=b*b*c*c-4*a*c*c*c-4*b*b*b*d-27*a*a*d*d+18*a*b*c*d
    assert discriminant==-50430544
    print('VERIFY_OK color_checks=%d orientation_bitstrings=%d multivariate_checks=%d cubic_discriminant=%d' %
          (color_checks,orientation_checks,multivar_checks,discriminant))


if __name__=='__main__':
    main()
