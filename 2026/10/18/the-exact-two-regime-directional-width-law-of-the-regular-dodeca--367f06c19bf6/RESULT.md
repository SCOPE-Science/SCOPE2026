# The exact two-regime directional-width law of the regular dodecahedron

## Finding
Let \(D\) be the centered regular dodecahedron whose twenty vertices are
\[
(\pm1,\pm1,\pm1),\qquad
(0,\pm\varphi^{-1},\pm\varphi),\qquad
(\pm\varphi^{-1},\pm\varphi,0),\qquad
(\pm\varphi,0,\pm\varphi^{-1}),
\]
where \(\varphi=(1+\sqrt5)/2\), with all indicated signs independent. Its circumradius is \(r=\sqrt3\), and its edge length is \(2/\varphi\). For \(U\) uniformly distributed on the unit sphere, define the width
\[
W=h_D(U)+h_D(-U),\qquad h_D(u)=\max_{v\in D}\langle u,v\rangle.
\]
Set
\[
q=\varphi^{-2}=\frac{3-\sqrt5}{2},\qquad
s=\frac{w}{2\sqrt3},\qquad
s_0=\frac1{\sqrt{1+4q^2}},\qquad
s_1=\frac1{\sqrt{1+q^2}}.
\]
**The width has a continuous distribution supported exactly on**
\( [2\sqrt3s_0,2\sqrt3] \), **with probability density**
\[
f_W(w)=
\begin{cases}
0,&s<s_0\text{ or }s>1,\\
\displaystyle\frac5{\sqrt3}\left[1-\frac3\pi\arccos\!\left(\frac{qs}{\sqrt{1-s^2}}\right)\right],&s_0\le s<s_1,\\
\displaystyle\frac5{\sqrt3},&s_1\le s\le1.
\end{cases}
\tag{1}
\]
The values assigned to a density at individual endpoints are immaterial.

For a closed-form cumulative distribution, write
\[
\beta(s)=\arccos\!\left(\frac{qs}{\sqrt{1-s^2}}\right),\qquad
z(s)=\sqrt{1-(1+q^2)s^2}
\]
when \(s_0\le s\le s_1\). Then
\[
\Pr(W\le w)=
\begin{cases}
0,&s\le s_0,\\
\displaystyle 10s-9+\frac{30}{\pi}\left[\arctan\!\left(\frac{z(s)}q\right)-s\beta(s)\right],&s_0<s<s_1,\\
10s-9,&s_1\le s<1,\\
1,&s\ge1.
\end{cases}
\tag{2}
\]
Thus the upper part of the width law is **exactly uniform**, not merely asymptotically so:
\[
\Pr(W\ge w)=10\left(1-\frac{w}{2\sqrt3}\right)
\quad(2\sqrt3s_1\le w\le2\sqrt3),
\tag{3}
\]
with upper-branch probability \(10(1-s_1)\approx0.658276410373\). The only interior transition is at \(w=2\sqrt3s_1\). The lower endpoint is approximately \(2.752763840942\), and the transition is approximately \(3.236067977500\).

## Assumptions and scope
The body is the **solid** Euclidean regular dodecahedron, and \(U\) is uniform for normalized spherical area measure \(d\sigma/(4\pi)\). Width is the **one-dimensional orthogonal projection length** along the specified direction. Scaling \(D\) by a positive factor scales both the random width and both endpoints by that factor. Formulas (1)--(3) apply to every similar regular dodecahedron after this scaling. They do not describe its chord-length distribution, random planar projection area, or widths under nonuniform direction sampling.

## Proof
**1. Reduction to one normal cell.** The vertex set is centrally symmetric, so \(W(u)=2h_D(u)\). Every vertex has norm \(\sqrt3\) and precisely three adjacent vertices. For example, \(v=(1,1,1)\) is adjacent to \((0,\varphi^{-1},\varphi)\) and its cyclic coordinate permutations; for each neighbor \(v'\),
\[
\langle v,v'\rangle=\sqrt5,\qquad
\frac{\langle v,v'\rangle}{\|v\|\,\|v'\|}=\frac{\sqrt5}{3}.
\tag{4}
\]
The spherical normal cell \(C_v\) consists of the directions where \(v\) maximizes the support function. Because \(v\) is a simple vertex, the three edge inequalities \(\langle u,v-v'\rangle\ge0\) cut out the entire normal cell. The twenty cells have disjoint interiors and cover the unit sphere.

Let \(n=v/\sqrt3\) be the cell center. The three great-circle sides lie at a common spherical distance \(\rho\) from \(n\), and their outward tangent directions differ by \(2\pi/3\). The bisector of two equal-radius vertex directions separated by angle \(\gamma\) is at distance \(\gamma/2\), so (4) gives
\[
\tan\rho
=\tan\left(\frac12\arccos\frac{\sqrt5}{3}\right)
=\sqrt{\frac{3-\sqrt5}{3+\sqrt5}}=q.
\tag{5}
\]
It follows that the greatest angular distance of a point of \(C_v\) from \(n\) is \(\rho_*=\arctan(2q)\), whereas the shortest angular distance to a side is \(\rho=\arctan q\).

**2. Angular aperture of the cell.** Use spherical polar coordinates \((\theta,\psi)\) centered at \(n\). The three side inequalities can be written, after rotating azimuths, as
\[
\sin\rho\cos\theta+\cos\rho\sin\theta
\cos(\psi-2\pi j/3)\ge0,
\qquad j=0,1,2.
\tag{6}
\]
For \(0\le\theta<\rho\) all azimuths satisfy (6). For \(\rho\le\theta\le\rho_*\), each inequality excludes an interval of azimuths of angular length
\[
2\beta_\theta,
\qquad \beta_\theta
=\arccos\!\bigl(q\cot\theta\bigr).
\tag{7}
\]
Their centers are separated by \(2\pi/3\), and \(0\le\beta_\theta\le\pi/3\), so the excluded intervals have disjoint interiors. At \(\theta=\rho_*\) they cover all azimuths, and for larger \(\theta\) there are no admissible directions. The allowed azimuthal aperture is therefore **exactly**
\[
L(\theta)=
\begin{cases}
2\pi,&0\le\theta\le\rho,\\
2\pi-6\arccos(q\cot\theta),&\rho<\theta<\rho_*,\\
0,&\theta\ge\rho_*.
\end{cases}
\tag{8}
\]
Because \(h_D(u)=\sqrt3\cos\theta\) on this cell, \(w=2\sqrt3\cos\theta\). Each of the twenty cells contributes the same angular measure, and \(d\sigma=\sin\theta\,d\theta\,d\psi\). The density transformation gives
\[
f_W(w)=\frac{20}{4\pi}\frac{L(\theta)}{2\sqrt3}
=\frac5{2\pi\sqrt3}L(\theta).
\tag{9}
\]
Substituting \(\cot\theta=s/\sqrt{1-s^2}\), \(\cos\rho=s_1\), and \(\cos\rho_*=s_0\) into (8)--(9) proves the exact density (1). The cell tiling shows that it integrates to one and has no atoms.

**3. Exact integration.** On the nonconstant branch, the auxiliary function \(\beta(s)\) satisfies
\[
\beta'(s)=-\frac q{(1-s^2)\sqrt{1-(1+q^2)s^2}}.
\tag{10}
\]
A direct differentiation, using \(q^2+z(s)^2=(1+q^2)(1-s^2)\), yields
\[
\frac d{ds}\left[\arctan\!\left(\frac{z(s)}q\right)-s\beta(s)\right]
=-\beta(s).
\tag{11}
\]
Integrating (1), matching at \(s_1\), and using normalization at the lower endpoint establishes (2). For \(s\ge s_1\), the density is constant, giving (3). The claimed support and unique interior transition follow from (8).

## Verification
Run `python3 verify.py` using only the Python standard library. The checker constructs all twenty vertex coordinates and confirms three neighbors and dot product \(\sqrt5\) at every vertex. It differentiates the cumulative formula numerically, integrates the proposed density independently, and compares its second moment (rescaled to unit edge) with the previously recorded exact value
\[
\mathbb E W_{\text{unit-edge}}^2
=\frac{3+\sqrt5}{2}+\frac{10}{\pi}\sqrt{1+\frac2{\sqrt5}}.
\tag{12}
\]
It also samples width directly from the support function on a deterministic 120,000-point Fibonacci sphere grid, comparing eleven distribution thresholds. The checks returned `VERIFY_OK`. Finite grid sampling and quadrature verify the calculations but do not establish equations (1)--(3); their proof is given above.

## Relationship to prior work
Finch (arXiv:1110.0671, initially public 4 October 2011) computed the mean and second moment for the regular tetrahedron and cube, and explicitly noted the density question in that setting. Kabluchko, Litvak and Zaporozhets (arXiv:1511.08479) treated regular cube, simplex and crosspolytope projection-length moments, not the full dodecahedral law. An earlier exact calculation of **the dodecahedron's second width moment** provides equation (12) but explicitly does not supply its full width distribution. A general polyhedral width-density coarea framework (Abas, arXiv:2609.26202, 2026) supplies abstract angular-aperture machinery; the accessible abstract identifies explicit examples for other bodies, not a two-branch closed formula for the regular dodecahedron. This result evaluates the particular dodecahedral normal fan to a closed elementary CDF and density. The generic theory is pertinent prior machinery and is not claimed as novel here.

## Limitations
Only **uniform-direction** widths of the regular dodecahedron are classified. The result makes no statement about joint width--shadow statistics, general icosahedral deformations, or other polyhedra. The 2026 general polyhedral framework's full 92-page text could not be inspected in this comparison; it remains an originality-priority risk whether it records the exact dodecahedral special case beyond its accessible abstract. Historic stereological tables indexed under caliper/Feret diameter terminology may also contain an equivalent formula. No independent external audit has been performed.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671; first version 4 October 2011; full text inspected at `https://arxiv.org/pdf/1110.0671`.
2. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, first version 26 November 2015; full text inspected at `https://arxiv.org/pdf/1511.08479`.
3. *Mean-square widths of all five Platonic solids*, public mathematical result, 11 October 2026, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mean-square-widths-of-all-five-platonic-solids--a3835a8d344f`.
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first public August 2026; abstract inspected at `https://arxiv.org/abs/2609.26202`.
