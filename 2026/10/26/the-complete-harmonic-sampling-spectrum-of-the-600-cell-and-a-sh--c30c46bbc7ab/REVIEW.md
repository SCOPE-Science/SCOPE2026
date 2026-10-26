# Scientific review

## Correctness — PASS

With normalized sphere area, the exact-degree addition kernel on \(S^3\) is \((\ell+1)U_\ell(\langle x,y\rangle)\), so dividing the evaluation rows by \(\ell+1\) produces \(U_\ell/(\ell+1)\), of diagonal \(1\). Since the vertex set is the binary icosahedral group, the matrix is group convolution. The affine \(E_8\) McKay recurrence gives the genuine nonnegative integer multiplicities in the symmetric powers of the defining representation; Schur orthogonality gives exactly nine spectral blocks (including absent-block eigenvalue zero), with total multiplicity \(120\). At each noncentral element, the icosahedral character has an angle denominator dividing \(2,3,5\), so the derived sixty-step multiplicity identity is exact in all degrees. The two displayed degree-\(58\) and degree-\(59\) multiplicity vectors prove the sharp threshold, with all larger degrees handled by the sixty-step identity. Vanishing of the off-antipodal kernel at three indicated angles proves both directions of the tight-degree characterization. A standalone checker reproduces the listed recurrence values and numerical Gram spectra; its finite range is not used to conclude the all-degree theorem.

## Originality — PASS, with residual priority risk

Weeks, arXiv:math/0502566, Section 10 analyzes the invariant Laplace eigenfunctions of the quotient, whose nonzero or zero invariant counts are precisely the trivial group-representation block; it does not state the evaluation Gram spectrum or the recovery cutoff. Dechant, arXiv:1307.6768, analyzes the binary-icosahedral spinor realization and McKay graph, which are explicitly treated as prior facts here. The 600-cell spherical-code article arXiv:1906.03062 investigates energy/design bounds, not exact-degree evaluation onto antipodal parity samples. OEIS A087866 records related constituent-count information, not the full weighted-by-irreducible-dimension block spectrum or interpolation implication. Targeted literature and research-record searches for 600-cell harmonic sampling, binary icosahedral Peter–Weyl blocks, affine \(E_8\) spectral sampling and rank thresholds found no dominating theorem. Nonetheless, classical character tables or a differently phrased group sampling theorem could imply the results; this remains a substantial specialist-verification risk, not a claim of absolute priority.

## Mathematical value — PASS

The 600-cell is a canonical highly symmetric spherical design, and exact-degree harmonic sampling is a natural stability/interpolation problem for such point sets. A complete finite-dimensional spectrum for every degree, a sharp eventual interpolation threshold, unexpected nonmonotonic rank at degree \(58\), and an infinite family of optimally conditioned parity frames are meaningful global structural statements rather than an arbitrary finite calculation. The value rests on the combined sampling and stability classification, not on rediscovering standard representation theory.

## Scope and limitations

All claims concern the entire 120-point set, exact homogeneous spherical-harmonic degree and normalized surface measure. No result for arbitrary subsets or mixed degrees is implied. Source priority remains subject to independent historical and specialist review.

Self-review: passed. Independent audit: not yet performed.
