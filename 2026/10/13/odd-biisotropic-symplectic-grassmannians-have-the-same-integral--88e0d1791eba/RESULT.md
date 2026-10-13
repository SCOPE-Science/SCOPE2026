# Odd biisotropic symplectic Grassmannians have the same integral Chow motive as an ordinary Grassmannian
## Finding
For integers \(n\ge1\) and \(1\le k\le n+1\), let
\[
X=\mathrm{S}_2\mathrm{Gr}(k,2n+1)
\]
be the odd biisotropic symplectic Grassmannian attached to a general pencil of skew forms, and put
\[
Y=\mathrm{Gr}(k,2n+2-k).
\]
Then their integral Chow motives over \(\mathbb C\) are noncanonically isomorphic:
\[
\boxed{M(X)\cong M(Y)}.
\]

More precisely, if \(a_d\) denotes the number of \(d\)-dimensional Białynicki--Birula cells of \(X\), then
\[
M(X)\cong\bigoplus_d \mathbb Z(d)^{\oplus a_d}.
\]
Fonarev--Kuznetsov prove that \(a_d\) is exactly the number of \(d\)-dimensional Schubert cells of \(Y\). Hence the same Tate decomposition holds for \(M(Y)\).

The same cell count also gives the motivic-measure identity
\[
\boxed{
[X]=[Y]=\sum_d a_d\,\mathbb L^d
}
\]
in \(K_0(\mathrm{Var}_{\mathbb C})\), where \(\mathbb L=[\mathbb A^1]\).

Thus the equality of graded singular cohomology groups proved in the source lifts to the integral Chow-motive level. In particular, the integral Chow groups of \(X\) and \(Y\) have equal graded ranks. No ring isomorphism is asserted.

## Assumptions and scope
The ground field is \(\mathbb C\). The variety \(X\) is the smooth projective variety defined in arXiv:2610.03309v1 by simultaneous isotropy for a general pencil of skew forms on a vector space of dimension \(2n+1\).

The range is
\[
n\ge1,\qquad 1\le k\le n+1.
\]
The source proves that
\[
\dim X=2k(n+1-k).
\]
The comparison Grassmannian has the same dimension:
\[
\dim Y
=
k\bigl((2n+2-k)-k\bigr)
=
2k(n+1-k).
\]

The Chow-motive statement uses integral coefficients. The isomorphism is noncanonical: it is obtained by identifying the multiplicities of the Tate summands, not by constructing a preferred correspondence between individual cells.

## Proof
Fonarev--Kuznetsov recall that \(X\) carries a \(\mathbb G_m\)-action with isolated fixed points and is smooth and projective. Białynicki--Birula theory therefore gives a filtration whose successive strata are affine spaces. If a fixed point has positive tangent-weight space of dimension \(d\), its attracting cell is isomorphic to \(\mathbb A^d\).

Brosnan's integral motivic Białynicki--Birula theorem applies to any smooth projective variety with a \(\mathbb G_m\)-action. When the fixed components are points, it gives
\[
M(X)\cong\bigoplus_{p\in X^{\mathbb G_m}}\mathbb Z(d_p),
\]
where \(d_p\) is the dimension of the positive tangent-weight space, equivalently the dimension of the corresponding attracting cell. Grouping fixed points by cell dimension yields
\[
M(X)\cong\bigoplus_d\mathbb Z(d)^{\oplus a_d}.
\]

The main theorem of arXiv:2610.03309v1 constructs a dimension-preserving bijection between these Białynicki--Birula cells and the Schubert cells of
\[
Y=\mathrm{Gr}(k,2n+2-k).
\]
Therefore \(Y\) has exactly \(a_d\) Schubert cells of dimension \(d\). Applying the same cellular-motive decomposition to the Schubert filtration gives
\[
M(Y)\cong\bigoplus_d\mathbb Z(d)^{\oplus a_d},
\]
which proves \(M(X)\cong M(Y)\).

For the Grothendieck ring, additivity across a finite algebraic cell decomposition gives
\[
[X]
=
\sum_d a_d[\mathbb A^d]
=
\sum_d a_d\mathbb L^d.
\]
The Schubert decomposition gives the identical formula for \(Y\), proving \([X]=[Y]\).

## Verification
The proof uses no finite experiment.

The initiating full text was checked at the points where it establishes all required geometric inputs: \(X\) is smooth and projective, the chosen \(\mathbb G_m\)-action has isolated fixed points, the Białynicki--Birula strata are affine spaces, and Theorem 1.1 gives a dimension-preserving equality of cell counts with the Schubert decomposition of \(Y\).

Brosnan's Theorem 3.5 was checked in the full text of arXiv:math/0407305v3. It gives an integral motivic decomposition for a smooth projective \(\mathbb G_m\)-variety into Tate twists of the motives of the connected fixed components. Here those components are points, so every summand is an integral Tate motive.

The two comparison varieties have equal dimension by the displayed elementary calculation, so the cell dimensions being matched refer to the same grading range.

## Relationship to prior work
Fonarev--Kuznetsov prove that the number of \(d\)-dimensional Białynicki--Birula cells of \(X\) equals the number of \(d\)-dimensional Schubert cells of \(Y\). Their stated consequence is an isomorphism
\[
H^\bullet(X,\mathbb Z)\cong H^\bullet(Y,\mathbb Z)
\]
of graded abelian groups. They explicitly note that the cohomology-ring structure is a separate question.

Brosnan proves the general integral motivic Białynicki--Birula decomposition, but his paper predates odd biisotropic symplectic Grassmannians and contains no specialization to this family.

The new conclusion is obtained by combining these two statements: the dimension-preserving cell bijection determines the full multiplicity list in Brosnan's Tate decomposition. Targeted searches for the source together with “Chow motive,” “Tate motive,” “Grothendieck class,” and the comparison Grassmannian did not locate a prior statement of this specialization.

## Limitations
The motive isomorphism is noncanonical and does not identify products. In particular, it does not answer the source's separate question about the ring structure of \(H^\bullet(X,\mathbb Z)\), nor does it assert an isomorphism of Chow rings.

The statement is made over \(\mathbb C\), matching the source's singular-cohomology setup.

The initiating paper cites an in-preparation manuscript on \(\mathrm{S}_2\mathrm{Gr}(3,7)\). No public full text of that manuscript was located, so it remains a residual literature risk for the special case \((k,n)=(3,3)\).

## References
1. Anton Fonarev and Alexander Kuznetsov, *Betti Numbers of Odd Biisotropic Symplectic Grassmannians*, arXiv:2610.03309v1, 2 October 2026.
2. Patrick Brosnan, *On motivic decompositions arising from the method of Białynicki--Birula*, arXiv:math/0407305v3; Inventiones Mathematicae 161 (2005), 91--111, DOI 10.1007/s00222-004-0419-7.
