# Independent mathematical audit

## correctness

PASS

For a selected vertex in part i the representation contains one 0, |W|-w_i ones and w_i-1 twos; for an unselected vertex it contains |W|-w_i ones and w_i twos. Across parts, selected-selected and unselected-unselected representations collide exactly at equal corresponding occupancies, while selected-unselected representations cannot collide because only the former contains 0. Hence positive occupancies must be pairwise distinct and at most one zero is allowed. Any valid profile therefore has at least r-1 distinct positive integers and size at least 1+...+(r-1). Such a minimum profile is feasible exactly when, after omitting one part, capacities can host 1,...,r-1; sorting shows this is equivalent to a_i>=i-1 for i>=2, with omitting a smallest part optimal. Summing binomial choices over every feasible permutation yields the basis count. The frozen verifier exhausts all isomorphism types through order nine but is only corroborative.

## originality

PASS

The 2019 foundational paper introduces local multiset dimension and treats basic families. The 2025 full primary paper on local (outer) multiset dimension was materially inspected: it gives general conditions, exact values for amalgamations/coronas, the theorem lmd=1 iff bipartite, and wheels/small-diameter families, but a whole-document search contains no 'multipartite' occurrence. The 2026 survey abstract emphasizes outer-multiset diameter-two bounds and lmd=2 results rather than this complete-multipartite classification. Resultary searches returned the different global outer-multiset theorem and unrelated multipartite invariants, not the submitted local theorem.

## value

PASS

Complete multipartite graphs are a canonical diameter-two family for a recently developed distance-multiset invariant. The theorem completely resolves existence, the exact minimum, every minimum occupancy profile, and the number of bases for arbitrary part sizes. This is a natural family classification rather than an arbitrary finite exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
