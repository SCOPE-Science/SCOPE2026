# Vertex rigidity and the exact maximum perimeter of parallelograms in centrally symmetric cyclic polygons

## Finding
Let \(K\) be a nondegenerate centrally symmetric cyclic Euclidean \(n\)-gon (even \(n\ge4\)) whose symmetry center is the origin and whose vertices \(V\) lie on the circle of radius \(R>0\). Write \(L(v)=\mathbb R v\) for the unoriented diameter line through a vertex \(v\). For two distinct vertex lines, denote their acute angular separation by \(\alpha(L,L')\in(0,\pi/2]\) and define
\[
\eta(K)=\min_{L\ne L'}\left(\frac{\pi}{2}-\alpha(L,L')\right).
\]
Then the largest perimeter of a parallelogram contained in \(K\) equals the largest perimeter of a rectangle contained in \(K\), namely
\[
\boxed{\max_{Q\subseteq K,\ Q\text{ a parallelogram}}\operatorname{Per}(Q)=\max_{Q\subseteq K,\ Q\text{ a rectangle}}\operatorname{Per}(Q)=4\sqrt{2}R\cos\left(\frac{\eta(K)}{2}\right).}
\]
Every maximizing parallelogram is a rectangle centered at the circle center. Its corners are precisely two antipodal pairs of vertices \(\{v,-v,w,-w\}\), where \(\alpha(L(v),L(w))=\pi/2-\eta(K)\); conversely, all such pairs maximize. The exact maximizing value and all its pairs can be located using \(O(n)\) arithmetic operations, given the cyclic vertex order.

In particular, a regular even \(n\)-gon has largest inscribed rectangle perimeter
\[
\boxed{P_{\max}(n)=\begin{cases}4\sqrt{2}R,&n\equiv0\pmod4,\\4\sqrt{2}R\cos(\pi/(2n)),&n\equiv2\pmod4.\end{cases}}
\]

## Assumptions and scope
The polygon is the convex hull of its vertices and is full-dimensional. All vertices lie on the same circle, centered at the center of symmetry. In particular, the polygon lies in the closed disk of radius \(R\). An inscribed rectangle or parallelogram means a complete, nondegenerate Euclidean quadrilateral contained in \(K\), with arbitrary position and orientation. Perimeter is ordinary Euclidean boundary length. Vertex order is the cyclic order, not an angularly unsorted point cloud. The result does not assert this rigidity for arbitrary centrally symmetric polygons with nonconcyclic vertices or for arbitrary convex polygons.

## Proof
**1. Centralization without loss.** Let a parallelogram \(Q\subseteq K\) have center \(c\) and four corners \(c\pm u\), \(c\pm v\) with linearly independent \(u,v\). The reflection of each original corner through the origin is in \(K\). The midpoint of \(c+u\) and \(-(c-u)\) is \(u\), so \(u\in K\); similarly \(-u,v,-v\in K\). Hence the centered parallelogram with corners \(\pm u,\pm v\) lies in \(K\) and has the same four edge vectors, and therefore the same perimeter. Consequently, the maximum can be sought among centered parallelograms.

**2. Reduction to polygon vertices.** Their perimeter is
\[
F(u,v)=2\big(\lVert u-v\rVert_2+\lVert u+v\rVert_2\big),\qquad u,v\in K.
\]
For each fixed \(v\), this is convex in \(u\), and likewise in \(v\). Expressing both arguments as convex combinations of polygon vertices and applying Jensen's inequality twice yields
\[
F(u,v)\le\max_{a,b\in V}F(a,b).
\]
For a pair of distinct diameter lines \(L(a)\ne L(b)\), the four points \(\pm a,\pm b\) form a nondegenerate rectangle because the diagonals bisect each other and have equal lengths \(2R\). Thus the right side is attained by an inscribed rectangle. Since at least two distinct vertex lines exist, its value exceeds \(4R\); denote the common maximum by \(M>4R\). For collinear \(a,b\) the value is \(4R\), so such pairs cannot maximize.

**3. Equality forces vertices.** Fix \(v\in K\), and set \(g_v(u)=\lVert u-v\rVert_2+\lVert u+v\rVert_2\). If \(v=0\), then \(F(u,v)=4\lVert u\rVert_2\le4R<M\). If \(v\ne0\), equality in Jensen's inequality for \(g_v\) on any nondegenerate segment \([u_1,u_2]\) requires simultaneous equality in each of the two Euclidean triangle inequalities. This forces the line through \(u_1,u_2\) to contain both \(v\) and \(-v\); hence that line is \(\mathbb Rv\). On that line the formula simplifies to
\[
F(u,v)=4\max(\lVert u\rVert_2,\lVert v\rVert_2)\le4R<M.
\]
Therefore no nonvertex argument can occur in an attaining pair, since expressing it as a nontrivial convex combination of vertices would contradict strictness (or would give a collinear pair below \(M\)). Applying this reasoning separately to \(u\) and \(v\), every *centered* maximizing parallelogram has \(u,v\in V\) on distinct diameter lines.

**4. Equality also forces the original center.** Suppose an uncentered parallelogram with center \(c\) attains \(M\). By step 1 its centered counterpart does also, so step 3 gives \(\lVert u\rVert_2=R\). Both original corners \(c+u,c-u\) belong to the circumdisk. The parallelogram identity gives
\[
2\lVert c\rVert_2^2+2R^2=\lVert c+u\rVert_2^2+\lVert c-u\rVert_2^2\le2R^2,
\]
whence \(c=0\). Thus the equality classification concerns *all* maximizers, not only centered ones.

**5. Angle formula.** For distinct vertex lines with acute angle \(\alpha\in(0,\pi/2]\), the associated rectangle has side lengths \(2R\sin(\alpha/2)\) and \(2R\cos(\alpha/2)\). Its perimeter is
\[
4R\big(\sin(\alpha/2)+\cos(\alpha/2)\big)=4\sqrt2 R\cos\big((\pi/2-\alpha)/2\big).
\]
This increases strictly with \(\alpha\) in the stated range, so choosing the pair nearest to perpendicular proves the formula and the equality classification. For a regular even \(n\)-gon, its vertex-diameter lines form a uniform grid modulo \(\pi\); the smallest angular distance to perpendicular is zero when \(4\mid n\) and \(\pi/n\) when \(n\equiv2\pmod4\). This yields the displayed mod-four formula.

**6. Linear selection.** Sort the \(n/2\) distinct vertex-line angles on the projective circle of circumference \(\pi\); the supplied cyclic order provides this ordering in linear time (each antipodal pair is processed once). Append a translated copy of the angle list by \(\pi\). For each original angle, find the predecessor and successor around its target offset by \(\pi/2\). A monotonically increasing pointer traverses the duplicated list only once. These two neighbors attain the minimum circular angular error for that angle, and all globally optimal pairs occur among these \(O(n)\) candidates. Each has constant-time length and angle evaluation; ties may be retained. The total selection cost is \(O(n)\).

## Verification
The standalone file `verify.py` checks the angle-pair linear scan against exhaustive pair enumeration for regular even polygons through 120 vertices and for randomly generated centrally symmetric cyclic polygons. Additional sampled convex combinations verify the separately convex vertex upper bound numerically, but these finite checks are not an infinite-dimensional certificate. Run `python3 verify.py`, which reports `VERIFY_OK 9862` with the included deterministic inputs. The six proof steps above establish the result for every stated polygon without relying on those experiments.

## Relationship to prior work
Cabello, Cheong, Knauer and Schlipf (arXiv:1405.1223, sections on maximizing perimeter) provide an \(O(n^3)\)-time method for the maximum-perimeter rectangle in an arbitrary convex polygon. Choi, Lee and Ahn later study maximum-area and maximum-perimeter rectangles in polygons, with cubic-time methods for general convex polygons. Those more general algorithms are not equivalent to the present exact vertex-pair formula, all-equality rigidity or linear method for the centrally symmetric cyclic subclass.

The published result *Exact maximum-area rectangles in every regular even polygon* determines area, rather than perimeter. Its stated limitations exclude maximum-perimeter rectangles. Maximal area does not directly establish maximal perimeter, nor does that regular-only finding establish rigidity among inscribed parallelograms for arbitrary centrally symmetric cyclic polygons. The present result uses the added circle condition and a separate convexity/equality argument; the area statement alone does not imply it.

## Limitations
The proof uses Euclidean distance, central symmetry and a common circumcircle. It gives neither a comparable classification for nonsymmetric cyclic polygons nor a maximum-perimeter result for centrally symmetric polygons with unequal vertex radii. The linear scan assumes cyclically ordered vertices and exact real arithmetic; obtaining robust finite-precision implementations requires additional attention to angular ties. An equivalent historical statement in poorly indexed computational or classical geometry literature is a remaining priority risk. No independent mathematical audit is claimed.

## References
S. Cabello, O. Cheong, C. Knauer, and L. Schlipf, “Finding Largest Rectangles in Convex Polygons,” arXiv:1405.1223 (initial public version, 2014-05-06), https://arxiv.org/abs/1405.1223.

Y. Choi, S. Lee, and H.-K. Ahn, “Maximum-area and maximum-perimeter rectangles in polygons,” Computational Geometry 95 (2021), 101710, DOI:10.1016/j.comgeo.2020.101710.

“Exact maximum-area rectangles in every regular even polygon,” published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-maximum-area-rectangles-in-every-regular-even-polygon--10bad5e59427.
