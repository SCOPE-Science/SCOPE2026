# Scientific review

## Correctness — PASS
The sketched one-vector formula follows directly from the published sketched Galerkin expression. With \(Av=\alpha v+\rho w\), Gaussian rotation gives independent sketch columns and the exact ratio of a standard normal to an independent chi random variable. The Student density, its power-law tail, and the exponential transformation provide the tail constant and all positive-moment divergence. The error has the same tail by a deterministic reverse-triangle bound, and the eigenvector case is exactly solved. The bundled standard-library verifier passed 120,028 checks. Simulations corroborate but do not replace the proof.

## Originality — PASS (subject to ordinary publication-priority risk)
Güttel–Schweitzer 2022 explicitly provides sketched FOM and recognizes outlying Ritz values/possible instability; this is prior and is not claimed new. Cortinovis–Kressner–Nakatsukasa 2022 supplies a related equivalent randomized compression. Palitta–Schweitzer–Simoncini 2023 analyzes outlying sketched Ritz values and sketched exponential convergence in larger Krylov spaces; it does not directly state an unconditional shifted-Student law or logarithmic error-tail constant for the one-vector Gaussian method. Bergermann 2026 investigates deterministic sketches with different guarantees. Relevant published-finding corpus records concerning sketched GMRES moment divergence and two-step Lanczos positivity concern non-equivalent numerical maps. Targeted searches found no direct coverage, but database absence is not uniqueness proof. Equivalent treatments under different random-regression terminology cannot be excluded.

## Mathematical value — PASS
The sharp distribution and error-tail classification expose a meaningful distinction between high-probability embedding stability and unconditional moment guarantees for an established matrix-function algorithm. Even massive **finite** Gaussian oversampling does not restore any positive-order unconditional error moment. It pinpoints a precise failure mode that could motivate post-draw checks or safeguarded projections, without claiming those designs are validated here. The unusually severe logarithmic rather than polynomial error tail gives a quantitative reason risk measures based on expectation can be misleading.

## Limitations and closest published work
The one-vector specialization may be only an early step of a larger practical solver. The statement concerns unconditioned random sketches, not certified embeddings, and should not be interpreted as typical-case large-error behavior. Exact arithmetic is essential to the mathematical distribution. Closest inspected primary sources: arXiv:2208.11447v1, arXiv:2212.12758v1, arXiv:2306.06481v1, and arXiv:2604.07158v1. More specialized random-projection literature may contain an equivalent formulation.

Self-review: passed. Independent audit: not yet performed.
