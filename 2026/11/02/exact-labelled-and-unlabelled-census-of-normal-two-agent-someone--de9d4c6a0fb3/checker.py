"""Independent finite checks for the exact normality census of two S5 agents.

Run with python3 checker.py. No third-party packages are required.
"""
from functools import lru_cache
from itertools import permutations
from math import comb

@lru_cache(None)
def partitions(n):
    if n == 0:
        return ((),)
    out = []
    for p in partitions(n - 1):
        out.append(p + ((n - 1,),))
        for j in range(len(p)):
            q = list(p)
            q[j] = q[j] + (n - 1,)
            out.append(tuple(q))
    return tuple(out)

def classes(part, n):
    result = [0] * n
    for cls in part:
        mask = sum(1 << v for v in cls)
        for v in cls:
            result[v] = mask
    return tuple(result)

def nested(E, F):
    return all((x & y) == x or (x & y) == y for x, y in zip(E, F))

def dominance(E, F):
    return all((x & y) == x for x, y in zip(E, F)) or all((x & y) == y for x, y in zip(E, F))

def incidence_is_star_forest(p, q):
    x = [set(block) for block in p]
    y = [set(block) for block in q]
    neighbors_x = [[j for j, block in enumerate(y) if a & block] for a in x]
    neighbors_y = [[i for i, block in enumerate(x) if b & block] for b in y]
    return all(len(neighbors_x[i]) == 1 or len(neighbors_y[j]) == 1
               for i in range(len(x)) for j in neighbors_x[i])

def operator(classes_, A):
    return sum(1 << i for i, block in enumerate(classes_) if (block & A) == block)

def is_meet_preserving(E, F, n):
    op = [operator(E, A) | operator(F, A) for A in range(1 << n)]
    return all(op[A & B] == (op[A] & op[B])
               for A in range(1 << n) for B in range(1 << n))

def is_distributed_knowledge(E, F, n):
    return all((operator(E, A) | operator(F, A)) ==
               operator(tuple(x & y for x, y in zip(E, F)), A)
               for A in range(1 << n))

def equivalence_signature(classes_, permutation):
    return tuple(int(classes_[permutation[i]] & (1 << permutation[j]) != 0)
                 for i in range(len(permutation)) for j in range(i + 1, len(permutation)))

def canonical_pair(E, F, n):
    return min((equivalence_signature(E, p), equivalence_signature(F, p))
               for p in permutations(range(n)))

N = 8
bell = [len(partitions(n)) for n in range(N + 1)]
labelled = [1]
for n in range(1, N + 1):
    labelled.append(sum(comb(n-1,j-1) * (2*bell[j]-1) * labelled[n-j]
                        for j in range(1, n+1)))
assert labelled == [1,1,4,19,111,774,6229,56529,569354]

# Number of partitions of integer m, counted independently by recursion.
@lru_cache(None)
def integer_partitions(m, minimum=1):
    if m == 0: return 1
    return sum(integer_partitions(m-j,j) for j in range(minimum,m+1))

# Coefficients of product_{m>=1} (1-z^m)^-(2p(m)-1).
unlabelled = [1]+[0]*N
for m in range(1,N+1):
    for _ in range(2*integer_partitions(m)-1):
        for j in range(m,N+1):
            unlabelled[j] += unlabelled[j-m]
assert unlabelled == [1,1,4,9,24,52,125,268,598]

for n in range(1,7):
    parts = partitions(n)
    classes_list = [classes(p,n) for p in parts]
    admissible = []
    globally_dominating = 0
    for i, E in enumerate(classes_list):
        for j, F in enumerate(classes_list):
            yes = nested(E,F)
            assert yes == incidence_is_star_forest(parts[i],parts[j]), (n,i,j)
            if n <= 4:
                assert yes == is_meet_preserving(E,F,n), (n,i,j)
                assert yes == is_distributed_knowledge(E,F,n), (n,i,j)
            if yes:
                admissible.append((E,F))
                globally_dominating += dominance(E,F)
    assert len(admissible) == labelled[n], (n,len(admissible),labelled[n])
    H = sum(__import__('math').prod(bell[len(block)] for block in p) for p in parts)
    assert globally_dominating == 2*H-bell[n]
    if n <= 5:
        orbits = {canonical_pair(E,F,n) for E,F in admissible}
        assert len(orbits) == unlabelled[n], (n,len(orbits),unlabelled[n])
    if n == 4:
        assert len(admissible)-globally_dominating == 6
    print('n=%d labelled=%d globally_comparable=%d locally_only=%d unlabelled=%d' %
          (n,len(admissible),globally_dominating,len(admissible)-globally_dominating,unlabelled[n]))
print('ALL_CHECKS_OK')
