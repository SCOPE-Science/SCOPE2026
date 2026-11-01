# Critical collar spectrum for hyperbolic-harmonic Bergman functions in four real dimensions

## Finding
Let \(\mathbb B^4=\{x\in\mathbb R^4:|x|<1\}\), let \(\alpha>-1\), and put \(p=\alpha+1\). Equip the space of hyperbolic-harmonic functions with the weighted Hilbert norm induced by \((1-|x|^2)^\alpha\,dx\). Let \(\mathcal V_N\) be the span of its spherical-harmonic components of degrees \(0,\ldots,N\), and let \(P_N\) denote the orthogonal projection onto \(\mathcal V_N\). For \(a>0\) and \(\beta>0\), set
\[
 \Omega_{N,\beta}(a)=\{x\in\mathbb B^4:1-|x|^2\le aN^{-\beta}\},\qquad
 T_{N,\beta}(a)=P_N\mathbf1_{\Omega_{N,\beta}(a)}\big|_{\mathcal V_N}.
\]
The operator is positive and has eigenvalues in \([0,1]\). Define the strictly increasing function
\[
 G_p(y)=\frac{\int_0^y e^{-s}s^{p-1}(s+2)^2\,ds}{\Gamma(p)(p+1)(p+4)}\quad(y\ge0).
\]
Writing \(M_N=\dim\mathcal V_N=\sum_{\ell=0}^N(\ell+1)^2\), for every continuous \(h:[0,1]\to\mathbb R\) one has
\[
 \lim_{N\to\infty}\frac{\operatorname{Tr}h(T_{N,\beta}(a))}{M_N}
 =\begin{cases}
 h(1),&0<\beta<1,\\
 3\int_0^1x^2h(G_p(ax))\,dx,&\beta=1,\\
 h(0),&\beta>1.
 \end{cases}
\]
Thus \(\beta=1\) is the only nondegenerate boundary-collar scaling. At \(\beta=1\), for \(0<\tau<G_p(a)\), the limiting fraction of eigenvalues at least \(\tau\) is
\[
 1-\bigl(G_p^{-1}(\tau)/a\bigr)^3;
\]
for \(G_p(a)\le\tau<1\) the fraction is zero.

The normalized limiting projection defect is the strictly positive quantity
\[
 \mathfrak D_p(a)=3\int_0^1x^2G_p(ax)(1-G_p(ax))\,dx,
 \qquad \lim_{N\to\infty}\frac{\operatorname{Tr}(T_{N,1}(a)(I-T_{N,1}(a)))}{M_N}=\mathfrak D_p(a).
\]
It obeys the two sharp *successive-limit* endpoint laws
\[
 \mathfrak D_p(a)\sim\frac{12a^p}{\Gamma(p+1)(p+1)(p+4)(p+3)}\quad(a\downarrow0),
\]
\[
 \mathfrak D_p(a)\sim\frac{3}{a^3}\int_0^\infty y^2G_p(y)(1-G_p(y))\,dy\quad(a\to\infty).
\]
For the ordinary Lebesgue weight \(\alpha=0\), the profile is explicit:
\[
 G_1(y)=1-e^{-y}\left(1+\frac{3y}{5}+\frac{y^2}{10}\right),\qquad
 \mathfrak D_1(a)\sim\frac{3a}{10}\ (a\downarrow0),\qquad
 \mathfrak D_1(a)\sim\frac{15837}{800a^3}\ (a\to\infty).
\]

## Assumptions and scope
The Laplace–Beltrami operator is taken for the real hyperbolic metric \(2(1-|x|^2)^{-1}|dx|\); only its nullspace enters. All norms and projections use the same positive radial weight \((1-|x|^2)^\alpha\,dx\), with an immaterial common normalization. The degree filtration \(\mathcal V_N\) is the finite direct sum of regular hyperbolic-harmonic spherical modes, not a Euclidean-polynomial subspace. The stated endpoint laws take \(N\to\infty\) with \(a\) fixed before varying \(a\); no joint uniform estimate in \(N\) and \(a\) is asserted.

## Proof
**1. Radial separation and multiplicity.** For a homogeneous Euclidean-harmonic polynomial \(H_\ell(x)=|x|^\ell Y_\ell(x/|x|)\), one has \(\Delta H_\ell=0\), \(x\cdot\nabla H_\ell=\ell H_\ell\), and \(\Delta(|x|^2H_\ell)=4(\ell+2)H_\ell\). Consequently,
\[
 U_\ell(x)=H_\ell(x)\left(1-\frac{\ell}{\ell+2}|x|^2\right)
\]
satisfies \(\Delta U_\ell+4(1-|x|^2)^{-1}x\cdot\nabla U_\ell=0\), which is equivalent to hyperbolic harmonicity. Separation of variables and regularity at the origin show that these exhaust the spherical-harmonic components. The spherical harmonics of degree \(\ell\) on \(S^3\) have dimension \((\ell+1)^2\). Radial multipliers preserve and act scalarly on each such component.

**2. Exact finite eigenvalues.** Put \(t=|x|^2\) and \(t_0=\max\{0,1-aN^{-\beta}\}\). For each \(0\le\ell\le N\), the eigenvalue (with multiplicity \((\ell+1)^2\)) is
\[
 \lambda_{\ell,N}=\frac{\int_{t_0}^1t^{\ell+1}(1-t)^{p-1}
 \left(1-\frac{\ell}{\ell+2}t\right)^2\,dt}
 {\int_0^1t^{\ell+1}(1-t)^{p-1}
 \left(1-\frac{\ell}{\ell+2}t\right)^2\,dt}.
\]
For \(\ell\ge1\), changing variables to \(s=\ell(1-t)\) gives the **exact identity**
\[
 \lambda_{\ell,N}=\frac{\int_0^{b_{\ell,N}}(1-s/\ell)^{\ell+1}s^{p-1}(s+2)^2\,ds}
 {\int_0^\ell(1-s/\ell)^{\ell+1}s^{p-1}(s+2)^2\,ds},\qquad
 b_{\ell,N}=\min\{\ell,a\ell N^{-\beta}\}.
\]
For \(\ell=0\), the displayed preceding beta-integral formula applies directly. Every denominator is strictly positive.

**3. Boundary gamma mixture.** Set \(f_\ell(s)=\mathbf1_{[0,\ell]}(s)(1-s/\ell)^{\ell+1}s^{p-1}(s+2)^2\). For fixed \(s>0\), \(f_\ell(s)\to e^{-s}s^{p-1}(s+2)^2\). Moreover \(0\le f_\ell(s)\le e^{-s}s^{p-1}(s+2)^2\), an integrable majorant for every \(p>0\). Dominated convergence gives the limiting denominator
\[
 \int_0^\infty e^{-s}s^{p-1}(s+2)^2\,ds
 =\Gamma(p+2)+4\Gamma(p+1)+4\Gamma(p)
 =\Gamma(p)(p+1)(p+4).
\]
If \(\ell/N\to x>0\), then \(b_{\ell,N}\to\infty\) for \(\beta<1\), \(b_{\ell,N}\to ax\) for \(\beta=1\), and \(b_{\ell,N}\to0\) for \(\beta>1\). The corresponding eigenvalue limits are \(1\), \(G_p(ax)\), and \(0\), respectively. Convergence is uniform over \(\varepsilon N\le\ell\le N\), for any fixed \(\varepsilon>0\), by compact-uniform convergence of the integrands and their common integrable tail bound.

**4. Full empirical spectrum and counts.** Since \(M_N=(N+1)(N+2)(2N+3)/6\sim N^3/3\), the normalized multiplicity weights converge to the probability density \(3x^2\,dx\) on \([0,1]\). The modes \(\ell<\varepsilon N\) contribute at most \(O(\varepsilon^3)\) to a normalized bounded trace. Weighted Riemann sums on \([\varepsilon,1]\), followed by \(\varepsilon\downarrow0\), establish the asserted continuous-test-function limits. The function \(G_p\) is continuous and strictly increasing from zero to one, so its pushforward under \(x\mapsto G_p(ax)\) has no atoms on \((0,1)\). This gives threshold counts by standard approximation of indicators with continuous functions; the endpoint \(\tau=G_p(a)\) also has zero limiting mass.

**5. Projection defect and endpoint coefficients.** Apply the trace limit to \(h(v)=v(1-v)\). As \(y\downarrow0\),
\[
 G_p(y)\sim\frac{4y^p}{p\Gamma(p)(p+1)(p+4)}.
\]
Substitution and integration of \(3x^{p+2}\) yields the small-\(a\) coefficient. For large \(a\), set \(y=ax\) in the defect integral. The function \(y^2G_p(y)(1-G_p(y))\) is integrable because \(G_p(y)\) vanishes like \(y^p\) at zero and \(1-G_p(y)\) has an exponential tail. The tail integral therefore converges to the stated constant. At \(p=1\), direct integration gives \(G_1(y)=1-e^{-y}(1+3y/5+y^2/10)\). Expanding the square and integrating each monomial against \(e^{-y}\) and \(e^{-2y}\) gives \(3\int_0^\infty y^2G_1(y)(1-G_1(y))\,dy=15837/800\).

**6. Hyperbolic versus Euclidean radial concentration.** For the Euclidean-harmonic degree \(\ell\) mode under the same weight, the radial probability density is proportional to \(t^{\ell+1}(1-t)^{p-1}\). The hyperbolic-harmonic radial density is this density multiplied by the strictly decreasing function \((1-\ell t/(\ell+2))^2\) when \(\ell>0\). Thus every proper outer-radius tail has strictly smaller probability in the hyperbolic-harmonic case, by the monotone-likelihood-ratio comparison. Equivalently, the limiting profile \(G_p(y)\) is strictly smaller for finite positive \(y\) than the shape-\(p\) gamma distribution function: the hyperbolic limiting density is a strictly increasing \((s+2)^2\) tilt of the gamma density.

## Verification
The standalone script `check.py` compares the exact finite eigenvalue integral with both the limiting incomplete-gamma expression and an independent direct radial integral. It executed 54 numerical assertions covering three weights, multiple finite bandwidths, different fractional degrees, full finite trace defects, the endpoint laws, and the exact rational constant \(15837/800\). The proof of all-degree and continuous-spectrum statements is analytical; numerical checks are supplementary and do not certify the limits. The script requires Python 3 with SciPy.

## Relationship to prior work
The radial separation of hyperbolic-harmonic Bergman functions and their hypergeometric norm coefficients were established in earlier work, including Üreyen's 2022 projection paper and the 2024 analysis of Blaschke, Engliš and Youssfi. The finite-mode integral is a specialization of this known radial machinery and is not claimed as novel. The result here concerns a **moving, degree-dependent boundary collar**: its unique nondegenerate scaling, the full multiplicity-weighted limiting law, threshold counts, and the two sharp limiting projection-defect coefficients. Üreyen's 2023 atomic-decomposition and interpolation paper studies the same spaces but a different problem. Fixed-radius radial eigenvalue asymptotics do not give these moving-boundary limits without a separate uniform transition argument.

## Limitations
The analysis is for real dimension four, where the radial hypergeometric factor terminates linearly. It does not assert an analogous closed gamma mixture in all dimensions, any nonradial collar, norm convergence of operators acting on varying spaces, or simultaneous asymptotics with \(a\) changing with \(N\). Historical novelty has not been independently certified; a previous general turning-point or concentration theorem may encompass this special case.

## References
1. A. E. Üreyen, *H-Harmonic Bergman Projection on the Hyperbolic Ball*, arXiv:2207.13140 (first posted July 26, 2022), https://arxiv.org/abs/2207.13140.
2. A. E. Üreyen, *Harmonic Bergman Spaces on the Real Hyperbolic Ball: Atomic Decomposition, Interpolation and Inclusion Relations*, arXiv:2303.12137 (first posted March 21, 2023), https://arxiv.org/abs/2303.12137.
3. P. Blaschke, M. Engliš and E.-H. Youssfi, *A Moebius Invariant Space of H-Harmonic Functions on the Ball*, arXiv:2404.07384 (first posted April 10, 2024), https://arxiv.org/abs/2404.07384.
4. M. Stoll, *The Reproducing Kernel of H2 and Radial Eigenfunctions of the Hyperbolic Laplacian*, Mathematica Scandinavica (2019), https://doi.org/10.7146/math.scand.a-109674.
