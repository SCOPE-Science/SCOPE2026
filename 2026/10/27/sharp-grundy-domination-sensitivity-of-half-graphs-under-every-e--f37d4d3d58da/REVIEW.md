# Independent mathematical audit

## correctness

PASS

In the bipartite half graph with edges x_i y_j iff i<=j, the independent shores and diagonal perfect matching give alpha=n. The chain-graph upper bound alpha+1 and the displayed sequence starting y_1,x_1 give the baseline n+1. I checked the fresh closed-neighborhood footprints of all four nonpendant witness constructions, including the adjacent-index endpoints and n=3: the two initial x-choices (or the interleaved choices in the extreme case), the local reversal of the y-order, and the missing edge supply exactly the additional steps; reflection x_r↔y_(n+1-r) covers the right boundary. All y-vertices are chosen, and every x-vertex retains a neighbor. The atomic deletion upper bound gives n+2; it also follows by restoring the edge and, if necessary, dropping the single step whose only fresh footprint was the opposite endpoint prematurely covered by the first selected endpoint. Deleting x_1 y_1 isolates y_1; Algorithm 1 on the connected remainder with X-class sizes 1,…,1,2 and singleton Y-classes gives n in all its candidates. Additivity gives n+1. At n=2 the middle deletion leaves two disjoint edges and has value 2. The source verifier is present and was inspected, not executed; the separate coverage-mask recurrence in branches/review-exact-small-checks.js corroborated every baseline and all 55 deletions for 2<=n<=6. These finite checks do not replace the proof.

## originality

PASS

The supported distinct claim is the complete equality-case profile of the universal deletion bound on strict half graphs, not the previously known bound or the baseline chain-graph theory. The relevant algorithms and bounds were compared at statement level; none of the examined sources supplies the all-nonpendant saturation assertion.

## value

PASS

This is a complete, size-uniform perturbation classification on a canonical nested-neighborhood family. It identifies exactly where a sharp generic bound is attained, including many deletions outside the class handled by the chain-graph algorithm, and locates the smallest-order exception. The constructive witnesses make the classification useful without recomputing the invariant for each deleted graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
