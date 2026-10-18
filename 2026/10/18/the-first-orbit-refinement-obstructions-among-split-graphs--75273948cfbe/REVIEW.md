# Scientific review of the split-graph first-obstruction classification

## Correctness — PASS

The claim is finite and explicitly exhaustive. Every split graph of order at most ten has at least one representation by a clique of size \(k\) and a nondecreasing multiset of independent-vertex neighbourhood masks; the enumeration covers every such representation without pruning any potential obstruction. Exact counting-colour refinement is iterated to a stable partition. An exhaustive partial-isomorphism backtracker tests every pair of same-colour vertices for existence of a full adjacency- and nonadjacency-preserving automorphism. The complete ten-vertex failure list contains 71 presentations. Every one has an intrinsic two-degree split partition, enabling complete isomorphism canonicalization by clique row permutations and column sorting. This yields exactly four unlabelled exceptions, each independently rechecked by full automorphism enumeration. Separate code independently verifies all smaller orders. The finite certificate depends on the correctness and complete execution of the supplied code, which has been examined and reproduced; it does not purport to prove anything above order ten.

## Originality — PASS, with residual priority risk

Full texts of arXiv:1502.01255, arXiv:1505.05683 and arXiv:1606.04383 were inspected in relevant portions or throughout their searchable text. They establish general refinability concepts, structural split-graph theory and individualization/fixing questions, respectively, but do not give the claimed sharp split-graph enumeration. Actual searches for split graph 1-WL refinement, orbit partitions, first obstructions, isomorphism reductions and equivalent logical terms were compared against retrieved published research records. Historical claims about unrestricted chordal graphs and other hereditary families do not imply the first-obstruction cutoff within split graphs. Neither failure of the searches nor graph-family separation alone establishes absolute novelty. Residual risk: an unlocated earlier result on regular incidence matrices or coherent split graphs could subsume one or all of the enumerated exceptions.

## Value — PASS

Split graphs are a natural, extensively studied hereditary family. The smallest order at which 1-WL fails to recover orbits within such a family is a structural threshold, and classifying all isomorphism types at that boundary distinguishes the phenomenon from an isolated counterexample. The four examples share only two stable colour classes but exhibit two different automorphism-orbit profiles. The result is sharply motivated by orbit-refinement behaviour of small chordal and related graphs; it does not claim general graph identification or all-order structural characterization.

## Literature limitations

Arvind–Köbler–Rattan–Verbitsky, arXiv:1502.01255, treats general colour refinement and refinability; Boros–Gurvich–Milanič, arXiv:1505.05683, discusses split-graph structural theory; Arvind–Fuhlbrück–Köbler–Kuhnert–Rattan, arXiv:1606.04383, focuses on individualization and fixing. No inspected source states this exact enumeration. Specialized unpublished or inaccessible covering work is a nonzero priority risk. Independent scientific and publication-priority validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
