# Independent mathematical audit

## correctness

PASS

The mixed directional derivative of the exact-degree addition kernel gives TT* up to a positive normalization. I rebuilt its rational matrix at dot product -1/3, using the unnormalized tangent directions but unit vertices, and recovered the symbolic determinant with factor multiplicities 2, 3, 3. Independently I generated solid harmonics from arbitrary z^0 and z^1 homogeneous coefficients, recursively solving (k+2)(k+1) f_{k+2}=-(∂_x²+∂_y²)f_k. Their directional derivatives at the sign vertices differ from the unit-vertex derivatives by a common nonzero degree-dependent factor. Exact row reduction yielded 0,3,5,6,8,5,8,8,8,8,8,8,8; multiplying the degree-three and degree-five evaluation matrices by the listed constraint rows gave zero, with independent rows spanning the full left nullspaces. For l≥13, DLMF 18.14.3 at alpha=beta=0 gives |P_m(-1/3)|≤sqrt(2/pi)(9/8)^(1/4)/sqrt(m+1/2)<1/sqrt(m). The Legendre differential identities bound the two derivative ratios as in the proof; the first two factors have off-diagonal ratio <6/16+5/2<3, and the third <18/16+5/2<9. This is an analytic tail exclusion, not extrapolation. Replay recipe: build the eight rows in RESULT.md order, use the solid-harmonic recurrence and exact rational row reduction through degree 12, then use the two displayed differential identities and inequalities; the frozen verify_tetra.py was inspected, not used for the independent calculation.

## originality

PASS

The defensible increment is the isolated-degree tetrahedral gradient rank law including both exceptional compatibility spaces and the all-degree cutoff, not general addition identities or the idea of rank defects on symmetric point sets. No equivalent or dominating theorem was found in the bounded comparisons.

## value

PASS

The tetrahedron is a canonical minimal symmetric spatial array, and the precise invariant answers whether arbitrary tangent data can be interpolated using one spectral degree. The degree-five loss after a surjective degree is not predictable from domain dimension; the explicit constraints identify which data are unavailable and the all-degree cutoff settles future exceptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
