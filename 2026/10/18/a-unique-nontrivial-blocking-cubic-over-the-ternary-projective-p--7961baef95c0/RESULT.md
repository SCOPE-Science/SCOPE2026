# A unique nontrivial blocking cubic over the ternary projective plane

## Finding
Let \(k=\mathbf F_3\). A ternary cubic \(F\in k[X,Y,Z]\) is **blocking** if every \(k\)-rational line of \(\mathbf P^2_k\) contains a rational point of \(\{F=0\}\). Among the \(29{,}524\) nonzero ternary cubic forms modulo nonzero scalars, precisely **\(936\)** are blocking and have no \(k\)-linear factor. Every one of these defines a geometrically smooth cubic with exactly six \(k\)-points, and all are projectively equivalent over \(k\). One representative is
\[
F_*=X^3+Y^3+Z^3-(X+Y+Z)(XY+XZ+YZ)+XYZ.
\]
Its stabilizer in \(\operatorname{PGL}_3(k)\) is the coordinate-permutation group \(S_3\), of order \(6\). Equivalently, **every irreducible blocking plane cubic over \(k\) is geometrically smooth and belongs to this one projective class**. The count \(936\) concerns projective equations, not abstract isomorphism classes.

## Assumptions and scope
The ground field is exactly \(\mathbf F_3\), and smoothness is geometric over its algebraic closure. Projective equivalence means the action of \(\operatorname{PGL}_3(\mathbf F_3)\) on homogeneous cubic equations, modulo nonzero scalar multiplication. A rational line divides a cubic form if and only if the curve contains all four rational points of that line: the forward direction is immediate; conversely, restricting a homogeneous cubic to a rational projective line gives a binary cubic, which cannot have four distinct roots unless it vanishes identically. An irreducible cubic over \(k\) has no \(k\)-linear factor.

## Proof
**1. The finite incidence lemma.** The plane \(\mathbf P^2(k)\) has thirteen points and thirteen lines, with four points on each line. Its inclusion-minimal blocking point sets are exactly its thirteen four-point lines and the \(234\) *vertexless triangles*: choose three nonconcurrent rational lines, remove their three pairwise intersection points, and take the other six points on the chosen lines. One exact verification of this small combinatorial lemma enumerates the \(2^{13}\) subsets of the normalized projective triples and tests incidence with all thirteen line equations. The standalone `verify.py` implements the complete, reproducible finite check, including the identification of all \(234\) triangles. There are \(\binom{13}{3}-13\binom43=234\) triples of nonconcurrent lines, and no two define the same six-point set; equivalently, these are the \(234\) six-point minimal blockers in the incidence enumeration. This incidence classification is also consistent with the published classification of small-order minimal blocking sets cited below.

**2. Interpolation through a vertexless triangle.** Let a blocking cubic have no rational line factor. Its rational point set must contain an inclusion-minimal blocker. It cannot contain a full rational line, so it contains a vertexless triangle. After an invertible projective change of coordinates we may take the triangle to be
\[
B=\{[0:1:\pm1],[1:0:\pm1],[1:\pm1:0]\}.
\]
The six vanishing conditions on an arbitrary cubic give the following complete four-dimensional family, with \(A,B_0,C,G\in k\):
\[
\begin{aligned}
F={}&A(X^3-XY^2-XZ^2)+B_0(Y^3-X^2Y-YZ^2)\\
&+C(Z^3-X^2Z-Y^2Z)+GXYZ.
\end{aligned}
\]
The symbol \(B_0\) is a coefficient and is distinct from the point set \(B\). The family has \((3^4-1)/2=40\) distinct projective equations.

**3. Elimination of extra rational points and rational factors.** The seven rational points outside \(B\) are the three coordinate vertices and the four points \([1:\varepsilon:\delta]\), with \(\varepsilon,\delta\in\{1,-1\}\). Every one of the four latter points lies on a rational line containing three points of \(B\). If a cubic through \(B\) also contains such a point, it has four collinear rational zeros, so the line divides its equation.

Suppose \(A=0\). If either \(B_0=0\) or \(C=0\), the defining equation visibly has a coordinate-line factor. If both are nonzero, evaluation at the four latter points gives the condition
\[
G=B_0\delta+C\varepsilon.
\]
The four choices of signs on the right range over all of \(k\), so an extra point and hence a line factor are unavoidable. The same reasoning applies cyclically. Consequently, any blocking cubic without a rational line factor has \(AB_0C\ne0\).

Rescaling the three coordinates by their signs reduces the equation to the same family with \(A=B_0=C=1\) and \(g=GAB_0C\in k\). At each of the four remaining points its value is
\[
-1-\varepsilon-\delta+g\varepsilon\delta.
\]
All four values are nonzero **if and only if \(g=1\)**: \(g=0\) vanishes when \((\varepsilon,\delta)=(1,1)\), and \(g=-1\) vanishes when \((\varepsilon,\delta)=(1,-1)\). Thus the only no-line-factor possibilities through the fixed triangle are the four forms with \(A,B_0,C\in\{\pm1\}\) and \(G=AB_0C\), modulo a common nonzero scalar. These are carried to \(F_*\) by diagonal sign changes and have precisely the six rational zeros \(B\).

**4. Geometric smoothness.** Put \(S=X+Y+Z\). Direct differentiation in characteristic three gives
\[
\frac{\partial F_*}{\partial X}=X^2-S^2,\qquad
\frac{\partial F_*}{\partial Y}=Y^2-S^2,\qquad
\frac{\partial F_*}{\partial Z}=Z^2-S^2.
\]
If all partial derivatives vanish at a projective point over \(\overline{k}\), then \(S\ne0\) and \((X,Y,Z)=S(\varepsilon_1,\varepsilon_2,\varepsilon_3)\), with each sign equal to \(1\) or \(-1\). The defining equality for \(S\) forces exactly one negative sign. By symmetry, evaluation at \((-S,S,S)\) gives \(F_*=S^3\ne0\). Thus there is no geometric singular point of \(\{F_*=0\}\), proving smoothness and geometric irreducibility.

**5. Counting and automorphisms.** Each of the \(234\) vertexless triangles supports exactly four no-line-factor smooth cubics, and each such cubic has precisely its own six rational points as that triangle. The \(234\cdot4=936\) equations are therefore distinct. The action of \(\operatorname{PGL}_3(k)\) is transitive on vertexless triangles; the four forms above one triangle are equivalent by diagonal sign changes. Hence there is one orbit. Its stabilizer has order
\[
\frac{|\operatorname{PGL}_3(\mathbf F_3)|}{936}
=\frac{(27-1)(27-3)(27-9)}{2\cdot936}=6.
\]
The symmetric equation \(F_*\) is fixed by all six permutations of the coordinates, so its full projective stabilizer is exactly \(S_3\). This completes the classification.

## Verification
Run `python3 verify.py` with a standard Python 3 installation; no additional packages or external datasets are required. The program independently enumerates all \(8192\) point subsets to establish the incidence lemma, the \(40\) cubics through the fixed vertexless triangle, and all \(29{,}524\) normalized cubic equations. It verifies that \(4940\) cubic equations are blocking and that exactly \(936\) of these have no rational line factor; all \(936\) have six rational points. The projective-count and stabilizer checks also pass. The all-characteristics geometric-smoothness step is the symbolic gradient argument in the proof, not a finite-field sampling claim.

## Relationship to prior work
Asgarli–Ghioca–Yip (2022/2023), Example 3.5, supplies a single smooth blocking cubic over \(\mathbf F_3\); Theorem 1.3 excludes irreducible blocking cubics when the field has at least five elements. It does not classify every such cubic over \(\mathbf F_3\), count equations, or determine the stabilizer. Coolsaet–Botteldoorn–Fack (2022) classify minimal blocking *point sets*, not the smooth cubic equations through them. The tangent-filling problem of Asgarli–Ghioca (2023) is different: it asks that *tangent lines* cover the plane, rather than that rational points of the curve meet every line. These results motivate but do not state the cubic-embedding classification proved here.

## Limitations
The theorem is restricted to \(\mathbf F_3\); it makes no assertion for extension fields. The exact count is of projective equations over \(\mathbf F_3\), not field-isomorphism classes of elliptic curves or a census of singular schemes. Only a finite exhaustive incidence computation is used; the smoothness assertion has a separate algebraic proof. Searches cannot rule out undiscovered earlier equivalent treatments. The full text of the 2022 blocking-set classification was not accessible in the sources inspected, though its stated subject concerns point sets rather than equations.

## References
1. S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299, first public version 2022-08-28; especially Theorem 1.3 and Example 3.5. https://arxiv.org/html/2208.13299v2
2. K. Coolsaet, A. Botteldoorn, V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, J. Combin. Des. 30 (2022), 561–580. https://doi.org/10.1002/jcd.21842
3. S. Asgarli, D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, first public version 2023-02-26. https://arxiv.org/html/2302.13420v2
4. *Generalizing blocking semiovals in finite projective planes* (2025), Section 3 (minimal blocking sets of \(\operatorname{PG}(2,3)\)). https://doi.org/10.1016/j.ffa.2025.102688
