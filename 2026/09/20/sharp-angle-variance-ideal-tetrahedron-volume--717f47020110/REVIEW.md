# Review — Sharp angle-variance profile for ideal tetrahedron volume

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The classical input is the ideal-tetrahedron volume formula
\[
V=\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma),
\qquad
\alpha+\beta+\gamma=\pi,
\]
together with the standard Lobachevsky identities.

For fixed nonzero
\[
Q=\sum(\alpha-\pi/3)^2,
\]
a volume maximizer is interior because boundary triples have volume zero,
whereas the displayed isosceles triple with the same \(Q\) is
nondegenerate and has positive volume. The two-constraint Lagrange
equations reduce the three angles to roots of a single strictly convex
function
\[
g(x)=\Lambda'(x)-2\mu x,\qquad g''(x)=\csc^2x>0.
\]
Thus at least two maximizing angles coincide.

For the isosceles parameterization
\[
(2s,\pi/2-s,\pi/2-s),
\]
the identities
\[
V=2\Lambda(s),\qquad
Q=6(s-\pi/6)^2
\]
were checked algebraically. When both stationary branches
\(s=\pi/6\pm r\) exist, their difference has derivative
\[
-\log(1-4\sin^2r)>0,
\]
so the \(+\) branch is the unique maximizing branch up to permutation.

The sharp quadratic corollary follows from
\[
f(r)=\Lambda(\pi/6)-\Lambda(\pi/6+r),
\]
whose second derivative
\[
f''(r)=\cot(\pi/6+r)
\]
is nonnegative and decreasing for \(0\le r\le\pi/3\). Pairing the
integral representation of \(rf'(r)-2f(r)\) at \(t\) and \(r-t\) proves
that \(f(r)/r^2\) decreases, so its boundary value gives the global best
coefficient. The family
\((\pi-2\varepsilon,\varepsilon,\varepsilon)\) verifies sharpness in the
limit.

The endpoint, equality, and Taylor-expansion calculations are consistent:
\[
v_3=2\Lambda(\pi/6),\qquad
Q\to2\pi^2/3,\qquad
\frac{v_3-V}{Q}\to\frac{3v_3}{2\pi^2}.
\]

## Originality

**PASS, to the best of our knowledge.**

The following coverage was checked.

- Classical sources give the Lobachevsky volume formula and the unique
  maximality of the regular ideal tetrahedron.
- Haagerup--Munkholm establish maximality of regular ideal simplices in
  all dimensions; Peyerimhoff studies related maximal-volume simplex
  problems.
- Thurston's notes state that volume close to \(v_3\) forces dihedral
  angles close to \(60^\circ\), but do not give the fixed-\(Q\)
  dihedral-angle profile or the sharp global coefficient stated here.
  A nearby quadratic estimate in the notes concerns a face-angle
  parameter for finite simplices and is not the same statement.
- Work on angle structures and hyperbolic polyhedral metrics uses strict
  concavity and volume optimization, but the located statements do not
  supply this exact variance-constrained envelope.
- Searches using "ideal tetrahedron", "Lobachevsky function", "volume
  deficit", "dihedral-angle variance", "quantitative stability",
  "maximal volume", "sum of squares", and equivalent simplex terminology
  did not locate the theorem or a stronger result implying it.
- Recent work on generalized tetrahedra and ideal-polyhedron volume
  optimization was checked for current-status coverage; no matching
  fixed-variance formula was located.

The main residual originality risk is terminological: because the proof
is an elementary constrained extremum for the Lobachevsky function, an
equivalent inequality could occur in special-function literature or as
folklore without tetrahedral terminology.

No specific inaccessible source was identified as especially likely to
contain this exact statement.

## Value

**PASS.**

The result strengthens the classical scalar statement "the regular ideal
tetrahedron maximizes volume" in two ways. First, it determines the
complete optimal volume profile at every prescribed squared
dihedral-angle deviation from regularity, including the unique equality
family. Second, it yields a simple global inverse-stability inequality
with the best possible coefficient, and separates the stronger local
quadratic behavior near the regular tetrahedron from the weaker constant
forced by degeneration.

The formula is directly usable wherever near-maximal ideal tetrahedra
must be converted into explicit control of their dihedral angles, for
example in arguments using angle structures or efficient hyperbolic
simplices.

## Scientific limitations

- Only ideal tetrahedra in \(\mathbb H^3\) are covered.
- The stability coordinate is Euclidean variance of dihedral angles, not
  an intrinsic moduli-space distance.
- No extension to general ideal polyhedra, finite simplices, hyperideal
  tetrahedra, or higher dimension is established.
- Originality is to the best of our knowledge, with residual risk of an
  equivalent special-function or folklore formulation.
