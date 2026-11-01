# A unique singular-weight perimeter minimizer among anchored rectangles

## Finding
Fix \(0<\alpha<1\) and let \(Q_t=[-t,t]\times[-1,1]\) for \(0<t\le1\). The radial weighted boundary length is
\[
E_\alpha(t)=\int_{\partial Q_t}\|x\|_2^{-\alpha}\,d\mathcal H^1(x).
\]
The class comprises all centered, axis-aligned nondegenerate rectangles whose larger half-side equals one, up to a coordinate exchange. **Exactly one aspect ratio \(t_\alpha\in(0,1)\) minimizes \(E_\alpha\)**. More precisely, \(E_\alpha\) strictly decreases on \((0,t_\alpha)\) and strictly increases on \((t_\alpha,1]\); consequently neither the square nor the degenerate segment minimizes the continuous extended functional.

Let
\[
H_\alpha(t)=\alpha\left(\frac{\sqrt{1+t^2}}t\right)^\alpha
 \int_0^{\arctan(1/t)}\cos^\alpha u\,du.
\]
The optimum is characterized by the **unique** solution \(H_\alpha(t_\alpha)=1\) in \((0,1)\). As the exponent varies, \(\alpha\mapsto t_\alpha\) is real analytic and strictly increasing, with limits zero and one at the endpoints. The sharp endpoint laws are
\[
t_\alpha=\frac12\left(\frac{\pi\alpha}{2}\right)^{1/\alpha}
 (1+O(\alpha))\quad(\alpha\downarrow0)
\]
and
\[
1-t_\alpha=\sqrt2\operatorname{artanh}(1/\sqrt2)(1-\alpha)
 +O((1-\alpha)^2)\quad(\alpha\uparrow1).
\]
In particular, the optimal aspect ratio emerges from the needle with an essential singularity rather than an ordinary power law. For example, \(t_{1/2}=0.310152114794695595\ldots\).

## Assumptions and scope
The ambient plane has its standard Euclidean metric. The radial weight is centered at the origin, not translated with a rectangle, and its exponent lies in the **full locally integrable singular range** \(0<\alpha<1\). Rectangles are centered and axis aligned and are normalized to have larger Euclidean coordinate half-side one; scaling any rectangle by \(s>0\) multiplies its energy by \(s^{1-\alpha}\). No fixed-area or fixed-ordinary-perimeter constraint is asserted.

For the limiting segment \(Q_0=\{0\}\times[-1,1]\), define its weighted boundary energy with multiplicity two, in agreement with the Hausdorff limit of nondegenerate rectangles:
\[
E_\alpha(0)=2\int_{-1}^1|y|^{-\alpha}\,dy=\frac4{1-\alpha}.
\]
The theorem optimizes continuously over the compact class \(0\le t\le1\), and its unique optimizer is nondegenerate.

## Proof
**1. Boundary integration.** Each of the two vertical sides and two horizontal sides contributes symmetrically. Direct arclength integration yields, for \(0<t\le1\),
\[
\frac{E_\alpha(t)}4
=\int_0^1(t^2+y^2)^{-\alpha/2}\,dy
 +\int_0^t(1+x^2)^{-\alpha/2}\,dx.\tag{1}
\]
Because \(\alpha<1\), dominated convergence on the vertical integral, together with the vanishing second term, gives the stated continuous extension at \(t=0\). Differentiation under the integral for \(t>0\) gives
\[
\frac{E_\alpha'(t)}4=(1+t^2)^{-\alpha/2}
 -\alpha t\int_0^1(t^2+y^2)^{-1-\alpha/2}\,dy.\tag{2}
\]
Substituting \(y=t\tan u\) into the last integral with \(\theta=\arctan(1/t)\) yields
\[
E_\alpha'(t)=4(1+t^2)^{-\alpha/2}[1-H_\alpha(t)].\tag{3}
\]
This identity fixes the sign and normalization of every derivative used below.

**2. Unique global minimizer.** Writing
\[
\mathcal H(\alpha,\theta)=\alpha(\cos\theta)^{-\alpha}
\int_0^\theta(\cos u)^\alpha du,
\qquad \theta\in[\pi/4,\pi/2),
\]
one obtains by direct differentiation
\[
\partial_\theta\mathcal H=\alpha+\alpha\tan\theta\,\mathcal H>0.\tag{4}
\]
Since \(\theta(t)=\arctan(1/t)\) is strictly decreasing in \(t\), \(H_\alpha(t)\) is strictly decreasing. The positive finite integral in (4) gives \(\lim_{t\downarrow0}H_\alpha(t)=+\infty\). For fixed \(\theta\), use
\[
\mathcal H(\alpha,\theta)=\alpha\int_0^\theta
 \left(\frac{\cos u}{\cos\theta}\right)^\alpha du.
\tag{5}
\]
Every ratio in the integrand is at least one, so (5) is strictly increasing with \(\alpha>0\). Directly, \(\mathcal H(1,\theta)=\tan\theta\); hence
\[
H_\alpha(1)<H_1(1)=1\quad (0<\alpha<1).\tag{6}
\]
Intermediate-value continuity, strict decrease, (6), and divergence at zero prove the unique \(t_\alpha\in(0,1)\). Equation (3) shows the energy is strictly decreasing before that point and strictly increasing after it, proving global uniqueness and strict inequalities at both endpoints.

**3. Exponent monotonicity and analyticity.** Equation (5) gives \(\partial_\alpha\mathcal H>0\), while (4) and \(\theta'(t)<0\) give \(\partial_tH_\alpha<0\). The implicit-function theorem applies at every root and gives
\[
\frac{dt_\alpha}{d\alpha}=-\frac{\partial_\alpha H_\alpha(t_\alpha)}{\partial_tH_\alpha(t_\alpha)}>0.
\tag{7}
\]
The defining integrals are jointly real analytic for positive \(t\) and \(\alpha\); consequently \(t_\alpha\) is real analytic. For each fixed \(t>0\), \(H_\alpha(t)\to0\) as \(\alpha\downarrow0\), forcing \(t_\alpha\downarrow0\). Likewise, at \(\alpha=1\), \(H_1(t)=1/t\), so the roots approach \(1\) as \(\alpha\uparrow1\).

**4. Essential-singularity endpoint.** Let
\[
C_\alpha=\int_0^{\pi/2}\cos^\alpha u\,du
=\frac{\sqrt\pi\,\Gamma((1+\alpha)/2)}{2\Gamma(1+\alpha/2)}.
\tag{8}
\]
The root equation is
\[
t_\alpha^\alpha=\alpha(1+t_\alpha^2)^{\alpha/2}
 \int_0^{\arctan(1/t_\alpha)}\cos^\alpha u\,du.\tag{9}
\]
Since the integral is at most \(C_\alpha\), and \(t_\alpha\le1\), one has
\[
t_\alpha\le(2\alpha C_\alpha)^{1/\alpha}
\]
for all sufficiently small \(\alpha\); thus \(t_\alpha\) is superalgebraically small. The missing cap of the integral in (9) is \(O(t_\alpha^{1+\alpha})\), uniformly for small \(\alpha\), and the square-root correction is \(1+O(\alpha t_\alpha^2)\). Consequently,
\[
\log t_\alpha=\frac{\log\alpha+\log C_\alpha}{\alpha}+o(1).\tag{10}
\]
By the gamma-function identity in (8), \(C_0=\pi/2\) and
\[
\log C_\alpha=\log(\pi/2)-\alpha\log2+O(\alpha^2).
\tag{11}
\]
Substituting (11) into (10) proves the first endpoint law with relative error \(1+O(\alpha)\).

**5. Linear endpoint at exponent one.** Set \(\theta=\arctan(1/t)\) and evaluate the smooth equation \(H_\alpha(t)=1\) at \((\alpha,t)=(1,1)\). The exact formulas above give
\[
H_1(t)=t^{-1},\quad
\left.\partial_tH_\alpha\right|_{(1,1)}=-1,\quad
\left.\partial_\alpha H_\alpha\right|_{(1,1)}
=\sqrt2\operatorname{artanh}(1/\sqrt2).\tag{12}
\]
For the last identity, put \(z=\sin u\) and use
\(\int\log(1-z^2)\,dz=z\log(1-z^2)-2z+2\operatorname{artanh}z\).
Implicit differentiation at (12) yields the second asserted expansion, with its quadratic remainder from analyticity. This completes the proof. \(\square\)

## Verification
The independent numerical script `verify.py` implements (1), the angular beta integral in \(H_\alpha\), the critical-point equation, a separate direct boundary-arclength quadrature, centered finite differences, homogeneity, endpoint calculations, and sample strict-minimum inequalities. On the package source, `python verify.py` returned `RECTANGLE_POWER_PERIMETER_FINITE_CHECKS_OK 194`, with critical aspect \(0.31015211479469559503\) at exponent \(1/2\) and linear-endpoint slope \(1.2464504802804610268\). It requires `mpmath` as specified in `requirements.txt`. The finite checks do **not** prove the universal claims; equations (1)--(12) are the proof.

## Relationship to prior work
Csató and Giovagnoli (2026-10-08) prove continuity of radial weighted perimeters under Hausdorff convergence and inclusion monotonicity for nonnegative increasing radial weights. Their Section 3 demonstrates that decreasing weights violate both directions of general inclusion monotonicity, but does not classify optimizers or exponents for anchored rectangles. Csató, Giovagnoli and Roy (2026-08-20) study fixed-*ordinary-perimeter* optimization and identify a needle extremizer for singular weights in a class of symmetric curves; neither that constraint nor its claimed extremum implies this fixed-longest-half-side interior minimum. Saracco and Stefani establish global inclusion-monotonicity rigidity, not a shape-specific critical-aspect law. A separate published result on singular radial weighted perimeters gives sharp Hausdorff regularity exponents for all planar convex sets; its bound cannot select a unique minimizing rectangle, an analytic exponent-to-shape bijection, or the essential-singularity rate. Existing fixed-major-axis ellipsoid examples similarly demonstrate nonmonotonicity but do not yield this rectangle theorem.

## Limitations
This is a complete classification only for centered axis-aligned rectangles with their largest half-side fixed, and for locally integrable negative radial powers. It is not a universal minimization theorem over all planar convex bodies, does not assume fixed area or ordinary perimeter, and does not extend the pointwise weight to the origin when \(\alpha\ge1\). A literature comparison cannot establish absolute historical priority; unindexed equivalent older computations remain possible. No independent scientific validation is claimed.

## References
1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, first public 2026-10-08, https://arxiv.org/html/2610.11677v1.
2. G. Csató, D. Giovagnoli and P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, first public 2026-08-20, https://arxiv.org/html/2608.19851v1.
3. G. Saracco and G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770, first public 2023-06-13, https://doi.org/10.1002/mana.202300280.
4. *Sharp Hausdorff regularity exponents of planar radial weighted perimeters*, public mathematical result, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-hausdorff-regularity-exponents-of-planar-radial-weighted-p--840cdd1da1ee/RESULT.md.
