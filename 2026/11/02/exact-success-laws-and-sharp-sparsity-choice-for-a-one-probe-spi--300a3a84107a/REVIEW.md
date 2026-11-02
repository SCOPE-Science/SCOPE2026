# Scientific review

## Correctness — PASS

The object and conventions are explicit, including the all-zero probe. The proof computes the exact nonzero-probe projection residual, its nontrivial spectral eigenvalue, the two missing-leading outcomes, and their independent binomial masses. The ordering of all support levels is strict because \(a>b>0\). Differentiation of the binomial CDF gives an exact polynomial with one sign change, hence a unique optimum for each nontrivial success band. Root convergence plus binomial-to-Poisson convergence establishes the fixed-band asymptotic. Independent finite matrix computations from `verify.py` passed 384994 checks. Numerical checks are not presented as an infinite proof.

## Originality — PASS (qualified)

The closest directly motivating literature is Saibaba–Międlar, arXiv:2308.05814v1 (2023), Theorem 3.3, the sparse-Rademacher discussion, Appendix B.1, and Appendix C; the actual full 37-page text was searched and its relevant PDF pages inspected. It provides general sample-size/error bounds and experiments, not the all-threshold one-probe law or the optimizer. Halko–Martinsson–Tropp, arXiv:0909.4061, gives general range-finding machinery. Available prior results about Rademacher expected loss with nonzero coordinates or Gaussian covariance optimization do not imply a sparse-zero-atom, threshold-probability optimum. A dedicated earlier special-case calculation, if located, could still subsume this claim. This comparison does not certify publication priority.

## Value — PASS

A distribution with fewer nonzero entries can strictly outperform dense signs for a stringent *success probability*, although general sparse-sketch results emphasize larger sample requirements as sparsity increases. The result identifies exactly where that reversal occurs, for **both** spectral and Frobenius losses, and quantifies its dimension-dependent cost in repeated one-probe trials. This is a complete naturally parameterized benchmarking classification, not an arbitrary numerical slice. Its practical relevance is restricted to the rank-one single-spike model, coordinate-aligned probes, and this specific tail objective; it does not claim general sparse-sketch superiority.

## Evidence and residual risk

Primary evidence: https://arxiv.org/pdf/2308.05814 (37 pages, relevant main theorem and appendices), https://arxiv.org/abs/0909.4061 (range-finding algorithm and general error results), and reproducible `verify.py`. General deterministic projection identities, Descartes' rule, and the Poisson limit are background mathematical tools. Key residual priority risk: a specialized existing one-vector sparse Rademacher calculation not found among the inspected literature or records; failure to find it is not proof of uniqueness.

Self-review: passed. Independent audit: not yet performed.
