# Euler characteristic of projective type-A quiver loci ignores higher composite ranks
## Finding
Let
\[
V_0\longrightarrow V_1\longrightarrow\cdots\longrightarrow V_m
\]
be the equioriented type-\(A\) quiver over \(\mathbb C\), with
\[
d_i=\dim V_i.
\]
Put
\[
H
=
\bigoplus_{i=0}^{m-1}\operatorname{Hom}(V_i,V_{i+1}).
\]

Let
\[
r=(r_{ij})_{0\le i<j\le m}
\]
be an admissible rank array, meaning that it occurs as the exact composite-rank data of at least one representation with these dimension spaces. Let
\[
\Omega_r
=
\left\{
(\phi_0,\ldots,\phi_{m-1})\in H:
\operatorname{rank}(\phi_{j-1}\cdots\phi_i)\le r_{ij}
\text{ for every }i<j
\right\}.
\]
Because all defining minors are homogeneous, \(\Omega_r\) is an affine cone. Let
\[
\mathbb P\Omega_r\subset\mathbb P H
\]
be its projectivization.

Then
\[
\boxed{
\chi_{\mathrm{top}}(\mathbb P\Omega_r)
=
\sum_{i:r_{i,i+1}>0} d_i d_{i+1}.
}
\]

Thus the ordinary Euler characteristic depends only on which individual arrows are allowed to be nonzero. Every rank bound on a composite of two or more arrows is invisible to this invariant.

In particular, if
\[
r_{i,i+1}>0
\qquad
(0\le i<m),
\]
then
\[
\boxed{
\chi_{\mathrm{top}}(\mathbb P\Omega_r)
=
\sum_{i=0}^{m-1}d_i d_{i+1}
=
\chi_{\mathrm{top}}(\mathbb P H).
}
\]
Hence a proper and singular quiver locus can have exactly the same Euler characteristic as the whole ambient projective representation space.

If every direct-arrow bound is zero, then \(\Omega_r=\{0\}\), its projectivization is empty, and the displayed formula gives zero.

## Assumptions and scope
The base field is \(\mathbb C\).

The orientation is equioriented. The rank array is the standard type-\(A\) composite-rank datum: for each interval from vertex \(i\) to vertex \(j\), the corresponding bound is imposed on the composite map.

No expected-codimension, smoothness, normality, or Cohen--Macaulay assumption is needed for the Euler formula. Only the closed projective set underlying the homogeneous rank conditions is used.

## Proof
Let
\[
T
=
\prod_{i=0}^{m}(\mathbb C^*)^{d_i}
\]
be the diagonal torus in
\[
\prod_i\operatorname{GL}(V_i).
\]
It acts on \(H\) by change of basis at the vertices, and every composite-rank condition is invariant under this action.

Choose a one-parameter subgroup
\[
\lambda:\mathbb C^*\to T
\]
generically so that its weights on all matrix coordinates of all arrows are pairwise distinct. Such a choice exists because equality of two coordinate weights is one of finitely many proper integral hyperplane conditions on the cocharacter lattice.

Therefore the fixed locus of the ambient projective space \(\mathbb P H\) consists exactly of the coordinate points. A coordinate point is determined by an arrow
\[
i\longrightarrow i+1
\]
and a matrix unit
\[
E_{ab}\in\operatorname{Hom}(V_i,V_{i+1}).
\]
At this point, \(\phi_i=E_{ab}\) and every other arrow map is zero.

For this representation, the direct map on arrow \(i\) has rank one. Every composite involving at least two arrows is zero, because it contains at least one zero arrow. Hence the coordinate point lies in \(\Omega_r\) if and only if
\[
r_{i,i+1}\ge1.
\]

Consequently the fixed locus is the finite set
\[
(\mathbb P\Omega_r)^{\mathbb C^*}
=
\left\{
[E_{ab}^{(i)}]:
0\le i<m,
\ r_{i,i+1}>0,
\ 1\le a\le d_i,
\ 1\le b\le d_{i+1}
\right\},
\]
and therefore
\[
\#(\mathbb P\Omega_r)^{\mathbb C^*}
=
\sum_{i:r_{i,i+1}>0}d_i d_{i+1}.
\]

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One obtains this by removing the fixed locus and using a finite Rosenlicht stratification refined by stabilizer type; every nonfixed stratum has a locally trivial \(\mathbb C^*\)-orbit factor and hence compactly supported Euler characteristic zero.

Since \(\mathbb P\Omega_r\) is projective,
\[
\chi_{\mathrm{top}}(\mathbb P\Omega_r)
=
\chi_c(\mathbb P\Omega_r)
=
\#(\mathbb P\Omega_r)^{\mathbb C^*},
\]
which proves the formula.

## Verification
The bundled checker constructs equioriented type-\(A\) rank arrays from direct sums of interval representations.

For every subset of interval summands on quivers with at most five vertices, it computes every composite rank exactly. It then tests each arrow-coordinate representation against all rank inequalities, without using the closed Euler formula, and verifies that the surviving coordinate count is exactly
\[
\sum_{i:r_{i,i+1}>0}d_i d_{i+1}.
\]

The checker also verifies directly that all length-two-or-more composites vanish at every coordinate point.

These finite computations are regression evidence only. The all-dimension theorem follows from the symbolic fixed-point argument.

## Relationship to prior work
Buch's archival work treats the same equioriented type-\(A\) quiver loci defined by rank conditions on arbitrary composites and computes their Grothendieck classes. The paper lists primary MSC \(14M15\) and contains the standard admissibility conditions for rank arrays.

Kinser and Rajchgot place type-\(A\) quiver loci into Schubert geometry and review the long-standing results on their normality, Cohen--Macaulayness, rational singularities, and Zelevinsky maps.

The inspected full texts do not state the ordinary Euler characteristic of the projectivized quiver locus, nor the collapse to direct-arrow support. A recent paper on Chern--Schwartz--MacPherson classes of open equioriented quiver loci is adjacent and explicitly contains Euler information for open strata, but its inspected abstract does not state this projective closed-locus formula.

## Limitations
The theorem is intentionally coarse: quiver loci with identical sets of positive direct-arrow ranks have the same Euler characteristic even when their higher composite-rank data, dimensions, singularities, multidegrees, and Grothendieck classes differ substantially.

The proof is stated for equioriented type \(A\). Arbitrary orientations have a different interval-rank formalism, and no extension to them is asserted here.

The localization argument is short once the coordinate fixed points are isolated, so an older unindexed observation remains a residual novelty risk.

## References
Anders Skovsted Buch, *Grothendieck classes of quiver varieties*, arXiv:math/0104029, first submitted 2 April 2001; *Duke Mathematical Journal* 115 (2002), 75--103, DOI 10.1215/S0012-7094-02-11513-0.

Ryan Kinser and Jenna Rajchgot, *Type A quiver loci and Schubert varieties*, arXiv:1307.6261, first submitted 23 July 2013; *Journal of Commutative Algebra* 7 (2015), 265--301, DOI 10.1216/JCA-2015-7-2-265.

Moriah Elkin, *Three formulas for CSM classes of open quiver loci*, arXiv:2511.17723, first submitted 21 November 2025.
