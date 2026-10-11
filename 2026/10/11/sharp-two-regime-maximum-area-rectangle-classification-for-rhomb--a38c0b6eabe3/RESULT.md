# Sharp two-regime maximum-area rectangle classification for rhombi

## Finding
For every Euclidean rhombus with acute angle \(\alpha\in(0,\pi/2]\), the largest area fraction occupied by an inscribed Euclidean rectangle of **unrestricted orientation** is
\[
\frac{\max_{R\subseteq K}\operatorname{area}(R)}{\operatorname{area}(K)}
=\max\left\{\frac12,\tan\frac\alpha2\right\}.
\]
There is a sharp optimizer switch at \(\alpha_*=2\arctan(1/2)\approx53.130102^\circ\). Below the threshold, the only optimum is the diagonal-parallel rectangle whose four vertices are side midpoints. Above it, the only optimum is a square whose one diagonal equals the shorter diagonal of the rhombus. At the threshold there are exactly these two distinct optimal rectangles. At the endpoint \(\alpha=\pi/2\), the optimal square is the rhombus itself.

## Assumptions and scope
Represent the closed rhombus in Cartesian diagonal coordinates as
\[
K_{A,B}=\{(x,y):|x|/A+|y|/B\le1\},\qquad A\ge B>0.
\]
Its diagonals have lengths \(2A\) and \(2B\); its area is \(2AB\); its acute angle satisfies \(\tan(\alpha/2)=B/A\). An inscribed rectangle is a nondegenerate closed Euclidean rectangle (a square is permitted) entirely contained in \(K_{A,B}\). No side-alignment or fixed-center assumption is made.

The exact maximum is
\[
\boxed{\max_{R\subseteq K_{A,B}}\operatorname{area}(R)=\max\{AB,\,2B^2\}.}
\]
For \(B/A<1/2\) the unique maximizer has vertices \((\pm A/2,\pm B/2)\), all four combinations. For \(B/A>1/2\) the unique maximizer has vertices \((A',0),(-A',0),(0,B),(0,-B)\) with \(A'=B\). At equality \(B/A=1/2\) the preceding two distinct rectangles are exactly the optimizers.

## Proof
**Centering.** An arbitrary rectangle is \(c+R_0\) with center \(c\) and centrally symmetric \(R_0\). Since \(K_{A,B}=-K_{A,B}\), its reflection \(-c+R_0\) is also contained in the rhombus. Convexity gives \(R_0=((c+R_0)+(-c+R_0))/2\subseteq K_{A,B}\). It suffices to optimize centered rectangles.

A centered rectangle is exactly \(\operatorname{conv}\{v,w,-v,-w\}\) with \(v,w\in K_{A,B}\), \(|v|=|w|>0\), and area \(2|\det(v,w)|\). Compactness gives a maximizer, which must have at least one of \(v,w\) on the boundary: otherwise a common dilation would increase area. If one vector lies in the interior, varying its direction slightly on the fixed-radius circle is feasible. Differentiating the determinant forces the two equal-length diagonals to be perpendicular. Thus it remains to bound (i) perpendicular pairs, and (ii) boundary pairs.

**Perpendicular pairs.** Coordinate reflections, a possible exchange of \(v,w\), and the equality of their lengths reduce this case to \(v=r(\cos\theta,\sin\theta)\), \(w=r(-\sin\theta,\cos\theta)\), \(0\le\theta\le\pi/4\). Since \(A\ge B\), their membership in \(K_{A,B}\) gives
\[
r\left(\frac{\sin\theta}{A}+\frac{\cos\theta}{B}\right)\le1.
\]
The factor in parentheses is strictly concave as a function of \(\theta\) on this interval, and therefore is minimized at an endpoint. Consequently
\[
|\det(v,w)|=r^2\le\max\left\{B^2,\frac{2A^2B^2}{(A+B)^2}\right\}
\le\max\left\{B^2,\frac{AB}{2}\right\},
\]
where the last step follows from \((A+B)^2\ge4AB\).

**Pairs on the boundary.** Reflecting individual coordinate signs if necessary increases the determinant's absolute value without changing norms or rhombus membership; it is therefore sufficient for an upper bound to consider \(v=(A(1-s),Bs)\) and \(w=(A(1-t),-Bt)\), with \(0\le s,t\le1\). The equality of norms is
\[
A^2(1-s)^2+B^2s^2=A^2(1-t)^2+B^2t^2,
\]
so either \(s=t\) or \(s+t=2s_0\), where \(s_0=A^2/(A^2+B^2)\ge1/2\). In the first case,
\[
|\det(v,w)|=2ABs(1-s)\le AB/2.
\]
In the second case write \(s=s_0+h\), \(t=s_0-h\). Membership in \([0,1]\) implies \(|h|\le1-s_0\), and hence
\[
|\det(v,w)|=2AB\bigl(s_0(1-s_0)+h^2\bigr)
\le\frac{2AB^3}{A^2+B^2}\le B^2.
\]
Both cases thus satisfy \(2|\det(v,w)|\le\max\{AB,2B^2\}\), establishing the global upper bound.

**Attainment and uniqueness.** The midpoint rectangle has area \(AB\); the diagonal square has area \(2B^2\). For \(B/A<1/2\), the strict inequalities in the perpendicular and unequal-parameter boundary cases exclude those branches at equality; the equal-parameter boundary case forces \(s=t=1/2\), giving the midpoint rectangle. For \(1/2<B/A\le1\), the boundary branches are strictly suboptimal except at the square endpoint \(A=B\); the perpendicular branch reaches \(B^2\) only at \(\theta=0\), giving the diagonal square (the case \(A=B\) also follows from equality of areas with the rhombus). At \(B/A=1/2\) both and no other centered rectangles optimize. Finally, the midpoint rectangle contacts all four supporting sides, whereas the diagonal square meets the two opposite short-diagonal tips. No nonzero translation of either stays within the rhombus, so these are unique among all placements.

## Verification
The separate standalone standard-library program `verify.py` exhaustively sweeps a finite angle/aspect grid of centered rectangles at twelve aspect/scale settings, independently checks actual vertex containment via the rhombus gauge, and checks both boundary-regime determinant inequalities at sampled parameters. Running `python verify.py` returned `VERIFY_OK: 12 dimensions, centered rectangle grids, and boundary regimes`. These finite numerical checks support debugging and **are not the infinite proof**, which is the analytic two-case argument above.

## Relationship to prior work
The general exact algorithm of Cabello, Cheong, Knauer, and Schlipf determines a largest inscribed rectangle in any convex polygon using a fixed-dimensional algebraic optimization; it does not state the two-branch rhombus formula or its complete equality classification. Knauer, Schlipf, Schmidt, and Tiwary study approximation algorithms for the same general optimization problem, without the present analytic rhombus phase law. Lassak established a universal rectangle-area lower benchmark for planar convex bodies; that general estimate does not identify the optimal rhombus-specific rectangle. The square specialization is compatible with the known regular-even-polygon rectangle theorem, but does not imply the non-square parameter transition.

## Limitations
This theorem concerns Euclidean rhombi, not arbitrary parallelograms, whose side-length asymmetry introduces another parameter. It classifies unrestricted-orientation **area** maximizers, not perimeter maximizers or prescribed-aspect rectangles. The analytic formula is proved; the finite verifier alone cannot establish universal optimality. Prior mathematical searches and primary-paper inspections do not establish absolute historical novelty; an older elementary formulation might exist.

## References
1. S. Cabello, O. Cheong, C. Knauer, and L. Schlipf, *Finding Largest Rectangles in Convex Polygons*, arXiv:1405.1223v1, first posted 2014-05-06; revised arXiv:1405.1223v2 (2014), Theorem 4, https://arxiv.org/abs/1405.1223.
2. C. Knauer, L. Schlipf, J. M. Schmidt, and H. R. Tiwary, *Largest Inscribed Rectangles in Convex Polygons*, Journal of Discrete Algorithms **13** (2012), 78–85, DOI:10.1016/j.jda.2012.01.002; author-hosted full text https://kam.mff.cuni.cz/~hansraj/publications/rectangle.pdf.
3. M. Lassak, *Approximation of Convex Bodies by Rectangles*, Geometriae Dedicata **47** (1993), 111–117, DOI:10.1007/BF01263495.
