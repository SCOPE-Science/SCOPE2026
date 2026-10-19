# Scientific review

## Correctness — PASS
The three-by-three Gaussian Gram system is inverted symbolically in symmetry-reduced form; the nonstandard sign criterion is equivalent exactly to a strictly increasing hyperbolic-logarithm ratio. Its monotonicity follows from the strictly positive derivative \(y\operatorname{sech}^2y\). The all-bandwidth natural Gauss–Hermite inequality is split into two ranges of \(\ell^2\), each supported by explicit inequalities. Tensor instability follows from the exact norm of a signed discrete linear functional, not simulation. The coalescence constant follows by Taylor expansion of the proved weight formulas. A reproducible deterministic script checks 441 numerical and symbolic instances but is not used to replace any infinite proof.

## Originality — PASS, subject to publication-priority uncertainty
The nearest source [1] studies scaled Gauss–Hermite nodes and states that positivity of exact and approximate weights is indicated by numerical evidence; its proved formulas for approximate Mercer quadrature weights do not give the exact three-node sign frontier. The general sufficient local-optimum positivity theorem and tensor product observations in [2] are acknowledged and do not entail a necessary-and-sufficient parameter test for these fixed nodes. The flat-limit polynomial correspondence in [3] is acknowledged and does not imply the present all-finite-bandwidth threshold. Targeted scholarly and mathematical-finding searches located related positivity work for different interpolation or quadrature operators, but no identified stronger statement implying the full exact claim. Such searches cannot exclude an equivalent result in unindexed literature. The novelty assertion is therefore a supported best-knowledge conclusion, not a proof of global uniqueness.

## Value — PASS
Positive quadrature weights control the worst-case amplification of noisy bounded nodal data, and the source motivates scaled nodes precisely through observed positivity and stability. The theorem proves a nontrivial instance of that observation (three exact weights at all length scales) and gives a sharp, actionable design boundary where weight signs reverse, with explicit normalized high-dimensional amplification when nodes cluster. It separates exact kernel weights from Mercer-surrogate weights, and unnormalized exactness from normalized constant reproduction. It is a structural classification for a motivated configuration, rather than a routine arbitrary slice or unsupported speedup claim.

## Scientific limitations
Only three symmetric nodes, a standard-Gaussian target, a Gaussian kernel, and tensor powers are covered. The normalized tensor functional no longer integrates the original kernel translates exactly. The analysis does not establish positivity at every Gauss–Hermite order or a kernel-RKHS approximation-error bound. Equivalent specialized results may exist beyond the inspected literature.

## References
[1] Karvonen and Särkkä, arXiv:1803.09532, Sections 1, 2.4, 4, 5.3.
[2] Karvonen, Kanagawa, and Särkkä, arXiv:1812.08509, Sections 3–4.
[3] Karvonen and Särkkä, arXiv:1906.02096, flat-kernel convergence results.

Self-review: passed. Independent audit: not yet performed.
