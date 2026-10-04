# The cyclic-quadrilateral case of the tangent-line Erdős–Mordell conjecture
## Finding
Let \(A_1A_2A_3A_4\) be a strictly convex cyclic quadrilateral with circumradius \(R>0\), and let \(P\) be an interior point. Indices are taken modulo \(4\). Define \(d_i\) as the Euclidean distance from \(P\) to the supporting line of side \(A_iA_{{i+1}}\), and \(D_i\) as the distance from \(P\) to the tangent line of the circumcircle at \(A_i\). Then
\[
\sum_{{i=1}}^4 D_i\ge \sqrt{{2}}\sum_{{i=1}}^4 d_i.
\]
The constant \(\sqrt{{2}}=\sec(\pi/4)\) is sharp. For interior \(P\), equality holds if and only if \(A_1A_2A_3A_4\) is a square; in a square equality holds for every interior point.

When consecutive tangents meet in a finite tangential quadrilateral, its sides are precisely these tangent lines up to cyclic relabelling. Thus the theorem proves the \(n=4\) case of the cyclic-polygon/tangential-polygon conjecture posed publicly in 2016. The supporting-line formulation also remains meaningful when two consecutive tangents are parallel.

## Assumptions and scope
The four vertices are distinct and appear in their cyclic order, so the quadrilateral is strictly convex. Distances are distances to supporting lines, which is the standard side-distance convention in Erdős–Mordell inequalities. The point \(P\) is interior for the equality classification; the inequality itself extends to boundary points by continuity. No claim is made here for polygons with \(n\ge5\).

## Proof
For a tangent line to a circle of radius \(R\) with outward unit normal \(u_i\), every point of the cyclic quadrilateral lies in the closed circumdisk, so
\[
D_i(P)=R-u_i\cdot P,
\]
which is affine in \(P\). On the quadrilateral, the sign of the signed distance to each side line is fixed, so each \(d_i(P)\) is also affine. Hence
\[
F(P)=\sum_{{i=1}}^4D_i(P)-\sqrt2\sum_{{i=1}}^4d_i(P)
\]
is affine on the quadrilateral. It is therefore enough to show \(F(A_j)\ge0\) at the four vertices.

Write the four consecutive central arc gaps as \(2\alpha,2\beta,2\gamma,2\delta\), where
\[
\alpha,\beta,\gamma,\delta>0,\qquad \alpha+\beta+\gamma+\delta=\pi.
\]
At \(A_1\), elementary chord and tangent-distance formulas give
\[
\sum_{{i=1}}^4D_i(A_1)=2R\left(\sin^2\alpha+\sin^2(\alpha+\beta)+\sin^2\delta\right),
\]
and
\[
\sum_{{i=1}}^4d_i(A_1)=2R\sin(\alpha+\beta)\left(\sin\alpha+\sin\delta\right).
\]
Set \(x=\sin\alpha\), \(y=\sin(\alpha+\beta)\), and \(z=\sin\delta\). Dividing the vertex defect by \(2R\) leaves
\[
E=x^2+y^2+z^2-\sqrt2\,y(x+z).
\]
It has the exact sum-of-squares decomposition
\[
2E=(x-z)^2+(x+z-\sqrt2\,y)^2\ge0.
\]
Thus \(F(A_1)\ge0\). Cyclic relabelling gives the same conclusion at every vertex, and affinity gives \(F(P)\ge0\) throughout the quadrilateral.

For equality, suppose \(P\) is interior and \(F(P)=0\). Its barycentric coordinates with respect to the convex quadrilateral can be chosen strictly positive, while all four vertex values of \(F\) are nonnegative; hence all four vertex values vanish. At \(A_1\), the first square above forces \(\sin\alpha=\sin\delta\). Since \(\alpha+\delta<\pi\), this implies \(\alpha=\delta\). At \(A_2\), the analogous condition gives \(\beta=\alpha\), and continuing cyclically gives
\[
\alpha=\beta=\gamma=\delta=\frac{\pi}{4}.
\]
Thus the quadrilateral is a square. Conversely, for a square the four tangent normals sum to zero and the four side normals sum to zero, so
\[
\sum_iD_i=4R,\qquad \sum_i d_i=2\sqrt2\,R,
\]
for every interior \(P\), giving equality identically.

## Verification
The proof is analytic and does not depend on finite enumeration. The bundled `verify.py` expands the decisive sum-of-squares identity over the exact quadratic ring \(\mathbb{{Q}}(\sqrt2)\) and independently checks the direct coordinate formulas on a deterministic family of cyclic quadrilaterals and interior points. Its finite coordinate checks are only smoke tests; the affine reduction and sum-of-squares identity establish the quantified theorem.

## Relationship to prior work
Dao, Nguyen, and Pham proved the corresponding tangent-line inequality for triangles. Dao then publicly posed the cyclic \(n\)-gon extension on July 24, 2016, with factor \(\sec(\pi/n)\), explicitly identifying only the triangle case as proved. The present theorem supplies the first polygonal case beyond triangles, \(n=4\), and proves the sharp factor \(\sec(\pi/4)=\sqrt2\).

Classical polygonal Erdős–Mordell extensions of Lenhard and the weighted polygon theorem of Gueron–Shafrir compare vertex distances or angle-bisector lengths with side distances; they do not use distances to the circumcircle tangents and therefore do not imply this statement. A later full-text paper by Tran develops weighted versions of the Dao–Nguyen–Pham inequality but states and proves them for a triangle \(ABC\) and its three circumcircle tangents. It does not cover cyclic quadrilaterals.

## Limitations
This result does not address \(n\ge5\). The 2016 Forum Geometricorum article itself was not directly retrievable in the literature check, although its bibliographic record, classification, and the 2016 conjecture page identify it as the triangle case; the later arXiv full text reproduces the Dao–Nguyen–Pham triangle formulation. Searches found no quadrilateral theorem with the present tangent-line/side-line implication, but unindexed or differently phrased literature remains a residual originality risk.

## References
1. O. Thanh Đào, “An inequality in cyclic polygon and tangential polygon,” MathOverflow question 244984, first posted 2016-07-24.
2. T. O. Dao, N. T. Dung, P. N. Mai, “A strengthened version of the Erdős-Mordell inequality,” Forum Geometricorum 16 (2016), 317–321; zbMATH Open 1354.51019, MR 3556993.
3. Q. H. Tran, “A family of weighted Erdős-Mordell inequality and applications,” arXiv:2105.07885; Journal of Geometry 112 (2021), article 33.
4. S. Gueron, I. Shafrir, “A Weighted Erdős-Mordell Inequality for Polygons,” American Mathematical Monthly 112 (2005), 257–264, DOI 10.1080/00029890.2005.11920191.
5. F. F. Abi-Khuzam, “A trigonometric inequality and its geometric applications,” Mathematical Inequalities & Applications 3 (2000), 437–442.
