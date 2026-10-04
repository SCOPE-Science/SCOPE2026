# Sharp radial product profile for vertex distances in a regular tetrahedron
## Finding
Let \(A_1A_2A_3A_4\) be a regular tetrahedron with circumcenter \(O\) and circumradius \(R>0\). For a point \(P\in\mathbb R^3\), put \(\rho=OP\) and
\[
\Pi(P)=\prod_{i=1}^4 PA_i.
\]
Then, for every \(\rho\ge 0\), the complete set of values of \(\Pi(P)\) on the sphere \(OP=\rho\) is the interval
\[
\left[
|R-\rho|\left(R^2+\rho^2+\frac{2R\rho}{3}\right)^{3/2},
\ (R+\rho)\left(R^2+\rho^2-\frac{2R\rho}{3}\right)^{3/2}
\right].
\]
For \(\rho>0\), the lower endpoint occurs exactly when \(P\) lies on one of the four rays from \(O\) through a vertex, and the upper endpoint occurs exactly when \(P\) lies on one of the four opposite rays. At \(\rho=0\), both endpoints equal \(R^4\).

## Assumptions and scope
The tetrahedron is Euclidean and regular. The point \(P\) is arbitrary in \(\mathbb R^3\), including points inside, on, or outside the circumsphere. Distances are ordinary Euclidean distances. The statement is radial: \(R\) and \(\rho=OP\) are fixed while the direction of \(P-O\) varies. No assertion is made here for nonregular tetrahedra or for regular simplices in dimensions other than three.

## Proof
Translate \(O\) to the origin and write the four vertex vectors as \(R u_i\), where \(\|u_i\|=1\) and
\[
u_i\cdot u_j=-\frac13\quad(i\ne j),\qquad \sum_{i=1}^4u_i=0.
\]
For \(\rho>0\), write \(P=\rho p\) with \(\|p\|=1\), set \(x=\rho/R\), and define \(t_i=p\cdot u_i\). The regular-tetrahedron frame identities give
\[
\sum_{i=1}^4t_i=0,
\qquad
\sum_{i=1}^4t_i^2=\frac43.
\]
Conversely, these two equations describe the image of the unit sphere under \(p\mapsto(t_1,t_2,t_3,t_4)\): the vectors \(u_i\) form a tight frame with \(\sum_i u_i u_i^{\mathsf T}=\frac43 I\).

The normalized squared distances are
\[
\frac{PA_i^2}{R^2}=1+x^2-2x t_i.
\]
Hence it is enough to extremize
\[
F(t_1,t_2,t_3,t_4)=\prod_{i=1}^4(1+x^2-2x t_i)
\]
subject to the two displayed constraints. If \(x=0\), then \(F\equiv1\), so assume \(x>0\). The factors are positive unless \(x=1\) and one \(t_i=1\), which is exactly a vertex direction and already gives the lower endpoint \(F=0\).

At every other extremum, apply Lagrange multipliers to \(\log F\). For constants \(\lambda,\mu\), each coordinate satisfies
\[
-\frac{2x}{1+x^2-2x t_i}=\lambda+2\mu t_i.
\]
After clearing the denominator, every \(t_i\) is a root of one quadratic polynomial. That quadratic cannot vanish identically because \(x>0\). Thus an extremal quadruple has exactly two distinct coordinate values. If one value has multiplicity \(k\in\{1,2,3\}\), the equations \(\sum t_i=0\) and \(\sum t_i^2=4/3\) leave, up to permutation, only the three symmetry types
\[
(1,-1/3,-1/3,-1/3),
\quad
(-1,1/3,1/3,1/3),
\quad
(1/\sqrt3,1/\sqrt3,-1/\sqrt3,-1/\sqrt3).
\]
Their values of \(F\) are respectively
\[
A=(x-1)^2\left(1+x^2+\frac{2x}{3}\right)^3,
\]
\[
B=(x+1)^2\left(1+x^2-\frac{2x}{3}\right)^3,
\]
and
\[
C=\left(1+\frac{2x^2}{3}+x^4\right)^2.
\]
Direct subtraction factors as
\[
A-C=-\frac{64}{27}x^3(x^2+x+1),
\]
\[
B-C=\frac{64}{27}x^3(x^2-x+1),
\]
\[
A-B=-\frac{128}{27}x^3(x^2+1).
\]
For every \(x>0\), these identities give \(A<C<B\). Therefore \(A\) is the global minimum and \(B\) the global maximum on the compact direction sphere. Taking square roots and restoring \(R\) yields exactly the claimed endpoints.

The type giving \(A\) has \(p=u_i\), hence \(P\) lies on a vertex ray. The type giving \(B\) has \(p=-u_i\), hence \(P\) lies on the opposite ray. The strict inequalities \(A<C<B\) show that no other direction has either endpoint value. Finally, for \(\rho>0\), the direction sphere is connected and \(\Pi\) is continuous, so its image is the entire interval between its minimum and maximum.

## Verification
A standalone deterministic checker reconstructs a unit-circumradius regular tetrahedron, evaluates the theorem on a fixed radial grid and seeded random directions, verifies all equality rays, and checks the three branch-factorization identities numerically. The analytic proof above, not the finite sampling, establishes the infinite statement.

The checker is `verify.py`. Its packaged run returns `VERIFY_OK`; it reports the number of checks and normalized numerical errors. The special cases \(\rho=0\) and \(\rho=R\) are included explicitly.

## Relationship to prior work
Hajja, Hayajneh, Nguyen, and Shaqaqha study the distances from an arbitrary point to the vertices of a regular simplex and prove that the familiar quartic relation among those distances is essentially the only global polynomial relation. Their first public preprint is arXiv:1609.06552v1, submitted 2016-09-21. The full text also records earlier work of Bentin on regular simplicial distances and lists further questions about algebraic relations on the circumsphere. The inspected full text does not state an extremal product problem or a fixed-radius product profile.

The present result asks a different, symmetry-invariant question: after the radius \(OP\) is fixed, what is the complete range of the multiplicative vertex-distance invariant \(\Pi(P)\)? The answer is not implied merely by the quartic distance relation; one must optimize over the remaining directional degrees of freedom, and the proof identifies all stationary symmetry types and orders them exactly.

A recent planar paper of Murphy and Tran, arXiv:2605.12985, treats optimization of the product of distances from a moving point to the vertices of a fixed triangle. It supplies independent motivation for the multiplicative invariant but studies a different object, domain, and constraint and contains no tetrahedral radial theorem in the inspected text.

## Limitations
The result is proved only for regular tetrahedra in Euclidean three-space. No higher-dimensional analogue is claimed. Direct full-text access to Bentin's one-page 1995 note was not available in this review; the 2016 paper characterizes that note as a proof of the standard regular-simplex distance relation, but an unindexed older equivalent extremal statement remains a residual literature risk. Search absence is not treated as proof of novelty.

## References
1. M. Hajja, M. Hayajneh, B. Nguyen, and S. Shaqaqha, “Distances from the vertices of a regular simplex,” arXiv:1609.06552v1, first submitted 2016-09-21; later Results in Mathematics 72 (2017), 633–648, DOI 10.1007/s00025-017-0689-1.
2. J. Bentin, “Regular simplicial distances,” The Mathematical Gazette 79 (1995), 106, DOI 10.2307/3620008.
3. T. Murphy and K. Tran, “An optimization problem for triangles,” arXiv:2605.12985 (2026).
