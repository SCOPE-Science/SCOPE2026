# The regular icosahedron has X-ray number three
## Finding
Let
\[
\varphi=\frac{1+\sqrt5}{2}
\]
and let
\[
I=\operatorname{conv}\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}\subset\mathbb R^3.
\]
This is a regular icosahedron of edge length \(2\). Its X-ray number is
\[
X(I)=3.
\]
More explicitly, the three coordinate lines
\[
L_1=\mathbb Re_1,\qquad L_2=\mathbb Re_2,\qquad L_3=\mathbb Re_3
\]
X-ray every point of \(I\).

## Assumptions and scope
For a convex body \(K\subset\mathbb R^3\), a point \(p\in K\) is X-rayed along a line \(L\) through the origin when the affine line through \(p\) parallel to \(L\) meets \(\operatorname{int}K\). The X-ray number \(X(K)\) is the minimum number of line directions needed to X-ray every point of \(K\).

For a face \(F\) of a convex body, its Gauss image \(\nu(F)\subset S^2\) is the set of outer unit normals of supporting planes containing \(F\). The standard Gauss-image criterion says that a boundary point whose minimal face is \(F\) is X-rayed along \(L\) exactly when
\[
L^\perp\cap\nu(F)=\varnothing.
\]

The result concerns the ordinary Euclidean regular icosahedron. Scaling, rigid motion, or any invertible linear image preserves the numerical X-ray number after transporting the line directions, but no claim is made for arbitrary combinatorial icosahedra.

## Proof
Every vertex in the displayed coordinate model has exactly one coordinate of absolute value \(\varphi\). It is therefore enough, by cyclic coordinate permutations and independent sign changes, all of which preserve the vertex set, to verify one representative vertex
\[
v=(\varphi,0,1).
\]

The five neighbors of \(v\) are
\[
(0,1,\varphi),\quad (0,-1,\varphi),\quad (1,\varphi,0),\quad (1,-\varphi,0),\quad (\varphi,0,-1).
\]
The five triangular facets through \(v\) have outward normals proportional to
\[
\begin{aligned}
n_1&=(\sqrt5-1,0,\sqrt5+1),\\
n_2&=(2,2,2),\\
n_3&=(2,-2,2),\\
n_4&=(\sqrt5+1,\sqrt5-1,0),\\
n_5&=(\sqrt5+1,1-\sqrt5,0).
\end{aligned}
\tag{1}
\]
All five first coordinates in (1) are strictly positive. Hence the entire spherical convex hull of these normalized normals, which is the Gauss image \(\nu(v)\), lies in the open hemisphere
\[
\{u\in S^2:u_1>0\}.
\]
Consequently
\[
L_1^\perp\cap\nu(v)=\varnothing,
\]
so \(v\) is X-rayed along \(L_1\).

The signed-coordinate symmetries of the coordinate model now give the complete vertex statement: if a vertex has \(i\)-th coordinate of absolute value \(\varphi\), then it is X-rayed along \(L_i\). Thus every vertex is X-rayed by one of \(L_1,L_2,L_3\).

Let \(F\) be any proper face of \(I\), and choose a vertex \(v_F\in F\). Every supporting plane containing \(F\) also contains every point of \(F\), so
\[
\nu(F)\subseteq\nu(v_F).
\]
Choose a coordinate line \(L_i\) that X-rays \(v_F\). Since
\[
L_i^\perp\cap\nu(v_F)=\varnothing,
\]
we also have
\[
L_i^\perp\cap\nu(F)=\varnothing.
\]
The Gauss-image criterion therefore X-rays every boundary point whose minimal face is \(F\). As every boundary point belongs to such a face, the three coordinate lines X-ray the whole boundary, and interior points are automatic. Hence
\[
X(I)\le3.
\]

For every three-dimensional convex body, the general dimension bound gives
\[
X(K)\ge3.
\]
Therefore
\[
X(I)=3.
\]

Finally, this equality is not supplied by the standard almost-smooth theorem. At \(v\), the normals
\[
n_1=(\sqrt5-1,0,\sqrt5+1),
\qquad
n_4=(\sqrt5+1,\sqrt5-1,0)
\]
both have norm \(2\sqrt3\) and satisfy
\[
\frac{n_1\cdot n_4}{\lVert n_1\rVert\lVert n_4\rVert}
=
\frac13.
\]
In dimension three, almost smoothness requires every such cosine to be at least \(1/2\). Thus the regular icosahedron lies outside that sufficient class.

## Verification
The supplied `verify.py` reconstructs all twelve vertices in exact arithmetic over \(\mathbb Q(\sqrt5)\). It enumerates the thirty unit-pattern edges of squared length \(4\), then the twenty edge-clique triangular facets, and derives an outward normal for each facet.

For every vertex it checks that exactly five facets are incident and that at least one coordinate axis has a strictly same-signed dot product with all five outward normals. It also verifies that the three axes collectively cover all twelve vertices and that the minimum normalized inner product among two incident facet normals is exactly \(1/3\).

The checker uses no floating-point tolerance for the scientific assertions. Numerical conversion is used only to print human-readable diagnostics after the symbolic equalities and inequalities have already passed.

## Relationship to prior work
Bezdek and Kiss define the X-ray number, record the universal lower bound \(X(K)\ge d\), and prove \(X(M)=d\) for every almost smooth \(d\)-dimensional convex body. Their Gauss-image Lemma 2.2 is the criterion used above. Their full text contains no occurrence of “icosahedron” or “Platonic,” and the regular icosahedron does not satisfy their almost-smooth hypothesis because two incident facet normals at a vertex have cosine \(1/3<1/2\).

Bezdek's earlier affine-subspace illumination paper proves broad illumination results for convex polytopes with affine symmetry, but its published main theorem is an eight-source-style covering statement in three dimensions rather than the exact three-line X-ray value established here.

Targeted searches under “X-ray number,” “regular icosahedron,” “Platonic solids,” “coordinate axes,” “illumination number,” and the almost-smooth terminology did not locate a statement implying this exact value. The nearest indexed results concern illumination numbers of different polyhedral families or unrelated icosahedral graph invariants.

## Limitations
The proof is special to the regular metric realization and its signed-coordinate symmetry. It does not classify the X-ray number of arbitrary convex icosahedra.

The literature search cannot rule out an unindexed classical observation or a differently phrased result in the older illumination literature. In particular, the conclusion is elementary once the correct coordinate directions are identified, so this residual risk is real and is recorded explicitly.

No claim is made about the illumination number \(I(I)\), although the general inequalities between illumination and X-ray numbers provide immediate bounds.

## References
1. K. Bezdek and Gy. Kiss, *On the X-ray number of almost smooth convex bodies and of convex bodies of constant width*, arXiv:0903.4830v1, 27 March 2009; Canadian Mathematical Bulletin 52 (2009), 342--348, DOI: 10.4153/CMB-2009-037-0.
2. K. Bezdek, *The problem of illumination of the boundary of a convex body by affine subspaces*, Mathematika 38 (1991), 362--375, DOI: 10.1112/S0025579300006707.
