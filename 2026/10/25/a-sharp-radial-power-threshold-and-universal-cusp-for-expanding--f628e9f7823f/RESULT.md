# A sharp radial-power threshold and universal cusp for expanding translated spheres

## Finding
Let \(n\ge 2\), \(p>1-n\), and \(c\in\mathbb R^n\). For every \(r>0\), define the weighted perimeter
\[
E_p(r,c)=\int_{\partial B_r(c)}|x|^p\,d\mathcal H^{n-1}(x).
\]
Here \(B_r(c)\) is the closed Euclidean ball, and \(p=0\) means constant weight one. The weighted perimeter is finite, including when \(|c|=r\).

**Sharp monotonicity threshold.** For every center \(c\), the function \(r\mapsto E_p(r,c)\) is strictly increasing on \((0,\infty)\) if and only if \(p\ge2-n\). In the complementary allowed interval \(1-n<p<2-n\), every nonzero center gives a strict local maximum at \(r=|c|\); the function increases strictly for \(0<r<|c|\), decreases on a sufficiently small interval immediately after \(|c|\), and tends to infinity as \(r\to\infty\).

**Exact cusp, independent of the offset.** In the latter interval put \(q=n-1+p\in(0,1)\). For every \(c\ne0\), as \(h\to0\) through either sign,
\[
E_p(|c|,c)-E_p(|c|+h,c)
=\omega_{n-1}C_{n,p}|h|^q+o(|h|^q),
\quad
C_{n,p}=\frac{\Gamma(n/2)\Gamma(1-q/2)}{\sqrt\pi\,q\,\Gamma(-p/2)}.
\]
Here \(\omega_{n-1}=2\pi^{n/2}/\Gamma(n/2)\) is the area of the unit sphere. The coefficient is strictly positive and is exactly independent of \(|c|\). Therefore the profile is locally exactly \(q\)-Hölder at the touching radius, and is not locally Hölder of any higher order there.

**Newtonian boundary.** When \(n\ge3\), \(p=2-n\), and \(a=|c|>0\), the complete profile is
\[
E_{2-n}(r,c)=\omega_{n-1}\begin{cases}
a^{2-n}r^{n-1},&0<r\le a,\\
r,&r\ge a.
\end{cases}
\]
For \(c=0\) and every admissible \(p\), the exact formula is \(E_p(r,0)=\omega_{n-1}r^{n-1+p}\).

## Assumptions and scope
All dimensions are integers \(n\ge2\), all radii and center offsets are real, and \(p>1-n\) is necessary for integrability when the sphere passes through the origin. The result concerns **spheres with one fixed center**, not all nested convex sets or arbitrary varying centers. For \(n=2\), the sharp boundary exponent is \(p=0\), so the negative-power interval \((-1,0)\) is exactly the cusp regime.

## Proof
Set \(a=|c|\), \(q=n-1+p>0\), \(\omega=\omega_{n-1}\). Rotational invariance and scaling give
\[
E_p(r,c)=\omega r^q G_p(a/r),\qquad
G_p(t)=\fint_{\mathbb S^{n-1}}|u-te_1|^p\,d\sigma(u).
\]
The average \(G_p\) is continuous on \([0,\infty)\): around \(t=1\) local polar integration reduces the singular part to \(\int_0^1\theta^{n-2+p}\,d\theta\), which is finite because \(q>0\).

**Above the threshold.** If \(p=0\), the assertion follows directly. If \(p>0\), \(x\mapsto |x|^p\) is distributionally subharmonic in \(\mathbb R^n\) since
\[
\Delta |x|^p=p(p+n-2)|x|^{p-2}\ge0
\]
with a locally integrable right side. Its spherical mean about any center \(c\) is nondecreasing in radius, while the surface factor \(r^{n-1}\) is strictly increasing. Therefore \(E_p(r,c)\) is strictly increasing.

Now suppose \(n\ge3\) and \(2-n\le p<0\). For \(t>1\), differentiating the integrand gives
\[
G_p'(t)=p\fint_{\mathbb S^{n-1}}(t-u_1)|te_1-u|^{p-2}\,d\sigma(u)<0.
\]
For \(0<t<1\), the spherical-potential Poisson identity is
\[
G_p''(t)+\frac{n-1}{t}G_p'(t)
=p(p+n-2)\fint_{\mathbb S^{n-1}}|u-te_1|^{p-2}\,d\sigma(u)\le0.
\]
As \(G_p'(0)=0\), multiplying by \(t^{n-1}\) and integrating proves \(G_p'(t)\le0\) throughout \((0,1)\). Continuity at one shows \(G_p\) is nonincreasing on all positive \(t\). Thus, as \(r\) grows, \(G_p(a/r)\) does not decrease, while \(r^q\) grows strictly. This proves monotonicity. At \(p=2-n\), the Poisson right side vanishes and \(G_p(t)=1\) for \(0\le t\le1\); the outside derivative or decay at infinity yields \(G_p(t)=t^{2-n}\) for \(t\ge1\), giving the stated Newtonian profile.

**Below the threshold.** Let \(1-n<p<2-n\); then \(p<0\) and \(p(p+n-2)>0\). The first displayed derivative still implies \(G_p'(t)<0\) for \(t>1\). Therefore, for \(0<r<a\), differentiating \(\omega r^qG_p(a/r)\) gives
\[
E_p'(r,c)=\omega r^{q-1}\big(qG_p(t)-tG_p'(t)\big)>0,\qquad t=a/r>1.
\]
For \(0<t<1\), the Poisson identity has strictly positive right side, hence \(G_p'(t)>0\). Moreover, writing \(\delta=1-t\), a spherical cap of angular radius proportional to \(\delta\) gives, for \(t\uparrow1\),
\[
\fint_{\mathbb S^{n-1}}|u-te_1|^{p-2}\,d\sigma(u)
\asymp\delta^{q-2}.
\]
The integrated Poisson identity
\[
G_p'(t)=p(p+n-2)t^{1-n}\int_0^t s^{n-1}\fint_{\mathbb S^{n-1}}|u-se_1|^{p-2}\,d\sigma(u)\,ds
\]
then gives \(G_p'(t)\asymp(1-t)^{q-1}\to+\infty\). Because \(G_p(1)<\infty\), the bracket \(qG_p(t)-tG_p'(t)\) is strictly negative when \(t<1\) is close enough to one. Hence the profile strictly decreases immediately after \(r=a\). Finally \(G_p(a/r)\to1\), so \(E_p(r,c)\sim\omega r^q\to\infty\). These assertions rule out global increasing monotonicity for every nonzero center and prove sharpness.

**Cusp coefficient.** Near \(t=1\), use the angular-coordinate representation
\[
G_p(t)=\frac{\omega_{n-2}}{\omega_{n-1}}\int_0^\pi\big((1-t)^2+2t(1-\cos\theta)\big)^{p/2}\sin^{n-2}\theta\,d\theta.
\]
Split at any fixed small angle. Away from zero, changing \(t\) by \(\varepsilon\) contributes \(O(\varepsilon)\), negligible compared with \(\varepsilon^q\) because \(q<1\). In the small-angle part, put \(\theta=\varepsilon v\); dominated convergence applied to the **difference** of integrands yields, from either side,
\[
\lim_{\varepsilon\downarrow0}\frac{G_p(1)-G_p(1\pm\varepsilon)}{\varepsilon^q}
=\frac{\omega_{n-2}}{\omega_{n-1}}\int_0^\infty v^{n-2}\big(v^p-(1+v^2)^{p/2}\big)\,dv.
\]
The integral converges at zero since \(q>0\), and at infinity because its integrand is \(O(v^{q-3})\). Write \(v^p-(1+v^2)^{p/2}=(-p/2)\int_0^1(v^2+s)^{p/2-1}ds\). Tonelli, a beta integral, and \(\Gamma(1-z)=(-z)\Gamma(-z)\) give
\[
\int_0^\infty v^{n-2}\big(v^p-(1+v^2)^{p/2}\big)dv
=\frac{\Gamma((n-1)/2)\Gamma(1-q/2)}{q\Gamma(-p/2)}.
\]
Using \(\omega_{n-2}/\omega_{n-1}=\Gamma(n/2)/(\sqrt\pi\Gamma((n-1)/2))\) gives exactly \(C_{n,p}\). In \(E_p(r,c)=\omega r^qG_p(a/r)\) at \(r=a+h\), the smooth factor changes by \(O(h)=o(|h|^q)\) and \(a^q|1-a/(a+h)|^q=|h|^q(1+o(1))\). The dependence on \(a\) therefore cancels and the asserted symmetric cusp follows. Since the coefficient is positive, its exponent is optimal.

## Verification
The supplementary standalone script `checks/verify.py` uses high-precision independent angular quadrature and the pre-existing hypergeometric expression for normalized spherical Riesz means to cross-check the sphere integral at thirty sample configurations, then verifies the critical Newtonian profile, the gamma-valued cusp coefficient on both sides for four dimension-power pairs, and monotonicity at representative supercritical values. It reports `WEIGHTED_SPHERE_OK numerical_cases= 71`. The proof above, not numerical interpolation, establishes the universal quantifiers. A direct check in three dimensions follows from the elementary identity
\[
\frac{E_p(r,c)}{4\pi}=\frac{r}{2a(p+2)}\big((a+r)^{p+2}-|a-r|^{p+2}\big),\qquad a>0,\;p\ne-2,
\]
which is valid when \(p>-2\). These formulas supply independently checkable normalization and boundary cases.

## Relationship to prior work
Csató and Giovagnoli (2026, arXiv:2610.11677v1) define the same weighted-perimeter functional and prove continuity and an inclusion theorem under **nondecreasing** radial weights when the smaller convex set contains the origin. Their theorem does not treat decreasing powers on expanding spheres with arbitrary displaced fixed center and does not assert the threshold or contact cusp. Their discussion includes different counterexamples for general convex-body inclusion.

Chafaï, Matzke, Saff, Vu, and Womersley (2024 preprint / 2025 journal article, arXiv:2405.00120, Appendix C, Lemma C.3) supply the **general exact spherical Riesz potential via a hypergeometric function**, so the spherical average used here is known and is **not** claimed as new. Standard properties of hypergeometric functions give another route to our conclusions, and their formula mathematically determines the profile; the present claim concerns the geometric monotonicity classification and the sharp scale-free singular coefficient, supported by the separate sign and boundary arguments above. This is a substantial priority caveat, not evidence of historical uniqueness.

Saracco and Stefani (arXiv:2306.07770) characterize weighted-perimeter monotonicity over arbitrary inclusions; that strictly stronger *geometric domain* requirement only permits constant weights and therefore does not itself classify translated concentric balls. The available research-record search identified a separate planar global Hausdorff-modulus result, but no stated all-dimensional fixed-center monotonicity phase theorem with universal contact coefficient.

## Limitations
Historical priority is provisional. In particular, the known hypergeometric potential formula could already have been used elsewhere to derive the sharp sign classification and cusp coefficient; a search-result absence is not a proof of novelty. The theorem makes no claim about arbitrary nested convex bodies or changing centers. It assumes the radial weight is a pure power and excludes exponents \(p\le1-n\) because the contact perimeter diverges. The checker supplies finite numerical corroboration only.

## References
1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, first posted 2026-10-08. https://arxiv.org/html/2610.11677v1
2. D. Chafaï, R. W. Matzke, E. B. Saff, M. Q. H. Vu, R. S. Womersley, *Riesz Energy with a Radial External Field: When is the Equilibrium Support a Sphere?*, arXiv:2405.00120, Appendix C, Lemma C.3. Open-access journal version: https://doi.org/10.1007/s11118-024-10186-w
3. G. Saracco and G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770.
4. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1 (abstract consulted).
