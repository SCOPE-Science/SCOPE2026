#!/usr/bin/env python3
"""Reproduce finite checks of higher-independence complexes of double stars.

Python 3 standard library only. Vertex order: a leaves at hub u, then b
leaves at hub v, then u, v. All computations are exact integers or F2.
"""
from itertools import permutations
from math import comb


def enumerate_faces(a, b, r):
    n = a + b + 2
    u, v = n - 2, n - 1
    adj = [0] * n
    for i in range(a):
        adj[i] |= 1 << u
        adj[u] |= 1 << i
    for j in range(a, a+b):
        adj[j] |= 1 << v
        adj[v] |= 1 << j
    adj[u] |= 1 << v
    adj[v] |= 1 << u
    result = set()
    for mask in range(1, 1 << n):
        unseen, good = mask, True
        while unseen:
            first = unseen & -unseen
            unseen ^= first
            frontier, size = first, 0
            while frontier:
                bit = frontier & -frontier
                frontier ^= bit
                size += 1
                extension = adj[bit.bit_length()-1] & unseen
                unseen ^= extension
                frontier |= extension
            if size > r:
                good = False
                break
        if good:
            result.add(mask)
    return result


def direct_criterion(a, b, r, mask):
    n = a + b + 2
    u, v = n - 2, n - 1
    u_on, v_on = bool(mask & (1 << u)), bool(mask & (1 << v))
    if u_on and v_on:
        return 2 + (mask & ((1 << (n-2)) - 1)).bit_count() <= r
    if u_on:
        return 1 + (mask & ((1 << a) - 1)).bit_count() <= r
    if v_on:
        return 1 + (mask & (((1 << b)-1) << a)).bit_count() <= r
    return True


def test_relative_collapse(a, b, r, faces):
    n = a + b + 2
    u, v = n-2, n-1
    active = {m for m in faces if (m & (1 << u) == 0) or (m & (1 << v) == 0)}
    initial = len(active)
    pairs = 0
    # Every face containing a hub is paired with the face adding a fixed
    # leaf at the opposite hub; descending-cardinality order is used.
    for hub, opposite_leaf in ((u, a), (v, 0)):
        lows = [m for m in active if m & (1 << hub) and not m & (1 << opposite_leaf)]
        lows.sort(key=lambda z: (-z.bit_count(), z))
        for low in lows:
            high = low | (1 << opposite_leaf)
            assert low in active and high in active, (a,b,r,'missing pair',low)
            strict = [f for f in active if f != low and (f & low) == low]
            assert strict == [high], (a,b,r,'not elementary free face',low,strict)
            active.remove(low)
            active.remove(high)
            pairs += 1
    expected = set(range(1, 1 << (n-2)))
    assert active == expected, (a,b,r,'collapse target',len(active),len(expected))
    assert initial == 2*pairs + len(active)
    return pairs


def betti_mod_two(faces, n):
    by_dim = [[f for f in faces if f.bit_count() == d + 1] for d in range(n)]
    for layer in by_dim:
        layer.sort()
    indices = [{f: i for i, f in enumerate(layer)} for layer in by_dim]
    ranks = [0]* (n+1)
    for d in range(1,n):
        pivots = {}
        for face in by_dim[d]:
            col, remaining = 0, face
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                col ^= 1 << indices[d-1][face ^ bit]
            while col:
                pivot = col.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = col
                    break
                col ^= pivots[pivot]
        ranks[d] = len(pivots)
    return [(d, len(by_dim[d])-ranks[d]-ranks[d+1]-(d==0))
            for d in range(n) if len(by_dim[d])-ranks[d]-ranks[d+1]-(d==0)]


def reduced_lefschetz(faces, n, perm):
    value = -1
    for face in faces:
        vertices = [i for i in range(n) if face & (1 << i)]
        targets = [perm[i] for i in vertices]
        if set(targets) != set(vertices):
            continue
        inversions = sum(targets[i] > targets[j]
                         for i in range(len(targets)) for j in range(i+1,len(targets)))
        value += (-1) ** (len(vertices)-1+inversions)
    return value


def augmentation_exterior_trace(perm, degree):
    seen = set()
    coeff = [1]
    for i in range(len(perm)):
        if i in seen:
            continue
        cur, length = i, 0
        while cur not in seen:
            seen.add(cur)
            length += 1
            cur = perm[cur]
        new = coeff + [0]*length
        for j,x in enumerate(coeff):
            new[j+length] += (-1)**(length-1)*x
        coeff = new
    divided = []
    prev = 0
    for c in coeff:
        v = c-prev
        divided.append(v)
        prev = v
    return divided[degree]


def symmetry_generators(a,b):
    n = a+b+2
    ret = []
    for base, size, name in ((0,a,'left'),(a,b,'right')):
        if size >= 2:
            p = list(range(n));p[base],p[base+1] = p[base+1],p[base]
            ret.append((name+'_transposition',p,1))
        if size >= 3:
            p = list(range(n));p[base],p[base+1],p[base+2] = base+1,base+2,base
            ret.append((name+'_3cycle',p,1))
    if a == b:
        p = list(range(a,2*a))+list(range(a))+[n-1,n-2]
        ret.append(('hub_interchange',p,-1))
        if a>=2:
            p2=p.copy()
            p2[0],p2[1] = p2[1],p2[0]
            ret.append(('hub_interchange_times_leaf_swap',p2,-1))
    return ret


def full_automorphism_group(a, b):
    n = a + b + 2
    u, v = n-2, n-1
    perms = []
    for aa in permutations(range(a)):
        for bb in permutations(range(a,a+b)):
            base = list(aa) + list(bb) + [u,v]
            perms.append(base)
            if a == b:
                # Compose a block-preserving permutation with full hub exchange.
                tau = list(range(a,2*a)) + list(range(a)) + [v,u]
                perms.append([tau[base[i]] for i in range(n)])
    assert len({tuple(p) for p in perms}) == len(perms)
    return perms


def test_quotient_ranks():
    checks = 0
    for a in range(1,4):
        for b in range(1,4):
            n = a+b+2
            group = full_automorphism_group(a,b)
            for r in range(2,n):
                fs = enumerate_faces(a,b,r)
                actual_numerator = sum((-1)**(r-1)*reduced_lefschetz(fs,n,g)
                                       for g in group)
                assert actual_numerator % len(group) == 0
                rank = actual_numerator // len(group)
                expected = int(r == 3 or (r == 2 and a != b))
                assert rank == expected, (a,b,r,'quotient',rank,expected)
                checks += 1
    return checks


def main():
    count_cases = count_homology = count_collapse = count_char = 0
    for a in range(1,5):
        for b in range(1,5):
            n = a+b+2
            for r in range(1,n+1):
                faces = enumerate_faces(a,b,r)
                expected_faces = {m for m in range(1,1<<n) if direct_criterion(a,b,r,m)}
                assert faces == expected_faces, (a,b,r,'face criterion')
                count_cases += 1
                if r == 1 or r == n:
                    target = []
                else:
                    target = [(r-1,comb(a+b-1,r-2))]
                euler = sum((-1)**(face.bit_count()-1) for face in faces)-1
                assert euler == sum((-1)**d*c for d,c in target), (a,b,r,'Euler')
                pairs = test_relative_collapse(a,b,r,faces)
                count_collapse += pairs
                if n <= 8:
                    assert betti_mod_two(faces,n)==target, (a,b,r,'F2 homology')
                    count_homology += 1
                if 2<=r<=n-1:
                    for name,p,hub_sign in symmetry_generators(a,b):
                        actual = (-1)**(r-1)*reduced_lefschetz(faces,n,p)
                        predicted = hub_sign*augmentation_exterior_trace(p[:n-2],r-2)
                        assert actual == predicted, (a,b,r,name,actual,predicted)
                        count_char += 1
    print('PASS: independently generated face models for',count_cases,'parameter triples')
    print('PASS: verified elementary relative collapses, total pairs',count_collapse)
    print('PASS: complete F2 chain homology in',count_homology,'parameter triples')
    print('PASS: reduced Lefschetz/exterior-character comparisons',count_char)
    print('PASS: quotient invariant ranks for',test_quotient_ranks(),'parameter triples')
    print('NOTE: finite tests corroborate but do not prove the general theorem')


if __name__ == '__main__':
    main()
