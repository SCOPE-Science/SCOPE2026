# The largest tetrahedron in a Steinmetz bicylinder

## Finding

For every radius \(R>0\), let the **bicylinder** be the intersection of two perpendicular, equal-radius solid circular cylinders,
\[
K_R=\{(x,y,z)\in\mathbb R^3:x^2+z^2\le R^2,\ y^2+z^2\le R^2\}.
\]
The largest volume of any tetrahedron \(T\subseteq K_R\), without restrictions on vertex position or tetrahedron shape, is
\[
\boxed{\max_{T\subseteq K_R}\operatorname{Vol}_3(T)=\frac{16R^3}{9\sqrt3}}.
\]
All maximizers are obtained by taking the four vertices
\[
(\pm R\sqrt{2/3},\ \pm R\sqrt{2/3},\ R/\sqrt3)
\quad\text{(correlated signs)},
\]
and
\[
(\pm R\sqrt{2/3},\ \mp R\sqrt{2/3},\ -R/\sqrt3)
\quad\text{(opposite signs)},
\]
or by reversing both displayed height signs. Thus, apart from a rigid symmetry of the bicylinder, there is a single maximizing tetrahedron. These are disphenoids, each having two perpendicular, equal-length horizontal edges in parallel horizontal planes.

Since \(\operatorname{Vol}_3(K_R)=16R^3/3\), the sharp maximal occupied-volume fraction is
\[
\boxed{\frac{\max_{T\subseteq K_R}\operatorname{Vol}_3(T)}{\operatorname{Vol}_3(K_R)}=\frac1{3\sqrt3}}.
\]

## Assumptions and scope

The cylinders are infinite along their axes, but their intersection \(K_R\) is compact; their axes meet orthogonally at the origin. A tetrahedron is the convex hull of four arbitrary points of \(K_R\), and degeneracy is permitted (volume zero). Volume is ordinary Euclidean three-dimensional volume. Scaling reduces the proof to \(R=1\). In particular, no assumption of central symmetry, equal edges or special orientation is imposed on the competitor.

## Proof

**1. A disk-hull model.** Set \(u=(x+y)/2\), \(v=(x-y)/2\). The Jacobian magnitude of the inverse coordinate map \((u,v,z)\mapsto(x,y,z)=(u+v,u-v,z)\) is \(2\). The elementary identity \(|u|+|v|=\max\{|x|,|y|\}\) transforms \(K_1\) into
\[
D=\{(u,v,z):(|u|+|v|)^2+z^2\le1\}.
\]
Let \(D_u=\{(u,0,z):u^2+z^2\le1\}\) and \(D_v=\{(0,v,z):v^2+z^2\le1\}\). At height \(z\), the section of \(D\) is the diamond \(|u|+|v|\le\sqrt{1-z^2}\), exactly the convex hull of the two sections of \(D_u\) and \(D_v\) at that same height. Also \(D\) is convex, since it is the unit ball of the norm \(\sqrt{(|u|+|v|)^2+z^2}\). Consequently
\[
D=\operatorname{conv}(D_u\cup D_v).
\]
Fixing three vertices of a tetrahedron makes its signed determinant affine-linear in the fourth vertex. By replacing each vertex successively with a point of one generating rim circle (the relative boundary of \(D_u\) or \(D_v\) in its supporting plane), an at-least-as-large tetrahedron is produced. Therefore there exists a global maximizer with all vertices on these two unit circles. This reduction does not assert that arbitrary maximizing vertices initially lie on the circles; that issue is resolved in step 4.

**2. Vertex distributions.** If all four vertices lie on a single generating circle, their tetrahedral volume vanishes. If three lie on one generating circle and one on the other, the triangle determined by the first three has area at most \(3\sqrt3/4\), the sharp triangle-area bound in a unit disk. The remaining vertex is at distance at most \(1\) from the first circle's plane. Hence that tetrahedron has volume at most
\[
\frac{\sqrt3}{4}<\frac8{9\sqrt3}.
\]
It remains to maximize the configurations with two vertices on each circle.

**3. Exact two-and-two bound.** Parametrize the two points on the first circle as
\[
A_\pm=(\cos(\phi\pm\alpha),0,\sin(\phi\pm\alpha)),
\]
and the other two as
\[
B_\pm=(0,\cos(\psi\pm\beta),\sin(\psi\pm\beta)),
\]
where the shorter angular half-chords permit \(0\le\alpha,\beta\le\pi/2\). Expanding the determinant by the two chord difference vectors and their midpoint difference gives the exact identity
\[
\left|\det(A_--A_+,B_+-A_+,B_--A_+)\right|
=4\sin\alpha\sin\beta
\left|\sin\psi\cos\alpha-\sin\phi\cos\beta\right|.
\]
Write \(a=\cos\alpha\), \(b=\cos\beta\), \(s=a+b\), so \(0\le a,b\le1\). The determinant is at most
\[
4\sqrt{1-a^2}\sqrt{1-b^2}(a+b)
\le4s\left(1-\frac{a^2+b^2}{2}\right)
\le4s\left(1-\frac{s^2}{4}\right)
\le\frac{16}{3\sqrt3}.
\]
The first inequality is the triangle inequality and \(|\sin\phi|,|\sin\psi|\le1\). The second is arithmetic–geometric mean; the third uses \(a^2+b^2\ge s^2/2\). The last inequality is maximization of \(s-s^3/4\) over \(0\le s\le2\), with its unique maximum at \(s=2/\sqrt3\). Equality forces
\[
a=b=1/\sqrt3,\qquad \sin\psi=-\sin\phi=\pm1.
\]
Thus the only circle-supported maximal tetrahedra in \(D\) have vertices
\[
(\pm\sqrt{2/3},0,1/\sqrt3),\quad(0,\pm\sqrt{2/3},-1/\sqrt3),
\]
or their simultaneous reflection in the horizontal plane. Their volume is \(8/(9\sqrt3)\). The inverse affine map multiplies volume by \(2\), proving the claimed bound and attaining coordinates in \(K_1\).

**4. No other equality cases.** Put \(h=\sqrt{2/3}\) and \(c=1/\sqrt3\). For the canonical tetrahedron in \(D\), fix the three vertices other than \(p=(h,0,c)\). Their plane has equation
\[
(2c,0,h)\cdot(u,v,z)=-hc.
\]
The support function of \(D\) in direction \(n=(2c,0,h)\) is
\[
h_D(n)=\max\{\sqrt{4c^2+h^2},h\}=\sqrt2=3hc.
\]
The positive support is attained uniquely at \(p\) on the first circle, and \(\min_{q\in D}n\cdot q=-\sqrt2\). Therefore \(|n\cdot q+hc|\), which is proportional to the volume when the other three vertices are fixed, has its **unique** maximum at \(q=p\): the positive-end value is \(4hc\), and the negative-end value only \(2hc\). Sign changes and swapping \(u,v\) give the same uniqueness property for each of the four canonical vertices.

Now begin with any volume-maximizing tetrahedron in \(D\), and successively replace its four vertices by generating-circle maximizers as in step 1. The final tetrahedron must be canonical by step 3. Undo the replacements in reverse order. At each reversal, the other three points have already been shown canonical; the just-proved strict coordinatewise optimality forces the original vertex to equal its replacement. Thus every maximizing tetrahedron is canonical, and the stated equality classification is complete.

Finally, direct integration of the square sections of \(K_R\), each of area \(4(R^2-z^2)\) at height \(z\), gives \(\operatorname{Vol}_3(K_R)=\int_{-R}^R4(R^2-z^2)\,\mathrm dz=16R^3/3\), yielding the ratio.

## Verification

The standalone standard-library Python file `verify.py` reproduces the proposed equality coordinates, evaluates their volume and occupied-volume ratio, and independently checks the sharp determinant inequalities on 6,000 exact-rational circle configurations, as well as 5,000 random tetrahedra throughout the bicylinder. Run `python verify.py`. These tests corroborate numerical and algebraic details; the universal optimization and equality classification rest on steps 1–4 above, not finite enumeration.

## Relationship to prior work

Finch's *Convex Hull of Two Orthogonal Disks*, publicly available from 19 November 2012, studies precisely the two perpendicular unit disks with coincident centers and calculates their hull's volume \(8/3\), surface area and mean width. The affine change of variables in step 1 connects that hull to the classical Steinmetz bicylinder. The disk-hull body itself, its volume, and the basic cross-sectional geometry are therefore not claimed as discoveries. Finch's inspected source does not give a maximal contained tetrahedron or an equality classification.

Horváth's survey *Volume of convex hull of two bodies and related problems* discusses maximal volume simplices on spheres and volumes of convex hulls of two convex bodies; its relevant extremal statements concern different objects and objectives. Other publicly available results on concurrent-disk hulls establish intrinsic-volume identities and on orthogonal-disk hulls establish mean-width behavior; they do not imply the extremal tetrahedron-volume claim. These are mathematical scope comparisons, not a proof of global historical priority.

## Limitations

Only **equal-radius perpendicular** cylinders whose axes meet are addressed. The theorem does not classify unequal-radius, oblique, translated or triple-cylinder intersections. The exact bound and equality classification are analytically proved, but unindexed or differently named historical calculations could affect the priority assessment. The checker samples finitely many configurations and has no status as an independent infinite-proof certification.

## References

1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first submitted 2012-11-19, https://arxiv.org/abs/1211.4514 and https://arxiv.org/pdf/1211.4514. Especially introduction and Section 1 (the concentric right-angle case).
2. Á. G. Horváth, *Volume of convex hull of two bodies and related problems*, arXiv:1509.08859, https://arxiv.org/html/1509.08859v2. Especially Sections 3.1–3.2.
3. *A universal surface–volume identity for hulls of concurrent circular disks*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-universal-surface-volume-identity-for-hulls-of-concurrent-circ--f6dccc1bad11 .
4. *A one-dimensional derivative law for orthogonal-disk mean width*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-dimensional-derivative-law-for-orthogonal-disk-mean-width--6e52fbc79bdf .
5. *Exact intrinsic volumes and boundary decomposition of the orthogonal three-disk hull*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-intrinsic-volumes-and-boundary-decomposition-of-the-orthog--14663bdfc53a .
