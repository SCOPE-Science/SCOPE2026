# Sharp local geodesic-length conditioning for ellipsoids near the round sphere

## Finding

Let \(E\subset\mathbb R^3\) be a centered ellipsoid with principal semiaxes \(a_i=1+\epsilon_i>0\), for \(i=1,2,3\), and suppose \(\rho(E)=\max_i|\epsilon_i|\) is small. For each pair \(i<j\), let \(L_{ij}\) be the length of the coordinate-plane section in the plane spanned by the corresponding principal axes; this section is a simple closed geodesic of \(E\). Define

\[
\Delta(E)=\max_{i<j}|L_{ij}-2\pi|.
\]

Then the sharp local inverse condition number at the unit sphere is

\[
\lim_{\eta\downarrow0}\ \sup\left\{\frac{\rho(E)}{\Delta(E)}:E\text{ is centered and }0<\rho(E)<\eta\right\}=\frac{3}{2\pi}.
\]

Equivalently, as \(E\) tends to the unit sphere, \(\rho(E)\le(3/(2\pi)+o(1))\Delta(E)\), and the leading constant cannot be decreased.

## Assumptions and scope

The ellipsoid is centered at the origin and its principal axes are fixed orthogonal coordinates. Its semiaxes are positive and sufficiently close to \(1\); no equality or distinctness assumption on the semiaxes is needed. The three observations are the lengths of the three coordinate-plane sections, not the full closed-geodesic length spectrum. The statement is local at the unit sphere and makes no global estimate for ellipsoids far from it.

## Proof

For positive \(a,b\) near \(1\), the perimeter of the ellipse with semiaxes \(a,b\) is

\[
L(a,b)=\int_0^{2\pi}\sqrt{a^2\sin^2 t+b^2\cos^2 t}\,dt.
\]

The integrand is smooth in \((a,b)\) on a compact neighborhood of \((1,1)\), so Taylor's theorem gives a uniform second-order remainder. Direct differentiation under the integral yields

\[
L(1,1)=2\pi,\qquad \partial_aL(1,1)=\int_0^{2\pi}\sin^2t\,dt=\pi,
\qquad \partial_bL(1,1)=\int_0^{2\pi}\cos^2t\,dt=\pi.
\]

Write \(\rho=\rho(E)\). Consequently, uniformly over the three pairs,

\[
L_{ij}=2\pi+\pi(\epsilon_i+\epsilon_j)+O(\rho^2).
\]

Each coordinate-plane reflection is an isometry of the ellipsoid. Its fixed-point set on the surface is the corresponding coordinate-plane section, which is therefore totally geodesic; the section is an embedded ellipse and hence a simple closed geodesic.

Define \(T:\mathbb R^3\to\mathbb R^3\) by

\[
T(\epsilon_1,\epsilon_2,\epsilon_3)
=(\epsilon_1+\epsilon_2,\epsilon_1+\epsilon_3,\epsilon_2+\epsilon_3).
\]

Writing \(s=T\epsilon\), the inverse is

\[
\epsilon_1=(s_{12}+s_{13}-s_{23})/2,\quad
\epsilon_2=(s_{12}+s_{23}-s_{13})/2,\quad
\epsilon_3=(s_{13}+s_{23}-s_{12})/2.
\]

Thus the operator norm from \(\ell_\infty^3\) to \(\ell_\infty^3\) is \(\|T^{-1}\|_{\infty\to\infty}=3/2\), and this value is attained for \(s=(1,1,-1)\). If \(M=\|T\epsilon\|_\infty\), then \(\rho\le(3/2)M\) and \(M\ge(2/3)\rho\). The perimeter expansion gives \(\Delta(E)=\pi M+O(\rho^2)\); the lower bound on \(M\) makes the remainder relative to \(M\) uniformly \(O(\rho)\). Hence the limiting supremum of \(\rho/\Delta(E)\) is \(\|T^{-1}\|_{\infty\to\infty}/\pi=3/(2\pi)\).

Sharpness follows by taking \(\epsilon=t(3/2,-1/2,-1/2)\) with nonzero \(t\to0\). Then \(T\epsilon=t(1,1,-1)\), so \(\rho=3|t|/2\) and \(\Delta(E)=\pi|t|+O(t^2)\). The ratio tends to \(3/(2\pi)\). If one restricts to ellipsoids with three distinct axes, arbitrarily small distinct-axis perturbations of this path give the same limiting ratio.

## Verification

The proof reduces to a Taylor expansion of a one-dimensional integral and the explicit inverse of a three-by-three linear map. The expansion is uniform because the perimeter integrand and its first two parameter derivatives are continuous near \((1,1)\). The sharpness path supplies an attaining direction for the limiting condition number. No finite numerical experiment is used as proof.

## Relationship to prior work

Máximo and Stufflebeam prove a qualitative stability theorem: if all simple closed geodesics on a strictly convex two-sphere have lengths close to \(2\pi\), the sphere is close to round in the \(C^0\) Cheeger–Gromov sense. The present claim is a separate, sharp local inverse calculation for the three reflection-plane geodesics in the ellipsoid family; it supplies an explicit condition number not stated in that qualitative theorem. Related work on ellipsoid normal multiplicity and random central-section radii uses different observables, and does not imply the three-geodesic length constant.

## Limitations

This is a local first-order stability law near the unit sphere, not a global inequality with an explicit remainder constant. It treats centered ellipsoids only and uses the three coordinate-plane geodesics singled out by reflection symmetry. It does not claim that three geodesic lengths control arbitrary convex surfaces. The general stability paper's full text was not available for inspection; its abstract and bibliographic record were checked, and this remains a limited overlap risk.

## References

1. Davi Máximo and Hunter Stufflebeam, “Stability of Convex Spheres,” arXiv:2312.13995, first publicly posted 21 December 2023; DOI: 10.1093/imrn/rnae275. https://arxiv.org/abs/2312.13995
