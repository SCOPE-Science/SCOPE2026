# Independent mathematical audit

## correctness

PASS

Wang's Theorem 4.3 supplies a nonzero intertwined harmonic sector of dimension 8C_(m+1) under exactly the four-layer spin condition. From (4.20), only the pairs (0,1), (2,4), (3,5), (3,4), (6,7) contribute to half the second trace; their products give the stated coefficient A_d and agree with the source polynomial. The determinant is 1 (also checked by factoring out the row phases: their product is ω^(4d)=1 and the remaining rational matrix has determinant 1). For α=ζ+ζ⁻¹, A_d=(4−2d+dα)/d² is nonzero, since equality to zero would make α=2−4/d a rational nonintegral algebraic integer. All its conjugates have magnitude less than 1 for odd d≥3. A nonzero integer norm is therefore impossible. A scalar power would have scalar ξ with ξ⁸=1, so the matrix would have finite order and A_d would be an algebraic integer. This contradiction passes through the intertwiner and rules out scalar powers of the full walk. For precision about the entire set of nonreviving states, not just a full-measure open subset: partition the finite spectrum by λ∼μ iff λ/μ is a root of unity. A vector revives projectively exactly when its spectral support lies in one equivalence class (take a common multiple of the finite orders). The reviving states are thus a finite union of proper spectral subspaces, in either restriction or full space, since either spectrum has at least two classes. This also handles repeated eigenvalues without needing simplicity, and does not exclude eigenstate or approximate recurrence. The supplied floating-point tests were inspected, not treated as proof or executed.

## originality

PASS

The invariant sectors and the explicit odd characteristic polynomial are prior. No exact scalar-power obstruction for those odd sectors, or the resulting generic projective nonrevival for this model, was located in the strongest inspected sources. The conclusion is limited to that distinct arithmetic use of the known spectrum.

## value

PASS

The known eight-dimensional reduction leaves a qualitative dynamics question open: unit-circle spectral locations permit both exact global revival and nonperiodicity. A single exact obstruction resolves this uniformly in odd dimension and for both allowed signs, with arbitrary exterior spins, rather than checking individual spectra to a time cutoff. The result distinguishes generic projective nonrevival from recurrence of special states; the even comparison is a known fixed sector, not a statement that the full even walk revives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
