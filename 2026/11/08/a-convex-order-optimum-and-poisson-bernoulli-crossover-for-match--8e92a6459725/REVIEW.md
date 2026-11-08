# Scientific review: matching-weighted bipartite spanning-tree degrees

## Correctness
**PASS.** The finite weighted root-degree polynomial follows by applying the weighted matrix-tree theorem to the displayed block Laplacian cofactor, diagonalizing its \((n-2)\)-dimensional zero-sum sector, and explicitly evaluating the remaining \(2\times2\) determinant. This gives independent binomial and Bernoulli factors with valid probabilities for every \(n\ge3\) and \(t>0\). The exact parameter derivatives and discrete second-difference formula prove both convex-order monotonicities; positive binomial zero-mass gives strict leaf optimization. The local scaling limit follows from binomial-to-Poisson convergence. The standalone exact-rational checker reconstructed relevant cofactors and finite laws and returned `VERIFY_OK 212 exact rational assertions`. It is supplementary to the analytic proof.

## Originality
**PASS, with a historical-priority risk.** A general Gibbs spanning-tree degree-polynomial framework appears in Fita Sanmartín, Schnörr and Hamprecht (2024, arXiv:2409.13472); Rapoport (2023, arXiv:2312.14992) supplies unweighted degree-field formulas; Klee and Stamps (2020, arXiv:2008.01669, Proposition 8) treat the Laplacian of the complete bipartite graph after deletion of a perfect matching. Those frameworks and the matrix-tree theorem are prior work. The claimed addition is the explicit all-positive-weight, one-parameter **convex-order classification** and the scale-\(n\) local Poisson–Bernoulli crossover. The inspected results do not state those comparative conclusions for the matching-weighted graph. General determinant and Bernoulli-balancing principles make the result approachable, and unlocated earlier specializations remain a residual risk; no priority certification is claimed.

## Value
**PASS.** The parameter is a natural conductance bias toward one fixed perfect matching. The theorem shows that despite a weight-independent local mean degree, the full local degree distribution has a unique and sharp convex-order maximum at unbiased weights, implying simultaneous variance and leaf-optimality. The exact scale-\(n\) crossover detects a changed limiting local law and leaf density rather than an arbitrary numerical instance. It is a finite-graph structural and probabilistic classification, not merely a computation of a generic determinant.

## Limitations
Only the single-vertex degree law and expected total leaves are treated, not their joint distributions. Results are for shared matching conductance, not independent weight vectors. Infinite-size limits concern the local marginal; uniform rates and higher-dimensional extensions are not claimed. An independent external audit and exhaustive historical-priority check are outstanding.

Self-review: passed. Independent audit: not yet performed.
