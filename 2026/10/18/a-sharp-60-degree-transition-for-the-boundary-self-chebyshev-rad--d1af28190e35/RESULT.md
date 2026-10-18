# A sharp 60-degree transition for the boundary self-Chebyshev radius of rhombi

## Finding
For every nondegenerate Euclidean rhombus \(Q\), define its **boundary self-Chebyshev radius**
\[
\delta(Q)=\min_{x\in\partial Q}\max_{y\in\partial Q}\|x-y\|_2.
\]
Choose orthogonal axes through the diagonal intersection, so that
\(Q=\operatorname{conv}\{(u,0),(0,v),(-u,0),(0,-v)\}\) with \(u\ge v>0\), and put \(r=u^2/v^2\ge1\). Then
\[
\boxed{\delta(Q)^2=\begin{cases}
\displaystyle\frac{v^2(r^2+18r+1)}{4(r+1)},&1\le r\le3,\\[4pt]
v^2(r+1),&r\ge3.
\end{cases}}
\]
For \(1\le r<3\), the self-Chebyshev centers are **exactly** the four distinct points
\[
\left(\pm\frac{u(3-r)}{2(r+1)},\;\pm\frac{v(3r-1)}{2(r+1)}\right)
\]
with independent signs. For \(r\ge3\), the center set consists **exactly** of the two vertices \((0,\pm v)\).

Writing \(A(Q)=2uv\) and \(L(Q)=4\sqrt{u^2+v^2}\), these formulas yield two sharp, different extremal classifications:
\[
\boxed{\delta(Q)^2\ge\frac{2}{\sqrt3}A(Q),}
\]
with equality precisely for rhombi with acute angle \(60^\circ\) (equivalently \(r=3\)); and
\[
\boxed{\frac{8}{\sqrt5}\le\frac{L(Q)}{\delta(Q)}\le4.}
\]
The first perimeter-ratio equality holds only for squares. The second holds precisely when the acute rhombus angle is at most \(60^\circ\). Equivalently, among rhombi of a prescribed area the \(60^\circ\) rhombus uniquely minimizes \(\delta\) up to congruence, whereas among rhombi of a prescribed perimeter the square uniquely maximizes \(\delta\), and every rhombus with acute angle at most \(60^\circ\) minimizes it.

## Assumptions and scope
All distances are Euclidean. Rhombi have positive area, so \(u,v>0\). The boundary includes edges and vertices, and minimizers must be on the boundary rather than in the interior. The formula covers every similarity class including the square and the exact transition \(r=3\), but not degenerate segments. The smaller interior angle \(\phi\in(0,90^\circ]\) obeys \(r=\cot^2(\phi/2)\), and hence \(r\ge3\) if and only if \(\phi\le60^\circ\).

## Proof
**1. Reduction to a single side and two vertices.** The four reflections across the diagonal axes act transitively on the four sides, so it suffices to consider \(x(t)=(u(1-t),vt)\), \(0\le t\le1\). Squared Euclidean distance to a fixed point is convex along every polygonal edge. Consequently, the maximum of \(\|x(t)-y\|_2\) over \(y\in Q\) is attained at a vertex. The distances to \((u,0)\) and \((0,v)\) are no larger, respectively, than the distances to \((-u,0)\) and \((0,-v)\). The latter squared distances are
\[
F(t)=u^2(2-t)^2+v^2t^2,\qquad
G(t)=u^2(1-t)^2+v^2(1+t)^2.
\]
Thus \(\delta(Q)^2=\min_{0\le t\le1}\max\{F(t),G(t)\}\).

**2. Unique center on a side and the transition.** Their difference is
\[
F(t)-G(t)=3u^2-v^2-2(u^2+v^2)t,
\]
with unique zero \(t_*=(3r-1)/(2(r+1))\). For every \(r\ge1\), \(F\) decreases strictly along \([0,1)\). The quadratic \(G\) reaches its minimum at \(t_0=(r-1)/(r+1)\), and \(t_*-t_0=1/2\). If \(1\le r<3\), then \(t_*\in[1/2,1)\); the maximum equals the decreasing \(F\) to its left and the increasing \(G\) to its right. Hence its unique minimum on the side is at \(t_*\). Substitution gives
\[
F(t_*)=G(t_*)=\frac{v^2(r^2+18r+1)}{4(r+1)}.
\]
If \(r\ge3\), then \(t_*\ge1\), so \(F\ge G\) throughout the side and the unique minimum there is at \(t=1\), with value \(F(1)=u^2+v^2\). At \(r=3\) the two formulas agree. Reflecting these side minimizers yields the asserted complete center locus; duplication at the two short-diagonal vertices accounts for the change from four centers to two.

**3. Sharp area inequality.** Since \(A(Q)=2uv\), the scale-free squared-radius/area ratio equals
\[
H(r):=\frac{\delta(Q)^2}{A(Q)}=
\begin{cases}
\displaystyle\frac{r^2+18r+1}{8\sqrt r\,(r+1)},&1\le r\le3,\\[5pt]
\displaystyle\frac{r+1}{2\sqrt r},&r\ge3.
\end{cases}
\]
On the first interval its derivative is
\[
H'(r)=\frac{(r-1)(r^2-14r+1)}{16r^{3/2}(r+1)^2},
\]
which is strictly negative for \(1<r<3\). On the second interval \(H'(r)=(r-1)/(4r^{3/2})>0\) for \(r>3\). It follows that the unique minimum is at \(r=3\), where \(H(3)=2/\sqrt3\). Positive similarity transformations account for the fixed-area equality family.

**4. Sharp perimeter-ratio interval.** Since \(L(Q)=4\sqrt{u^2+v^2}\),
\[
\frac{\delta(Q)^2}{u^2+v^2}=
\begin{cases}
\displaystyle\frac{r^2+18r+1}{4(r+1)^2},&1\le r\le3,\\[4pt]
1,&r\ge3.
\end{cases}
\]
The derivative of the first branch is \(4(1-r)/(r+1)^3\), strictly negative for \(r>1\). It decreases from \(5/4\) at \(r=1\) to \(1\) at \(r=3\) and remains \(1\) thereafter. Taking positive square roots and reciprocals proves the two sharp bounds on \(L(Q)/\delta(Q)\) and all equality cases. In particular \(\delta(Q)\) is largest at the square, and smallest throughout the \(r\ge3\) plateau, when \(L(Q)\) is fixed.

## Verification
The included standalone `checker.py` works over exact rational squares of diagonal ratios and exact rational edge coordinates. It confirms the formulas by independent point-to-all-four-vertices comparisons for 10 parameter choices and 10,410 edge points in total, including the square, both sides of the phase boundary, and increasingly thin rhombi. Execute `python3 checker.py` with the standard Python library only. These finite comparisons are consistency tests, not substitutes for the preceding all-parameter proof.

## Relationship to prior work
Nikitenko and Nikonorov (arXiv:2301.03218, first public 9 January 2023) prove a sharp **global** perimeter-to-boundary-self-Chebyshev-radius inequality for all convex quadrilaterals, whose minimizing shape is a non-rhombic magic kite. That theorem does not identify the exact radius or all constrained centers of each rhombus, nor the sharp area-normalized minimizer. Their full accessible HTML preprint also contains general local-center criteria and subsequent conjectures about higher-sided polygons. The rhombus calculation here uses the general farthest-vertex observation but determines a different, complete two-constraint phase diagram. Walter (arXiv:1606.06717, 2016) introduced the underlying minimax geometry and a finite polygonal algorithm; the closed rhombus phase classification and the area extremizer are not asserted by the abstracts and primary text inspected in the searches described in the review. A mathematical-record search for this exact result found no equivalent item; searches cannot rule out unindexed work.

## Limitations
The result is restricted to Euclidean rhombi; no claim is made for arbitrary parallelograms, for other metrics, or for arbitrary convex quadrilaterals. It does not improve the published sharp **global quadrilateral** perimeter bound and it does not address the open higher-sided cases. Independent scientific audit has not been performed. Walter's full text was not available for full-text comparison, leaving a bibliographic risk; the available 2023 primary full text was examined in the relevant sections.

## References
1. E. V. Nikitenko and Yu. G. Nikonorov, *The extreme polygons for the self Chebyshev radius of the boundary*, arXiv:2301.03218 (submitted 2023-01-09; HTML revision v3 examined), https://arxiv.org/abs/2301.03218.
2. R. Walter, *On a Minimax Problem for Ovals*, arXiv:1606.06717 (2016); *Minimax Theory and Its Applications* 2 (2017), 285–318, https://arxiv.org/abs/1606.06717.
3. Yu. G. Nikonorov and O. Yu. Nikonorova, *Some extremal problems for polygons in the Euclidean plane*, arXiv:2209.05940 (submitted 2022-09-13), https://arxiv.org/abs/2209.05940.
