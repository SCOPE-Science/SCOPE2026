# Equality cases of the planar Makai-volume flag inequality

## Finding
Let \(P\subset\mathbb R^2\) be a full-dimensional convex polygon with precisely \(n\ge3\) genuine vertices. Write \(D=P-P=\{x-y:x,y\in P\}\), define \(D^\circ=\{z:\langle z,d\rangle\le1\text{ for every }d\in D\}\), and put
\[
\mathcal M(P)=\operatorname{area}(P)\operatorname{area}(D^\circ).
\]
Then
\[
\boxed{\mathcal M(P)\le\frac n2,\qquad\mathcal M(P)=\frac n2\ \Longleftrightarrow\ P\text{ is a triangle or a parallelogram}.}
\]
Every triangle has \(\mathcal M(P)=3/2\). A quadrilateral has \(\mathcal M(P)\le2\), with equality precisely when its diagonals bisect one another. For \(n\ge5\), the stronger universal estimate
\[
\mathcal M(P)\le\frac{\pi^2}{4}<\frac52\le\frac n2
\]
provides the explicit positive flag deficit \(n/2-\pi^2/4\).

A planar \(n\)-gon has exactly \(2n\) maximal face flags, so the upper bound \(n/2\) is exactly the planar instance of Winter's 2026 flag-number inequality. The equality classification is the additional assertion here.

## Assumptions and scope
Area is planar Lebesgue area. Polygons are convex, compact, have nonempty interior, and are counted by *extreme* vertices rather than collinear subdivisions. The difference body \(D\) contains the origin in its interior. The polar is taken with respect to the fixed origin; the difference construction makes the functional translation invariant. No symmetry, smoothness, or normalization is imposed on \(P\).

The product \(\mathcal M(P)\) is invariant under invertible affine transformations: translations cancel in \(P-P\), and an invertible linear map \(T\) multiplies \(\operatorname{area}(P)\) by \(|\det T|\) while multiplying \(\operatorname{area}((T D)^\circ)\) by \(|\det T|^{-1}\). We may therefore use convenient affine coordinates for triangles and quadrilaterals.

## Proof
**Five or more vertices.** The planar Brunn–Minkowski inequality applied to \(P\) and \(-P\) gives
\[
\operatorname{area}(P-P)^{1/2}\ge\operatorname{area}(P)^{1/2}+\operatorname{area}(-P)^{1/2}=2\operatorname{area}(P)^{1/2},
\]
so \(\operatorname{area}(D)\ge4\operatorname{area}(P)\). Since \(D=-D\), its Santaló point is the origin, and the symmetric planar Blaschke–Santaló inequality yields
\[
\operatorname{area}(D)\operatorname{area}(D^\circ)\le\pi^2.
\]
Consequently \(\mathcal M(P)\le\pi^2/4\). For \(n\ge5\), \(\pi^2<10\) implies \(\pi^2/4<5/2\le n/2\), proving strictness and the deficit bound.

**Triangles.** Affine invariance reduces to \(P=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\) of area \(1/2\). The three independent difference vectors are \((1,0),(0,1),(1,-1)\), together with their negatives, hence
\[
D^\circ=\{(x,y):|x|\le1,\ |y|\le1,\ |x-y|\le1\}.
\]
Its successive vertices are \((1,1),(1,0),(0,-1),(-1,-1),(-1,0),(0,1)\). The shoelace formula gives area \(3\); thus \(\mathcal M(P)=(1/2)\cdot3=3/2\).

**Quadrilaterals.** Their diagonals meet in an interior point. Translate that point to the origin and use an invertible linear map to write the four consecutive vertices as
\[
(1,0),\quad(0,1),\quad(-s,0),\quad(0,-t),\qquad s,t>0.
\]
Then \(\operatorname{area}(P)=(1+s)(1+t)/2\). Put \((X,Y)=((1+s)x,(1+t)y)\) in polar coordinates \((x,y)\). The two diagonal differences imply that the transformed polar \(Q'\) lies in the square \(S=[-1,1]^2\). Its area satisfies
\[
\operatorname{area}(D^\circ)=\frac{\operatorname{area}(Q')}{(1+s)(1+t)},\qquad\mathcal M(P)=\frac{\operatorname{area}(Q')}{2}\le2.
\]
The remaining four absolute-value inequalities defining \(Q'\) come from cross-axis vertex pairs and read
\[
\left|\frac{X}{1+s}-\frac{Y}{1+t}\right|\le1,\qquad
\left|\frac{sX}{1+s}+\frac{Y}{1+t}\right|\le1,
\]
\[
\left|\frac{sX}{1+s}-\frac{tY}{1+t}\right|\le1,\qquad
\left|\frac{X}{1+s}+\frac{tY}{1+t}\right|\le1.
\]
An absolute linear form has its maximum over \(S\) at a corner, where its absolute maximum is the sum of its nonnegative coefficient magnitudes. Therefore the four inequalities contain *all* of \(S\) exactly when
\[
\frac1{1+s}+\frac1{1+t}\le1\ \Longleftrightarrow\ st\ge1,
\]
\[
\frac{s}{1+s}+\frac1{1+t}\le1\ \Longleftrightarrow\ s\le t,
\]
\[
\frac{s}{1+s}+\frac{t}{1+t}\le1\ \Longleftrightarrow\ st\le1,
\]
\[
\frac1{1+s}+\frac{t}{1+t}\le1\ \Longleftrightarrow\ t\le s.
\]
All four hold precisely when \(s=t=1\). If one fails, a square corner violates a strip strictly; by continuity, a region of positive area is excluded from \(S\), so \(\operatorname{area}(Q')<4\) and \(\mathcal M(P)<2\). For \(s=t=1\) every inequality holds throughout \(S\), so \(Q'=S\) and \(\mathcal M(P)=2\). The condition \(s=t=1\) means the diagonals bisect each other, which is equivalent to \(P\) being a parallelogram.

These three cases exhaust all full-dimensional convex polygons and establish the claimed equality classification. \(\square\)

## Verification
The proof is exact and uses no finite enumeration. The triangle's six rational dual vertices are checked by the shoelace formula. For quadrilaterals, four explicit corner inequalities give a necessary-and-sufficient condition for the normalized polar to fill its containing square. The many-vertex case invokes two classical global convex-body inequalities; it is not inferred from sampling.

The accompanying standalone `check_polygon.py` uses exact rational arithmetic to verify the triangle calculation, the four inequality equivalences, and representative quadrilateral polar intersections by polygon clipping. Execute with `python check_polygon.py`; expected output: `PLANAR_MAKAI_FLAG_RATIONAL_REGRESSIONS_OK`. Such finite checks are supplementary and do not establish the universal theorem.

## Relationship to prior work
Martin Winter, *A relation between Mahler volume and flag number for convex polytopes* (first arXiv version October 7, 2026, arXiv:2610.09990v1), proves \(\operatorname{vol}(P)\operatorname{vol}((P-P)^\circ)\le\mathcal F(P)/(d!)^2\) for every full-dimensional polytope, and explicitly leaves equality unresolved while conjecturing Hanner polytopes and their faces. This result resolves that equality question in dimension two only, with an independent elementary proof of the planar inequality.

Böröczky, Makai, Meyer and Reisner, *Volume product of planar polar convex bodies—lower estimates with stability* (arXiv:1507.01481v1), discuss Eggleston's opposite-direction estimate \(\mathcal M(K)\ge3/2\), equality only for triangles. That lower estimate neither implies the flag-dependent upper bound nor classifies its parallelogram equality case. Meyer and Reisner, *On the volume product of polygons* (2011, DOI 10.1007/s12188-011-0054-3), treat the ordinary Santaló-centered polar product, not the polar of the difference body. These distinctions matter despite shared polygon and volume-product terminology.

## Limitations
The conclusion is planar only. The displayed gap for polygons with five or more vertices is a valid uniform separation from the flag threshold, not a claim that the constant \(\pi^2/4\) is the sharp bound for each prescribed number of vertices. The result does not characterize equality for Winter's higher-dimensional theorem. Novelty is assessed against inspected sources and searches, not established merely by an unsuccessful search; unavailable or unindexed equivalent results remain possible.

## References
1. M. Winter, *A relation between Mahler volume and flag number for convex polytopes*, arXiv:2610.09990v1 (2026), https://arxiv.org/html/2610.09990v1.
2. K. J. Böröczky, E. Makai Jr., M. Meyer, S. Reisner, *Volume product of planar polar convex bodies—lower estimates with stability*, arXiv:1507.01481v1, https://arxiv.org/html/1507.01481v1.
3. M. Meyer and S. Reisner, *On the volume product of polygons*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 81 (2011), 93–100, DOI 10.1007/s12188-011-0054-3.
4. Classical Brunn–Minkowski and Blaschke–Santaló inequalities for planar convex bodies (used in the five-or-more-vertices case).
