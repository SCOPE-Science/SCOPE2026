#!/usr/bin/env python3
import itertools

def mul(A, B, q):
    return (
        (A[0]*B[0] + A[1]*B[2]) % q,
        (A[0]*B[1] + A[1]*B[3]) % q,
        (A[2]*B[0] + A[3]*B[2]) % q,
        (A[2]*B[1] + A[3]*B[3]) % q,
    )

def det(A, q):
    return (A[0]*A[3] - A[1]*A[2]) % q

def actual_graph_prime(q):
    zero = (0, 0, 0, 0)
    V = [A for A in itertools.product(range(q), repeat=4)
         if A != zero and det(A, q) == 0]
    adj = [set() for _ in V]
    for i, A in enumerate(V):
        for j in range(i+1, len(V)):
            B = V[j]
            if mul(A, B, q) == zero or mul(B, A, q) == zero:
                adj[i].add(j)
                adj[j].add(i)
    return V, adj

def domination_number(V, adj, max_k):
    n = len(V)
    for k in range(1, max_k+1):
        for S_tuple in itertools.combinations(range(n), k):
            S = set(S_tuple)
            if all(v in S or bool(adj[v] & S) for v in range(n)):
                return k, S_tuple
    raise AssertionError("no dominating set in searched range")

# Direct arithmetic reconstruction for the two smallest prime fields.
actual = {}
for q in (2, 3):
    V, adj = actual_graph_prime(q)
    g, witness = domination_number(V, adj, q+1)
    actual[q] = (len(V), g, witness)

assert actual[2][0] == 9 and actual[2][1] == 2
assert actual[3][0] == 32 and actual[3][1] == 4

def adjacent_type(t, u):
    # t=(image,kernel), u=(image,kernel)
    return u[0] == t[1] or t[0] == u[1]

def support_check(q):
    # This checks the combinatorial lower-bound mechanism on the projective
    # type graph.  Labels 0,...,q represent the q+1 projective lines.
    m = q + 1
    types = [(i, j) for i in range(m) for j in range(m)]
    for k in range(m):
        for S_tuple in itertools.combinations(types, k):
            S = set(S_tuple)
            # If an absent type has no neighbor in S, no vertex choice with
            # this support can dominate its fiber.
            all_absent_covered = all(
                t in S or any(adjacent_type(t, u) for u in S)
                for t in types
            )
            if not all_absent_covered:
                continue
            if q == 2:
                # The exceptional q=2 case genuinely has support size 2.
                assert k >= 2
                continue
            # For q>2, if k<m and every absent type is covered, the proof says
            # some selected off-diagonal type has no selected type-neighbor.
            # Because its fiber contains q-1>=2 vertices, one unselected scalar
            # multiple remains undominated.
            bad_selected_type = any(
                t[0] != t[1]
                and not any(u != t and adjacent_type(t, u) for u in S)
                for t in S
            )
            assert bad_selected_type, (q, k, S)
    return True

for q in (2, 3, 4, 5):
    assert support_check(q)

print("VERIFY_OK")
print("actual_q2_vertices=9 gamma=2")
print("actual_q3_vertices=32 gamma=4")
print("projective_support_checks=q2,q3,q4,q5")
print("theorem_values=q2:2,q3:4,q4:5,q5:6")
