# Cheeger rigidity and two singular onsets for disk-clipped squares

## Finding

Let \(Q=[-1,1]^2\), \(B_R=\{x\in\mathbb R^2:\|x\|_2\le R\}\), and
\[
K_R=Q\cap B_R,\qquad 1\le R\le\sqrt2.
\]
For the ordinary planar Cheeger constant
\[
h(R)=\inf_{\substack{E\subseteq K_R\\0<|E|<\infty}}
\frac{P(E)}{|E|},
\]
with full Euclidean perimeter and measurable finite-perimeter competitors, set
\[
t_\square=\frac{2}{2+\sqrt\pi},\qquad
R_*=\sqrt2-(\sqrt2-1)t_\square.
\]
Numerically \(t_\square\approx0.5301589043\) and \(R_*\approx1.1946145540\).

**Exact profile and structural plateau.** For every \(R\in[R_*,\sqrt2]\),
\[
\boxed{h(R)=\frac1{t_\square}=1+\frac{\sqrt\pi}{2}}.
\]
The unique Cheeger set is independent of \(R\) on this entire interval and equals the square's rounded Cheeger set. For \(1<R<R_*\), write \(h(R)=1/t(R)\), where \(t(R)\in(1/2,t_\square)\) is characterized uniquely by
\[
\boxed{
4a\sqrt{b^2-a^2}
+4b^2\left(\arcsin\frac ab-\frac\pi4\right)
=\pi t^2,
\quad a=1-t,\quad b=R-t.
}
\]
Throughout this branch \(a<b<\sqrt2a\), and \(h(R)\) is strictly decreasing.
The disk endpoint has \(h(1)=2\).

**Distinct sharp onset laws.** As \(R\downarrow1\),
\[
t(R)=\frac R2-\frac8{3\pi}(R-1)^{3/2}+O((R-1)^{5/2}),
\]
equivalently
\[
h(R)=\frac2R+\frac{32}{3\pi}(R-1)^{3/2}
+O((R-1)^{5/2}).
\]
As \(R\uparrow R_*\) from below,
\[
t_\square-t(R)=\frac{(R_*-R)^2}{\sqrt\pi}
+O((R_*-R)^3),
\]
and hence
\[
h(R)-\frac1{t_\square}
=\frac{(2+\sqrt\pi)^2}{4\sqrt\pi}(R_*-R)^2
+O((R_*-R)^3).
\]
In particular, \(h\) is continuously differentiable but not twice differentiable at \(R_*\), and the plateau starts at the exact threshold above.

## Assumptions and scope

All sets are planar; the host is the centered intersection of a unit half-side square with a centered disk of radius \(R\in[1,\sqrt2]\). The Cheeger constant uses the full perimeter (not relative perimeter). Equalities at the two endpoints are included. The uniqueness and inner-parallel characterization of Cheeger sets for planar convex domains are used as classical input; this paper calculates their shape-dependent consequences for the clipped-square family.

## Proof

**1. Inner parallel sets and Cheeger radius.** For a compact convex planar body \(K\), write
\[
K_{-t}=\{x:x+tB_1\subseteq K\}.
\]
The convex Cheeger theorem of Kawohl and Lachand-Robert yields a unique \(t=h(K)^{-1}\) such that \(|K_{-t}|=\pi t^2\), and the unique Cheeger set is \(K_{-t}+tB_1\). Erosion distributes over intersections, and the erosions of a square and disk are explicit:
\[
(K_R)_{-t}=[-(1-t),1-t]^2\cap B_{R-t},
\qquad 0<t<1.
\]
Let \(a=1-t\) and \(b=R-t\). Define \(F_R(t)=|[-a,a]^2\cap B_b|-\pi t^2\). The first term is continuous and nonincreasing with \(t\), while the second is strictly increasing, so \(F_R\) is strictly decreasing. At \(t=0\) it is positive and at the inradius \(t=1\) it is negative. Thus the unique Cheeger radius is the unique zero in \((0,1)\).

**2. Area of the clipped inner square.** For \(a<b<\sqrt2a\), cut the centered square into four congruent quadrants. Writing \(c=\sqrt{b^2-a^2}\), each quadrant has area
\[
ac+\int_c^a\sqrt{b^2-x^2}\,dx
=ac+b^2\left(\arcsin(a/b)-\pi/4\right).
\]
The second equality follows from the elementary circular-antiderivative formula, evaluated at \(c\) and \(a\). Four quadrants give the announced root equation. If \(b\ge\sqrt2a\) the inner intersection is the entire square and its area is \(4a^2\); if \(b\le a\) it is the entire disk and its area is \(\pi b^2\).

**3. Exact retention threshold and strict change below it.** For the full square, the unique Cheeger radius solves \(4(1-t)^2=\pi t^2\), namely \(t=t_\square\). Its inner square \([-(1-t_\square),1-t_\square]^2\) lies in \(B_{R-t_\square}\) precisely when \(R-t_\square\ge\sqrt2(1-t_\square)\), that is \(R\ge R_*\). Thus the same \(t_\square\) solves the eroded-area equation for all such \(R\). The eroded inner set, and hence its Minkowski sum with \(t_\square B_1\), is literally independent of \(R\) on that interval.

When \(1<R<R_*\), clipping the square's eroded corners at \(t_\square\) makes \(F_R(t_\square)<0\), so its unique root \(t(R)<t_\square\). Since \(K_R\) properly contains the unit disk for \(R>1\), at \(t=1/2\) its erosion properly contains the radius-\(1/2\) disk, giving \(F_R(1/2)>0\) and \(t(R)>1/2\). For the root \(t(R)\), one has \(b-a=R-1>0\) and
\[
\sqrt2 a-b=(R_*-R)+(\sqrt2-1)(t_\square-t(R))>0,
\]
so exactly the intermediate formula applies. Strict inclusion of the inner clipped disks before saturation shows \(F_{R_2}(t(R_1))>F_{R_1}(t(R_1))=0\) whenever \(1<R_1<R_2<R_*\). Hence \(t(R_2)>t(R_1)\), establishing strict decrease of \(h\).

**4. The disk-end cap singularity.** Let \(\delta=R-1\downarrow0\), \(t=t(R)\), and \(\varepsilon=R/2-t\ge0\). The inner disk radius is \(b=R-t\), and the square side lies a distance \(a=1-t=b-\delta\) from its center. The amount removed by four side caps is
\[
L_{\rm side}=\frac{16}{3}\sqrt{2b}\,\delta^{3/2}
+O(\delta^{5/2}),
\]
by integrating the circular-segment width \(2\sqrt{b^2-x^2}\) over the cap height \(\delta\); for small \(\delta\) these four caps are disjoint. The Cheeger area equation becomes
\[
\pi(b^2-t^2)=L_{\rm side},
\qquad b^2-t^2=2R\varepsilon.
\]
As \(R\downarrow1\), continuity of the unique root gives \(t\to1/2\), hence \(b\to1/2\). Consequently
\[
\varepsilon=\frac8{3\pi}\delta^{3/2}
+O(\delta^{5/2}).
\]
Inverting \(h=1/t\) gives the stated expansion.

**5. The quadratic corner-activation singularity.** Put \(\delta=R_*-R\downarrow0\) and \(\Delta=t_\square-t(R)\). Define the positive corner depth
\[
d=\sqrt2a-b=\delta+(\sqrt2-1)\Delta.
\]
Elementary expansion of the circle near each square corner shows that the four removed corner regions have total area \(4d^2+O(d^3)\). Indeed, to first order the tangent line removes a right isosceles corner triangle with legs \(\sqrt2d\), hence area \(d^2\) per corner. The Cheeger equation is therefore
\[
4(1-t)^2-\pi t^2=4d^2+O(d^3).
\]
Since \(4(1-t_\square)^2=\pi t_\square^2\), Taylor expansion on the left gives \(4\sqrt\pi\,\Delta+O(\Delta^2)\). Therefore \(\Delta=O(\delta^2)\), followed by \(d=\delta+O(\delta^2)\) and
\[
\Delta=\delta^2/\sqrt\pi+O(\delta^3).
\]
The expansion of \(1/t\), together with the exact constant plateau for \(R\ge R_*\), proves the claimed differentiability transition.

## Verification

The standalone `verify.py` uses high-precision arithmetic to evaluate the eroded-area equation at nine parameters including both endpoints and the plateau, tests both leading asymptotic constants over five decreasing perturbation scales, and independently integrates the circular-quadrant formula at selected intermediate points. It reports `VERIFY_OK clipped-square Cheeger profile; inner area, quadrature and both asymptotic constants` when all assertions pass. These checks are finite corroboration; the proof for the whole parameter interval is analytic and uses the stated planar convex Cheeger theorem.

## Relationship to prior work

Kawohl and Lachand-Robert's convex Cheeger construction gives the implicit inner-area equation and the rounded-square value. Cañete's work establishes planar rotationally symmetric Cheeger methods; it does not identify the exact plateau and two endpoint singularities for the intersection of a square with a centered expanding disk. Ftouhi, Masiello, and Paoli develop sharp shape inequalities for the usual Cheeger constant and study spherical slices, but their inspected treatment does not give this two-strip intersection profile. A related indexed theorem solves a *different* circumradius/area subset-functional over a square, not the ordinary Cheeger quotient on the clipped square.

This result specializes the established convex Cheeger characterization to a geometrically natural disk-to-square deformation, proving the exact first parameter where the Cheeger set stops changing and identifying two different singular boundary-layer exponents. It is not asserted that the general Cheeger characterization or the square's value is new.

## Limitations

The exact formula is specialized to a centered disk intersected with a square and to the Euclidean plane. The interior formula is implicit in the unique scalar root, not an elementary closed expression for that root. The two expansions are local, not uniform remainder bounds across all radii. The general Cheeger characterization is an input theorem. Related material could occur under an alternative naming of corner-truncated or rounded squares; publication priority and independent validation have not been certified.

## References

B. Kawohl and T. Lachand-Robert, “Characterization of Cheeger sets for convex subsets of the plane,” Pacific Journal of Mathematics 225 (2006), 103–118.

A. Cañete, “Cheeger Sets for Rotationally Symmetric Planar Convex Bodies,” Results in Mathematics 77 (2022), article 9, DOI 10.1007/s00025-021-01539-7; first publicly available online 2021-11-06.

I. Ftouhi, A. L. Masiello and G. Paoli, “Sharp inequalities involving the Cheeger constant of planar convex sets,” arXiv:2206.13158, first public submission 2022-06-27.
