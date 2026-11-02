"""Exact rational verification of the random-priority greedy independent-set law.

Self-contained Python 3.9+; run: python check_greedy_c4free.py
Only finite cases are checked; the general theorem is proved separately.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

CHECKS = 0

def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)

def complement_adjacencies(n, missing):
    adj = [0]*(2*n)
    for u in range(n):
        for v in range(n):
            if (u,v) not in missing:
                adj[u] |= 1 << (n+v)
                adj[n+v] |= 1 << u
    return adj

def greedy_order(order, adj):
    chosen = 0
    for v in order:
        if not (chosen & adj[v]):
            chosen |= 1 << v
    return chosen

def exact_distribution(adj):
    count = len(adj)
    @lru_cache(None)
    def go(available):
        if available == 0:
            return {0: Fraction(1)}
        k = available.bit_count()
        result = {}
        for v in range(count):
            if (available >> v) & 1:
                further = available & ~(1 << v | adj[v])
                for suffix, prob in go(further).items():
                    key = suffix | 1 << v
                    result[key] = result.get(key, Fraction(0)) + prob / k
        return result
    d = go((1 << count)-1)
    require(sum(d.values()) == 1, 'distribution normalization')
    return d

def from_cycles(lengths):
    n = sum(lengths)
    missing = set()
    first = 0
    for length in lengths:
        require(length >= 3, 'cycles length >= 3 for C4-free')
        for j in range(length):
            missing.add((first+j, first+j))
            missing.add((first+j, first+(j+1)%length))
        first += length
    return n,missing,2

def from_perfect_matching(n):
    return n,{(i,i) for i in range(n)},1

def from_fano():
    # Fano plane incidence: seven shifts of the difference set {0,1,3}.
    n = 7
    missing = {(j,(i+j)%n) for i in range(n) for j in (0,1,3)}
    # More transparently, first coordinate is a point, second is a line.
    missing = {((i+k)%n, i) for i in range(n) for k in (0,1,3)}
    return n,missing,3

def is_C4_free(n, missing):
    nn=[{v for u,v in missing if u == i} for i in range(n)]
    return all(len(nn[u]&nn[v]) < 2 for u in range(n) for v in range(u+1,n))

def test_graph(n, missing, degree):
    require(is_C4_free(n, missing), 'no C4')
    require(all(sum(u==i for u,v in missing)==degree for i in range(n)), 'left-regular')
    require(all(sum(v==j for u,v in missing)==degree for j in range(n)), 'right-regular')
    require(n >= degree + 2, 'distinct sizes')
    d = exact_distribution(complement_adjacencies(n,missing))
    p = Fraction(degree*n, (n+degree-1)*(n-degree+1))
    full_u = (1<<n)-1
    full_v = full_u << n
    require(d.get(full_u,0) == (1-p)/2, 'pure left atom')
    require(d.get(full_v,0) == (1-p)/2, 'pure right atom')
    require(set(key.bit_count() for key in d) == {n,degree+1}, 'two sizes')
    require(sum(prob for key,prob in d.items() if key.bit_count()==degree+1)==p, 'rare atom')
    expected = n - (n-degree-1)*p
    variance = (n-degree-1)**2*p*(1-p)
    require(sum(Fraction(key.bit_count())*v for key,v in d.items()) == expected, 'exact mean')
    require(sum((key.bit_count()-expected)**2*v for key,v in d.items()) == variance, 'exact variance')
    if degree == 1:
        for u,v in missing:
            require(d.get((1<<u)|(1<<(n+v)),0) == p/n, 'matching pair atom')
        require(len(d)==n+2, 'count of distinct outcomes')
    else:
        for u in range(n):
            key = (1<<u) | sum(1<<(n+v) for uu,v in missing if uu==u)
            require(d.get(key,0)==p/(2*n),'left-centered uniform star')
        for v in range(n):
            key = (1<<(n+v)) | sum(1<<u for u,vv in missing if vv==v)
            require(d.get(key,0)==p/(2*n),'right-centered uniform star')
        require(len(d)==2*n+2, 'count of distinct outcomes')
    return len(d),p

def exhaustive_check():
    n,missing,_=from_cycles([4])
    adj=complement_adjacencies(n,missing)
    dist=exact_distribution(adj)
    outcomes=Counter(greedy_order(order,adj) for order in permutations(range(2*n)))
    require(sum(outcomes.values()) == 40320, 'exhaustive orders count')
    for k,p in dist.items():require(Fraction(outcomes[k],40320)==p,'permutation-vs-DP')


def boundary_check():
    # Two missing 4-cycles, so the C4-free hypothesis fails.
    n=4
    H={(u,v) for k in (0,2) for u in (k,k+1) for v in (k,k+1)}
    require(not is_C4_free(n,H),'C4 present')
    dist=exact_distribution(complement_adjacencies(n,H))
    require({k.bit_count() for k in dist} == {4}, 'C4 changes support')


def main():
    print('exact tests:')
    cases = [from_perfect_matching(n) for n in range(3,10)]
    cases += [from_cycles([n]) for n in range(4,10)]
    cases += [from_cycles([3,3]), from_cycles([3,4]), from_cycles([4,4]), from_cycles([3,3,3]),from_fano()]
    for n,H,deg in cases:
        support,p=test_graph(n,H,deg)
        print(f' n={n:2d}, missing degree={deg}, outcomes={support:2d}, bad probability={p}')
    exhaustive_check()
    boundary_check()
    print(f'PASS {CHECKS} independent exact checks')

if __name__=='__main__':main()
