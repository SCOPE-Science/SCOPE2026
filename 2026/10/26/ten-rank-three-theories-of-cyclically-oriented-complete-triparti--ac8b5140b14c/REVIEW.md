# Scientific review: cyclic tripartite digraph rank-three classification

## Correctness — PASS

The finding is an exact statement for all positive part sizes, in the pure directed-edge vocabulary. Fixing a first vertex makes its own class, outgoing class, and incoming class atomic regions. With two moves remaining, their complete pointed Ehrenfeucht–Fraïssé profile is exactly the three capped cardinalities specified in the theorem. One more move lifts this to equality of sets of pointed profiles. The eleven cyclic orbits among the twenty-seven capped triples have exactly one pair of coincident profile sets, yielding ten classes. The nine-vertex kernel is sharp because only a triple with all parts of size at least three has a singleton footprint with first component three. All quantifier depths and equality cases have been checked; the packaged verifier independently checks the entire capped pair table.

## Originality — PASS, with residual risk

Pikhurko–Veith–Verbitsky (arXiv:math/0311041, first public 2003-11-04) provide general distinguishability bounds for binary structures, not a class-by-class quantifier-rank-three computation for directed-triangle blow-ups. Rabinovich's composition theorem (Fundamenta Informaticae 79, 2007) provides a general sum principle, and discusses complete bipartite graphs and cycles, but does not tabulate the necessary-and-sufficient oriented footprint or the nontrivial merger. The nearest identified published complete-multipartite depth classification concerns *undirected* adjacency, which discards the orientation information crucial here. Searches under the directed triangle, cyclic tripartite orientation, and lexicographic sum aliases did not locate stronger coverage. Non-indexed literature and the general composition method remain substantive originality risks, so PASS is a best-knowledge assessment, not a priority certificate.

## Value — PASS

This is a natural exact bounded-depth logical invariant for all nonempty independent-set blow-ups of the directed three-cycle, not an arbitrary finite slice. Orientation matters: \((1,2,3)\) and \((1,3,2)\) lie in different theories, yet the distinct cyclic size patterns \((2,2,3)\) and \((2,3,3)\) merge. The proof gives an interpretable rooted profile, an exact complete classification, and a sharp nine-vertex representative bound. These features support reuse in finite-model-theoretic comparisons of graph substitutions, beyond the finite verification exercise.

## Scope and remaining risk

The conclusions are restricted to rank three without extra predicates or counting. The result is supported by a mathematical proof and independently implemented finite verification of its small quotient. Equivalent historical literature cannot be ruled out, and the independent audit has not taken place.

Self-review: passed. Independent audit: not yet performed.
