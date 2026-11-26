# Independent mathematical audit

## correctness

PASS

At the specified specialization the matrix at P has an all-2 rank-one block of size three and two diagonal entries equal to 2, so has rank three. Independently, eliminate the lower block 2I: the upper Schur complement has diagonal u=2−d²/2, v=2−(b²+e²)/2, s=2−c²/2 and off-diagonals t=2−bd/2, y=2−ec/2, x=2−a in positions (1,2),(2,3),(1,3). The full determinant is four times the Schur determinant; its discriminant in a is 64(uv−t²)(vs−y²)=−4FG. The leading coefficient is −4v, a unit at P. The exact symbolic check also confirmed all three shifted coefficients and the branch-coordinate Jacobian −64, without running the supplied script. The two holomorphic unit square roots factor F and G into the four claimed coordinates with invertible Jacobian; W=(2Aa+B)/(2i) completes the local biholomorphism. In the equation W²=z1 z2 z3 z4 the Jacobian locus has W=0 and at least two vanishing z_i, giving exactly the six distinct surface branches. The nonsquare product gives a domain, the singular locus has codimension two, and the hypersurface is Cohen–Macaulay, so it is normal; it is Gorenstein and its lowest term W² gives multiplicity two. These statements concern only the indicated analytic germ and completion, not other rank-three points or global strata.

## originality

PASS

Hikami supplies this matrix, the exact parameter specialization, the accidental strata and their meeting point, and the incidence-fiber jump. His inspected collision discussion does not identify the full analytic/completed germ. The closest Resultary record is about transverse A1 geometry on an open rank-four stratum with different boundary traces, not this rank-three collision. The distinct contribution is the exact four-factor transverse discriminant and resulting analytic germ, not the collision, coordinate technique, or general properties of toric double covers. This conclusion is limited to the checked sources.

## value

PASS

The point is singled out by a collision of exceptional strata in an existing family. A full analytic normal form distinguishes the collision from generic transverse A1 behavior and determines its local singular branches; this is materially more informative than the already-known rank or incidence-fiber dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
