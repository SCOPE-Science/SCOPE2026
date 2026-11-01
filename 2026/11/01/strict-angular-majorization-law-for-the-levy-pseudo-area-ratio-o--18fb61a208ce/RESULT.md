# Strict angular-majorization law for the Levy pseudo-area ratio of cyclic symmetric hexagons

## Finding

Let \(H\) be any nondegenerate convex cyclic centrally symmetric Euclidean hexagon, with area \(A\), perimeter \(L\), and successive side lengths \(a_1,\ldots,a_6\). Its Levy pseudo-area is
\[
P=\frac{L^2}{4}\sqrt{\prod_{i=1}^6\left(1-\frac{2a_i}{L}\right)}.
\]
There is a unique triple of positive *half-central gap angles* \((x,y,z)\), up to cyclic ordering, such that the central gaps are \((2x,2y,2z,2x,2y,2z)\), with \(x+y+z=\pi/2\). Define \(\Phi(x,y,z)=A/P\). The function \(\Phi\) is **strictly Schur-convex** on this angle simplex: holding the sum of any two coordinates fixed, replacing them by their average strictly decreases \(\Phi\) unless they are already equal. In particular,
\[
\boxed{\frac{9\sqrt3}{16}\le\frac AP<1.}
\]
The lower bound is attained exactly for regular hexagons, while one is the unattained sharp upper bound. Every number in \([9\sqrt3/16,1)\) is attained. This is a global statement for all cyclic centrally symmetric convex hexagons, not a neighborhood-of-regular result.

## Assumptions and scope

The hexagon has six distinct vertices in convex cyclic order on a circle of positive radius \(R\); opposite vertices are antipodal. This gives three positive half-gaps \(x,y,z\) with sum \(\pi/2\). No fixed perimeter or area is required. Coincident-vertex limits are used only for sharpness of the strict upper bound, not claimed to be nondegenerate hexagons. The Schur order here concerns *half-central gaps*, not the six side lengths or the perimeter.

## Proof

**1. Exact reduction.** Put \(s_x=\sin x\), \(s_y=\sin y\), \(s_z=\sin z\), and \(S=s_x+s_y+s_z\). Each of the three side lengths \(2R s_x\), \(2R s_y\), \(2R s_z\) occurs twice, so \(L=4RS\) and
\[
P=\frac{4R^2(S-s_x)(S-s_y)(S-s_z)}{S}.
\]
The shoelace formula gives \(A=R^2(\sin2x+\sin2y+\sin2z)=4R^2\cos x\cos y\cos z\), using \(2x+2y+2z=\pi\). Thus the *exact* angle function is
\[
\Phi(x,y,z)=\frac{S\cos x\cos y\cos z}{(s_x+s_y)(s_y+s_z)(s_z+s_x)}.
\tag{1}
\]
Every factor in the denominator is strictly positive in the open simplex.

**2. Two-angle smoothing.** Keep \(z\) and \(x+y\) fixed. Write
\[
m=\frac{x+y}{2},\quad d=\frac{x-y}{2},\quad u=\sin m,\quad v=\cos m,\quad q=\cos d,\quad c=\cos2m=1-2u^2.
\]
Since \(0<m<\pi/4\) and \(|d|<m\), we have \(0<u<1/\sqrt2\), \(0<c<1\), and \(v<q\le1\). Formula (1) simplifies exactly to
\[
\Phi=v\,\frac{(2uq+c)(q^2-u^2)}{q\,[q^2-v^2+2cuq+c^2]}.
\tag{2}
\]
The bracket is \((\sin x+c)(\sin y+c)>0\). Define
\[
B(u,q)=(4u^2-1)q^2-2uq+4u^4-3u^2.
\]
Direct polynomial differentiation of (2), with \(u\) fixed, yields
\[
\frac{\partial\Phi}{\partial q}
=\frac{v c(q-u)^2 B(u,q)}{q^2[q^2-v^2+2cuq+c^2]^2}.
\tag{3}
\]
Here \(q>v>u\), so every factor except \(B\) is positive. If \(0<u\le1/2\), the coefficients of \(q^2\), \(-2uq\), and the remaining \(u^2(4u^2-3)\) are all nonpositive, with strict negativity overall. If \(1/2<u<1/\sqrt2\), use \(0<q\le1\) to obtain
\[
B(u,q)\le q(4u^2-2u-1)+u^2(4u^2-3)<0,
\]
because \(4u^2-2u-1<0\) and \(4u^2-3<0\) on this interval. Thus (3) is strictly negative. Equalizing the two angles raises \(q=\cos|d|\) to one and strictly decreases \(\Phi\) unless \(d=0\). The same argument applies to every coordinate pair, proving strict Schur-convexity on the fixed-sum open simplex.

**3. Sharp extrema and range.** Repeated pairwise averaging moves every triple toward \((\pi/6,\pi/6,\pi/6)\), never increasing \(\Phi\), with a strict decrease unless already equal. Formula (1) gives \(\Phi(\pi/6,\pi/6,\pi/6)=9\sqrt3/16\). Conversely, from any positive triple choose its largest and smallest entries and transfer the entire smaller entry into the larger while keeping the third unchanged. The strict two-angle result increases \(\Phi\), and the endpoint has one zero angle. Whenever \(x=0\), \(y+z=\pi/2\), \(y,z>0\), the continuous boundary extension of (1) is
\[
\Phi(0,y,z)=\cot y\cot z=1.
\]
Therefore every genuine hexagon has \(\Phi<1\). Letting \(x\downarrow0\) while \(y=z=(\pi/2-x)/2\) makes \(\Phi\uparrow1\); the lower equality occurs only at the regular triple. Continuity along this path gives the complete range \([9\sqrt3/16,1)\).

## Verification

The companion file `levy_hexagon_checker.py` uses only Python's standard library. Execute `python levy_hexagon_checker.py`. It independently verifies the exact *polynomial* identity underlying (3), checks the sign at 675 exact rational pairs in the admissible region, and compares analytic and coordinate-shoelace formulas plus averaging inequalities on 1,200 deterministic randomly generated angle triples (3,600 numerical comparisons). Its successful output is `PASS: polynomial identity; 4275 exact sign and numerical diagnostics`. The rational grid and floating-point diagnostics are finite checks; the proof of the universal sign rests on the explicit interval argument following (3), not on any grid.

## Relationship to prior work

Paul Levy's pseudo-area comparison conjectures a regular-polygon lower endpoint and an upper endpoint of one for cyclic polygons with more than four sides. Chouikha's 2026 papers study special subdivisions, two-length polygons and deformations near regular polygons; neither inspected statement provides strict Schur-convexity on the full three-independent-gap centrally symmetric hexagon family. Dulio and Laeng's 2021 cyclic-polygon area formulas are compatible with (1), but a symmetric area identity does not imply the directional derivative sign (3). Classical studies by Zhang of pseudo-perimeter bounds and Schur-convex isoperimetric inequalities are especially relevant; only their bibliographic descriptions and available abstracts could be examined, so precise historical priority relative to those works remains an explicit risk. The novelty claim concerns the **three-gap monotonicity and its sharp global consequences in this family**, not the definition of pseudo-area, the known regular value, or general Schur-convexity theory.

## Limitations

This theorem addresses only cyclic centrally symmetric convex *hexagons*, not general cyclic hexagons or larger polygons. Schur-convexity is asserted for half-central gaps and does not imply the same property for edge lengths under a fixed-perimeter constraint. The bound one is a supremum, not an attained value. Full historical-priority verification against certain older journal articles is incomplete, and independent mathematical validation has not been performed.

## References

1. A. R. Chouikha, *Paul levy's Isoperimetric Problems on cyclic polygons*, first posted 2026-07-08, arXiv:2607.07095, https://arxiv.org/abs/2607.07095.
2. A. R. Chouikha, *Isoperimetric Problems on cyclic polygons*, first posted 2026-09-01, arXiv:2609.00963, https://arxiv.org/abs/2609.00963.
3. P. Dulio and E. Laeng, *Generalization of Heron's and Brahmagupta's equalities to any cyclic polygon*, Aequationes Mathematicae 95 (2021), 941–952, https://doi.org/10.1007/s00010-020-00771-w.
4. X.-M. Zhang, *Bonnesen-style inequalities and pseudo-perimeters for polygons*, Journal of Geometry 60 (1997), 188–201, https://doi.org/10.1007/BF01252226.
5. X.-M. Zhang, *Schur-convex functions and isoperimetric inequalities*, Proceedings of the AMS 126 (1998), 461–470, https://doi.org/10.1090/S0002-9939-98-04151-3.
6. P. Levy, *Le problème des isopérimètres et des polygones articulés*, Bulletin des Sciences Mathématiques 90 (1966), 103–112.
