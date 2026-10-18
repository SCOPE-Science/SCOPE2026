# A sharp shallow-apex transition for minimum-radius cylinders of triangular pyramids

## Finding
Let \(Q=\operatorname{conv}\{a,b,c\}\subset\mathbb R^2\times\{0\}\) be an arbitrary nondegenerate triangle, and let \(q\) lie strictly inside \(Q\). For every \(h\ge0\), set
\[
T_h=\operatorname{conv}\bigl(Q\cup\{q+h e_3\}\bigr).
\]
Write \(A=\operatorname{area}(Q)\), \(L\) for its longest side length, and \(w=2A/L\) for its minimum planar width. For each side \(e\) of length \(L\), denote by \(\lambda_e\in(0,1)\) the barycentric coordinate of \(q\) at the vertex opposite \(e\), and define
\[
H_e=w\sqrt{\lambda_e(1-\lambda_e)},\qquad
H_* =\max_{e:\,|e|=L} H_e.
\]
Let \(R_2(T_h)\) be the least radius of an unrestricted infinite circular cylinder containing \(T_h\), with the cylinder axis free to tilt and translate. Then the **sharp plateau theorem** is
\[
R_2(T_h)=\frac w2\quad\Longleftrightarrow\quad 0\le h\le H_*;
\qquad R_2(T_h)>\frac w2\quad\text{when }h>H_*.
\]
Moreover, for every \(0\le h\le H_*\), **all** minimizing cylinder axes are the horizontal midlines of the width-\(w\) strips parallel to precisely those longest sides \(e\) for which \(h\le H_e\). In particular, the optimal-axis set can shrink as \(h\) increases while the optimal radius stays constant.

## Assumptions and scope
All lengths are ordinary Euclidean lengths. The triangle is noncollinear; the apex projection \(q\) is strictly interior, but need not be a centroid or a circumcenter. The height is nonnegative. At \(h=0\), the family has the flat limiting triangle. An infinite circular cylinder of radius \(r\) about a line \(\ell\) is \(\{x\in\mathbb R^3:\operatorname{dist}(x,\ell)\le r\}\). There are no restrictions on the axis or on which vertices touch its boundary. The theorem identifies the exact parameter range in which the base triangle's unavoidable cylinder radius persists; it does not give the optimal radius or all axes in the regime \(h>H_*\).

## Proof
**1. Universal lower bound.** Fix any unit cylinder-axis direction \(u\). Its perpendicular plane \(u^\perp\) contains a horizontal unit direction \(v\), because two planes through the origin in \(\mathbb R^3\) have a nonzero intersection. Orthogonal projection \(\pi_u\) onto \(u^\perp\) preserves scalar products with \(v\): \(v\cdot\pi_u(x)=v\cdot x\). Thus the projected base triangle has width \(w_Q(v)\ge w\) in direction \(v\). A radius-\(r\) disk in \(u^\perp\) has width \(2r\), hence every enclosing cylinder has \(r\ge w/2\).

**2. Exact equality rigidity.** For a triangle, the minimum directional width equals its smallest altitude, namely \(w=2A/L\). Its minimizing horizontal directions are exactly the inward or outward normals to its longest sides. To justify the latter assertion without a generic-position assumption, partition the unit-direction circle into the arcs on which the support-maximizing and support-minimizing vertices are fixed. On any open arc, \(w_Q(v)=(p_i-p_j)\cdot v>0\), so, parametrizing \(v\) by angle \(\theta\), the width has second derivative \(-w_Q(v)<0\). It has no interior local minimum. Arc endpoints are support ties at a side, and the corresponding values are that side's altitude. Thus precisely the normals to sides with minimal altitude, equivalently maximal length, minimize width.

Suppose some cylinder attains \(r=w/2\). Choose the horizontal \(v\in u^\perp\) from step 1. Equality must hold in the projected width, so \(v\) is normal to a longest side \(e=[b,c]\), and the projections of \(b,c\) have the same extreme \(v\)-coordinate. A disk of radius \(w/2\) whose width is exactly \(w\) has exactly one point in each of its two extreme supporting lines normal to \(v\). Therefore \(\pi_u(b)=\pi_u(c)\). The kernel of \(\pi_u\) is \(\mathbb Ru\), so \(u\) is parallel to \(c-b\), which is horizontal. In particular, **every equality axis** is horizontal and parallel to a longest side; tilted axes cannot attain the lower bound.

**3. Forced center and apex test.** Fix a longest side \(e\), choose the inward horizontal unit normal \(n_e\), and take the origin of the normal coordinate on the line containing \(e\). Orthogonal projection along the direction of \(e\) sends its endpoints to \((0,0)\), and the opposite base vertex to \((w,0)\), in \((n_e,z)\)-coordinates. The unique radius-\(w/2\) disk containing these projected endpoints has center \((w/2,0)\). Equivalently, its cylinder axis lies at normal coordinate \(w/2\), at height zero, and is parallel to \(e\). As \(q\) has opposite-vertex barycentric weight \(\lambda_e\), the lifted apex projects to \((\lambda_e w,h)\). Its squared distance to the forced disk center is
\[
(\lambda_e w-w/2)^2+h^2.
\]
The apex is contained if and only if this is no greater than \(w^2/4\), or equivalently
\[
h^2\le w^2\lambda_e(1-\lambda_e)\quad\Longleftrightarrow\quad h\le H_e.
\]
Convexity of the cylinder shows that containing the four vertices is equivalent to containing their convex hull. Hence the stated list of optimal axes attains \(w/2\) exactly when at least one corresponding inequality holds.

**4. Strictness beyond the threshold.** For each unoriented axis direction \(u\), the optimal radius of its projected vertex set is the radius of that finite set's minimum enclosing disk. This radius depends continuously on \(u\) (indeed, continuously under moving the four projected points). The unoriented direction space is compact, so the unrestricted cylinder minimum is attained. If \(h>H_*\), step 3 rules out every possible equality axis from step 2; therefore the attained radius is strictly greater than \(w/2\). The converse and the complete equality classification follow from steps 1–3. \(\square\)

## Verification
The argument is exact for every admissible real triangle, interior point and height; it does not extrapolate from finite numerical sampling. Two independent rational-coordinate sanity checks demonstrate the apex boundary equation. For \(a=(0,0,0)\), \(b=(4,0,0)\), \(c=(1,2,0)\), the longest side is \([a,b]\), \(A=4\), \(w=2\), and \(R_2(T_h)=1\) exactly up to \(h=2\sqrt2/3\) when \(q=(5/3,2/3,0)\), and up to \(h=3/5\) when \(q=(1,1/5,0)\). The identity at threshold is \((q_y-1)^2+H_*^2=1\) in each case. For a unit-circumradius equilateral base and apex above the centroid, \(w=3/2\), \(\lambda_e=1/3\) for all three sides, and the sharp cutoff is \(H_*=1/\sqrt2\), with \(R_2=3/4\) throughout the plateau. The enclosed `check_examples.py` repeats the exact squared-distance checks using rational arithmetic; it is corroborative, not a replacement for the proof.

## Relationship to prior work
Brandenberg and Theobald formulate the smallest enclosing cylinder of a simplex as an outer radius and give general algebraic reductions and contact alternatives (arXiv:math/0211344, Sections 2–3). Petitjean gives algebraic formulations for four arbitrary points and explicit analysis for regular tetrahedra and a symmetric five-vertex trigonal bipyramid (arXiv:1008.5259, Sections 3–6). His Theorem 5 detects a symmetric-bipyramid circumscribed-cylinder boundary at half-height \(1/\sqrt2\), numerically matching the regular one-apex threshold, but does not state the unrestricted minimum-radius plateau and all-axis classification for arbitrary triangular pyramids. Maehara analyzes congruent embeddings of a regular tetrahedron in a cylinder (Yokohama Mathematical Journal 55 (2010), 171–177). These results establish the natural broader problem, but the inspected portions do not give the exact barycentric sharp cutoff and classification of *all* minimizing axes for arbitrary shallow triangular pyramids. In particular, a minimum-width formula for a pyramid concerns a different functional: for \(h<w\) the pyramid's minimum width is at most \(h\), whereas its minimum enclosing cylinder radius on the plateau is \(w/2\).

## Limitations
No formula is claimed for \(R_2(T_h)\) when \(h>H_*\); only strict increase above the flat lower bound is established. The premise \(q\in\operatorname{relint}Q\) is essential to the statement as written. Independently reviewing the proof and checking further potentially overlapping literature remains desirable. The theorem makes no statement about finite-length cylinders or minimizing cylinder surface area/volume.

## References
1. R. Brandenberg and T. Theobald, *Algebraic Methods for Computing Smallest Enclosing and Circumscribing Cylinders of Simplices*, arXiv:math/0211344 (first posted 21 November 2002), https://arxiv.org/abs/math/0211344.
2. M. Petitjean, *About the Algebraic Solutions of Smallest Enclosing Cylinders Problems*, arXiv:1008.5259 (first posted 31 August 2010), https://arxiv.org/abs/1008.5259.
3. H. Maehara, *On Congruent Embeddings of a Tetrahedron into a Circular Cylinder*, Yokohama Mathematical Journal 55 (2010), 171–177, https://ymj.ynu.ac.jp/wp/wp-content/uploads/2022/03/N0907-A.pdf.
4. E. Schömer, J. Sellen, M. Teichmann and C.-K. Yap, *Smallest Enclosing Cylinders*, Algorithmica 27 (2000), 170–186, doi:10.1007/s004530010011.
