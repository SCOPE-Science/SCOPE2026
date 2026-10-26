# Mathematical review

## Correctness: PASS

The fixed-edge exact factor follows from sampling a star of \(n-1\) edges conditional on a disjoint three-edge triangle. Incidence with a vertex of the triangle makes degree one impossible. For a nonincident vertex, the remaining edge draw is hypergeometric and gives a simple ratio of falling factorials. The rational ratio reduces to \(Q_n\), and its sign changes at a real threshold strictly between \(n\) and \(n+1\) for every integer \(n\ge5\). A separate independent-edge calculation fixes the negative sign for all \(0<p<1\). The sparse covariance limit follows by expansion of the exact expression. Brute-force enumeration of all labeled graphs through six vertices independently verifies all fixed-edge strata; further exact sign tests cover 6948 cases. These finite tests corroborate, but do not replace, the analytic proof.

## Originality: PASS (conditional on the inspected record)

Janson's 2006 preprint (arXiv:math/0605642) treats marginal/joint degree-count normality, not degree-one/triangle mixed covariances. Goldstein (arXiv:1005.4390) treats normal approximation for degree counts, not the covariance reversal. The 1990 Janson functional subgraph theorem concerns fixed-subgraph asymptotics rather than the variable-size exclusion event defining degree one; only its abstract was available, leaving a nonzero historical-priority risk. Previously published computations concerning isolated-edge components with triangles and graph-component counts with triangles concern different observables and do not imply the present dependence classification. Search-based exclusion is not proof of absolute novelty.

## Mathematical value: PASS

The dependence sign is not a routine endpoint or normalizing artifact: independent Bernoulli edges force strictly negative covariance for every nontrivial parameter, whereas conditioning on the edge count produces a positive regime beginning at the exact integer \(m=n+1\). The exact finite threshold and the sign-changing limit \(8c^3(c-1)e^{-2c}\) give a parameter-uniform structural description of the relationship between local degree-one vertices and triangular motifs, including the contrast between two standard random-graph null models.

## Closest literature and limitations

The most closely related accessible full texts are Janson's *Monotonicity, asymptotic normality and vertex degrees in random graphs*, particularly Section 4, and Goldstein's *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, particularly Section 2. Both establish degree-count foundations rather than the claimed joint dependence. Janson (1990) was accessible by abstract only; this creates a residual archival priority limitation but does not supply a theorem logically covering a degree-one/triangle covariance, especially in the sparse fixed-edge regime. Neither stochastic-order dependence nor joint limit distribution is asserted.

Self-review: passed. Independent audit: not yet performed.
