# Review of the hemispherical affine projection theorem

## Correctness — PASS
The calculation specifies the normalized surface measure, four orthonormal affine basis functions, the symmetric kernel, and the exact \(L^1\)/\(L^\infty\) operator norms. The hard maximization is global, not based on sampled heights: conditional azimuthal symmetry makes the radial kernel absolute integral monotone, convex interpolation controls heights below \(1/3\), and a Hilbert-space Cauchy--Schwarz estimate controls all greater heights. The exact equatorial negative cap integral and a rational strict-gap comparison exclude all competing heights. Equality in the triangle inequality characterizes the bounded extremizers; kernel symmetry and strict almost-everywhere localization establish \(L^1\) nonattainment. The standalone checker corroborates arithmetic and quadrature, without standing in for proof.

## Originality — PASS within inspected evidence
The nearest full-sphere work (Defant and collaborators, arXiv:2405.12123, Corollary 4.12) computes a different, fully rotation-invariant projection constant. The manifold projector work (Hangelbroek and collaborators, arXiv:1005.2424, Theorem 5.1; arXiv:1012.4852, Section 5) proves general stability for different kernel-translate approximation spaces, without the present sharp four-dimensional hemisphere norm. A published simplex affine-projection constant and previously reported first-harmonic semicircle calculations involve different spaces and measures. The exact number, complete equatorial optimizer set, and cap-sign equality case do not follow from the inspected statements. This assessment does not establish exhaustive historical priority: older unindexed hemispherical approximation work remains a risk.

## Value — PASS
The curved hemisphere with normalized surface area is the simplest nontrivial spherical region with a boundary, and fitting ambient affine functions is a canonical, fixed finite-dimensional least-squares operation on it. The result supplies an exact stability benchmark \(61\sqrt5/15-7\), strictly larger than the full-sphere benchmark \(5/3\), and locates all maximizers at the equator despite no discrete boundary mass. It characterizes norm-attaining bounded data, proves nonattainment in the integrable endpoint, and gives the exact worst positivity overshoot for nonnegative bounded data. These features characterize a natural sharp invariant, not an arbitrary numerical slice or a general-bound restatement.

## Limits and comparison risk
The theorem is limited to ordinary uniform surface measure on the curved two-sphere hemisphere and a degree-one affine range. It neither solves general spherical caps nor identifies minimal projections among all possible projections. Bibliographic indexing can omit alternate terminology or early technical reports. The numerical checks are finite tests and do not independently certify a continuous theorem.

Self-review: passed. Independent audit: not yet performed.
