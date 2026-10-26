# Scientific review — open-boundary twist convergence

## Correctness — PASS

The claim is conditional on a primitive normalized transfer matrix, exact \(SU(2)\) covariance, fixed boundaries, and a nonzero leading norm-transfer coefficient. Moving the physical twist to virtual indices gives a constant transfer insertion with \(\delta=4\pi/L\). The invariant virtual fixed point makes the first derivative of the dominant transfer eigenvalue vanish; consequently its \(L\)-th power differs from \(1\) by \(O(L^{-1})\). Analytic boundary coefficients contribute at most the same order. The proof establishes the stated rate but not its coefficient.

## Originality — PASS

The closest primary source is Su, Yao, and Furusaki, arXiv:2506.02496. It proves the periodic-boundary criterion and provides exact open-boundary AKLT and Majumdar–Ghosh examples; its discussion says a rigorous open-boundary argument for a broader class remains lacking. The present claim covers the specific primitive finite-bond SU(2)-covariant MPS class with fixed boundary vectors. The transfer-matrix and virtual-symmetry formalism is established background, not claimed as new. published-finding corpus and literature searches found no direct matching statement, but absence from a search is not a novelty proof.

## Value — PASS

The result gives an analytic \(O(L^{-1})\) open-boundary benchmark for a widely used exact state representation and allows fixed edge-boundary vectors. It clarifies a useful subset of the open-boundary gap-diagnostic problem without claiming a theorem for all gapped chains.

## Closest literature and limitations

- Su, Yao, and Furusaki, “Identification of gapless phases by squaring a twist operator,” arXiv:2506.02496v1/v3: general periodic-boundary criterion and exact open-boundary examples.
- Pérez-García, Verstraete, Wolf, and Cirac, “Matrix Product State Representations,” arXiv:quant-ph/0608197v2: standard MPS transfer and boundary formalism.

The estimate is tensor- and boundary-dependent and does not cover nonprimitive transfer matrices, noninjective symmetry-breaking MPS, or arbitrary open-boundary ground states.

Self-review: passed. Independent audit: not yet performed.
