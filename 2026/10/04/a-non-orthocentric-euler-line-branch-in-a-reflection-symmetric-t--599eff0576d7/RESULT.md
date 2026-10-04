# A non-orthocentric Euler-line branch in a reflection-symmetric tetrahedron family

## Finding
For \(p,h>0\), consider
\[
T_{p,h}=\operatorname{conv}\{(-1,0,0),(1,0,0),(0,p,0),(0,0,h)\}.
\]
Let \(G\), \(O\), and \(I\) denote its centroid, circumcenter, and incenter. The incenter lies on the Euler affine hull \(\operatorname{aff}\{G,O\}\) exactly in the following cases:
\[
p=h,
\]
or
\[
ph\ge 2,\qquad (p+h)^2=\frac{4ph(ph+2)^2}{5ph+6}.
\]
The second branch meets the symmetric branch only at \(p=h=\sqrt2\). For every \(ph>2\), it supplies two distinct positive parameters obtained by interchanging \(p\) and \(h\).

A concrete point on the nonsymmetric branch is
\[
p=\sqrt7,\qquad h=\frac3{\sqrt7}.
\]
For this tetrahedron,
\[
G=\left(0,\frac{\sqrt7}{4},\frac{3}{4\sqrt7}\right),\quad
O=\left(0,\frac3{\sqrt7},\frac1{3\sqrt7}\right),\quad
I=\left(0,\frac1{\sqrt7},\frac1{\sqrt7}\right),
\]
and
\[
I-G=-\frac35(O-G).
\]
It is neither orthocentric nor biregular. Hence this natural two-parameter family already contains a continuous branch of solutions to the incenter-on-Euler-line problem that is genuinely outside the orthocentric/biregular regime described in the motivating literature.

## Assumptions and scope
All geometry is Euclidean. The parameters satisfy \(p,h>0\), so \(T_{p,h}\) is nondegenerate. The family is normalized by the edge \(AB\) of length \(2\) and has the reflection symmetry \((x,y,z)\mapsto(-x,y,z)\). Its remaining two vertices lie on perpendicular axes in the fixed plane \(x=0\). This is a low-dimensional but geometrically natural test family for the general tetrahedral problem: the symmetry forces the three relevant centers into the same plane while leaving two independent shape parameters.

The Euler line of a general simplex is the affine hull of its circumcenter and centroid. At the single parameter value \(p=h=\sqrt2\), those two centers coincide; the statement therefore uses the Euler affine hull, which is then one point. No characterization of all tetrahedra or all higher-dimensional simplices is claimed.

## Proof
Write
\[
L=\sqrt{p^2h^2+p^2+h^2}.
\]
The two faces opposite \(A\) and \(B\) have area \(L/2\), while the faces opposite \(C\) and \(D\) have areas \(h\) and \(p\), respectively. Using the standard facet-area barycentric formula for the incenter gives
\[
I=(0,t,t),\qquad t=\frac{ph}{L+p+h}.
\]
Direct averaging and equidistance from the four vertices give
\[
G=\left(0,\frac p4,\frac h4\right),
\qquad
O=\left(0,\frac{p^2-1}{2p},\frac{h^2-1}{2h}\right).
\]
Thus \(G,O,I\) are collinear exactly when the two-dimensional determinant in the \((y,z)\)-plane vanishes. Exact simplification yields
\[
\det(I-G,O-G)
=-\frac{(p-h)Q(p,h)}{8ph(L+p+h)},
\]
where
\[
Q(p,h)=2p^2h^2-p^2-h^2+2ph-(p+h)L.
\]
The factor \(p-h\) gives the entire symmetric branch.

For the remaining factor set
\[
x=p+h,\qquad y=ph.
\]
Then \(L^2=y^2+x^2-2y\) and
\[
Q=2y^2-x^2+4y-x\sqrt{y^2+x^2-2y}.
\]
If \(Q=0\), then the left algebraic term \(2y^2-x^2+4y\) is positive. Squaring therefore introduces no sign ambiguity on a genuine solution, and
\[
(2y^2-x^2+4y)^2-x^2(y^2+x^2-2y)
=-y\bigl(5x^2y+6x^2-4y^3-16y^2-16y\bigr).
\]
Since \(y>0\), this gives
\[
x^2=\frac{4y(y+2)^2}{5y+6}.
\]
Conversely, suppose this equation holds for positive \(p,h\). The discriminant condition for positive roots of \(u^2-xu+y=0\) becomes
\[
x^2-4y=\frac{4y(y-2)(y+1)}{5y+6}\ge0,
\]
so necessarily \(y\ge2\). On this range,
\[
2y^2+4y-x^2=\frac{2y(y+2)(3y+2)}{5y+6}>0.
\]
The positive sign recovers the unsquared equation \(Q=0\). Therefore the nonsymmetric branch is exactly
\[
ph\ge2,
\qquad
(p+h)^2=\frac{4ph(ph+2)^2}{5ph+6}.
\]
At \(ph=2\), the discriminant is zero, giving \(p=h=\sqrt2\). If \(ph>2\), the discriminant is positive, so the branch has \(p\ne h\).

For the explicit choice \(ph=3\), the branch relation gives \((p+h)^2=100/7\). Taking
\[
p=\sqrt7,\qquad h=\frac3{\sqrt7}
\]
meets these two symmetric equations. Here \(L=11/\sqrt7\), and substitution gives the displayed formulas for \(G,O,I\) and the exact affine relation \(I-G=-\frac35(O-G)\).

It remains to verify that this example is outside the previously characterized orthocentric class. A necessary condition for a tetrahedron to be orthocentric is that each pair of opposite edges be perpendicular: if the altitudes from two opposite vertices meet, subtracting their orthogonality relations to the opposite face gives the perpendicularity of the corresponding opposite edges. In the present example,
\[
(C-A)\mathbin{\cdot}(D-B)=(1,\sqrt7,0)\mathbin{\cdot}\left(-1,0,\frac3{\sqrt7}\right)=-1,
\]
so the tetrahedron is not orthocentric.

Its six edge lengths are
\[
AB=2,\quad AC=BC=2\sqrt2,\quad AD=BD=\frac4{\sqrt7},\quad CD=\sqrt{\frac{58}{7}}.
\]
No face is equilateral, excluding a \(1+3\) biregular partition. For a \(2+2\) partition the four cross edges would all have to be equal, which is impossible from the displayed edge lengths. Hence it is not biregular.

## Verification
The proof is symbolic and does not infer an infinite statement from numerical experiments. The bundled `verify.py` checks the polynomial factor identity after the substitution \(x=p+h\), \(y=ph\), the exact branch equations for \(ph=3\), the coordinates of the three centers, the affine ratio \(-3/5\), and the nonorthogonality and edge-length distinctions of the explicit example. The checker is supplemental; the classification follows from the exact determinant factorization and the sign-safe squaring argument above.

## Relationship to prior work
Hajja and Martini's 2013 survey explains that the ordinary Euler-line theorem extends to general simplices through the Monge point, and it explicitly says that the corresponding incenter-on-Euler-line question outside the orthocentric setting remained open. Bezdek, Deza, and Ye subsequently state this as Question 9: characterize the \(n\)-simplices whose incenter lies on the Euler line. Their comments record the known orthocentric theorem: in the orthocentric class, collinearity of circumcenter, centroid, and incenter is equivalent to biregularity. The 2008 paper of Edmonds, Hajja, and Martini is the cited source for that orthocentric result.

The present result does not solve the full characterization problem. It instead completely solves a canonical reflection-symmetric two-parameter tetrahedron family and, crucially, exhibits an exact continuous branch outside the orthocentric and biregular classes. Targeted searches using the exact coordinates, the branch equation, the nonorthocentric formulation, and aliases of the Euler-line problem did not locate a prior statement of this family or example.

## Limitations
Only the normalized family \(T_{p,h}\) is classified. No claim is made that every tetrahedron with one reflection symmetry is similar to this family, or that the second branch is a complete component of the full moduli space. The literature search cannot exclude unindexed or differently phrased prior work. The 2008 orthocentric paper was available in the inspected sources at abstract level; its theorem was also stated explicitly in two independently accessible later full texts. No independent audit has been performed.

## References
1. M. Hajja and H. Martini, *Orthocentric Simplices as the True Generalizations of Triangles*, The Mathematical Intelligencer 35 (2013), 16–28. DOI: 10.1007/s00283-013-9367-7.
2. K. Bezdek, A. Deza, and Y. Ye, *Selected Open Problems in Discrete Geometry and Optimization*, Fields Institute Communications 69 (2013), 321–336. DOI: 10.1007/978-3-319-00200-2_18.
3. A. L. Edmonds, M. Hajja, and H. Martini, *Orthocentric Simplices and Biregularity*, Results in Mathematics 52 (2008), 41–50. DOI: 10.1007/s00025-008-0294-4.
