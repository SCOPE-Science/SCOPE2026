# Every uniform antiprism has X-ray number three
## Finding
For every integer
\[
n\ge3,
\]
the Euclidean uniform \(n\)-gonal antiprism \(A_n\subset\mathbb R^3\) has
\[
X(A_n)=3.
\tag{1}
\]

There is a uniform three-line certificate for the entire infinite family. Put
\[
a=\frac{\pi}{2n},
\qquad
H=\sqrt{4\cos^2 a-1},
\qquad
\phi_j=\frac{2\pi j}{3}
\quad(j=0,1,2).
\]
Then the three lines
\[
L_j
=
\mathbb R
\left(
\cos\phi_j,\,
\sin\phi_j,\,
H
\right)
\tag{2}
\]
X-ray every point of \(A_n\).

Thus every convex uniform antiprism attains the absolute dimension lower bound for the X-ray number, although these polytopes are not almost smooth.

## Assumptions and scope
For a convex body \(K\subset\mathbb R^3\), a point \(p\in K\) is X-rayed along a line \(L\) through the origin when the affine line through \(p\) parallel to \(L\) intersects
\[
\operatorname{int}K.
\]
The X-ray number \(X(K)\) is the minimum number of line directions needed to X-ray every point of \(K\).

For a proper face \(F\) of a convex polytope, its Gauss image \(\nu(F)\subset S^2\) is the set of outer unit normals of supporting planes containing \(F\). The standard criterion used below is
\[
p\text{ is X-rayed along }L
\quad\Longleftrightarrow\quad
L^\perp\cap\nu(F)=\varnothing,
\]
where \(F\) is the minimal face containing \(p\).

The antiprism is the ordinary convex uniform antiprism: two congruent regular \(n\)-gons in parallel planes, rotated by half a base angle, with every edge of length \(1\). No claim is made here for nonuniform antiprisms with arbitrary height.

## Proof
Let
\[
a=\frac{\pi}{2n}.
\]
A unit-edge regular \(n\)-gon has circumradius
\[
R=\frac1{2\sin(2a)}.
\]
The horizontal distance between an upper vertex and either adjacent lower vertex is
\[
2R\sin a
=
\frac1{2\cos a}.
\]
Hence the vertical separation between the two base planes is
\[
h
=
\sqrt{1-\frac1{4\cos^2 a}}
=
\frac{H}{2\cos a},
\qquad
H:=\sqrt{4\cos^2 a-1}.
\tag{3}
\]

Use the vertex coordinates
\[
v_k^+
=
\left(
R\cos(4ak),
R\sin(4ak),
\frac h2
\right),
\]
\[
v_k^-
=
\left(
R\cos((4k+2)a),
R\sin((4k+2)a),
-\frac h2
\right),
\qquad
0\le k<n.
\tag{4}
\]

Consider first the upper vertex
\[
v_0^+=(R,0,h/2).
\]
It belongs to the upper \(n\)-gonal face and to three equilateral triangular faces. Put
\[
\gamma
=
\frac{H}{\sqrt3\cos a},
\qquad
\zeta
=
\frac{\tan a}{\sqrt3}.
\tag{5}
\]
Direct cross products give the four outward unit facet normals
\[
e_3,
\]
\[
m_0=(\gamma,0,-\zeta),
\]
\[
m_\pm
=
\left(
\gamma\cos(2a),
\pm\gamma\sin(2a),
\zeta
\right).
\tag{6}
\]
Indeed,
\[
\gamma^2+\zeta^2=1.
\]

For an azimuth \(\phi\), write
\[
d_\phi=(\cos\phi,\sin\phi,H).
\tag{7}
\]
The key identity
\[
\zeta H=\gamma\sin a
\tag{8}
\]
turns the four scalar products in (6) into
\[
e_3\cdot d_\phi=H>0,
\]
\[
m_0\cdot d_\phi
=
\gamma(\cos\phi-\sin a),
\]
\[
m_\pm\cdot d_\phi
=
\gamma\bigl(\cos(\phi\mp2a)+\sin a\bigr).
\tag{9}
\]

Let
\[
\beta=\frac{\pi}{2}-a.
\]
Because
\[
\sin a=\cos\beta,
\]
the middle expression in (9) is positive exactly when the circular distance from \(\phi\) to \(0\) is less than \(\beta\). If
\[
\operatorname{dist}_{S^1}(\phi,0)<\beta,
\]
then
\[
\operatorname{dist}_{S^1}(\phi,\pm2a)
<
\beta+2a
=
\frac{\pi}{2}+a,
\]
and therefore
\[
\cos(\phi\mp2a)>-\sin a.
\]
Thus every expression in (9) is strictly positive.

Conversely, if the line \(\mathbb R d_\phi\) X-rays \(v_0^+\), then all four incident facet normals must have scalar products of one strict sign with an orientation of that line. Since
\[
e_3\cdot d_\phi>0,
\]
that sign must be positive, and the \(m_0\) inequality forces
\[
\operatorname{dist}_{S^1}(\phi,0)<\beta.
\]
Hence
\[
\mathbb R d_\phi
\text{ X-rays }v_0^+
\quad\Longleftrightarrow\quad
\operatorname{dist}_{S^1}(\phi,0)<\beta.
\tag{10}
\]

Rotating (10) gives the complete upper-ring criterion:
\[
\mathbb R d_\phi
\text{ X-rays }v_k^+
\quad\Longleftrightarrow\quad
\operatorname{dist}_{S^1}(4ak,\phi)<\beta.
\tag{11}
\]

The lower ring is obtained from the upper ring by the isometry that rotates by \(2a\) around the vertical axis and reverses the vertical coordinate. Under this isometry the orientation required by the lower-base normal is opposite. Therefore
\[
\mathbb R d_\phi
\text{ X-rays }v_k^-
\quad\Longleftrightarrow\quad
\operatorname{dist}_{S^1}((4k+2)a-\pi,\phi)<\beta.
\tag{12}
\]

Now choose
\[
\phi_0=0,
\qquad
\phi_1=\frac{2\pi}{3},
\qquad
\phi_2=\frac{4\pi}{3}.
\]
Since
\[
n\ge3,
\qquad
a\le\frac{\pi}{6},
\qquad
\beta\ge\frac{\pi}{3}.
\tag{13}
\]
If \(n>3\), then
\[
\beta>\frac{\pi}{3},
\]
so the three open circular arcs of radius \(\beta\) centered at the \(\phi_j\) cover all of \(S^1\). Equations (11)--(12) therefore show that every upper and lower vertex is X-rayed by at least one of the three lines in (2).

For \(n=3\),
\[
\beta=\frac{\pi}{3}.
\]
The only points omitted by those three open arcs are
\[
\frac{\pi}{3},
\qquad
\pi,
\qquad
\frac{5\pi}{3}.
\]
But both the upper azimuths in (11) and the transformed lower azimuths in (12) are
\[
0,
\qquad
\frac{2\pi}{3},
\qquad
\frac{4\pi}{3}.
\]
Thus the same three lines still cover every vertex.

It remains only to pass from vertices to the whole boundary. Let \(F\) be any proper face and choose a vertex \(v\in F\). Every supporting plane that contains \(F\) also contains \(v\), hence
\[
\nu(F)\subseteq\nu(v).
\]
If one of the three lines has orthogonal great circle disjoint from \(\nu(v)\), it is also disjoint from \(\nu(F)\). The Gauss-image criterion therefore shows that all boundary points are X-rayed. Interior points are automatic, so
\[
X(A_n)\le3.
\]

Every three-dimensional convex body satisfies
\[
X(K)\ge3.
\]
Combining this with the upper bound gives (1).

Finally, this result is not an instance of the almost-smooth theorem. At every upper vertex, the upper-base normal \(e_3\) and the triangular-facet normal \(m_0\) satisfy
\[
e_3\cdot m_0
=
-\zeta
=
-\frac{\tan a}{\sqrt3}
<
0.
\]
In dimension three, almost smoothness would require every pair of incident outward unit normals to have scalar product at least
\[
\frac12.
\]
Hence no uniform antiprism in this family is almost smooth.

## Verification
The bundled `verify.py` checks the unit-edge coordinate model, the identities
\[
\gamma^2+\zeta^2=1,
\qquad
\zeta H=\gamma\sin a,
\]
and the three-line vertex coverage for every
\[
3\le n\le200.
\]
It derives the four representative incident normals from the analytic formulas and checks the strict sign criterion at every upper and lower vertex for the three directions in (2).

The finite sweep is only a regression test. The quantified theorem for all \(n\ge3\) follows from the exact normal formulas (6), the exact equivalences (10)--(12), and the elementary circular covering inequality (13).

## Relationship to prior work
Bezdek and Kiss define the X-ray number, give the universal lower bound
\[
X(K)\ge d,
\]
and prove
\[
X(M)=d
\]
for every almost smooth \(d\)-dimensional convex body. Their Gauss-image lemma is the criterion used in the proof above. Their complete public text contains no occurrence of “antiprism,” and the family here lies outside their almost-smooth class because an upper-base normal and an incident triangular-facet normal have negative scalar product.

Bezdek's earlier affine-subspace illumination theorem is a different invariant. In dimension three it illuminates suitable polyhedral boundaries using external affine lines, whereas the X-ray number fixes line directions through every tested point. That theorem therefore does not imply the three-direction statement proved here.

Targeted searches under “X-ray number,” “regular antiprism,” “uniform antiprism,” “illumination,” “Gauss image,” and “three directions” did not locate a published theorem giving (1). The triangular antiprism is the regular octahedron, whose value \(3\) is a special case; the contribution here is the complete infinite uniform-antiprism family together with one explicit three-line construction valid for every \(n\).

## Limitations
The proof uses the uniform metric realization, especially the height identity (3). It does not determine the X-ray number of arbitrary nonuniform antiprisms with the same combinatorial type.

The theorem concerns X-ray number, not ordinary illumination number and not illumination by external affine line sources.

A differently phrased classical observation in older illumination literature remains a residual originality risk. The closest X-ray primary source was inspected in full, and exact-object and equivalent-formulation searches did not locate the antiprism family result.

## References
1. K. Bezdek and Gy. Kiss, *On the X-ray number of almost smooth convex bodies and of convex bodies of constant width*, arXiv:0903.4830v1, 27 March 2009; *Canadian Mathematical Bulletin* 52 (2009), 342--348. DOI: 10.4153/CMB-2009-037-0.
2. K. Bezdek, *The problem of illumination of the boundary of a convex body by affine subspaces*, *Mathematika* 38 (1991), 362--375. DOI: 10.1112/S0025579300006707.
