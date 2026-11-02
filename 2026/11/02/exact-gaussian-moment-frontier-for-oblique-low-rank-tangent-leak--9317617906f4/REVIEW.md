# Scientific review

## Correctness — PASS

At a fixed rank-\(r\) state, Gaussian orthogonal invariance reduces the canonical source projector exactly to two independent Gaussian regressions \(A=G^\dagger K\) and \(B=J^\dagger M\). Orthogonality of the three resulting tangent blocks gives the deterministic energy decomposition. Conditioning and integrating a Wishart Gram matrix yields the unit-scale multivariate Student law with \(\nu=\ell-r+1\) degrees; its polar integral establishes the *if and only if* moment boundary, including divergence. When both degrees exceed two, inverse-Wishart second moments yield the exact mean-square multiplier. The extracted standalone program passed 460 assertions, including full-matrix projector comparisons and independent Gaussian simulations. The analytic proof, rather than simulations, covers all dimensions and quantifiers.

## Originality — PASS, with residual priority risk

Carrel and Grigori's 2026 full text (Lemma 4.2 and Proposition 4.4) establishes the structure and qualitative leakage of an oblique tangent projector but does not compute this all-moment law. Kressner and Lam's 2024 full text (Theorems 8–9 and Lemma 2) gives related inverse-Wishart and one-stage generalized-Nyström identities for a different reconstruction problem. Lam, Ceruti and Kressner's 2025 full text (Section 2.3, Theorem 2) gives probabilistic bounds for a different low-rank approximation operator, not the fixed-state two-sided tangent leakage. The general Gaussian pseudo-inverse ingredients are standard and properly acknowledged. No exact prior statement or dominating theorem for the combined projector law was identified in the checked literature and mathematical research records, but an older equivalent formulation remains a residual risk. The reviewed claim does not assume that keyword searches establish uniqueness.

## Value — PASS

This addresses a concrete choice in randomized dynamical low-rank algorithms: whether a sketch of a given size causes manageable spurious tangent velocity when a vector field has a normal component. The universal exact mean-square coefficient shows when the typical \(2r\)-row choice produces nonvanishing leakage and identifies an infinite-variance regime despite zero bias. The all-moment boundary gives precise limits for mean-square error analysis and motivates oversampling independently of the ambient dimensions. The result is not presented as a theorem about full time integrations, which would require handling state-dependent sketches and accumulation.

## Limitations and relationship to closest literature

The source projector uses a canonical full-space lift, fixed orthonormal bases, and independent real Gaussian sketches. Results cannot be transferred verbatim to adaptively dependent sketches, structured embeddings, truncation/regularization, or complete trajectories. The existing exact generalized-Nyström expected-error factors are mathematically close but concern different operators and do not imply the new pointwise tangent-normal moment classification without further arguments.

Self-review: passed. Independent audit: not yet performed.
