# Self-review

## Correctness — PASS

The invariant phase-locked ray proves necessity, including the stationary-ray equality case. Direct exact differentiation yields the quartic Gram identity; its eigenvalues are \(a(1\pm\gamma/\sqrt{a^2+\omega^2})>0\), while the quartic's two-square coefficients are positive. Degree sharpness follows from quarter-turn averaging of all strict quadratic candidates and parity of the leading term of any globally positive polynomial. `verify.py` reproduces the central algebra from the stated equations. The relaxation estimate follows from the minimum Gram eigenvalue and quartic norm equivalence.

## Originality — PASS under inspected material

The work is restricted to the phase-locked domain \(0\le\omega\le\gamma\). A prior rotating-domain quartic theorem assumed \(\gamma<\omega\) and therefore cannot be specialized to this sector; its quartic coefficient would not give a positive-definite certificate here. Shevchenko–Liu–Liu supply a general invariant-measure/angle characterization, not the claimed explicit fixed-degree dual-SOS and sharp degree boundary. Ahmadi–Parrilo establish generic degree-unbounded SOS conversion, not this fixed-degree formula. No exact matching mathematical-record entry was identified by searches of the angular-locked normal form, coefficient boundary, equivalences or sharp SOS-degree claim. This is best-knowledge originality, not an assertion that searches prove uniqueness. Residual risk: an equivalent treatment in older planar equivariant cubic or homogeneous-classification literature may exist; one related 2026 cubic counterexample was available only at abstract level.

## Mathematical value — PASS

The locked angular sector is qualitatively different from a rotating-angle system. This theorem gives a complete global attraction boundary there and determines an optimal finite SOS relaxation degree, even for parameters where Euclidean radius initially grows. The parameter-independent degree four closes a concrete computational certification gap not decided by broad converse Lyapunov existence theorems.

## Limitations and closest literature

The theorem is specific to a fourfold-equivariant cubic normal form, and the quadratic obstruction concerns **strict** derivatives. The full original text of the Liu–Fitzsimmons counterexample and the older Samardžija classification were not inspected; independent priority validation remains outstanding. Finite rational tests are diagnostics, not a substitute for the exact symbolic identities and proof.

Self-review: passed. Independent audit: not yet performed.
