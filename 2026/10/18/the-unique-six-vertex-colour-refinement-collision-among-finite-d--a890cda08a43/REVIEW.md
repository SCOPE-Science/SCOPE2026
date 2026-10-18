# Review of the six-vertex directed-DAG classification

## Correctness
PASS. Topological ordering enumerates every finite DAG by an upper-triangular adjacency matrix, and exact graph isomorphism inside globally refined colour classes yields a finite exhaustive certificate. The all-orders reduction from \(C^2\)-equivalence to directed colour refinement is classical for a single binary relation; absence of loops and reciprocal arcs makes the in/out multiset implementation faithful. Two independently coded procedures agree on \(1,2,6,31,302,5984\) DAG types and \(1,2,6,31,302,5983\) logical types. The exceptional pair is nonisomorphic by underlying weak connectivity yet has identical equitable in/out neighbourhoods. Risk: the finite certificate covers precisely orders at most six, not all orders.

## Originality
PASS with residual priority risk. Kiefer–Schweitzer–Selman (2015) already gives a broader \(C^2\) structural framework for finite relational structures, and Arvind–Köbler–Rattan–Verbitsky (2015) characterizes undirected colour-refinement amenability. The known DAG isomorphism counts appear in OEIS A003087. These facts are not claimed as new. The inspected sources did not tabulate the corresponding directed-DAG \(C^2\) quotient through six vertices or classify the unique collision there. A previous specialist census or a short derivation from the general structural theorem remains possible; no negative novelty claim is based solely on a search snippet.

## Value
PASS. The natural boundary of two-variable counting distinguishability on DAGs is sharply located and the entire first exceptional layer is classified. Distinguishing DAGs matters because acyclicity removes many classical regular-graph obstructions while retaining a finite but nontrivial logical ambiguity. The pair explicitly isolates the inability of local in/out counting to detect global component structure, supplying a minimal test case for directed refinement implementations.

## Closest sources and limitations
Kiefer–Schweitzer–Selman, arXiv:1503.08792, Theorem 27, is the strongest broad comparison; it is not a DAG-order census. Arvind–Köbler–Rattan–Verbitsky, arXiv:1502.01255, treats undirected amenability. OEIS A003087 contains only the isomorphism counts. Böker, arXiv:1903.12432, discusses DAG homomorphism-count expressiveness, a different invariant. The result is limited to loopless simple DAGs of at most six vertices in the directed-arc language, not their transitive closures.

Self-review: passed. Independent audit: not yet performed.
