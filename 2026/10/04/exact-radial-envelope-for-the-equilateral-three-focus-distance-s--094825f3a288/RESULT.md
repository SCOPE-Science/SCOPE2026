# Exact radial envelope for the equilateral three-focus distance sum
## Finding
Let \(ABC\) be an equilateral triangle with circumcenter \(O\) and circumradius \(R>0\). For every point \(P\in\mathbb{R}^2\), write \(\rho=OP\). Then \[|R-\rho|+2\sqrt{R^2+R\rho+\rho^2}\le PA+PB+PC\le R+\rho+2\sqrt{R^2-R\rho+\rho^2}.\] If \(\rho>0\), equality in the lower bound holds exactly when \(P\) lies on one of the three rays from \(O\) through a vertex, and equality in the upper bound holds exactly when \(P\) lies on one of the three opposite rays, equivalently on a ray from \(O\) through a side midpoint. For \(\rho=0\), both bounds equal \(3R\).

Thus every circle centered at \(O\) has an exact minimum and maximum of the three-focus distance sum, with the six extremal directions alternating between vertex rays and side-midpoint rays.

## Assumptions and scope
The setting is the Euclidean plane. The points \(A,B,C\) are the vertices of a nondegenerate equilateral triangle, \(O\) is their common centroid and circumcenter, \(R=OA=OB=OC>0\), and \(P\) is arbitrary, including points outside the triangle. The quantity \(\rho=OP\) is fixed while the polar angle of \(P\) varies. No smoothness or interior-point assumption is used.

## Proof
Choose polar angle \(\theta\) for \(OP\) measured from \(OA\), and number the vertices with arguments \(0,2\pi/3,4\pi/3\). Put
\[
d_i=PA_i,\qquad x_i=d_i^2=R^2+\rho^2-2R\rho\cos(\theta-2\pi i/3),\qquad i=0,1,2.
\]
The three numbers \(c_i=\cos(\theta-2\pi i/3)\) are the roots of
\[
4t^3-3t-\cos(3\theta)=0.
\]
Hence
\[
\sum c_i=0,\qquad \sum_{i<j}c_ic_j=-\frac34,\qquad c_0c_1c_2=\frac14\cos(3\theta).
\]
Writing \(a=R^2+\rho^2\) and \(b=2R\rho\), direct use of these symmetric sums gives
\[
S_1:=\sum x_i=3(R^2+\rho^2),
\]
\[
S_2:=\sum_{i<j}x_ix_j=3(R^4+R^2\rho^2+\rho^4),
\]
and
\[
x_0x_1x_2=R^6+\rho^6-2R^3\rho^3\cos(3\theta).
\]
Thus \(S_1\) and \(S_2\) are independent of \(\theta\), while
\[
q:=d_0d_1d_2=\sqrt{R^6+\rho^6-2R^3\rho^3\cos(3\theta)}.
\]

It remains to show that the perimeter-like sum \(p=d_0+d_1+d_2\) is strictly increasing with \(q\) when \(S_1,S_2\) are fixed. Let
\[
e=d_0d_1+d_1d_2+d_2d_0.
\]
The identities
\[
p^2=S_1+2e,\qquad e^2=S_2+2pq
\]
give
\[
e=\frac{p^2-S_1}2,\qquad q=\frac{e^2-S_2}{2p}.
\]
Differentiating the last expression along the algebraic relation with \(S_1,S_2\) fixed gives
\[
\frac{dq}{dp}=\frac{ep-q}p.
\]
For nonnegative distances not all zero,
\[
ep-q=d_0^2d_1+d_0d_1^2+d_1^2d_2+d_1d_2^2+d_0^2d_2+d_0d_2^2+2d_0d_1d_2>0.
\]
Therefore \(p\) is strictly increasing with \(q\) on the feasible family.

For \(\rho>0\), the product \(q\) is minimized exactly when \(\cos(3\theta)=1\), namely on the three vertex rays, and maximized exactly when \(\cos(3\theta)=-1\), namely on the three opposite rays. On a vertex ray the three distances are
\[
|R-\rho|,\quad \sqrt{R^2+R\rho+\rho^2},\quad \sqrt{R^2+R\rho+\rho^2},
\]
which gives the lower bound. On an opposite ray they are
\[
R+\rho,\quad \sqrt{R^2-R\rho+\rho^2},\quad \sqrt{R^2-R\rho+\rho^2},
\]
which gives the upper bound. For \(\rho=0\), all three distances equal \(R\), completing the proof.

## Verification
The proof is symbolic and covers all \(R>0\), \(\rho\ge0\), including the boundary case \(\rho=R\) where one distance can vanish. A separate deterministic checker samples multiple radii and a dense angular grid, verifies both inequalities numerically, checks equality on all six predicted rays, and verifies the three symmetric identities used in the proof. The numerical checker is supplementary and is not used as evidence for the universal quantifiers.

## Relationship to prior work
The classical Fermat--Torricelli literature studies minimization of \(PA+PB+PC\); Eriksson gives a modern account of that problem. Sekino studies \(n\)-ellipses as level sets of sums of distances and proves general convexity and critical-point results. Sándor studies equilateral triangles and the associated Pompeiu triangle; in particular, his formulas make the sum of squared vertex distances and the area of the Pompeiu triangle depend only on \(OP\), and he gives non-sharp bounds for \(PA+PB+PC\). Petrović, Banjac, and Malešević study trifocal curves and their level-set geometry. The statement here instead determines the exact minimum and maximum of \(PA+PB+PC\) on every circle \(OP=\rho\), together with all equality directions. Searches of the cited literature and direct statement/formula searches did not locate this exact radial envelope.

## Limitations
The literature terminology is diffuse: the same objects appear under \(n\)-ellipse, polyellipse, trifocal curve, Fermat--Torricelli, and Pompeiu-triangle language. Although several close sources and a full primary treatment of \(n\)-ellipses were inspected, the search is not an exhaustive proof of historical novelty. The result is specific to three equally spaced foci; the monotonicity argument uses symmetric invariants that are special to the equilateral three-focus configuration.

## References
1. F. Eriksson, “The Fermat-Torricelli Problem Once More,” *The Mathematical Gazette* 81(490) (1997), 37–44. DOI: 10.2307/3618766.
2. C. Groß and T.-K. Strempel, “On Generalizations of Conics and on a Generalization of the Fermat-Torricelli Problem,” *The American Mathematical Monthly* 105(8) (1998), 732–743. DOI: 10.1080/00029890.1998.12004955.
3. J. Sekino, “n-Ellipses and the Minimum Distance Sum Problem,” *The American Mathematical Monthly* 106(3) (1999), 193–202. DOI: 10.1080/00029890.1999.12005030.
4. J. Sándor, “On the Geometry of Equilateral Triangles,” *Forum Geometricorum* 5 (2005), 107–117.
5. M. Petrović, B. Banjac, and B. Malešević, “The Geometry of Trifocal Curves with Applications in Architecture, Urban and Spatial Planning,” *SPATIUM* 32 (2014), 28–33. DOI: 10.2298/SPAT1432028P.
