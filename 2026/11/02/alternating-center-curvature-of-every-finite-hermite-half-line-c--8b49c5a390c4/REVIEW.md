# Scientific review: alternating center curvature of finite Hermite concentration

## Correctness — PASS
The claim covers every positive integer \(q\), with Hermite functions normalized by the physicists' Gaussian convention. Differentiation of the finite concentration Gram matrix is exact. The proof establishes the centered Wronskian overlap, the finite central-binomial identity \(S_mR_m=H_m\), and the two successive order-increment formulas. Induction from \(q=1\) yields \(V_q''(0)=(-1)^q(2/\pi)H_{\lceil q/2\rceil}\). Parity provides \(V_q'(0)=0\), strict positivity of each \(H_m\) proves nondegenerate extrema, and Stirling's formula gives logarithmic magnitude. A standalone checker completed 260 finite rational tests and 16 separate numerical Hermite-integral tests. These tests support, but do not replace, the all-order proof.

## Originality — PASS (qualified)
Sánchez-Nungaray et al. (2018, DOI 10.1155/2018/8031259) provide a full polyanalytic Fock Hermite-matrix representation, not the all-order moving-boundary curvature classification. Lee-Guzmán et al. (2023, arXiv:2309.03410) extend that decomposition; their relevant sections are not an independent curvature theorem. Forrester and Witte (2011, arXiv:1110.0119) establish the exact GUE index variance at the fixed central threshold, an equivalent instance of \(V_q(0)\); their stated results do not imply the explicit second derivative in threshold without further calculation. Previously available two- and three-level extrema are special cases of the present all-order formula and are not treated as novel here. The strongest residual priority risk is an earlier moving-boundary finite-GUE formula, perhaps expressed through a Fredholm determinant or kernel derivative. Such a formula would dominate the claim if it explicitly yielded this exact all-order parity identity.

## Mathematical value — PASS
The defect \(\operatorname{tr}(A(I-A))\) is the natural concentration variance of a Hermite spectral projector, and is also the particle-number variance of its finite Hermite determinantal process. Its central curvature is directly related to stability of a symmetric localization threshold. The theorem settles a uniform all-finite-order sign classification, discovers an exact arithmetic coefficient, and exhibits logarithmic growth. It distinguishes local from global extrema and introduces no arbitrary slice of a classification problem.

## Limitations and evidence
The primary sources were materially examined in accessible HTML/arXiv text at their relevant structural and index-variance sections; the closely related published centered-Hermite spectral-gap record was available only in summary form. No claim of exhaustive historical novelty is made. The proof is independent of numerical finite checks; independent mathematical validation has not been conducted. The centered variance and its second derivative are different observables.

Self-review: passed. Independent audit: not yet performed.
