# Connected fertilitopes have an exact frontier formula for their Euclidean inradius
## Finding
Let \(\mathcal B\) be a connected binary building set on
\[
[m]=\{1,\ldots,m\},
\qquad
m\ge2,
\]
and let
\[
y_I>0
\qquad
(I\in\mathcal B).
\]
Consider the binary nestohedron
\[
P
=
\sum_{I\in\mathcal B}y_I\Delta_I
\subset\mathbb R^m,
\tag{1}
\]
where
\[
\Delta_I=\operatorname{conv}\{e_i:i\in I\}.
\]

For every \(I\in\mathcal B\), put
\[
z_I
=
\sum_{\substack{J\in\mathcal B\\J\subseteq I}}y_J.
\tag{2}
\]
For a proper building-set element \(I\ne[m]\), define its intrinsic facet-normal length
\[
\nu_I
=
\sqrt{\frac{|I|(m-|I|)}m}.
\tag{3}
\]

Call
\[
\mathcal F\subseteq\mathcal B\setminus\{[m]\}
\]
a frontier when its members are pairwise disjoint and
\[
\bigcup_{I\in\mathcal F}I=[m].
\tag{4}
\]
Because a binary building set is laminar and contains all singletons, frontiers always exist.

Then the Euclidean inradius of \(P\), measured intrinsically in its affine hull, is
\[
\boxed{
r_{\mathrm{in}}(P)
=
\min_{\mathcal F\text{ frontier}}
\frac{
z_{[m]}-\displaystyle\sum_{I\in\mathcal F}z_I
}{
\displaystyle\sum_{I\in\mathcal F}\nu_I
}.
}
\tag{5}
\]

Writing
\[
r=r_{\mathrm{in}}(P),
\]
the complete set of incenters is
\[
\boxed{
\operatorname{Cent}(P)
=
\left\{
c\in\mathbb R^m:
\sum_{i=1}^m c_i=z_{[m]},
\quad
\sum_{i\in I}c_i\ge z_I+r\nu_I
\text{ for every proper }I\in\mathcal B
\right\}.
}
\tag{6}
\]

The source proves that a nonempty polytope is a fertilitope exactly when it is an integral binary nestohedron. Therefore every connected fertilitope has the exact finite formula (5), using its positive integral binary-nestohedron data.

## Assumptions and scope
The Euclidean metric is the one induced from the standard orthonormal coordinates of \(\mathbb R^m\).

Connectedness means
\[
[m]\in\mathcal B.
\]
The source definition of a binary building set makes its members laminar: any two members are either disjoint or one contains the other. All singletons belong to \(\mathcal B\).

The weights in (1) are assumed strictly positive. Fertilitopes have positive integral weights in the source realization, so they are included.

The inradius is intrinsic to the affine hull
\[
H=
\left\{
x\in\mathbb R^m:
\sum_i x_i=z_{[m]}
\right\}.
\tag{7}
\]

## Proof
The source gives the generalized-permutohedral description
\[
\sum_{i\in I}x_i\ge z_I
\qquad
(I\in\mathcal B),
\tag{8}
\]
together with the fixed total
\[
\sum_{i=1}^m x_i=z_{[m]}.
\tag{9}
\]
For a connected nestohedron with positive coefficients, each proper
\[
I\in\mathcal B\setminus\{[m]\}
\]
indexes a facet.

The translation space of \(H\) is
\[
H_0=
\left\{
u:\sum_i u_i=0
\right\}.
\]
The ambient normal of the supporting hyperplane
\[
\sum_{i\in I}x_i=z_I
\]
is \(\mathbf1_I\). Its orthogonal projection to \(H_0\) is
\[
\mathbf1_I-\frac{|I|}{m}\mathbf1,
\]
whose squared norm is
\[
|I|-\frac{|I|^2}{m}
=
\frac{|I|(m-|I|)}m.
\]
Thus its intrinsic normal length is exactly \(\nu_I\) from (3).

Consequently a Euclidean ball of radius \(\rho\) centered at \(c\in H\) lies in \(P\) exactly when
\[
c(I):=\sum_{i\in I}c_i
\ge
z_I+\rho\nu_I
\qquad
\text{for every proper }I\in\mathcal B.
\tag{10}
\]

We first prove the upper bound in (5). Let \(\mathcal F\) be any frontier. Since its members partition \([m]\), summing (10) over \(I\in\mathcal F\) gives
\[
z_{[m]}
=
c([m])
\ge
\sum_{I\in\mathcal F}z_I
+
\rho\sum_{I\in\mathcal F}\nu_I.
\]
Hence
\[
\rho
\le
\frac{
z_{[m]}-\sum_{I\in\mathcal F}z_I
}{
\sum_{I\in\mathcal F}\nu_I
}.
\tag{11}
\]
Taking the minimum over frontiers gives the required upper bound.

It remains to show that this bound is always feasible.

Fix \(\rho\ge0\) and write
\[
L_I=z_I+\rho\nu_I
\tag{12}
\]
for every proper \(I\in\mathcal B\).

The laminar family \(\mathcal B\) is a rooted inclusion tree with root \([m]\). For a node \(I\), its children are the maximal proper members of \(\mathcal B\) contained in \(I\). Because all singletons are present, the children partition \(I\).

For each proper node define recursively
\[
M_I
=
\max\left\{
L_I,\ 
\sum_{J\text{ child of }I}M_J
\right\},
\tag{13}
\]
where for a singleton the child sum is \(0\).

Inductively, \(M_I\) is exactly the largest quantity
\[
\sum_{J\in\mathcal F_I}L_J
\tag{14}
\]
over all frontiers \(\mathcal F_I\) of the subtree on \(I\): either the frontier stops at \(I\), contributing \(L_I\), or it passes to all child subtrees.

Therefore
\[
\sum_{J\text{ child of }[m]}M_J
=
\max_{\mathcal F\text{ frontier}}
\sum_{I\in\mathcal F}
\left(z_I+\rho\nu_I\right).
\tag{15}
\]

Now choose \(\rho\) to be the right side of (5). Every frontier inequality (11) then says
\[
\sum_{I\in\mathcal F}
\left(z_I+\rho\nu_I\right)
\le z_{[m]},
\]
so (15) yields
\[
\sum_{J\text{ child of }[m]}M_J
\le z_{[m]}.
\tag{16}
\]

Assign total mass \(z_{[m]}\) to the root. Recursively distribute the mass assigned to any non-singleton node among its children so that each child \(J\) receives at least \(M_J\); this is possible by (13) and (16). At the leaves, the assigned singleton masses define a vector
\[
c=(c_1,\ldots,c_m).
\]
Every proper node \(I\) receives at least \(M_I\), hence at least \(L_I\). Thus
\[
c(I)\ge z_I+\rho\nu_I
\]
for all proper \(I\), while
\[
c([m])=z_{[m]}.
\]
By (10), the radius-\(\rho\) ball centered at \(c\) lies in \(P\). This proves the matching lower bound and establishes (5).

Finally, once \(r\) is fixed to the optimal value, condition (10) is both necessary and sufficient for a center to support a radius-\(r\) ball. This is precisely the system in (6), proving the complete incenter description.

## Verification
The proof is symbolic for every connected binary building set with positive weights.

The source-dependent ingredients were checked directly in the primary full text: binary building sets are laminar; binary nestohedra are positive Minkowski sums of simplices; the quantities \(z_I\) give the generalized-permutohedral inequality description; and fertilitopes are exactly integral binary nestohedra.

The accompanying `verify.py` checks many connected laminar building sets on
\[
2\le m\le6
\]
with two deterministic positive weight systems. It computes the frontier formula exactly up to floating evaluation, then independently solves the Chebyshev linear program by enumerating all candidate vertices of the normalized-facet system with a standalone Gaussian eliminator. Every tested case agrees. These finite checks are corroborative only.

## Relationship to prior work
Defant introduced fertilitopes to study fertility numbers and stack-sorting preimages, and proved that the nonempty fertilitopes are exactly the integral binary nestohedra. The same paper develops their face structure, vertices, lattice points, and Ehrhart-theoretic consequences.

The checked source gives exactly the laminar facet system needed here, but it does not state an Euclidean inradius, Chebyshev center, or largest-inscribed-ball theorem.

Formula (5) is stronger than merely writing the inradius as a generic linear program. Laminarity collapses the continuous optimization to a finite minimum over frontiers of the binary building-set tree, while (6) describes every optimal center.

Targeted searches under “fertilitope”, “binary nestohedron”, “inradius”, “Chebyshev center”, “largest inscribed ball”, and “laminar nestohedron” did not locate a theorem implying (5)--(6).

## Limitations
The theorem assumes a connected binary building set and the standard Euclidean realization.

It does not give a comparable frontier formula for arbitrary, nonlaminar nestohedra.

The result determines the inradius and complete incenter set, but not the minimum enclosing sphere, John ellipsoid, or other Euclidean extremal bodies.

A general theorem on Chebyshev centers of laminar generalized permutohedra or polymatroid base polytopes could subsume the calculation under different terminology. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Colin Defant, *Fertilitopes*, arXiv:2102.11836, first public version 2021-02-23; *Discrete & Computational Geometry* 70 (2023), 1340--1371, DOI 10.1007/s00454-023-00488-y.
