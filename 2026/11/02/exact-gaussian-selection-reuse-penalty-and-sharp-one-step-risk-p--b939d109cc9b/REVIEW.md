# Scientific review of the noisy-greedy two-row Kaczmarz classification

## Correctness — PASS

The exact one-step comparison follows from the Gaussian rotation into two independent coordinates, the sign-product selection rule, and the Gaussian truncated first moment. The reuse penalty depends only on the initial squared norm. Strict concavity of the explicitly differentiated radial factor supplies the exact orientation extrema, and a strictly decreasing-versus-increasing scalar equation gives uniqueness of the SNR boundary. All quantifiers, Gaussian independence requirements and equality cases are stated in the result. The standalone standard-library verifier passed 10,893 independent diagnostic assertions, including conditional Gaussian quadrature; finite numerical checks are corroboration, not an infinite proof.

## Originality — PASS, qualified

The closest examined literature comprises the 2019/2020 sampling Kaczmarz–Motzkin analysis, the 2022 greedy nonlinear Kaczmarz study (with the linear rule explicitly covered), the 2021 sparse noisy Kaczmarz analysis and the 2026 doubly noisy greedy Kaczmarz study. Their respective assumptions concern exact fixed data, deterministic greedy residuals, fixed noisy right-hand sides and general doubly noisy convergence/averaging rather than the exact independent-fresh-Gaussian, two-row, one-update **reuse versus split** risk classification. No inspected primary result directly implies the isotropic penalty or sharp angular/radial envelope. Broader noise-selection theory or specialized unindexed prior material could still overlap; no general greedy acceleration or novelty of selection bias is asserted.

## Value — PASS

The theorem resolves a natural implementation ambiguity—whether an adaptively selected noisy residual may safely be reused as the correction—with a nonzero, exact, direction-independent risk tax. It identifies the sharp SNR region in which the seemingly better-informed greedy rule loses to uniform selection for every starting direction, and a fresh-update alternative which removes the reversal. The result is a meaningful small-system reliability benchmark, not merely a numerical counterexample, while remaining limited to one step and a restricted Gaussian/orthonormal model.

## Source and verification boundaries

The exact Gaussian identities and their proof are reproduced in RESULT.md. The closest primary technical material was examined in publicly accessible full-text versions of arXiv:2209.06082, arXiv:1912.03544, arXiv:2101.04807, arXiv:2603.29372 and arXiv:2308.07987. Publication-priority completeness cannot be guaranteed. No general-dimensional, arbitrary-noise or long-horizon assertion was checked or accepted.

Self-review: passed. Independent audit: not yet performed.
