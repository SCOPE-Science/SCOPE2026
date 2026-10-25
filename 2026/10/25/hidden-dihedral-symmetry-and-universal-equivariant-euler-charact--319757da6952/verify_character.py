"""Exact finite-orbit certificate for the bidirected K_(2,n) multipath Lefschetz formula.

Python >= 3.9; standard library only. Run: python verify_bidirected_k2n_character.py
The coefficient certificate involves every partition of total cycle support <= 4;
the support bound (at most one arc of each of four types) is mathematical.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb, prod

MATCHINGS = {frozenset((0, 3)), frozenset((1, 2))}
IDENTITY = (0, 1, 2, 3)
HALFTURN = (3, 2, 1, 0)
SINGLE_FLIP = (3, 1, 2, 0)
PAIR_SWAP = (1, 0, 3, 2)
QUARTERTURN = (1, 3, 0, 2)
REPS = (IDENTITY, HALFTURN, SINGLE_FLIP, PAIR_SWAP, QUARTERTURN)


def admissible(face, n):
    """Equivalent to arc-set indegree/outdegree <= 1 and no directed cycle."""
    types = [v // n for v in face]
    if len(set(types)) != len(types):
        return False
    at_leaf = {}
    for v in face:
        at_leaf.setdefault(v % n, set()).add(v // n)
    seen_a = seen_b = False
    for selected in at_leaf.values():
        if len(selected) > 2:
            return False
        if len(selected) == 2:
            if frozenset(selected) not in MATCHINGS:
                return False
            seen_a |= selected == {0, 3}
            seen_b |= selected == {1, 2}
    return not (seen_a and seen_b)


def direct_digraph_test(face, n):
    """Independent reference test, constructed using actual directed arcs."""
    arcs = [(0, 2 + i) for i in range(n)] + [(1, 2 + i) for i in range(n)]
    arcs += [(2 + i, 0) for i in range(n)] + [(2 + i, 1) for i in range(n)]
    inc, out, nxt = set(), set(), {}
    for arc_id in face:
        source, target = arcs[arc_id]
        if source in out or target in inc:
            return False
        out.add(source)
        inc.add(target)
        nxt[source] = target
    for source in out:
        visited = set()
        v = source
        while v in nxt:
            if v in visited:
                return False
            visited.add(v)
            v = nxt[v]
    return True


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for i in range(minimum, n + 1):
            for rest in partitions(n - i, i):
                yield (i,) + rest


def cyclic_leaf_permutation(partition):
    sigma = list(range(sum(partition)))
    base = 0
    for length in partition:
        for j in range(length):
            sigma[base + j] = base + (j + 1) % length
        base += length
    return sigma


def signed_augmented_lefschetz(partition, type_perm):
    n = sum(partition)
    if n == 0:
        return 1
    sigma = cyclic_leaf_permutation(partition)
    vertex_action = [type_perm[i // n] * n + sigma[i % n] for i in range(4 * n)]
    total = 1  # the empty face, with augmented simplicial sign
    for k in range(1, 5):
        for face in combinations(range(4 * n), k):
            if not admissible(face, n):
                continue
            transported = [vertex_action[v] for v in face]
            if set(transported) != set(face):
                continue
            parity = sum(transported[i] > transported[j]
                         for i in range(k) for j in range(i + 1, k))
            total += (-1) ** (k + parity)
    return total


def cycles_from_counts(counts):
    return tuple(length for length, count in enumerate(counts, 1)
                 for _ in range(count))


def polynomial(counts, rep_index):
    a, b, _, d = counts
    choose = lambda x, k: comb(x, k) if x >= k else 0
    if rep_index == 0:
        return 1 - 2*a + 4*choose(a,2) - 12*choose(a,3) + 24*choose(a,4)
    if rep_index == 1:
        return 1-2*a-4*b+4*a*b+8*choose(b,2)
    if rep_index == 2:
        return (1-2*a-2*b+6*choose(a,2)+2*a*b-6*choose(a,3)
                -4*b*choose(a,2))
    if rep_index == 3:
        return 1-4*b+8*choose(b,2)
    return 1-4*d


def templates():
    result = []
    for a in range(5):
        for b in range(3):
            for c in range(2):
                for d in range(2):
                    k = (a,b,c,d)
                    if a + 2*b + 3*c + 4*d <= 4:
                        result.append(k)
    return sorted(result, key=lambda k:(sum((i+1)*z for i,z in enumerate(k)),k))


def coeff_via_finite_difference(template, type_perm, eval_cache):
    coeff = 0
    for sub in product(*(range(x+1) for x in template)):
        coeff += ((-1)**(sum(template)-sum(sub))
                  * prod(comb(template[j], sub[j]) for j in range(4))
                  * eval_cache[(sub,type_perm)])
    return coeff


def main():
    symmetries = [p for p in permutations(range(4))
                  if {frozenset((p[0],p[3])),frozenset((p[1],p[2]))} == MATCHINGS]
    assert len(symmetries) == 8 and len(set(REPS)) == 5
    face_tests=0
    symmetry_tests=0
    for n in range(1, 6):
        for k in range(5):
            for face in combinations(range(4*n),k):
                assert admissible(face,n)==direct_digraph_test(face,n)
                face_tests+=1
                if not admissible(face,n):
                    continue
                for tau in symmetries:
                    image=tuple(tau[v//n]*n+v%n for v in face)
                    assert admissible(image,n)
                    symmetry_tests+=1
    print('FACE_DIGRAPH_EQUIVALENCE:',face_tests,'sets')
    print('ALL_EIGHT_DIHEDRAL_ACTIONS:',symmetry_tests,'face transformations')

    input_templates=templates()
    cache={}
    for c in input_templates:
        part=cycles_from_counts(c)
        for tau in REPS:
            cache[(c,tau)] = signed_augmented_lefschetz(part,tau)
    expected={
        0:{(0,0,0,0):1,(1,0,0,0):-2,(2,0,0,0):4,(3,0,0,0):-12,(4,0,0,0):24},
        1:{(0,0,0,0):1,(1,0,0,0):-2,(0,1,0,0):-4,(1,1,0,0):4,(0,2,0,0):8},
        2:{(0,0,0,0):1,(1,0,0,0):-2,(0,1,0,0):-2,(2,0,0,0):6,(1,1,0,0):2,(3,0,0,0):-6,(2,1,0,0):-4},
        3:{(0,0,0,0):1,(0,1,0,0):-4,(0,2,0,0):8},
        4:{(0,0,0,0):1,(0,0,0,1):-4},
    }
    for i,tau in enumerate(REPS):
        got={c: coeff_via_finite_difference(c,tau,cache) for c in input_templates}
        got={c:v for c,v in got.items() if v}
        assert got==expected[i],(i,got)
        print('DIHEDRAL_CLASS',i,'WEIGHTED_CYCLE_COEFFICIENTS',sorted(got.items()))
    assert len(input_templates)==12
    print('ALL_EXHAUSTIVE_CYCLE_TEMPLATES:',len(input_templates))

    compared=0
    for n in range(1, 8):
        for partition in partitions(n):
            c=tuple(partition.count(i) for i in (1,2,3,4))
            for j,tau in enumerate(REPS):
                actual=signed_augmented_lefschetz(partition,tau)
                assert actual==polynomial(c,j),(partition,j,actual,polynomial(c,j))
                compared+=1
    print('DIRECT_FULL_COMPLEX_CHARACTER_COMPARISONS:',compared)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':
    main()
