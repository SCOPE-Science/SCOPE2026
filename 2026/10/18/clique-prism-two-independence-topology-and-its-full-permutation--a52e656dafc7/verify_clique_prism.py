#!/usr/bin/env python3
"""Finite cross-checks for two-independence complexes of clique prisms.

Finite tests validate the face characterization, mod-two homology, and
signed Lefschetz traces; the proof for all n uses shellability and
an exact fixed-face argument, not extrapolation from these tests.
"""
from itertools import combinations, permutations
from math import comb, factorial
import random


def graph_adjacency(n):
    adj = [set() for _ in range(2*n)]
    for row in range(2):
        for i, j in combinations(range(n), 2):
            u, v = row*n+i, row*n+j
            adj[u].add(v); adj[v].add(u)
    for i in range(n):
        adj[i].add(n+i); adj[n+i].add(i)
    return adj


def is_two_independent(face, adj):
    remaining = set(face)
    while remaining:
        u = remaining.pop()
        component = {u}; frontier = [u]
        while frontier:
            v = frontier.pop()
            for w in adj[v].intersection(remaining):
                remaining.remove(w)
                component.add(w)
                frontier.append(w)
        if len(component) > 2:
            return False
    return True


def classified(face, n):
    a = {v for v in face if v < n}
    b = {v-n for v in face if v >= n}
    if len(a) > 2 or len(b) > 2:
        return False
    if not a.intersection(b):
        return True
    return len(a) == len(b) == 1


def face_layers(n):
    adj = graph_adjacency(n)
    layers = []
    for k in range(1, 5):
        actual = []
        for f in combinations(range(2*n), k):
            truth = is_two_independent(f, adj)
            rule = classified(f, n)
            assert truth == rule, (n, f, truth, rule)
            if truth:
                actual.append(f)
        layers.append(actual)
    return layers


def rank_gf2(cols):
    pivots = {}
    for col in cols:
        while col:
            j = col.bit_length()-1
            if j in pivots:
                col ^= pivots[j]
            else:
                pivots[j] = col
                break
    return len(pivots)


def homology_mod2(layers):
    ranks = [0, 0, 0, 0, 0]
    for k in range(1, 4):
        index = {f: i for i, f in enumerate(layers[k-1])}
        columns = []
        for f in layers[k]:
            col = 0
            for sub in combinations(f, k):
                col ^= 1 << index[sub]
            columns.append(col)
        ranks[k] = rank_gf2(columns)
    betti = [len(layers[k]) - ranks[k] - ranks[k+1] for k in range(4)]
    betti[0] -= 1
    return betti


def core_faces(n):
    result = [()]
    for a in range(3):
        for b in range(3):
            if a+b == 0: continue
            for left in combinations(range(n), a):
                for right in combinations(range(n), b):
                    if set(left).isdisjoint(right):
                        result.append(tuple(left)+tuple(n+i for i in right))
    return result


def image(face, n, perm, swap):
    return tuple(perm[v%n]+n*((v//n)^swap) for v in face)


def permutation_sign(z):
    return -1 if sum(z[i] > z[j] for i in range(len(z))
                     for j in range(i+1, len(z))) % 2 else 1


def lefschetz_top_character(n, perm, swap, faces):
    trace = 0
    for face in faces:
        destination = image(face, n, perm, swap)
        if set(destination) != set(face): continue
        lookup = {v:i for i,v in enumerate(sorted(face))}
        trace += (-1)**len(face)*permutation_sign([lookup[v] for v in destination])
    return trace


def character_formula(n, perm, swap):
    visited = set(); cycles = {}
    for i in range(n):
        if i in visited: continue
        j = i; length = 0
        while j not in visited:
            visited.add(j)
            length += 1
            j = perm[j]
        cycles[length] = cycles.get(length, 0)+1
    f, t = cycles.get(1,0), cycles.get(2,0)
    if swap:
        return 1 - 2*t + 4*comb(t, 2) - 2*cycles.get(4,0)
    s = 0
    for a in range(3):
        for b in range(3):
            for i in range(t+1):
                for j in range(t-i+1):
                    u, v = a-2*i, b-2*j
                    if u < 0 or v < 0 or u+v > f: continue
                    choices = (factorial(f) // (factorial(u)*factorial(v)*factorial(f-u-v)))
                    choices *= factorial(t)//(factorial(i)*factorial(j)*factorial(t-i-j))
                    s += (-1)**(u+v+i+j) * choices
    return s


def beta(n):
    return 1-2*n+2*n*(n-1)-n*(n-1)*(n-2)+comb(n,2)*comb(n-2,2)


def main():
    for n in range(5, 10):
        layers = face_layers(n)
        ranks = homology_mod2(layers)
        want = [0,n,0,beta(n)]
        assert ranks == want, (n,ranks,want)
        print(f'n={n}: face_vector={[len(x) for x in layers]}, reduced_F2_betti={ranks}; PASS')
    for n in (5,6):
        all_p = list(permutations(range(n)))
        if n == 6:
            all_p = random.Random(5).sample(all_p, 60)
        faces = core_faces(n)
        for perm in all_p:
            for swap in (0,1):
                got = lefschetz_top_character(n,perm,swap,faces)
                want = character_formula(n,perm,swap)
                assert got == want, (n,perm,swap,got,want)
        print(f'n={n}: signed_Lefschetz_checks={2*len(all_p)}; PASS')
    print('Finite checks passed; no infinite conclusion inferred from enumeration.')


if __name__ == '__main__':
    main()
