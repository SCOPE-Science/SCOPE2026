# Exact coverage multiplicities and dual contact exponents of tetrahedral spherical caps

## Finding

Let \(v_1,v_2,v_3,v_4\in S^2\) be the vertices of a regular tetrahedron, normalized by \(v_i\cdot v_j=-1/3\) for distinct indices. Let \(X\) be uniform with respect to spherical area on \(S^2\). For every angular radius \(0\le r\le\pi\), let
\[
K_r(X)=\#\{i\in\{1,2,3,4\}:\arccos(X\cdot v_i)\le r\},\qquad p_k(r)=\Pr(K_r=k).
\]
Define
\[
d=\arccos(-1/3),\quad r_0=d/2,\quad b_0=\arccos(1/3)=\pi-d.
\]
For \(0\le r\le\pi/2\), set \(a(r)=(1-\cos r)/2\), and set \(b(r)=0\) when \(r\le r_0\). When \(r_0<r\le\pi/2\), put
\[
\begin{aligned}
 g(r)&=\arccos\bigl(\sqrt2\cot r\bigr),\\
 h(r)&=\arccos\left(\frac{-1/3-\cos^2r}{\sin^2r}\right),\\
 b(r)&=\frac{2\pi-4g(r)\cos r-2h(r)}{4\pi}.
\end{aligned}
\]
Then the **complete exact five-state multiplicity distribution** is
\[
\bigl(p_0,p_1,p_2,p_3,p_4\bigr)=
\begin{cases}
\bigl(1-4a+6b,\ 4a-12b,\ 6b,\ 0,\ 0\bigr),&0\le r\le b_0,\\
\bigl(0,\ 3-8a+6b,\ 12a-12b-3,\ 1-4a+6b,\ 0\bigr),&b_0\le r\le\pi/2,
\end{cases}
\]
with \(a=a(r)\), \(b=b(r)\). For \(\pi/2\le r\le\pi\), the remaining values follow *without additional integrals* from
\[
p_k(r)=p_{4-k}(\pi-r)\qquad(0\le k\le4).
\]
Both formulas agree at the shared endpoints. At \(r=\pi/2\), in particular,
\[
p_1=p_3=2-\frac{3d}{\pi},\qquad p_2=\frac{6d}{\pi}-3,\qquad p_0=p_4=0.
\]
The packing and covering thresholds have sharp **distinct** exponents. As \(\varepsilon\downarrow0\),
\[
\begin{aligned}
p_2(r_0+\varepsilon)&\sim\frac{4\,2^{3/4}}\pi\varepsilon^{3/2},\\
p_0(b_0-\varepsilon)&\sim\frac{3\sqrt3}\pi\varepsilon^2,\\
p_3(b_0+\varepsilon)&\sim\frac{3\sqrt3}\pi\varepsilon^2.
\end{aligned}
\]
Thus the last uncovered gaps close and the first threefold-covered patches open with the **same exact quadratic coefficient**, whereas twofold coverage starts with exponent \(3/2\). The upper-radius critical laws follow by the stated antipodal duality.

## Assumptions and scope

All distances are intrinsic great-circle angular distances on the *unit* two-sphere. Closed versus open caps have equal area, since the circle boundaries have zero spherical area. The centers are fixed and exactly tetrahedral; they are not random. All probabilities are normalized by the full spherical area \(4\pi\). The radius \(r\) ranges over the entire closed interval \([0,\pi]\); formulas are not asymptotic except in the three displayed contact limits.

## Proof

**1. Exact contact and cover thresholds.** The angular separation of any two distinct centers is \(d\), so two equal caps first touch at \(r=r_0\). The tetrahedron \(T=\operatorname{conv}\{v_1,\dots,v_4\}\) has facet planes \(x\cdot v_i=-1/3\) and contains the Euclidean ball centered at zero of radius \(1/3\). Hence for every \(x\in S^2\), its support function satisfies \(\max_i x\cdot v_i\ge1/3\). Equality occurs precisely at the four outward facet normals \(-v_i\). Consequently the four caps cover \(S^2\) exactly when \(r\ge b_0\), and the uncovered set near the sharp threshold is concentrated around those four normals.

For any three distinct tetrahedron vertices, their sum equals minus the remaining vertex and has Euclidean norm \(1\). A point \(x\) belonging to all three caps at radius \(r\) would give \(3\cos r\le x\cdot(v_i+v_j+v_k)\le1\). Thus no triple intersection has positive area before \(r=b_0\), when the three caps meet at one point. For \(r\le\pi/2\), a positive-area fourfold intersection is impossible: otherwise all four dot products \(x\cdot v_i\) would be nonnegative, while their sum is \(0\); equality would force \(x=0\), contradicting \(x\in S^2\).

**2. Two-cap lens.** Fix two centers separated by \(d\). For \(r>r_0\), the two small-circle boundaries intersect in two points. In either isosceles spherical triangle formed by the centers and an intersection, the angle at either cap center is
\(g(r)=\arccos(\sqrt2\cot r)\), while the angle at the intersection is \(h(r)=\arccos((-1/3-\cos^2r)/\sin^2r)\), by the spherical cosine law and \(\tan(d/2)=\sqrt2\). Two circular sectors of angle \(2g\), each of area \(2g(1-\cos r)\), contain a spherical kite consisting of two congruent triangles, each of area \(2g+h-\pi\). Subtracting the kite gives the exact lens area
\[
L(r)=4g(1-\cos r)-2(2g+h-\pi)
=2\pi-4g\cos r-2h.
\]
For \(r\le r_0\), the intersection has zero area. Each individual cap has area \(A(r)=2\pi(1-\cos r)\), so the normalized one-cap and two-cap intersection measures are respectively \(a=A/(4\pi)\) and \(b=L/(4\pi)\).

**3. Multiplicity inversion.** By symmetry and counting cap memberships pointwise, the first two binomial moments are
\[
\sum_{k=0}^4 k p_k=4a,\qquad
\sum_{k=0}^4\binom{k}{2}p_k=6b.
\]
For \(r\le b_0\), only multiplicities \(0,1,2\) have positive area. Solving these two equations together with \(\sum p_k=1\) gives the first distribution row. For \(b_0\le r\le\pi/2\), the support-function argument makes \(p_0=0\) and the zero-sum argument makes \(p_4=0\); solving the same equations for \(p_1,p_2,p_3\) gives the second row.

For any \(r\), \(\arccos((-x)\cdot v_i)=\pi-\arccos(x\cdot v_i)\), so away from zero-area boundaries one has \(K_r(x)=4-K_{\pi-r}(-x)\). Uniform area is invariant under the antipodal map, proving \(p_k(r)=p_{4-k}(\pi-r)\). This proves the complete formula, including \(r=0,\pi\).

**4. Sharp contact exponents.** At a two-cap tangency point, let \(s\) be the local tangent coordinate along the common tangent and \(u\) the transverse coordinate. The small-circle boundaries have geodesic curvature \(\kappa=\cot r_0=1/\sqrt2\). When \(r=r_0+\varepsilon\), their overlap has transverse width \(2\varepsilon-\kappa s^2+o(\varepsilon+s^2)\) on \(|s|\le\sqrt{2\varepsilon/\kappa}(1+o(1))\). Consequently
\[
L(r_0+\varepsilon)\sim
\int_{-\sqrt{2\varepsilon/\kappa}}^{\sqrt{2\varepsilon/\kappa}}
(2\varepsilon-\kappa s^2)\,ds
=\frac83\sqrt{\frac2\kappa}\,\varepsilon^{3/2}
=\frac83\,2^{3/4}\varepsilon^{3/2}.
\]
As \(p_2=6L/(4\pi)\) just above \(r_0\), the asserted first coefficient follows.

For the covering transition consider any of the four equality points \(w=-v_i\). The three other cap centers are at angular distance \(b_0\) from \(w\), and their unit tangent directions at \(w\) form angles of \(120^\circ\): the projected tangent vectors are \((v_j+v_i/3)/\sin b_0\) for \(j\ne i\), whose mutual dot products equal \(-1/2\). In geodesic normal coordinates \(t\) at \(w\), their distance functions are \(b_0-u_j\cdot t+O(|t|^2)\). For radius \(b_0-\varepsilon\), the local uncovered region rescales under \(t=\varepsilon y\) to the equilateral triangle \(u_j\cdot y<1\) with inradius \(1\). Its area is \(3\sqrt3\). For radius \(b_0+\varepsilon\), the new threefold-covered region rescales to the reflected triangle \(u_j\cdot y>-1\), with the same area. Smoothness and isolation of the four contact points imply that each patch has spherical area \(3\sqrt3\varepsilon^2+o(\varepsilon^2)\). Dividing their sum by \(4\pi\) proves the two quadratic laws. This completes the analytic proof.

## Verification

The standalone `VERIFY.py` recomputes the spherical lens formula, verifies normalization and the first moment at fifteen radii, compares the full five-state distribution against deterministic equal-area spherical samples at interior radii, and checks numerically both critical coefficients. These checks are corroborative only: the proof above, including the two limiting coefficients, applies to all real radii and does not depend on finite sampling.

## Relationship to prior work

Tarnai, Fowler and Kabai (2003) study spherical circle packing of rigid tetrahedral quartets and discuss the intermediate uncovered-area objective; they do not present a full five-state area-multiplicity distribution across all cap radii. Finch (2015) studies the *random-center* probability of complete coverage by four caps, an inequivalent probabilistic model. A later published published-finding corpus finding gives a third-order intersection integral for spherical caps on regular simplices in sphere dimension at least three (its parameter \(n\ge4\)); its hypotheses exclude the present \(S^2\) tetrahedral case and it does not yield this five-state law or the dual quadratic gap/triple handoff. Classical two-cap intersection formulas, including a SIGGRAPH 2006 course description, provide the lens ingredient but not the tetrahedral multiplicity inversion or the simultaneous critical coefficients.

## Limitations

The result is for the fixed regular tetrahedral center set only and does not identify an optimum among irregular four-center configurations. It does not solve Finch's random-center coverage problem. A general formula for two-cap areas is prior art; novelty is asserted only for the complete tetrahedral cap-multiplicity and critical-transition statement, not for that ingredient or for known packing/covering radii. Closely related but unindexed equivalent formulas may exist; exhaustive bibliographic uniqueness and independent validation have not been established.

## References

1. T. Tarnai, P. W. Fowler, S. Kabai, “Packing of regular tetrahedral quartets of circles on a sphere,” *Proceedings of the Royal Society A* 459 (2003), 2847–2859, DOI: 10.1098/rspa.2003.1160. Public online date: 2003-09-10.
2. S. R. Finch, “Covering a Sphere with Four Random Circular Caps,” arXiv:1502.06931, first posted 2015-02-24.
3. “Exact third-order union formula at the first multiple-overlap threshold for simplex-centred spherical caps,” published-finding corpus, 2026-10-04, published record `2026/10/4/SCOPE-exact-third-order-union-formula-at-the-first-multiple-overlap-th--e4ea7f0caeb7`.
4. “Advanced Real-Time Rendering in 3D Graphics and Games,” SIGGRAPH 2006 course notes, Section 8.4.1 (pairwise spherical-cap intersection area).
