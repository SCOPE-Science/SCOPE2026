# Mathematical review

## Correctness

**PASS.** The exact model specifies uniformly sampled edge subsets. Conditioning on a designated vertex of degree one exposes a uniformly selected \((m-1)\)-edge graph on \(n-1\) vertices, and the motif minimum-degree assumption prevents a copy using the designated vertex. Injective-embedding counts yield the two exact conditional and unconditional expectations. Their ratio proves the covariance formula for all integer parameters, with disjoint zero-support cases. For triangles the unique real threshold lies strictly between \(n\) and \(n+1\) when \(n\ge5\); the exceptional \(n=4\) range is stated. The sparse limit follows from explicit hypergeometric probabilities. Standalone exact finite checks independently corroborate the proof.

## Originality

**PASS, with historical-priority qualification.** Janson (2006/2007), arXiv:math/0605642, Section 4, describes degree-class asymptotics, not the exact fixed-edge covariance between degree-one vertices and non-induced 2-core motifs. Alm–Janson–Linusson (2009), arXiv:0906.0720, study reachability correlations of oriented paths, not these statistics. General classical first moments and the already-known independent-edge sign are not treated as new. The closely related isolated-vertex/motif identity does not imply this result: a degree-one event removes one selected edge, adding the factor \((m-e)/m\) and creating an actual edge-count-dependent sign reversal. The matched fixed-edge degree-one motif covariance and exact threshold were not located in available comparisons. Janson's 1990 broad subgraph-count work was accessible only in abstract, so implicit earlier coverage is a residual risk.

## Mathematical value

**PASS.** The precise sign at every finite integer edge count exposes a qualitative reversal from negative to positive association, occurring at the sparse natural excess-edge boundary \(m=n+1\). The motif-general identity separates universal conditioning geometry from motif topology, while the nonzero \(c\)-dependent limit demonstrates a persistent sparse phenomenon. These conclusions concern a natural degree-class statistic and a natural cyclic-subgraph statistic and are not determined by their marginal moments.

## Scope and limitations

This is a statement about uniform simple \(G(n,m)\), non-induced motifs with minimum degree at least two, and covariance only. The counting argument is exact; finite verifications are not used as infinite proofs. Older general moment treatments might imply the formulas implicitly. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
