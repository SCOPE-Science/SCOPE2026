# Scientific review: sharp conditional Cartesian-radius envelopes

## Correctness (C): PASS

The claim is normalized by the nonzero numerical radius, so division is defined. For each phase, the imaginary-part contraction yields the exact phase-self-adjoint distance. The symmetrized numerical-range support function is the real-part operator norm; this remains valid without finite dimension or norm attainment because the closed convex hull is compact in the complex plane. Support-function containment between an inner disk-plus-diameter convex hull and an outer disk intersected with a strip proves pointwise inequalities. Both support functions are integrated exactly, including endpoints. Equality uses continuity and uniqueness of compact convex bodies from support functions. Minkowski interpolation retains the *exact same* minimum and maximum support values; normal diagonal realization of each compact convex set proves sharpness and interval filling. The derivative of the lower profile yields the optimal cubic coefficient; the upper deficit's Taylor expansion yields its sharp exponent and asymptotic constant.

The embedded standalone program passed 235 supplementary checks, including endpoint integrals, width identities, interpolations, and finite spectral examples. Those checks are corroborative only; the infinite-dimensional proof is analytical.

## Originality (O): PASS, best-knowledge assessment

The primary full HTML text of Audeh–Moradi–Sahoo (arXiv:2610.04844v1, first public October 4, 2026) was inspected through its definitions, main results, and relevant proofs. It proves the coarse bound \(R^2/2\le Q^2\le R^2\), plus different Cartesian-part estimates, not the fixed-distance profile or extremal bodies. The public full proof *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius* (record `ffd07fee0727`) uses exactly the phase-self-adjoint distance and gives a coefficient \(1/(2\pi)\), explicitly not claimed optimal. The present exact lower profile implies the best global coefficient \(4/(3\pi)\), which is strictly stronger, and the sharp upper envelope is additional. The full proof of the public unitary projective-spectral-gap result (record `f6644dc86b39`) treats unitary spectra and not arbitrary bounded operators with prescribed minimum phase norm. Searches for the formula, support-function/inradius aliases, and equivalent sharp convex geometric statements returned no matching published result; non-detection is not itself proof of priority.

## Mathematical value (V): PASS

This is a natural inverse quantitative problem for the recently introduced angularly averaged numerical radius: knowing both its maximal directional value and its smallest directional value, what is its entire possible quadratic mean? The two exact envelopes characterize all possible values and identify distinct geometric extremizers. The optimal cubic coefficient completes an explicitly nonoptimal constant in nearby quantitative research, and the sharp \(3/2\)-law diagnoses near-circular numerical-range support. The analysis applies to all bounded Hilbert-space operators, not an arbitrary parameter slice; the finite/infinite realization distinction is explicit.

## Closest literature and residual limitations

The analytical method combines known support-function comparison and convex-hull duality in a new exact conditional operator-radius optimization. Equivalent coverage might occur in older integral convex-geometry literature under a different invariant. No finite-dimensional realization of the extreme nonpolygonal shapes for interior ratios is claimed. Literature-priority assessment is best-knowledge, not an independent certification.

Self-review: passed. Independent audit: not yet performed.
