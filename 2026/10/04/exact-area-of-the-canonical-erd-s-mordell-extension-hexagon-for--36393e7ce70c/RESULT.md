# Exact area of the canonical Erdős–Mordell extension hexagon for an equilateral triangle
## Finding
For the equilateral triangle \(A=(0,\sqrt3)\), \(B=(-1,0)\), \(C=(1,0)\), consider the three one-vertex inequalities used by Malešević, Petrović, Obradović and Popkonstantinović to extend the Erdős–Mordell inequality to the plane. Let \(M\) be their canonical intersection of the three corner areas containing the original triangle. Then \(M\) is exactly the hexagon with cyclic vertices
\[
A,\quad U=\left(\frac{{2(\sqrt6-1)}}5,\frac{{\sqrt3+2\sqrt2}}5\right),\quad C,\quad D=\left(0,\frac{{3\sqrt3-4\sqrt2}}5\right),\quad B,\quad U'=\left(-\frac{{2(\sqrt6-1)}}5,\frac{{\sqrt3+2\sqrt2}}5\right).
\]
Its area is
\[
\operatorname{{area}}(M)=\frac45(3\sqrt2-\sqrt3),
\]
while \(\operatorname{{area}}(ABC)=\sqrt3\). Therefore
\[
\frac{{\operatorname{{area}}(M)}}{{\operatorname{{area}}(ABC)}}=\frac45(\sqrt6-1)=1.159591794226542\ldots.
\]
Since the source proves \(M\subset E\subset E'\), this gives the exact analytic equilateral certificate
\[
\operatorname{{area}}(E')\ge \frac45(\sqrt6-1)\operatorname{{area}}(ABC).
\]

## Assumptions and scope
Distances to sides mean distances to the supporting lines, as in the cited extension paper. The set \(M\) is the specific polygon obtained by choosing, at each vertex, the corner component of the corresponding one-vertex inequality that contains the triangle, then intersecting those three components. The statement concerns this canonical guaranteed subregion. It does not assert that \(M=E\) or \(M=E'\), and it does not compute the full Erdős–Mordell-curve area.

## Proof
Because the triangle is equilateral, the source's inequality at \(A\) becomes
\[
R_A\ge r_b+r_c.
\]
Put \(X=x\) and \(Y=y-\sqrt3\). The two side-line distances adjacent to \(A\) are
\[
r_b=\frac{|Y+\sqrt3X|}{2},\qquad r_c=\frac{|Y-\sqrt3X|}{2}.
\]
Using \((|u+v|+|u-v|)/2=\max(|u|,|v|)\), the inequality is
\[
\sqrt{{X^2+Y^2}}\ge \max(|Y|,\sqrt3|X|),
\]
which is equivalent to \(|Y|\ge\sqrt2|X|\). The corner component containing the triangle is therefore
\[
y-\sqrt3\le-\sqrt2|x|.
\]
Equivalently it is the intersection of the two half-planes
\[
y+\sqrt2x\le\sqrt3,\qquad y-\sqrt2x\le\sqrt3.
\]

The corresponding corner conditions at \(B\) and \(C\) are obtained by rotations through \(120^\circ\) and \(240^\circ\) about the centroid. Equivalently, if \(u_V\) is the unit median direction from a vertex \(V\) toward the centroid and \(v_V\) is a perpendicular unit vector, the inward corner is
\[
(P-V)\cdot u_V\ge\sqrt2\,|(P-V)\cdot v_V|.
\]
Thus \(M\) is the intersection of six explicit half-planes. Solving consecutive boundary-line pairs gives precisely the six displayed vertices. Direct substitution shows that each vertex satisfies all six inequalities, so no additional boundary intersection truncates the polygon.

The shoelace formula in cyclic order \(A,U,C,D,B,U'\) gives
\[
\operatorname{{area}}(M)=\frac{12\sqrt2-4\sqrt3}{5}=\frac45(3\sqrt2-\sqrt3).
\]
Division by \(\sqrt3\) yields \(\frac45(\sqrt6-1)\).

## Verification
The bundled `verify.py` performs exact arithmetic in the biquadratic number field \(\mathbb Q(\sqrt2,\sqrt3)\). It checks the six half-plane incidences, reconstructs the six active boundary intersections, evaluates the shoelace area exactly, and verifies the stated area ratio. The proof itself is analytic; the program is a finite replay of the displayed algebra, not evidence for an unproved infinite assertion.

## Relationship to prior work
The 2012 preprint arXiv:1204.1003 introduces the three one-vertex extension regions, defines \(M\) as the intersection of the corner areas containing the original triangle, proves \(M\subset E\), and states only that \(M\) has quadrilateral or hexagonal shape. It also introduces \(E'\), the component bounded by the Erdős–Mordell curve that contains the triangle, and poses an area-gap problem, conjecturing that the finite-area extremal value is determined by the equilateral case.

The later arXiv:1309.7927 studies the full Erdős–Mordell curve and numerically estimates the equilateral \(E'\)-area ratio as part of a large computational test. That is a different object and a stronger numerical area enlargement; it does not imply the exact analytic area of the canonical polygon \(M\). Targeted searches for the exact radical ratio and for an equilateral corner-area hexagon did not locate a prior statement of this formula.

## Limitations
The result gives an exact, rigorous lower-area certificate for the equilateral \(E'\), not the exact area of \(E'\). It therefore neither proves nor disproves the universal positive-gap problem and does not establish that the equilateral triangle minimizes the full \(E'\)-area ratio. A residual originality risk remains for unindexed or differently phrased literature, and the 2013 curve paper could not be exhaustively searched as full structured text in this run; its abstract, extracted methodological passages, and conclusion were compared materially.

## References
1. B. Malešević, M. Petrović, M. Obradović, B. Popkonstantinović, “On the Extension of the Erdös–Mordell Type Inequalities,” arXiv:1204.1003v1, first public 2012-04-04; later Mathematical Inequalities & Applications 17 (2014), 269–281, DOI 10.7153/mia-17-22. Primary MSC 51M16.
2. B. D. Banjac, B. J. Malešević, M. M. Petrović, M. Đ. Obradović, “A Computer Verification of a Conjecture About Erdös-Mordell Curve,” arXiv:1309.7927v1, first public 2013-09-30.
