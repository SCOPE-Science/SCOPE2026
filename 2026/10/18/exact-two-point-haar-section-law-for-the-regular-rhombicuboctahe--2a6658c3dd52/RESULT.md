# Exact two-point Haar section law for the regular rhombicuboctahedron

## Finding

Let \(r=1+\sqrt2\). The **regular (small) rhombicuboctahedron** in \(\mathbb R^3\) is
\[
P=\operatorname{conv}\{\text{all signed permutations of }(r,1,1)\}.
\]
It has 24 vertices, 48 edges, eight triangular facets and eighteen square facets. Let \(U\) be Haar-uniform on \(\mathbb S^2\), and let \(N(U)\) be the number of vertices of the central section \(P\cap U^\perp\). Put
\[
\theta=\arccos\left(\frac{r^2}{r^2+2}\right)
=\arccos\left(\frac{7+4\sqrt2}{17}\right).
\]
The complete distribution is
\[
\boxed{\Pr(N=8)=3-\frac{12\theta}{\pi},\qquad
\Pr(N=12)=\frac{12\theta}{\pi}-2.}
\]
Numerically these probabilities are approximately \(0.207863937034155\) and \(0.792136062965845\), respectively. There are no generic central decagonal, hexagonal, or other polygonal sections.

More precisely, rearrange \((|u_1|,|u_2|,|u_3|)\) in nonincreasing order as \(a\ge b\ge c\ge0\). For every generic section normal,
\[
\boxed{N(u)=8\quad\Longleftrightarrow\quad a>(1+\sqrt2)b+c.}
\]
If this strict inequality fails and the normal is generic, then \(N(u)=12\).

## Assumptions and scope

The polyhedron is Euclidean and regular with the above fixed coordinate normalization. A normal is generic if it is not orthogonal to any of the 24 original vertices and does not lie on the finitely many algebraic comparison boundaries used below. These exceptions are contained in a finite union of great circles and have Haar probability zero. The plane always passes through the center. Since the normal signs are irrelevant, an unoriented random plane gives the same distribution as a uniform oriented normal. These probabilities do not automatically remain invariant under arbitrary affine deformation, because affine transformations change the angular distribution of the corresponding normals.

## Proof

**1. Edges and section crossings.** Every vertex has squared norm \(r^2+2\). A direct comparison of pairs of signed-permutation vertices shows that the minimum nonzero squared intervertex distance is \(4\), and precisely 48 unordered pairs achieve it. These are the edges: each vertex has four such neighbours and they bound its three square facets and one triangular facet. For instance, the four edge-neighbours of \((r,1,1)\) are \((r,-1,1)\), \((r,1,-1)\), \((1,r,1)\), \((1,1,r)\); signed permutations give every remaining edge. A generic central plane intersects a polytope edge in its relative interior precisely when its two endpoints have opposite normal signs. Every vertex of the section is one such crossing, counted once, since the section avoids original vertices. Therefore
\[
N(u)=\#\{\{v,w\}\in E(P):\langle u,v\rangle\langle u,w\rangle<0\}.
\]

**2. Exhaustive signed fundamental-chamber analysis.** Signed coordinate permutations preserve \(P\). It suffices to consider unit normals with \(a>b>c>0\), representing \((|u_1|,|u_2|,|u_3|)\). Put
\[
A=a-rb-c,\quad B=a-rb+c,\quad C=a-b-rc,\quad H=a+b-rc.
\]
All 24 vertex signs are determined by the signs of these four expressions: in the vertices with long coordinate \(ra\), the \(ra\) term dominates the other two because \(r>2\); in vertices with long coordinate \(rb\) the only variable expressions, up to overall sign, are \(A,B\); and for long coordinate \(rc\) they are \(C,H\). The other signed combinations retain a fixed sign on \(a>b>c>0\).

There are four exact inequalities throughout this sector:
\[
A<B,\qquad A<C,\qquad B<H,\qquad C<H.
\]
For example, \(C-A=(r-1)(b-c)>0\), and \(H-B=(r+1)(b-c)>0\). These partial-order relations imply that **exactly six** patterns of the signs of \((A,B,C,H)\) are logically possible. Every pattern below is realized by the displayed rational witness, where the triple is proportional to \((a,b,c)\). The final column is obtained by the 48-edge sign-crossing formula from Step 1:

| Signs of \((A,B,C,H)\) | Representative \((a,b,c)\) | Crossing edges / section vertices |
|---|---|---:|
| \((+,+,+,+)\) | \((100,20,10)\) | 8 |
| \((-,+,+,+)\) | \((100,40,15)\) | 12 |
| \((-,+,-,+)\) | \((100,40,25)\) | 12 |
| \((-,-,+,+)\) | \((100,60,10)\) | 12 |
| \((-,-,-,+)\) | \((100,60,30)\) | 12 |
| \((-,-,-,-)\) | \((100,90,85)\) | 12 |

This is exhaustive for a continuum of normals, not a finite sampling argument: the sign reduction proves the crossing count is constant on each of the six chambers. The first pattern occurs exactly when \(A>0\) (because \(A<B,C<H\)), proving the stated orientation criterion and support \(\{8,12\}\).

**3. Exact Haar probabilities.** Every edge has endpoint squared distance \(4\), so the angle between its endpoints, each of norm \(\sqrt{r^2+2}\), equals \(\theta\) defined above. For any two nonantipodal radial vectors separated by angle \(\theta\), a uniform plane normal separates their signs with probability \(\theta/\pi\). This follows by projecting the normal onto their span, where its azimuth is uniform. The 48 edge indicators therefore give, by linearity of expectation,
\[
\mathbb E N(U)=\frac{48\theta}{\pi}.
\]
Write \(p=\Pr(N=8)\). By the exhaustive two-point support classification, \(8p+12(1-p)=48\theta/\pi\). Hence \(p=3-12\theta/\pi\) and its complement gives the second probability. Finally
\[
\frac{r^2}{r^2+2}=\frac{3+2\sqrt2}{5+2\sqrt2}=\frac{7+4\sqrt2}{17},
\]
completing the exact evaluation.

**4. Independent spherical-cone identity.** In the positive octant, the octagon normals form three disjoint congruent pieces specified by one coordinate exceeding \(r\) times the second largest coordinate plus the smallest. One such piece consists of two congruent spherical triangles with generating rays \((1,0,0)\), \((r,1,0)\), and \((r+1,1,1)\). If
\[
D_*=\sqrt{r^2+1}\sqrt{(r+1)^2+2}+r\sqrt{(r+1)^2+2}
+(r+1)\sqrt{r^2+1}+r(r+1)+1,
\]
then the classical trihedral solid-angle formula gives the alternative exact expression
\[
\Pr(N=8)=\frac{24}{\pi}\arctan\left(\frac1{D_*}\right).
\]
This agrees with the edge-crossing law above; the exact first formula follows from Steps 1–3 independently of any spherical-cone integration.

## Verification

The standalone Python checker `verify_rhombicuboctahedron.py` uses only the standard library and exact arithmetic in \(\mathbb Z[\sqrt2]\). It enumerates all 24 vertices, verifies the minimum squared intervertex distance and all 48 edges, checks the common edge endpoint dot product, evaluates the six sign-table entries for exact integer witnesses, and compares the edge-angle and spherical-angle probability formulas numerically. Execute `python3 verify_rhombicuboctahedron.py`; successful output begins `EXACT_SIGN_CHAMBERS_OK`.

The exact algebraic finite verification supports the exhaustive reduction, while the proof that the six sign patterns cover all generic normals and the rotational-invariance expectation argument establish the infinite-direction theorem. Numerical decimal values do not constitute an infinite proof.

## Relationship to prior work

De Loera, Lopez-Campos and Torres (arXiv:2412.12419, first publicly posted December 17, 2024) study possible numbers of vertices in polytope sections, extreme vertex counts and gaps. Their inspected work does not evaluate the Haar distribution of central sections of the regular rhombicuboctahedron. Thom (arXiv:2511.12773, first posted November 16, 2025) studies discrete dodecahedral vertex-plane statistics and nonuniqueness of unoriented section distributions; this is a different model and does not imply the above law.

Existing exact Haar section laws for cubes, octahedra, icosahedra, and truncated octahedra use related edge-crossing or normal-chamber methods, but none of the inspected statements covers the 24-vertex rhombicuboctahedron or the six-pattern incidence reduction here. The standard vertices, edges and facet counts of the Archimedean solid are established background, not a novelty claim. The proposed contribution is the **complete two-atom Haar law and explicit direction criterion** for this specific, previously untreated polyhedral geometry.

## Limitations

The theorem applies to central sections of one regular Archimedean solid. It is almost sure and does not classify planes containing original vertices or lying on the listed comparison great circles. It does not address offset planes, generalized rhombicuboctahedra, inverse determination of shape from section counts, or arbitrary affine images with Haar-distributed Euclidean normals. A corresponding calculation might be implicit in older stereology or spherical-arrangement tables not indexed in the accessible searches. Historical priority has not been independently established.

## References

1. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419 (first public December 17, 2024), https://arxiv.org/html/2412.12419v3.
2. A. Thom, *On planar sections of the dodecahedron*, arXiv:2511.12773 (first public November 16, 2025), https://arxiv.org/html/2511.12773.
3. H. S. M. Coxeter, *Regular Polytopes*, 3rd edition (Dover, 1973), standard references for the Archimedean rhombicuboctahedron.
4. *Rhombicuboctahedron*, Polyhedra Viewer, https://polyhedra.tessera.li/rhombicuboctahedron/info (standard vertex, edge and face counts; publication date not established).
