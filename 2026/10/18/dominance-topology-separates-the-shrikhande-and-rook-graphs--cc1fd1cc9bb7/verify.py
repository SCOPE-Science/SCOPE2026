"""Exhaustive certificate for dominance complexes of two 16-vertex strongly regular graphs.

Usage: python verify.py
Only Python's standard library is required.
"""
from collections import Counter, deque
from hashlib import sha256

N = 16
FULL = (1 << N) - 1
DIRECTIONS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}


def graph(kind):
    rows = []
    for a in range(N):
        x, y = a % 4, a // 4
        row = 0
        for b in range(N):
            X, Y = b % 4, b // 4
            if a != b and ((kind == 'Shrikhande' and ((X-x) % 4, (Y-y) % 4) in DIRECTIONS)
                           or (kind == 'rook' and (X == x or Y == y))):
                row |= (1 << b)
        rows.append(row)
    return rows


def graph_properties(rows):
    assert all(r.bit_count() == 6 for r in rows)
    assert all((rows[a] >> b & 1) == (rows[b] >> a & 1) for a in range(N) for b in range(N))
    assert all((rows[a] & rows[b]).bit_count() == 2 for a in range(N) for b in range(a+1, N))
    return 48


def complex_faces(rows):
    closed = [rows[v] | (1 << v) for v in range(N)]
    faces = bytearray(1 << N)
    for s in range(1 << N):
        # Two independent evaluations of the defining condition:
        forbidden = any((s & c) == c for c in closed)
        complement = FULL ^ s
        dominating = all((c & complement) != 0 for c in closed)
        assert forbidden != dominating
        if dominating: faces[s] = 1
    assert faces[0] == 1
    assert all(not faces[s] or all(faces[s ^ (1 << v)] for v in range(N) if s >> v & 1)
               for s in range(1 << N))
    return faces


def matching(faces):
    available = faces[:]
    pairs = []
    for v in range(N):
        for s in range(1 << N):
            if not available[s] or (s >> v & 1): continue
            larger = s | (1 << v)
            if available[larger]:
                available[s] = available[larger] = 0
                pairs.append((s, larger))
    return pairs, [s for s in range(1 << N) if available[s]]


def check_directed_hasse(faces, pairs):
    # Unmatched cover arrows point downward. Matched covers point upward.
    # A completed topological sort is an exhaustive acyclicity certificate.
    matched = {upper: lower for lower, upper in pairs}
    assert len(matched) == len(pairs)
    indegree = [0] * (1 << N)
    edges = 0
    for upper in range(1, 1 << N):
        if not faces[upper]: continue
        for v in range(N):
            if not (upper >> v & 1): continue
            lower = upper ^ (1 << v)
            assert faces[lower]
            edges += 1
            if matched.get(upper) == lower: indegree[upper] += 1
            else: indegree[lower] += 1
    queue = deque(s for s in range(1 << N) if faces[s] and indegree[s] == 0)
    visited = 0
    while queue:
        u = queue.popleft(); visited += 1
        # If u is a lower face of its matched upper face, arrow goes upward.
        # Otherwise all present upper faces have downward arrows into u.
        for v in range(N):
            if not (u >> v & 1):
                upper = u | (1 << v)
                if faces[upper] and matched.get(upper) == u:
                    indegree[upper] -= 1
                    if indegree[upper] == 0: queue.append(upper)
            else:
                lower = u ^ (1 << v)
                if matched.get(u) != lower:
                    indegree[lower] -= 1
                    if indegree[lower] == 0: queue.append(lower)
    assert visited == sum(faces), ('directed Hasse cycle',visited,sum(faces))
    return edges, visited


def translation_character(faces):
    char = {}
    for dy in range(4):
        for dx in range(4):
            if dx == 0 and dy == 0: continue
            perm = [4 * ((a//4+dy)%4)+(a%4+dx)%4 for a in range(N)]
            seen = set(); orbits = []
            for a in range(N):
                if a in seen: continue
                orbit = []; b=a
                while b not in seen:
                    seen.add(b);orbit.append(b);b=perm[b]
                orbits.append(orbit)
            subtotal = 0
            for s in range(1 << N):
                if not faces[s]: continue
                fixed = all(bool(s >> a & 1) == bool(s >> perm[a] & 1) for a in range(N))
                if not fixed: continue
                # Sign on oriented vertices in the face = (-1)^(number of
                # vertices minus number of occupied permutation cycles).
                occ = sum(bool(s >> orbit[0] & 1) for orbit in orbits)
                subtotal += (-1)**occ
                # Euler sign times permutation sign is (-1)^occupied_orbits.
            # In degree nine only, reduced Lefschetz is -trace; with the
            # empty simplex included its contribution is -1, hence trace
            # is the alternating oriented-face sum, equal to subtotal.
            char[(dx,dy)] = subtotal
    return char


def verify(kind):
    rows=graph(kind)
    graph_properties(rows)
    faces=complex_faces(rows)
    pairs,critical=matching(faces)
    edges,visited=check_directed_hasse(faces,pairs)
    face_vector=dict(sorted(Counter(s.bit_count()-1 for s in range(1,1<<N) if faces[s]).items()))
    crit_vector=dict(sorted(Counter(s.bit_count()-1 for s in critical).items()))
    assert (0, 1) in pairs
    # On the ordinary (nonempty) face poset, omit that pair and declare
    # vertex 0 critical. The directed Hasse graph remains acyclic.
    ordinary_critical = Counter(s.bit_count()-1 for s in critical)
    ordinary_critical[0] += 1
    assert 2*(len(pairs)-1)+sum(ordinary_critical.values())==sum(faces)-1
    assert 2*len(pairs)+len(critical)==sum(faces)
    assert sum(((-1)**dim)*ct for dim,ct in face_vector.items())-1==sum(((-1)**dim)*ct for dim,ct in crit_vector.items())
    if kind=='Shrikhande':
        assert sum(faces)==59819
        assert face_vector[12]==32
        assert crit_vector=={9:11}
        chars=translation_character(faces)
        chars[(0,0)] = 11
        for dx in range(4):
            for dy in range(4):
                expected=(11 if (dx,dy)==(0,0) else 3 if (dx==0 or dy==0 or dx==dy) else -1)
                assert chars[(dx,dy)]==expected
        # Fourier inversion on the finite abelian translation group.
        exp_real=(1,0,-1,0)
        exp_imag=(0,-1,0,1)
        multiplicities={}
        for a in range(4):
            for b in range(4):
                real=imag=0
                for (dx,dy),t in chars.items():
                    k=(a*dx+b*dy)%4
                    real+=t*exp_real[k]
                    imag+=t*exp_imag[k]
                assert imag==0 and real>=0 and real%16==0
                if real:multiplicities[(a,b)]=real//16
        assert sum(multiplicities.values())==11
        assert multiplicities[(0,0)]==2
        print('Shrikhande translation Fourier multiplicities:',dict(sorted(multiplicities.items())))
        print('Shrikhande nontrivial translation traces:',dict(sorted((k,v) for k,v in chars.items() if k!=(0,0))))
    else:
        assert sum(faces)==59747
        assert face_vector[11]==488
        assert crit_vector=={9:1,11:2}
    print(kind,'vertices',N,'edges',48,'faces_inc_empty',sum(faces),
          'fvec',face_vector,'pairs',len(pairs),'critical',crit_vector,
          'Hasse_incidences',edges,'DAG_visited',visited,
          'ordinary_critical',dict(sorted(ordinary_critical.items())))
    return faces,crit_vector

if __name__=='__main__':
    a,ca=verify('Shrikhande')
    b,cb=verify('rook')
    # Characteristic certificates distinguish the two complexes by homology.
    assert ca != cb
    print('VERIFIED: Shrikhande dominance complex is wedge of eleven 9-spheres;')
    print('rook complex has integral reduced homology Z in degree 9 and Z^2 in degree 11.')
