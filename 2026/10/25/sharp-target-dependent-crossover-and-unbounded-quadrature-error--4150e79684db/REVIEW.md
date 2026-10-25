# Self-review: sharp target-dependent quadrature crossover

## Correctness — PASS

For the specified finite diagonal RKHS the optimal quadrature weights equal the target coefficients at sampled nodes. Squared worst-case error is exactly the weighted omitted-coordinate sum. Residual-diagonal pivots produce the stated sequential omission product; determinant-subset counting produces the companion rational probability. Comparing logarithmic derivatives yields strict ordering when the budget is at least two. Symmetry and a fixed number of omitted nodes yield both all-target risk identities. The large-contrast limit is a fixed-degree rational asymptotic. A standalone rational-enumeration script corroborates all major formulas in smaller finite settings; it does not replace the proof.

## Originality — PASS (best-knowledge comparison)

The closest primary references are Epperly and Moreno (2023), who introduced RPChol kernel quadrature and explicitly highlighted comparison to volume sampling; Belhadji, Bardenet, and Chainais (2020), who derived volume-sampling expected kernel errors; Chen, Epperly, Tropp, and Webber (2022 preprint), who compared RPChol and DPP matrix approximations; and Yu (2010), who established inclusion-probability majorization for successive versus rejective sampling. The last qualitative inclusion comparison is **prior work**, not novel here. No inspected result establishes the complete target-dependent quadrature sign boundary together with its sharp unbounded squared-error ratio. Equivalent classical sampling formulations remain a real residual risk.

## Mathematical value — PASS

The study was motivated by a published gap between pivoted-Cholesky and fixed-size volume-sampling kernel quadrature. The complete target-risk crossover shows why a single trace or average-error ranking can obscure opposite outcomes for different integration functionals; a concrete dominant-coordinate functional yields an unbounded advantage even though both samplers nearly always include that coordinate at high contrast. The finding provides an exact model benchmark rather than a new general guarantee. No downstream theorem, smooth-domain extension, or typical-case advantage is claimed.

## Scope and limitations

The result applies only to fixed finite counting-measure sets, diagonal one-spike positive-definite kernels, optimal quadrature weights, and expected **squared** RKHS worst-case error. The precise high-contrast asymptotic fixes the number of nodes. Its formula is not an expectation of unsquared error, and it does not show high-probability or continuous-domain superiority. The finite verifier is supporting evidence and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
