# Uniform directional illumination and exact illumination numbers of the rhombic triacontahedron

## Finding
Let \(\varphi=(1+\sqrt5)/2\) and take the regular icosahedral vertex set
\[
I=\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
Let \(E\) contain the thirty unordered pairs of vertices of \(I\) whose squared Euclidean distance is \(4\). Define
\[
K=\operatorname{conv}\{v+w:\{v,w\}\in E\},\qquad P=K^\circ.
\]
The thirty vertices of \(K\) are twice the edge midpoints of the icosahedron; \(K\) is an icosidodecahedron. Its polar \(P\) is a rhombic triacontahedron with twelve vertices incident to five facets and twenty vertices incident to three facets.

**Theorem.** Every direction \(u\) satisfying
\[
\langle u,v+w\rangle\ne0 \quad\text{for every }\{v,w\}\in E
\]
illuminates **exactly three five-valent and seven three-valent vertices** of \(P\). Every other direction illuminates at most three and seven, respectively. Moreover,
\[
\boxed{i(P)=i^*(P)=4},
\]
where \(i\) is ordinary parallel-direction illumination and \(i^*\) is fractional illumination.

The four explicit directions
\[
(-2,-2,1),\qquad(-1,2,-1),\qquad(1,1,2),\qquad(2,-2,-1)
\]
illuminate all thirty-two vertices. Each of the twelve five-valent vertices is illuminated by **exactly one** of these directions, while among the twenty three-valent vertices twelve are illuminated once and eight twice.

## Assumptions and scope
A direction \(u\ne0\) illuminates a boundary point \(x\) of a full-dimensional convex body \(C\) when \(x+\varepsilon u\in\operatorname{int}C\) for some \(\varepsilon>0\). The number \(i(C)\) is the least size of a finite set of directions illuminating the boundary. The fractional number \(i^*(C)\) is the minimum total weight, or infimum of total weight, over finite nonnegative weighted collections of directions such that each boundary point receives illuminating weight at least one. Here all signs are **strict**; the proof addresses both generic and nongeneric directions.

For a polytope, it suffices to check vertices: if \(x\) lies in the relative interior of a face \(F\) and \(v\) is a vertex of \(F\), each facet inequality active at \(x\) is also active at \(v\). Hence a direction entering all the active inequalities strictly at \(v\) does so at \(x\) as well. This also justifies the fractional reduction by applying the incidence inequality face by face.

## Proof
**1. Polar face correspondences.** For an icosahedral vertex \(v\in I\), the five edges of \(I\) incident to \(v\) yield five vertices \(v+w\) spanning one pentagonal facet of \(K\). Each of the twenty icosahedral triangular faces gives three edge-sum vertices spanning one triangular facet of \(K\). These are all the facets of \(K\); an independent exhaustive supporting-plane construction from all noncollinear triples of its thirty edge-sum vertices finds precisely these twelve pentagons and twenty triangles (see `verify.py`). Their dual vertices in \(P\) accordingly have valences five and three.

Let \(F\) be any facet of \(K\), and let \(p_F\) be its dual vertex in \(P\). A direction \(u\) illuminates \(p_F\) if and only if
\[
\langle u,n\rangle<0\qquad\text{for every }n\in\operatorname{vert}(F).
\tag{1}
\]
Indeed the active inequalities at \(p_F\) in the polar description \(\langle x,n\rangle\le1\) are precisely those with \(n\in\operatorname{vert}(F)\).

**2. A reflection arrangement with uniform incidence.** For each edge-sum vertex \(n=v+w\) of \(K\), define its orthogonal reflection
\[
R_n(z)=z-2\frac{\langle n,z\rangle}{\langle n,n\rangle}n.
\tag{2}
\]
A direct exact calculation in \(\mathbb Z[\varphi]\), using \(\varphi^2=\varphi+1\), shows that \(R_n\) permutes the original twelve vertices \(I\), for **each** of the thirty choices of \(n\). This is certified by the thirty-by-twelve exact permutation tests in `verify.py`; its reflection test checks equality after multiplying through by the nonzero denominator in (2). Therefore \(R_n\) permutes the edge set \(E\), the vertices of \(K\), and its triangular and pentagonal facets separately.

The hyperplanes
\[
H_n=\{u:\langle u,n\rangle=0\},\qquad n\in\operatorname{vert}(K),
\]
form a finite **reflection arrangement**. Every chamber is a connected component of the complement of their union. Two chambers sharing a codimension-one wall in \(H_n\) are exchanged by \(R_n\). The chamber-adjacency graph of any finite real hyperplane arrangement is connected: a generic straight path between points in any two chambers can be chosen to cross one wall at a time. Hence the reflections (2) act transitively on its chambers.

For a generic direction \(u\), the set of vertices illuminated by (1) is constant within a chamber. Under each \(R_n\), illumination incidence is carried to the corresponding incidence for the reflected direction, preserving both vertex valence classes. Chamber transitivity therefore forces the ordered pair
\[
(\#\text{ illuminated five-valent vertices},\ \#\text{ illuminated three-valent vertices})
\]
to have **one value for every generic direction**. Exact sign evaluation at \(u=(-2,-2,1)\) gives that value as \((3,7)\).

For any nongeneric direction \(u\), every vertex that it illuminates satisfies finitely many strict inequalities (1), so remains illuminated after a sufficiently small generic perturbation of \(u\). Thus its pair of illumination counts is bounded componentwise by \((3,7)\).

**3. Sharp lower bounds.** There are twelve five-valent vertices, and every direction illuminates at most three of them. Consequently any ordinary illuminating family contains at least \(\lceil12/3\rceil=4\) directions. For a fractional illumination of total weight \(W\), sum the required weights over those twelve vertices. Each direction contributes at most three times its weight, so \(12\le3W\) and \(W\ge4\). Thus \(i(P),i^*(P)\ge4\).

**4. Sharp upper bounds.** The four integer directions in the theorem's statement are all generic. Their exact sign matrices against the thirty vertices of \(K\) are evaluated in `verify.py`. They jointly illuminate each of the twelve five-valent vertices once, and each of the twenty three-valent vertices at least once. As the vertex constraints imply all boundary constraints, \(i(P)\le4\); assigning unit weight to these directions also gives \(i^*(P)\le4\). This completes the theorem.

## Verification
Run `python3 verify.py` using Python's standard library. All algebra, coplanarity, incidence, and strict sign comparisons use pairs of integers representing \(a+b\varphi\); no floating-point tolerance or geometry package is used. The program enumerates all 66 possible icosahedral vertex pairs and identifies thirty edges, enumerates every triple of the thirty edge-sum vertices to reconstruct the complete facet set, proves exactly twelve five-vertex facets and twenty three-vertex facets, verifies 360 reflection identities, computes the reference incidence \((3,7)\), and checks the complete four-direction vertex cover. An additional 150 sample directions are checked diagnostically, **not** used as an infinite proof.

Expected output:
```
EXACT_OK original_vertices=12 roots=30 hull_facets=32 pentagons=12 triangles=20
EXACT_OK reflections=30x12 generic_incidence=(3,7) witnesses=4 min_vertex_coverage=1
EXACT_OK ordinary_illumination=4 fractional_illumination=4
```
The analytic wall-reflection argument, not sampling, extends the reference incidence calculation to **all** generic directions.

## Relationship to prior work
Naszódi introduced fractional illumination and established a universal exponential bound for centrally symmetric bodies [1], but did not determine the values for this Catalan solid. Gorodzha's September 2026 paper [2] gives a sharp general bound and motivating fractional-illumination framework, not this object-specific exact two-orbit directional spectrum. Prior exact studies determine fractional values of the regular icosahedron and dodecahedron [3], and ordinary illumination of certain centrally symmetric three-dimensional solids [4]. Kiss and de Wet [6] calculate a different, norm-weighted parameter for Platonic and Archimedean solids, without identifying the present Catalan-solid ordinary/fractional directional values. Those results neither state nor imply the two-class directional constancy or the four-witness equality for the rhombic triacontahedron.

A geometric presentation of the rhombic triacontahedron and its dual icosidodecahedron is available in [5]. The result concerns the **ordinary and fractional parallel-direction illumination** invariants, not a norm-weighted cost of external point light sources.

## Limitations
The theorem applies to the stated standard regular dual pair and to its invertible linear images; it does not assert the same spectrum for arbitrary combinatorially equivalent polyhedra. The chamber reflection identity depends on the metric icosahedral realization. Historical priority for an equivalent value under another illumination terminology remains open to independent bibliographic review. No independent scientific audit is claimed.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, *Contributions to Discrete Mathematics* 4(2) (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022; https://cdm.ucalgary.ca/article/download/62022/46694/177154.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1 (first posted 20 September 2026); https://arxiv.org/pdf/2609.23913.
3. *Exact fractional illumination of the regular dodecahedron and icosahedron*, full mathematical result accessible at https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-fractional-illumination-of-the-regular-dodecahedron-and-ic--760696b5ce34/RESULT.md.
4. *Exact illumination numbers of five canonical parallelohedron representatives*, publicly indexed result at https://github.com/published-finding corpus/2026/tree/main/2026/9/8/SCOPE008.
5. *Rhombic Triacontahedron*, Virtual Math Museum (3DXM), https://www.virtualmathmuseum.org/Polyhedra/RhombicTriacontaeder/index.html.
6. G. Kiss and P. O. de Wet, *Notes on the illumination parameters of convex polytopes*, *Contributions to Discrete Mathematics* 7(1) (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108; https://cdm.ucalgary.ca/article/download/62108/46729/177610.
