# Scientific review — four Gaussian Gabor atoms

## Correctness (C): PASS

For the specified unit Gaussian and Weyl action, Bargmann coherent-kernel inner products give a four-by-four Gram matrix with the exact determinant in Equation (1) of `RESULT.md`. A polynomial symbolic check and independent high-precision coherent-kernel products verify the matrix identity, while the analytic proof supplies all-parameter validity. The positivity representation separates the small-area scales into: larger side tending to zero, to a positive constant, or to infinity. Only the finite nonzero limit contributes at order \(h^4\); its coefficient is \(\pi^4F(\pi a^2)\). The derivative sign law has a unique positive critical root by successive integration of a strictly decreasing fourth derivative. The same three-regime compactness argument proves uniform optimality and convergence of **all** maximizing shapes. The square asymptotic follows directly from Taylor expansion. The proof does not rely on finite computations for its infinite-quantifier conclusions.

## Originality (O): PASS, with residual historical-priority uncertainty

The full original research results inspected were V. Oussa, arXiv:2609.27774 (four time-frequency shifts of a specially constructed non-Gaussian Gelfand–Shilov window), and M. Faulhuber, DOI 10.1007/s00041-017-9526-x (sharp **infinite-lattice frame-operator** upper bounds). Two additional published mathematical results were inspected in full: an integer-area mixed-arithmetic four-point independence theorem (all \(L^2\) windows, a rational-rank-two restriction) and an arithmetic frame criterion for Gaussian-derivative **infinite lattices**. The latter two concern linear independence or frame existence, not four-atom Gram volume. Neither the window-restricted four-point dependence theorem nor the infinite-lattice frame theorems implies the new exact finite Gaussian Gram determinant or the small-area optimized asymmetry constant. Searches of equivalent formulations, broader coverage, exact constants and published mathematical records found no equivalent theorem. However an unindexed earlier identity or design calculation could exist; that uncertainty remains and is not replaced by a declaration of absolute priority.

## Value (V): PASS

The product of four Gram eigenvalues is the squared volume of the four-atom parallelepiped, a natural geometric measure of joint independence and design quality. Fixed phase-space area alone does not determine the best finite sampling geometry. The unique nonzero optimal long-side scale and the \(h^4\)-versus-\(h^6\) square loss reveal an order-two symmetry-breaking effect not deducible from the existence of independence or from infinite-lattice frame-bound minimization. The theorem concerns this natural canonical object and exact rate, not an arbitrary numerical slice.

## Scope and risks

The result optimizes four Gaussian atoms only, under a fixed rectangular cell area and only in the \(h\downarrow0\) regime; there is no assertion about general point sets or spectral condition numbers. Exact constants rely on the explicit Gaussian and Weyl normalizations. Supplementary symbolic and finite numerical checks are not independent certification. Full text of one potentially related 2024 Gaussian Gabor frame paper was not systematically examined and historical-priority risk remains.

Self-review: passed. Independent audit: not yet performed.
