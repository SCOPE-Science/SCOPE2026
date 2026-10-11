# Path symmetric edge polytopes have an exact inradius and a codimension-one incenter family
## Finding
Let
\[
n\ge2,
\]
let \(P_n\) be the path on vertex set \([n]\), and put
\[
\alpha_i=e_i-e_{i+1}
\qquad
(1\le i<n).
\]
Its symmetric edge polytope is
\[
\mathcal A_n
=
\operatorname{conv}\{\pm\alpha_i:1\le i<n\}
\subset
H_n,
\qquad
H_n=
\left\{
x\in\mathbb R^n:
\sum_{i=1}^n x_i=0
\right\}.
\tag{1}
\]
All distances below are intrinsic Euclidean distances in the affine span \(H_n\).

The exact inradius is
\[
\boxed{
r_{\mathrm{in}}(\mathcal A_n)
=
\sqrt{\frac{12}{n(n^2-1)}}.
}
\tag{2}
\]
The origin is an incenter. Its maximal inscribed ball is tangent to exactly two opposite facets.

The incenter is not unique once \(n\ge3\). In fact, the full set of incenter locations has affine dimension
\[
\boxed{n-2.}
\tag{3}
\]

There is also an exact facet-normal description. For each
\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_{n-1})
\in\{\pm1\}^{n-1},
\]
let \(x^\varepsilon\in H_n\) be the unique vector satisfying
\[
x_i^\varepsilon-x_{i+1}^\varepsilon=\varepsilon_i
\qquad
(1\le i<n).
\tag{4}
\]
Then the corresponding facet inequality is
\[
\langle x^\varepsilon,y\rangle\le1.
\tag{5}
\]
Moreover,
\[
\boxed{
\|x^\varepsilon\|^2
=
\frac1n
\sum_{1\le p<q\le n}
\left(
\sum_{k=p}^{q-1}\varepsilon_k
\right)^2.
}
\tag{6}
\]
If
\[
M_n=
\sqrt{\frac{n(n^2-1)}{12}},
\tag{7}
\]
then
\[
\|x^\varepsilon\|\le M_n,
\tag{8}
\]
with equality exactly for the two constant sign vectors.

Let \(x^+\) denote the normal for the all-positive sign vector. The complete incenter set is
\[
\boxed{
\mathcal I_n
=
\left\{
c\in H_n:
\langle x^+,c\rangle=0,\ 
\langle x^\varepsilon,c\rangle
\le
1-\frac{\|x^\varepsilon\|}{M_n}
\text{ for every nonconstant }\varepsilon
\right\}.
}
\tag{9}
\]
This set has nonempty relative interior in
\[
H_n\cap(x^+)^\perp.
\tag{10}
\]

At the opposite scale, the unique minimum enclosing Euclidean ball has center \(0\) and radius
\[
\boxed{
R_{\mathrm{out}}(\mathcal A_n)=\sqrt2.
}
\tag{11}
\]
All \(2(n-1)\) vertices lie on that sphere. Thus
\[
\boxed{
\frac{R_{\mathrm{out}}(\mathcal A_n)}
{r_{\mathrm{in}}(\mathcal A_n)}
=
\sqrt{\frac{n(n^2-1)}6}.
}
\tag{12}
\]

## Assumptions and scope
The symmetric edge polytope of a graph \(G=([n],E)\) is taken in the standard realization
\[
\operatorname{conv}
\{\pm(e_i-e_j):ij\in E\}.
\]
The primary source uses this realization and lists primary MSC \(52B20\).

For a path, the \(n-1\) edge vectors
\[
\alpha_1,\ldots,\alpha_{n-1}
\]
form a basis of \(H_n\). Hence \(\mathcal A_n\) is combinatorially a crosspolytope, but the basis is not orthogonal:
\[
\langle\alpha_i,\alpha_i\rangle=2,
\qquad
\langle\alpha_i,\alpha_{i+1}\rangle=-1.
\]
The theorem concerns the Euclidean shape of this canonical graph realization, not merely its crosspolytope combinatorics.

The same object also occurs as the fundamental polytope of the unit-edge path metric: normalized differences of nonadjacent path vertices are convex combinations of the edge differences in (1).

## Proof
Because the vectors
\[
\alpha_1,\ldots,\alpha_{n-1}
\]
are linearly independent, every facet of the crosspolytope (1) chooses exactly one vertex from each opposite pair. Thus facets are indexed by
\[
\varepsilon\in\{\pm1\}^{n-1}.
\]
For each sign vector there is a unique
\[
x^\varepsilon\in H_n
\]
such that
\[
\langle x^\varepsilon,\alpha_i\rangle
=
x_i^\varepsilon-x_{i+1}^\varepsilon
=
\varepsilon_i.
\]
The facet containing the vertices
\[
\varepsilon_i\alpha_i
\qquad
(1\le i<n)
\]
therefore has supporting equation
\[
\langle x^\varepsilon,y\rangle=1,
\]
which proves (5).

For every zero-sum vector \(x\in H_n\), the variance identity gives
\[
\|x\|^2
=
\frac1n
\sum_{1\le p<q\le n}
(x_p-x_q)^2.
\tag{13}
\]
Applying this to \(x^\varepsilon\) and telescoping (4) yields (6).

For \(p<q\),
\[
\left|
\sum_{k=p}^{q-1}\varepsilon_k
\right|
\le q-p.
\tag{14}
\]
Therefore
\[
\|x^\varepsilon\|^2
\le
\frac1n
\sum_{1\le p<q\le n}(q-p)^2
=
\frac1n
\sum_{d=1}^{n-1}(n-d)d^2.
\tag{15}
\]
The finite sum evaluates to
\[
\frac1n
\sum_{d=1}^{n-1}(n-d)d^2
=
\frac{n(n^2-1)}{12}.
\tag{16}
\]
For \(n\ge3\), equality in (14) for every interval of length \(2\) forces adjacent signs to agree, so all signs are equal. The case \(n=2\) is immediate. Hence exactly two facet normals have norm \(M_n\).

The distance from the origin to the facet (5) is
\[
\frac1{\|x^\varepsilon\|}.
\]
Consequently the centered largest ball has radius
\[
\frac1{M_n}
=
\sqrt{\frac{12}{n(n^2-1)}}.
\tag{17}
\]

This is also the global inradius, not merely the largest radius at the origin. Let a ball of radius \(\rho\), centered at \(c\in H_n\), lie in \(\mathcal A_n\). The two constant-sign facets have normals \(x^+\) and \(-x^+\), both of norm \(M_n\). Their two clearance inequalities give
\[
\rho
\le
\frac{1-|\langle x^+,c\rangle|}{M_n}
\le
\frac1{M_n}.
\tag{18}
\]
Thus no translated ball is larger than (17).

Equality in (18) forces
\[
\langle x^+,c\rangle=0.
\tag{19}
\]
For a nonconstant sign vector \(\varepsilon\), a radius-\(1/M_n\) ball centered at \(c\) stays behind facet (5) exactly when
\[
\langle x^\varepsilon,c\rangle
+
\frac{\|x^\varepsilon\|}{M_n}
\le1.
\tag{20}
\]
Equations (19)--(20) give precisely (9).

At \(c=0\), every inequality (20) is strict because
\[
\|x^\varepsilon\|<M_n
\]
for every nonconstant sign vector. There are finitely many such inequalities, so a relative neighborhood of \(0\) inside (10) still satisfies all of them. Therefore \(\mathcal I_n\) has affine hull (10), whose dimension is \(n-2\). This proves (3).

Finally,
\[
\|\pm\alpha_i\|=\sqrt2
\]
for every vertex, so the ball centered at \(0\) of radius \(\sqrt2\) contains all vertices.

For any competing center \(c\in\mathbb R^n\) and any \(i\),
\[
\frac{
\|\alpha_i-c\|^2+
\|-\alpha_i-c\|^2
}{2}
=
2+\|c\|^2.
\tag{21}
\]
Hence at least one member of every opposite pair has squared distance at least
\[
2+\|c\|^2.
\]
Every enclosing ball therefore has radius at least \(\sqrt2\), with equality only when \(c=0\). This proves (11), uniqueness, and the all-vertex contact statement. Combining (2) and (11) gives (12).

## Verification
The proof is symbolic for every \(n\ge2\).

The primary full text was inspected at the definition of symmetric edge polytopes, the path-graph preliminaries, and the sections on facets and regular unimodular triangulations. Targeted full-text searches found no inradius, circumradius, or Euclidean-ball theorem.

The tree-metric fundamental-polytope literature was also inspected because the unit path metric yields the same convex body. That source defines the fundamental and Lipschitz polytopes, identifies their polarity, places full trees inside the symmetric-edge-polytope framework, and concentrates on face numbers and simpliciality. Targeted full-text searches found no inradius, circumradius, or Euclidean treatment.

The accompanying `verify.py` exhaustively enumerates all facet sign vectors for
\[
2\le n\le11.
\]
It reconstructs every normal from (4), checks the variance identity, verifies the sharp norm maximum and its two equality cases, checks the closed inradius and circumradius formulas, and confirms the codimension-one affine constraint for incenter locations. The finite replay is corroborative only.

## Relationship to prior work
D'Alì, Juhnke-Kubitzke, Köhne, and Venturello study symmetric edge polytopes through their \(h^*\)- and \(\gamma\)-vectors, graph structure, facets, and regular unimodular triangulations. Their paper explicitly includes path graphs in its graph-theoretic preliminaries but does not give the Euclidean ball profile above.

Delucchi and Hoessly study fundamental polytopes of tree metrics. Their work makes the metric-space connection especially relevant to paths, but its main invariants are face numbers, matroidal structure, and simpliciality rather than Euclidean radii or incenter loci.

The new point is not that the path polytope is abstractly a crosspolytope. Its canonical simple-root embedding has a highly anisotropic dual facet geometry. The longest facet normals are exactly the two monotone sign choices, and the gap to all other normals leaves an entire codimension-one family of optimal inscribed-ball centers.

At the same time, every primal vertex has the common norm \(\sqrt2\). Thus the outer radius stays fixed while the inradius decays on the order of \(n^{-3/2}\), producing the exact distortion ratio (12).

## Limitations
The theorem concerns unweighted path graphs in the standard symmetric-edge realization.

For weighted path metrics, the corresponding normalized edge generators have unequal lengths and the facet-normal optimization changes. For general trees, sign choices interact with branching and the two-facet extremal mechanism need not persist.

The incenter set is described exactly by the finite system (9), but no closed vertex enumeration of that incenter polytope is claimed.

Because a path symmetric edge polytope is a linear image of a standard crosspolytope, the calculation becomes elementary after the correct dual normals are written down. An equivalent observation could therefore exist under root-system, Lipschitz-free, or finite-metric terminology not surfaced by the targeted searches.

## References
1. Alessio D'Alì, Martina Juhnke-Kubitzke, Daniel Köhne, and Lorenzo Venturello, *On the gamma-vector of symmetric edge polytopes*, arXiv:2201.09835, first public version 2022-01-24; *SIAM Journal on Discrete Mathematics* 37 (2023), 487--515, DOI 10.1137/22M1492799.
2. Emanuele Delucchi and Linard Hoessly, *Fundamental polytopes of metric trees via parallel connections of matroids*, arXiv:1612.05534; *European Journal of Combinatorics* 87 (2020), 103098.
