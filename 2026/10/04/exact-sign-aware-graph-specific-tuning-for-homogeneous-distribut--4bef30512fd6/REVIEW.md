# Same-model scientific review

## Correctness
PASS. The proof reconstructs the homogeneous reduced dynamics from the primary source rather than relying on a numerical fit. The source factorization and monotonicity reduce the exact fixed-spectrum radius to three scalar branches. Solving both branch intersections with \(1-\beta\) yields the claimed optimizer. The negative-mode quadratic has a complex-conjugate pair for \(0<\beta<2\), so its modulus is exactly \(\sqrt{n(n+\beta)}\). The bundled checker independently verifies the formulas against direct polynomial roots and dense minimization.

## Originality
PASS with stated access risk. Full-text inspection of arXiv:2608.03548v1 found the positive-dominance formula, the endpoint functions, and the sign-blind certified envelope, but not the graph-specific negative-endpoint optimizer or its switching criterion. published-finding corpus searches for DGT/ATC-DIGing/AugDGM, homogeneous quadratics, negative consensus modes, exact root radii, and the radical expression returned no implication-equivalent record. arXiv:2607.23601v1 and arXiv:2607.25463v1 are close and were checked via abstracts plus an accessible detailed review for the former; their full PDFs were not retrievable, which remains a residual risk rather than being silently treated as absence.

## Value
PASS. The result closes a natural gap left by the source's \(\lambda_2\ge|\lambda_N|\) special regime. It shows that negative consensus eigenvalues create a quantitatively weaker obstruction than a sign-blind spectral radius predicts and supplies the exact graph-specific tuning and rate. For negative-dominant spectra this can strictly improve the constant step and asymptotic factor.

## Closest literature and limitations
The closest primary source is Wang et al., arXiv:2608.03548v1. Tian--Chai--Xu arXiv:2607.23601v1 gives exact worst-case rates for DIGing/AugDGM under class-level connectivity information, while arXiv:2607.25463v1 performs graph-frequency parameter design for DIGing. Nedić et al., arXiv:1609.05877v1, is foundational for ATC-DIGing convergence. The accepted theorem is limited to homogeneous scalar quadratics, symmetric fixed mixing, and a common constant step.

Same-model review: passed. Independent audit: not yet performed.
