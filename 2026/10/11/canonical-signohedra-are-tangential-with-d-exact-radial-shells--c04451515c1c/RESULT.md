# Canonical signohedra are tangential with \(d\) exact radial shells
## Finding
Let
\[
d\ge2,
\qquad
C_d=[-1,1]^d,
\qquad
\Diamond_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}.
\]
Define
\[
Q_d=C_d+\Diamond_d,
\qquad
\Sigma_d=Q_d^\circ.
\tag{1}
\]
Black and De Loera prove that \(\Sigma_d\) is a canonical representative of the signohedron: it is combinatorially equivalent to the monotone path polytope of a generically oriented \((d+1)\)-dimensional cross-polytope.

The polar partner \(Q_d\) has a complete Euclidean shell decomposition. Its vertices are the signed coordinate permutations of
\[
(2,1,\ldots,1),
\tag{2}
\]
so every vertex has norm
\[
\boxed{R_{\min}(Q_d)=\sqrt{d+3}}.
\tag{3}
\]
Its facets are indexed by nonzero sign vectors \(s\in\{-1,0,1\}^d\). If
\[
k=|\operatorname{supp}(s)|,
\]
then the facet inequality is
\[
\langle s,x\rangle\le k+1,
\tag{4}
\]
and its distance from the origin is
\[
\boxed{\delta_k(Q_d)=\frac{k+1}{\sqrt{k}}}.
\tag{5}
\]
Thus there are exactly \(d\) strict facet-distance shells, with multiplicity
\[
\boxed{\binom dk2^k}
\tag{6}
\]
in shell \(k\). In particular,
\[
\boxed{r_{\mathrm{in}}(Q_d)=2}.
\tag{7}
\]
Both the incenter and the minimum-enclosing center are uniquely the origin.

The canonical signohedron \(\Sigma_d\) has the reciprocal structure. Since every vertex in (2) has norm \(\sqrt{d+3}\), every facet of \(\Sigma_d\) is tangent to the same origin-centered sphere. Hence
\[
\boxed{r_{\mathrm{in}}(\Sigma_d)=\frac1{\sqrt{d+3}}}.
\tag{8}
\]
There are exactly
\[
\boxed{d2^d}
\tag{9}
\]
tangent facets.

The source gives one vertex of \(\Sigma_d\) for each nonzero sign vector. In the notation above,
\[
\boxed{v_s=\frac{s}{k+1}}.
\tag{10}
\]
Consequently
\[
\|v_s\|=\frac{\sqrt{k}}{k+1}.
\tag{11}
\]
These values strictly decrease with \(k\), so \(\Sigma_d\) has exactly \(d\) strict vertex-radial shells, with the same multiplicities (6). Its outer shell is \(k=1\), giving
\[
\boxed{R_{\min}(\Sigma_d)=\frac12}.
\tag{12}
\]
The contact vertices are exactly
\[
\boxed{\left\{\pm\frac{e_i}{2}:1\le i\le d\right\}}.
\tag{13}
\]
Again, both extremal Euclidean centers are uniquely the origin.

The two polar partners therefore satisfy
\[
\boxed{
r_{\mathrm{in}}(\Sigma_d)R_{\min}(Q_d)=1,
\qquad
R_{\min}(\Sigma_d)r_{\mathrm{in}}(Q_d)=1,
}
\tag{14}
\]
and have the common Euclidean radius ratio
\[
\boxed{\frac{R}{r}=\frac{\sqrt{d+3}}2}.
\tag{15}
\]

## Assumptions and scope
The metric is the standard Euclidean metric in the source realization (1). The theorem concerns the canonical representative \((C_d+\Diamond_d)^\circ\), not every affine realization of the signohedron combinatorial type.

The source uses \(n=d+1\) for the dimension of the cross-polytope whose generic monotone path polytope has signohedron dimension \(d\). The restriction \(d\ge2\) corresponds to cross-polytope dimension at least three; the one-dimensional endpoint is elementary and omitted.

Polarity is taken with respect to the origin and the standard inner product. Both \(C_d\) and \(\Diamond_d\) contain the origin in their interiors, so the polar in (1) is well defined and full dimensional.

## Proof
The source proves that
\[
Q_d=C_d+\Diamond_d
\]
has vertices obtained by signed coordinate permutations of
\[
2e_1+e_2+\cdots+e_d.
\]
Therefore every vertex \(q\) satisfies
\[
\|q\|^2=4+(d-1)=d+3.
\tag{16}
\]
Because \(Q_d\) is centrally symmetric, the origin-centered sphere of radius \(\sqrt{d+3}\) contains all of \(Q_d\). If a translated ball of the same radius were centered at \(c\ne0\), then for any antipodal vertex pair \(q,-q\),
\[
\frac{\|q-c\|^2+\|-q-c\|^2}{2}
=
(d+3)+\|c\|^2
>
d+3.
\]
At least one of the two vertices would lie outside. This proves (3) and uniqueness of the minimum-enclosing center.

The source also proves that every nonzero sign vector \(s\in\{-1,0,1\}^d\) defines a facet of \(Q_d\), with inequality (4). If its support has size \(k\), then
\[
\|s\|=\sqrt{k},
\]
so its origin distance is exactly (5). The squared shell distance is
\[
\delta_k(Q_d)^2
=
\frac{(k+1)^2}{k}
=
k+2+\frac1k.
\]
Hence
\[
\delta_{k+1}(Q_d)^2-\delta_k(Q_d)^2
=
1-\frac1{k(k+1)}>0,
\]
so the shells are strict. The number of sign vectors of support \(k\) is \(\binom dk2^k\), proving (6). The minimum occurs at \(k=1\), proving (7). At radius \(2\), the \(2d\) support-one facets are
\[
\pm x_i\le2.
\]
Any radius-two incenter \(c\) must satisfy simultaneously \(2-c_i\ge2\) and \(2+c_i\ge2\) for every \(i\), so \(c=0\). Thus the incenter is unique.

Now polarize. A vertex \(q\) of \(Q_d\) defines a facet
\[
\langle q,x\rangle\le1
\]
of \(\Sigma_d\). By (16), every such facet has origin distance
\[
\frac1{\sqrt{d+3}},
\]
so the origin supports an insphere tangent to all \(d2^d\) facets. No larger ball is possible because every pair of opposite facets has separation \(2/\sqrt{d+3}\). At the optimal radius, a center \(c\) must satisfy
\[
\langle q,c\rangle=0
\]
for every vertex \(q\) of \(Q_d\). These vertices span \(\mathbb R^d\), so \(c=0\). This proves (8)--(9) and uniqueness.

The source's explicit vertex formula for the polar representative is (10). Its norm is (11). To order the shells, write
\[
f(k)=\frac{k}{(k+1)^2}.
\]
Then
\[
f(k)-f(k+1)
=
\frac{k^2+k-1}{(k+1)^2(k+2)^2}>0
\]
for every \(k\ge1\). Hence the outer shell is exactly \(k=1\), giving (12)--(13). If a ball of radius \(1/2\) centered at \(c\) contains both \(e_i/2\) and \(-e_i/2\), then
\[
\frac{\|e_i/2-c\|^2+\|-e_i/2-c\|^2}{2}
=
\frac14+\|c\|^2.
\]
Containment forces the left side to be at most \(1/4\), hence \(c=0\). The minimum-enclosing center is unique.

Equations (14)--(15) now follow from (3), (7), (8), and (12).

## Verification
The proof is symbolic for every \(d\ge2\).

The source-dependent facts were checked directly in the open-access full text: the signohedron terminology; the combinatorial equivalence of generic cross-polytope monotone path polytopes with \((C_d+\Diamond_d)^\circ\); the signed-permutation vertex description of \(C_d+\Diamond_d\); the complete sign-vector facet system of that Minkowski sum; and the explicit sign-vector vertex coordinates of the polar representative.

The accompanying `verify.py` independently enumerates all source vertices and facets for \(2\le d\le7\). It checks the source inequalities and facet affine ranks, verifies every shell formula and multiplicity, checks the reciprocal polar incidence, and solves the complete Chebyshev linear programs for both polar partners. The finite computation is corroborative only.

## Relationship to prior work
Black and De Loera introduce the name signohedron for the generic cross-polytope monotone-path combinatorial type and give the canonical representative (1). Their main results concern coherent monotone paths, face lattices, explicit vertices and facets, \(f\)-vectors, the one-skeleton, and flip distances. The inspected full text contains no occurrence of “inradius”, “circumradius”, “sphere”, or “Euclidean”.

The paper itself supplies all combinatorial and coordinate data needed here but does not normalize the facets or vertices metrically. The Euclidean conclusion is particularly rigid: the canonical signohedron is tangential despite having \(d2^d\) facets, while its vertices occupy exactly \(d\) strict shells.

A previously published result on coherent-path flip distance concerns graph distance in the one-skeleton and does not imply Euclidean norm or supporting-hyperplane distances. Likewise, results on cube--cross-polytope intersections concern a different polytope operation from the Minkowski sum and its polar.

Targeted searches under “signohedron”, “cross-polytope monotone path polytope”, “cube plus cross-polytope polar”, “inradius”, “circumradius”, “tangential”, and “Euclidean radius” did not locate a theorem implying (3)--(15).

## Limitations
The formulas are realization-sensitive. Generic cross-polytope monotone path polytopes are affinely equivalent in the source sense, but a general affine realization need not preserve the Euclidean radii in this theorem.

The theorem does not determine John or Löwner ellipsoids, Euclidean edge lengths, or radii of the source's orientation-dependent explicit monotone-path coordinates.

The radius identities themselves become short once the canonical polar pair is recognized. The substantive family-wide content is the simultaneous all-facet tangentiality, the complete strict shell spectra with multiplicities, and uniqueness of all four Euclidean extremal centers.

## References
1. Alexander E. Black and Jesús A. De Loera, *Monotone Paths on Cross-Polytopes*, arXiv:2102.01237, first public version 2021-02-02; *Discrete & Computational Geometry* 70 (2023), 1245--1265, DOI 10.1007/s00454-023-00563-4.
