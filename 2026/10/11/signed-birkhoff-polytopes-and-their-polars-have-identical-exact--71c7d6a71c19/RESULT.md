# Signed Birkhoff polytopes and their polars have identical exact Euclidean radii
## Finding
Let
\[
n\ge1.
\]
Let
\[
\mathcal{BB}(n)
=
\operatorname{conv}\{M_\sigma:\sigma\in B_n\}
\subset
\mathbb R^{n\times n}
\tag{1}
\]
be the signed, or type-\(B\), Birkhoff polytope, with the Frobenius inner product
\[
\langle X,Y\rangle=\operatorname{tr}(X^{\mathsf T}Y).
\]
Let
\[
\mathcal C(n)=\mathcal{BB}(n)^\circ
\tag{2}
\]
be its polar.

Then both polytopes have the origin as their unique Euclidean incenter and unique minimum-enclosing-sphere center, and both have the same two radii:
\[
\boxed{
r_{\mathrm{in}}(\mathcal{BB}(n))
=
r_{\mathrm{in}}(\mathcal C(n))
=
\frac1{\sqrt n},
}
\tag{3}
\]
\[
\boxed{
R(\mathcal{BB}(n))
=
R(\mathcal C(n))
=
\sqrt n.
}
\tag{4}
\]

Every vertex of each polytope lies on its minimum enclosing sphere. Every facet of each polytope is tangent to its insphere. Hence the Euclidean radius ratio of both members of the polar pair is
\[
\boxed{
\frac{R}{r}=n.
}
\tag{5}
\]

For \(\mathcal{BB}(n)\), the outer contacts are exactly its \(2^n n!\) signed permutation matrices. Its facets are
\[
\langle X,\varepsilon\otimes e_i\rangle\le1,
\qquad
\langle X,e_i\otimes\varepsilon\rangle\le1,
\tag{6}
\]
where
\[
i\in[n],
\qquad
\varepsilon\in\{\pm1\}^n.
\]
All normals in (6) have Frobenius norm \(\sqrt n\).

For \(\mathcal C(n)\), the source facet normals in (6) become vertices under polarity, and the signed permutation matrices become facet normals. Thus the same two Euclidean radii recur on the dual side.

## Assumptions and scope
The realization is the standard matrix-coordinate realization used in the source, with the Frobenius metric on
\[
\mathbb R^{n\times n}.
\]

The polar is taken with respect to the origin and this inner product:
\[
P^\circ
=
\{Y:\langle X,Y\rangle\le1\text{ for all }X\in P\}.
\]

The source proves that \(\mathcal{BB}(n)\) is full-dimensional, unconditional, and reflexive, so the origin is in its interior and the polar in (2) is a full-dimensional polytope.

The statement includes \(n=1\), where both polytopes are simply the interval \([-1,1]\).

## Proof
The source proves that the vertices of \(\mathcal{BB}(n)\) are exactly the signed permutation matrices
\[
M_\sigma.
\tag{7}
\]
Each such matrix has exactly one nonzero entry, equal to \(\pm1\), in every row and every column. Therefore
\[
\|M_\sigma\|_{\mathrm F}^2=n.
\tag{8}
\]
The set of signed permutation matrices is centrally symmetric: if \(M_\sigma\) occurs, so does \(-M_\sigma\).

It follows that the origin-centered sphere of radius \(\sqrt n\) contains every vertex and hence the whole polytope. Conversely, any ball containing an antipodal pair
\[
M_\sigma,\ -M_\sigma
\]
must have radius at least half their mutual distance,
\[
\frac12\|M_\sigma-(-M_\sigma)\|_{\mathrm F}
=
\sqrt n.
\]
Equality for that pair forces the center to be its midpoint, namely the origin. Hence
\[
R(\mathcal{BB}(n))=\sqrt n
\]
and the minimum enclosing sphere has unique center \(0\).

The source gives the complete irredundant facet description
\[
\langle X,\varepsilon\otimes e_i\rangle\le1,
\qquad
\langle X,e_i\otimes\varepsilon\rangle\le1
\tag{9}
\]
for all
\[
i\in[n],
\qquad
\varepsilon\in\{\pm1\}^n.
\]
Each normal has exactly \(n\) entries equal to \(\pm1\), so
\[
\|\varepsilon\otimes e_i\|_{\mathrm F}
=
\|e_i\otimes\varepsilon\|_{\mathrm F}
=
\sqrt n.
\tag{10}
\]
Thus the distance from the origin to every facet is
\[
\frac1{\sqrt n}.
\tag{11}
\]
The origin-centered ball of that radius is therefore contained in \(\mathcal{BB}(n)\) and tangent to every facet.

No larger ball can fit. Indeed, for every normal \(A\) in (9), the opposite normal \(-A\) also occurs. These two parallel facets form the slab
\[
-1\le\langle A,X\rangle\le1,
\]
whose width is
\[
\frac2{\|A\|_{\mathrm F}}=\frac2{\sqrt n}.
\]
Any Euclidean ball inside this slab has radius at most \(1/\sqrt n\).

If a ball of radius \(1/\sqrt n\) centered at \(Y\) lies in \(\mathcal{BB}(n)\), then the two inequalities for \(A\) and \(-A\) force
\[
\langle A,Y\rangle=0.
\tag{12}
\]
For each fixed column \(i\), the matrices
\[
\varepsilon\otimes e_i,
\qquad
\varepsilon\in\{\pm1\}^n,
\]
span the full \(i\)-th column coordinate subspace. Varying \(i\) spans all of \(\mathbb R^{n\times n}\). Equation (12) therefore gives
\[
Y=0.
\]
This proves the first equality in (3) and uniqueness of the incenter.

Now use polarity. Since the inequalities in (9) are facet-defining, their normals are exactly the vertices of
\[
\mathcal C(n)=\mathcal{BB}(n)^\circ.
\tag{13}
\]
By (10), every vertex of \(\mathcal C(n)\) has norm \(\sqrt n\), and the vertex set is centrally symmetric. The same antipodal-pair argument gives
\[
R(\mathcal C(n))=\sqrt n
\]
with unique center \(0\).

Likewise, vertices of \(\mathcal{BB}(n)\) correspond to facets of \(\mathcal C(n)\). Thus the complete facet family of \(\mathcal C(n)\) is
\[
\langle M_\sigma,Y\rangle\le1
\qquad
(\sigma\in B_n).
\tag{14}
\]
Every normal has norm \(\sqrt n\) by (8), so every facet is at distance \(1/\sqrt n\) from the origin.

The origin-centered radius-\(1/\sqrt n\) ball is therefore tangent to all facets of \(\mathcal C(n)\). For uniqueness, suppose equality is attained by a center \(Z\). Applying each facet together with its opposite forces
\[
\langle M_\sigma,Z\rangle=0
\qquad
\text{for every }\sigma.
\tag{15}
\]
Signed permutation matrices span \(\mathbb R^{n\times n}\). To see this directly, fix a coordinate \((i,j)\), choose a permutation \(\pi\) with
\[
\pi(i)=j,
\]
and average the signed permutation matrices having underlying permutation \(\pi\), weighting each matrix by the sign in row \(i\). All rows except \(i\) cancel and the result is a nonzero multiple of
\[
E_{ij}.
\]
Hence (15) implies
\[
Z=0.
\]
This proves the second equality in (3), and (5) follows.

## Verification
The proof is exact for every \(n\ge1\).

The source-dependent ingredients were checked in the full primary source: the signed-permutation vertex description, full dimensionality, the complete facet system (9), and the definition of \(\mathcal C(n)\) as the polar. A later same-object full paper was also inspected: it restates the signed permutation vertices and the signed row/column halfspace description and studies faces, graph diameter, Hamiltonian connectivity, and toric ideals rather than Euclidean in- or circumradii.

The accompanying `verify.py` enumerates all signed permutation matrices for
\[
1\le n\le5.
\]
For each \(n\), it checks the exact vertex norms, the row/column facet-normal norms, validity of every source facet on every vertex, central symmetry, full span of both normal families, and the corresponding polar contact identities. The finite enumeration is corroborative only.

## Relationship to prior work
Kohl and Olsen's first public preprint on type-\(B\) Birkhoff polytopes already states that the signed Birkhoff polytope and its dual are reflexive and possess regular unimodular triangulations. The replacement paper with Sanyal gives the precise vertex and facet descriptions, the unconditional-reflexive interpretation, the dual \(\mathcal C(n)\), volume and \(h^*\)-data, and Gale-dual structure.

The replacement paper remarks that all signed-permutation defining points lie on a sphere, but it does not identify the minimum enclosing sphere, the exact inradius, uniqueness of either center, or the matching radius profile of the polar. Its facet theorem is the critical extra input for the inradius calculation.

Chen and Zhu later give a detailed full-text study of faces and facets of the signed Birkhoff polytope, together with graph diameter, Hamiltonian connectivity, and Gröbner-basis results. Their full text contains no occurrence of “inradius”, “circumradius”, or “sphere” in the metric sense relevant here.

The result is also distinct from the ordinary Birkhoff polytope. The ordinary Birkhoff polytope lies in a lower-dimensional affine space and has a different intrinsic Euclidean inradius. The signed Birkhoff polytope is full-dimensional in \(\mathbb R^{n^2}\).

Targeted published-result searches under “signed Birkhoff polytope”, “type-B Birkhoff polytope”, “insphere”, “circumsphere”, “minimum enclosing sphere”, “Chebyshev center”, “Frobenius radius”, and the dual notation \(\mathcal C(n)\) did not locate a theorem implying (3)--(5).

## Limitations
The theorem concerns only the standard Frobenius realization.

It does not determine John or Löwner ellipsoids, mean width, intrinsic volumes, or Euclidean radii after arbitrary non-orthogonal unimodular transformations.

The circumradius of \(\mathcal{BB}(n)\) is immediate once the signed-permutation vertices are recognized as one Euclidean shell. The substantive combined statement also uses the complete facet theorem, proves uniqueness of both centers, transfers the metric structure to the polar, and shows that every vertex and every facet is a contact.

A residual originality risk remains for a general centrally symmetric polar-pair theorem applied to an equinorm vertex/equifacet-normal configuration. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Florian Kohl and McCabe Olsen, *Birkhoff polytopes of different type and the orthant-lattice property*, arXiv:1903.12634, first public version 2019-03-29; withdrawn after replacement by the next reference.
2. Florian Kohl, McCabe Olsen, and Raman Sanyal, *Unconditional Reflexive Polytopes*, arXiv:1906.01469, first public version 2019-06-03; Discrete & Computational Geometry 64 (2020), 427--452, DOI 10.1007/s00454-020-00199-8.
3. Zhi Chen and Kebin Zhu, *Faces of the signed Birkhoff polytopes*, Electronic Journal of Linear Algebra 40 (2024), 747--765, DOI 10.13001/ela.2024.8153.
