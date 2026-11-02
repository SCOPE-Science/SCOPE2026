# Mathematical review

## Correctness — PASS

The sampling map, normalized Gegenbauer basis, and sign criterion were reconstructed explicitly. The centered-difference exponential generating function gives the exact top-degree coefficient, and Gegenbauer leading terms give the all-dimensional obstruction. On the two-sphere, direct low-degree Legendre expansions cover every nonnegative Schoenberg coefficient; the only nonalgebraic step uses the published Bernstein estimate for Legendre polynomials to bound all odd input degrees at the single interior sample. The checker passed 292 exact rational supplementary assertions. Finite checks are corroboration, not evidence for an infinite conclusion.

## Originality — PASS under inspected evidence

The closest motivating manuscript, Otten–Nguyen–Watts, arXiv:2608.04836 (first public 2026-08-05), proves positivity preservation for a *different operator* in the geodesic-distance variable on the circle, and separately gives an affine two-sphere failure at exactly degree four with coefficient -9/256. Its accessible theorem, Section 4 and conclusion were inspected; they do not provide an all-degree affine classification, nor the all-dimensional top Gegenbauer formula. Schoenberg's 1942 characterization and the published 2008 Legendre inequality are methodological inputs, not claims of this result. Adjacent Gegenbauer positivity and dimension-walk results employ different functionals. Text searches for equivalent affine/spherical Bernstein cone-preservation statements found no stronger theorem covering the claims; as always, incomplete indexing of older approximation theory remains a residual originality risk.

## Value — PASS

The natural shape-preserving question of whether ordinary Bernstein approximation can maintain a spherical covariance kernel receives an exact, all-degree answer on the usual two-sphere. The closed degree/dimension obstruction exposes the general mechanism and converts a previously given isolated fourth-degree example into a sharp preservation frontier. The classification is intrinsic to Schoenberg positivity and does not depend on arbitrarily chosen parameter slices.

## Closest literature and limitations

Otten, Nguyen & Watts (2026), arXiv:2608.04836, Section 4, supplies the degree-four affine counterexample; it does not give the degree-one-through-three preservation classification or universal coefficient formula. Schoenberg (1942) characterizes zonal positive-definite kernels. Gautschi–Giordano (2008), Eq. (56), records the Bernstein–Legendre bound required in the proof. The remaining low-degree preservation problem for spheres of dimension greater than two is not decided here. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
