# Independent mathematical audit

## correctness

PASS

An odd-cycle transversal is exactly a vertex set whose residual induced graph is 2-colourable. Each cyclic column (a_i,b_i) with signed ±1 colours or 0 deletion has 7 allowed spoke patterns; consecutive outer and distance-two inner constraints correspond bijectively to closed walks on the exact 41-state pair automaton. An explicit integer 41-state potential satisfies 2w−1+P(s)−P(t)>=0 for EVERY one of 203 allowed arcs, giving universal deletion cost >=ceil(n/2). Equality for even n requires each arc tight; an independent graph-algorithm verification found exactly one cyclic tight SCC of 22 states, and every tight arc in it advances a Z/4 level, so a closed zero-reduced-cost walk can have length only 0 mod4. This excludes deletion count n/2 at n=2 mod4. Five explicit cyclic upper-bound words W4..W8 and their boundary-compatible concatenations W_b W4^t attain the formula for every n>=5. Independently brute-tested all smaller deletion subsets and all optimal-cardinality subsets for every n=5..10: optimal values (3,4,4,4,5,6) and positive attainment counts. Exhaustive finite automaton inequalities plus general pattern concatenation, not brute-force samples, prove all n.

## originality

PASS

Novelty is a qualified best-of-knowledge mathematical comparison, not a guarantee of priority; exact original claim was searched against equivalent formulations, general theorems and data tables.

## value

PASS

A sharp all-order odd-cycle vertex-transversal formula for a classical cubic graph family is a natural structural invariant. The mod4 exceptional family arises from an actual periodic obstruction in a minimal-cost automaton, not generic hardness or a single small instance. It supplies exact maximum induced-bipartite cardinality and reusable finite-state lower-bound certificates, distinct from known decycling and independence invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
