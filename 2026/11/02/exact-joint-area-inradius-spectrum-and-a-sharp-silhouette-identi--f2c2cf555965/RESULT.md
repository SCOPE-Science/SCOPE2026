# Exact joint area–inradius spectrum and a sharp silhouette-identifiability transition for regular-octahedron shadows

## Finding
Let \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3\), the regular octahedron of circumradius \(1\). For every two-dimensional linear plane \(E\), denote by \(A(E)\) the ordinary Euclidean area of the orthogonal shadow \(P_EO\) and by \(r(E)\) its Euclidean inradius. Put
\[
q=\sqrt{r^{-2}-2},\qquad 0\le q\le1,
\]
and define four explicit functions on \([0,1]\):
\[
\begin{aligned}
H_-(q)&=\frac{3-q}{\sqrt{q^2-2q+3}},&
H_+(q)&=\sqrt{\frac{2(q^2+3)}{q^2+2}},\\
Q_-(q)&=\frac{2}{\sqrt{1+q^2}},&
Q_+(q)&=\frac{2}{\sqrt{1+q^2/2}}.
\end{aligned}
\]
**Complete sharp feasible set.** For each \(r\in[1/\sqrt3,1/\sqrt2]\), the exact set of attainable \(A(E)\) at that inradius is
\[
\boxed{[H_-(q),H_+(q)]\ \cup\ [Q_-(q),Q_+(q)].}
\]
Every area in each closed interval is attained, including its endpoints. If \(0\le q<1\), the first interval is achieved by hexagonal shadows and the second by quadrilateral shadows. At \(q=1\), the formulas give the common closed interval \([\sqrt2,\sqrt{8/3}]\). Every such normal lies on the combinatorial transition; the shadow has four extreme vertices, with the remaining projected pair on its boundary (possibly coincident with an existing pair).

**Sharp gap transition.** Define
\[
q_* =r_* =\sqrt{\sqrt2-1},\qquad A_*=2^{3/4}.
\]
For \(r\in(r_*,1/\sqrt2]\) (equivalently \(0\le q<q_*\)), the two feasible area intervals are disjoint: there is a genuine forbidden open area band \((H_+(q),Q_-(q))\) at the specified inradius. Thus two scalar shadow measurements, area and inradius, determine whether the shadow is hexagonal or quadrilateral. At \(r=r_*\) the gap closes at the unique contact \(A=A_*\). For \(r\in[1/\sqrt3,r_*)\) the intervals overlap and the feasible area set is a single interval \([H_-(q),Q_+(q)]\); in its interior overlap, both polygonal types occur for the same pair \((A,r)\), apart from the nongeneric endpoint \(r=1/\sqrt3\).

More globally, the sharp inequalities are
\[
\frac{3-q}{\sqrt{q^2-2q+3}}\le A(E)\le\frac{2}{\sqrt{1+q^2/2}},
\]
with the stronger two-band restriction above. At the maximal inradius \(r=1/\sqrt2\), only two areas occur: \(\sqrt3\) (a hexagon, body-diagonal view) and \(2\) (a square, coordinate-axis view). This gives a disconnected two-point fiber, not an interval.

## Assumptions and scope
All lengths and areas use the fixed ambient Euclidean metric. The octahedron has exactly the six vertices \(\pm e_i\) and hence edge length \(\sqrt2\), not edge length \(1\). The plane may have any orientation; no random sampling is needed to state the feasible set. In each fixed fiber \(0<q<1\), both types occur along arcs of positive length. The fiber has zero spherical area, but directions of both types have positive Haar probability in every open interval of \(q\) meeting \((0,1)\). The inradius is the largest radius of a disk *anywhere* in the planar polygon; central symmetry shows that an optimal disk can be centered at the shadow origin. Polygon type counts distinct extreme vertices, not nonextreme points along edges.

## Proof
**Step 1: normalization and an exact brightness identity.** Let \(u\) be a unit normal to \(E\), and let \(0\le a\le b\le c\) be the ordered absolute values of its three coordinates, so \(a^2+b^2+c^2=1\). The eight triangular octahedral facets have outward unit normals the normalized signed vectors \((\pm1,\pm1,\pm1)\), each facet having area \(\sqrt3/2\). Cauchy's planar projection area identity therefore gives
\[
A(E)=\frac14\sum_{\varepsilon_i\in\{-1,1\}}\left|\varepsilon_1a+\varepsilon_2b+\varepsilon_3c\right|
=\max\{a+b+c,\,2c\}.
\]
The final equality follows by grouping the four sign pairs \(\{s,-s\}\) and distinguishing \(c<a+b\) from \(c>a+b\). No distributional claim is used.

**Step 2: polarity determines the inradius exactly.** The polar body of \(O\) is \(C=[-1,1]^3\), and polarity within \(E\) yields \((P_EO)^\circ=C\cap E\). Central symmetry centers a largest inscribed disk, hence
\[
r(E)^{-1}=\max\{\|x\|_2:x\in C\cap E\}.
\]
Each vertex of the central cube section lies on a cube edge (including limiting cases), so two of its coordinates have absolute value \(1\). In the **dominant case** \(c\ge a+b\), the only relevant cube-edge intersections have the free coordinate in the \(c\)-direction and the maximal free-coordinate magnitude is \((a+b)/c\). It follows that
\[
r^{-2}=2+((a+b)/c)^2 \quad(c\ge a+b).
\]
In the **triangle case** \(c\le a+b\), all three free-coordinate positions are possible. Their largest magnitudes are \((b-a)/c\), \((c-a)/b\), and \((c-b)/a\); the middle ratio is largest, because
\[
\begin{aligned}
c(c-a)-b(b-a)&=(c-b)(c+b-a)\ge0,\\
a(c-a)-b(c-b)&=(b-a)(a+b-c)\ge0.
\end{aligned}
\]
Thus
\[
r^{-2}=2+((c-a)/b)^2 \quad(c\le a+b).
\]
Limits cover zero coordinates and cases of equality. Both ratios lie between \(0\) and \(1\), giving \(1/\sqrt3\le r\le1/\sqrt2\).

**Step 3: all quadrilateral-shadow areas for fixed \(r\).** In the dominant case \(c\ge a+b\), the fixed invariant is \(q=(a+b)/c\). For \(0\le q\le1\), use the full continuous parametrization
\[
(a,b,c)=\frac{(q(1-z)/2,\ q(1+z)/2,\ 1)}{\sqrt{1+q^2(1+z^2)/2}},\qquad 0\le z\le1.
\]
Every ordered normal in this regime is obtained, including endpoints. Indeed, writing \(p_i=P_Ee_i\) after choosing a nonnegative normal, \(ap_1+bp_2+cp_3=0\). Since \(c>0\), \(p_1,p_2\) are linearly independent, so their two signed pairs span the quadrilateral \(\{s p_1+t p_2:|s|+|t|\le1\}\). The pair \(\pm p_3\) is strictly interior if \(c>a+b\) and on the boundary if \(c=a+b\). In either case the shadow is this quadrilateral. The area is \(A=2c=2/\sqrt{1+q^2(1+z^2)/2}\), strictly decreasing in \(z\) for \(q>0\). Therefore the **entire** attainable quadrilateral area range is \([Q_-(q),Q_+(q)]\), with the bounds achieved by \(a=0\) and \(a=b\), respectively. The fixed-\(q\) curves in both parametrizations are smooth arcs and hence have zero spherical area. At any interior parameter choice in either strict chamber, continuity gives a neighborhood with positive spherical area in every open interval around that value of \(q\).

**Step 4: all hexagonal-shadow areas for fixed \(r\).** In the triangle case \(c\le a+b\), \(q=(c-a)/b\). Write \(t=a/b\). The exact ordered-normal restrictions are \(1-q\le t\le1\), and every such normal has representative
\[
(a,b,c)=\frac{(t,1,t+q)}{\sqrt{2t^2+2qt+q^2+1}}.
\]
For \(q<1\) the shadow is hexagonal: the strict triangle inequalities make all six projected vertices extreme. In fact, solving the projected linear relation for any of the three projected vertices expresses it in the basis of the other two with sum of absolute coefficients greater than one. Its area is
\[
F_q(t)=\frac{2t+1+q}{\sqrt{2t^2+2qt+q^2+1}},\qquad
\operatorname{sign}F_q'(t)=\operatorname{sign}(q^2-q-2t+2).
\]
For \(0<q<1\), its unique interior maximum occurs at \(t_*=1+(q^2-q)/2\), which belongs to \((1-q,1)\). Direct substitution gives \(F_q(t_*)=\sqrt{2(q^2+3)/(q^2+2)}=H_+(q)\). Its two endpoint values are
\[
F_q(1-q)=\frac{3-q}{\sqrt{q^2-2q+3}},\qquad
F_q(1)=\frac{3+q}{\sqrt{q^2+2q+3}}.
\]
Their squared difference, second minus first, is
\[
\frac{8q^3}{(q^2-2q+3)(q^2+2q+3)}\ge0.
\]
Hence the minimum is \(H_-(q)=F_q(1-q)\). Continuity gives the entire closed range. At \(q=0\) it degenerates to the body-diagonal viewing direction; the formulas hold as limits. At \(q=1\), the two parametrizations meet on the triangle-inequality boundary and their area ranges coincide as asserted.

**Step 5: sharp gap and contact.** For \(0<q<1\), direct simplification gives
\[
\begin{aligned}
Q_-(q)^2-H_+(q)^2
&=\frac{2(1-2q^2-q^4)}{(1+q^2)(2+q^2)},\\
Q_-(q)^2-H_-(q)^2
&=\frac{(1-q)^2(3+4q-q^2)}{(1+q^2)(3-2q+q^2)}>0,\\
Q_+(q)^2-H_+(q)^2
&=\frac{2(1-q^2)}{2+q^2}>0.
\end{aligned}
\]
Thus the quadrilateral interval starts above the hexagonal interval exactly when \(1-2q^2-q^4>0\), or \(q<q_*=\sqrt{\sqrt2-1}\). At equality their common endpoint is \(Q_-(q_*)=H_+(q_*)=2^{3/4}\), and the inradius at that parameter equals \(r_*=1/\sqrt{2+q_*^2}=\sqrt{\sqrt2-1}=q_*\). Above the threshold in \(q\), the intervals overlap; since each is closed and contains all intermediate areas, their union is then a single interval. The strict extremizer inequalities also prove the global range and the asserted identifiability conclusion. This completes the classification for all plane orientations. \(\square\)

## Verification
Run `python3 verify_octa_joint.py` using NumPy and SciPy. The program independently computes planar convex hulls of projected octahedron vertices for 2,500 randomly chosen normals, extracting both area and the origin-centered inradius from hull equations and counting vertices. It includes a separate check at the transition normal \((0,1,1)/\sqrt2\), tests band inclusion along discretized curves at 61 fixed inradius levels, tests the analytical interior hexagon maximum and contact constant, and checks another 200,000 sampled normals for inclusion in the exact feasible bands. The symbolic inequalities and exhaustive parametrizations above, not finite numerical tests, prove the infinite statement.

## Relationship to prior work
Finch (2012), Section 2.3, reports area and perimeter moments, a mixed area–perimeter moment, and four-versus-six-vertex shadow probabilities. The paired metric there is perimeter, not inradius, and those moments do not give the feasible fibers of area at fixed inradius. Black and Criado (2024), Theorem 1.1 and related results, bound the expected combinatorial complexity of random shadows of fixed polytopes, not the exact metric tradeoff under a shared orientation. The 2026 *Exact inradius law for random planar projections of the regular octahedron* gives the marginal inradius distribution and the pointwise radius formulas from polarity and cube sections, which are reused here. The triaxial shadow result gives hexagon probabilities under axis stretching. The conditional-brightness law [5] conditions area on the largest absolute normal coordinate, not inradius. The joint diameter–silhouette result [6] pairs projected cube diameter with octahedron-shadow vertex count, not area with inradius. The claim here is the **two complete attainable area intervals at fixed inradius, their gap-closing transition and identifiability consequence**, not a conditional probability law or a new derivation of the separate invariants. No claim of exhaustive historical uniqueness is made.

## Limitations
The result applies to orthogonal projections of this fixed, circumradius-one, three-dimensional regular octahedron. It is a deterministic image-set theorem: it does not assert the joint probability density, the conditional distribution of area given inradius, or corresponding bounds for distorted octahedra and other convex bodies. The full equality fibers, including the transition directions, are deterministic; historical priority could still be affected by an unindexed equivalent tradeoff in convex stereology. The cited analytic reductions remain classical; the new content is their sharp joint optimization.

## References
1. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1, first posted 11 June 2024; full manuscript https://arxiv.org/abs/2406.06936 .
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, first posted 12 March 2012; full manuscript https://arxiv.org/html/1203.2464v1 .
3. *Exact inradius law for random planar projections of the regular octahedron*, publicly available scientific record (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5/RESULT.md .
4. *Sharp triaxial octahedron shadow bound and quadratic shape stability*, publicly available scientific record (2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-triaxial-octahedron-shadow-bound-and-quadratic-shape-stabi--c544249c351b/RESULT.md .
5. Conditional-brightness law for octahedron shadows, record dated 2026-11-01, https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-conditional-brightness-law-and-two-sharp-phase-transitions-for-a--faf057c3e230/RESULT.md .
6. Joint cube-shadow diameter and octahedron-silhouette law, record dated 2026-11-02, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-joint-exact-diameter-and-silhouette-law-for-random-cube-octahedr--ee7a93325dd3/RESULT.md .
