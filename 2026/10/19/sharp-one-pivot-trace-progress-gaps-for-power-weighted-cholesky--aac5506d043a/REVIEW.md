# Scientific review

## Correctness — PASS
The stated update is exactly the rank-one positive-semidefinite Schur correction. The mean trace gains, Rayleigh quotient upper bound, rank-constrained spectral optimization, and both block-family sharpness calculations were independently reconstructed. The two-by-two identity and explicit three-by-three example are algebraically exact. Exact-rational tests in `verify.py` passed, but are only supplementary to the infinite-parameter proof. The result is limited to one step and permits rank-deficient Gram matrices.

## Originality — PASS
The primary randomly pivoted Cholesky work proves the canonical expected-residual formula and full-run best-rank bounds. Steinerberger studies diagonal-power rules with a Frobenius objective and empirical uniform comparisons. Accelerated RPCholesky preserves the same distribution. No inspected primary full text states the sharp uniform-to-standard trace-gain envelope, the minimal reversal dimension, or divergence for every superlinear power at rank two. These are additional consequences requiring a spectral optimization and explicit extremizers; their absence from searches is not itself a proof of novelty. A later closely related preprint could only be inspected at abstract level; that and unindexed equivalent results remain risks.

## Value — PASS
The comparisons quantify an actual choice in pivot-selection design, distinguish improved average one-step trace progress from rank-approximation bounds, and identify a finite-rank stability boundary when diagonal weighting is made more aggressive. The exact factor and the diverging construction motivate caution with power rules rather than claiming they are universally poor.

## Sources and limitations
Primary sources: arXiv:2207.06503 (Sections 2.3, 5 and Appendix C); arXiv:2404.11487 (Sections 1–3); arXiv:2410.03969 (Sections 2 and 4). The later arXiv:2608.20633 is an unresolved full-text coverage risk. These results concern one initial pivot; finite simulations alone do not establish the theorem, and neither long-run convergence nor the interval of powers between zero and one is classified.

Self-review: passed. Independent audit: not yet performed.
