# Exact Gaussian heavy tails and sharp weak-regularization risk for depth-one Anderson acceleration

## Finding

A strict scalar contraction, evaluated with arbitrarily small nonzero independent Gaussian noise, can produce a nonintegrable *first accelerated iterate* under ordinary unrestricted depth-one Anderson acceleration (AA). The inverse first-moment tail is sharp; two elementary ridge variants restore finite moments but incur an exact squared-error singularity proportional to \(\lambda^{-1/2}\) as their penalty vanishes.

Fix \(0<q<1\), \(\sigma>0\), and define
\[
\delta=1-q,\qquad B=(2-q)^2+1,\qquad
h=\frac{\exp[-\delta^4/(2\sigma^2B)]}{\sqrt{2\pi\sigma^2B}},\qquad
m=-\frac{\delta(\delta+2)}{B},\quad v=\frac{\sigma^2}{B}.
\]
Set \(M_2=m^2+v\) and \(M_4=m^4+6m^2v+3v^2\). For the unregularized accelerated value \(Z\),
\[
\lim_{T\to\infty}T\,\mathbb P(|Z|>T)=2hM_2>0,\qquad
\mathbb E|Z|^p<\infty\ \Longleftrightarrow\ 0<p<1.
\]
For the correction-coefficient ridge and the symmetric coefficient ridge, respectively,
\[
\lim_{\lambda\downarrow0}\sqrt\lambda\,\mathbb E Z_\lambda^2=\frac\pi2hM_4>0,\qquad
\lim_{\lambda\downarrow0}\sqrt\lambda\,\mathbb E (Z_\lambda^{\mathrm{sym}})^2=\frac\pi{2\sqrt2}hM_4>0.
\]
Both regularized random variables have moments of every finite positive order whenever \(\lambda>0\). No claim of long-run instability of safeguarded or regularized AA is made.

## Assumptions and scope

The exact affine fixed-point operator is \(G(x)=qx\) on the real line, with fixed point \(0\). Start deterministically at \(x_0=1\). Let \(\varepsilon_0,\varepsilon_1\) be independent mean-zero Gaussians with common variance \(\sigma^2>0\). Use two successive *fresh* noisy map evaluations:
\[
y_0=qx_0+\varepsilon_0,\qquad x_1=y_0,\qquad y_1=qx_1+\varepsilon_1.
\]
Set \(r_0=y_0-x_0\), \(r_1=y_1-x_1\), and \(D=r_0-r_1\). Ordinary depth-one AA minimizes \((r_1+Dt)^2\) over all real \(t\) and mixes the **images** \(y_0,y_1\) as \(t y_0+(1-t)y_1\), with no damping, clipping, coefficient bounds, or acceptance safeguard. Since \(D\) has a nondegenerate Gaussian density, its zero event has probability zero. At the deterministic limit \(\sigma=0\), this same unregularized first acceleration solves the affine fixed-point equation exactly.

For \(\lambda>0\), the first regularizer minimizes \((r_1+Dt)^2+\lambda t^2\). The second minimizes \((r_1+Dt)^2+\lambda[t^2+(1-t)^2]\), a two-coefficient ridge under the sum-one constraint. The two penalty normalizations are intentionally distinct and explicitly specified.

## Proof

**1. Exact stochastic update and Gaussian conditioning.** Write \(\delta=1-q\). Direct expansion yields
\[
r_1=-q\delta-\delta\varepsilon_0+\varepsilon_1,\qquad
D=-\delta^2+(2-q)\varepsilon_0-\varepsilon_1,\qquad
y_1=1+D+2r_1.
\]
The minimizer is \(t=-r_1/D\) for \(D\ne0\). Because \(y_0-y_1=-r_1\), the accelerated image mixture equals
\[
Z=y_1+\frac{r_1^2}{D}=1+D+2r_1+\frac{r_1^2}{D}.
\]
The linear transformation from \((\varepsilon_0,\varepsilon_1)\) to \((D,r_1)\) has determinant of magnitude one, so their joint Gaussian law is nondegenerate. Furthermore,
\[
\mathbb ED=-\delta^2,\quad \operatorname{Var}(D)=\sigma^2 B,
\quad \operatorname{Cov}(D,r_1)=-\sigma^2[(2-q)\delta+1].
\]
The density of \(D\) at zero is \(h\). Elementary bivariate-normal regression gives
\[
r_1\mid(D=0)\sim N(m,v),\qquad
m=-\frac{\delta(\delta+2)}{B},\quad v=\frac{\sigma^2}{B}.
\]
Consequently the conditional second and fourth raw moments at zero are \(M_2\) and \(M_4\), respectively.

**2. Exact tail and all fractional moments.** The joint density \(f(d,r)\) of \((D,r_1)\) is smooth and has Gaussian decay. For each fixed \(r\ne0\), the pole term \(r^2/d\) makes the set of small \(d\) satisfying \(|1+d+2r+r^2/d|>T\) have total width \(2r^2/T+o(T^{-1})\). Integrating over \(r\) yields
\[
\lim_{T\to\infty}T\,\mathbb P(|Z|>T)
=2\int_{\mathbb R}r^2 f(0,r)\,dr=2hM_2.
\]
To justify interchange, truncate \(|r|\le R\), \(|d|\le\eta\), apply the one-dimensional change of variables at the simple pole, then let \(R\uparrow\infty\) and \(\eta\downarrow0\); Gaussian polynomial moment bounds dominate discarded \(r\)-tails, while \(|d|>\eta\) has subexponential Gaussian tails in \(T\). In particular the positive tail constant is nonzero for every \(\sigma>0\). The tail-integral identity for positive moments gives divergence for all \(p\ge1\). For \(0<p<1\), \(|Z|^p\) is bounded by a constant times \(1+|D|^p+|r_1|^p+|r_1|^{2p}|D|^{-p}\); Gaussian conditional moments stay locally bounded and \(\int_{|d|<1}|d|^{-p}\,dd<\infty\), proving finite moments.

**3. Ridge laws.** The minimizers of the two explicitly stated quadratic objectives are
\[
t_\lambda=-\frac{Dr_1}{D^2+\lambda},\qquad
t_\lambda^{\mathrm{sym}}=\frac{\lambda-Dr_1}{D^2+2\lambda}.
\]
The corresponding image mixtures are
\[
Z_\lambda=y_1+\frac{r_1^2D}{D^2+\lambda},\qquad
Z_\lambda^{\mathrm{sym}}=y_1+\frac{r_1^2D-\lambda r_1}{D^2+2\lambda}.
\]
For fixed \(\lambda>0\), their coefficients in \(r_1\) and \(r_1^2\) are uniformly bounded in \(D\), proving all finite-order moments. Conditionally on \(D=d\), the fourth moment \(\mathbb E[r_1^4\mid D=d]\) is a polynomial in \(d\) continuous at zero, with value \(M_4\). The only contribution of order \(\lambda^{-1/2}\) to \(\mathbb E Z_\lambda^2\) is
\[
\int_{\mathbb R}\frac{d^2}{(d^2+\lambda)^2}
\,\mathbb E[r_1^4\mid D=d]\,f_D(d)\,dd.
\]
After substitution \(d=\sqrt\lambda u\), multiplication by \(\sqrt\lambda\), and dominated convergence first on a fixed neighborhood of zero (the complement contributes \(O(1)\)), the integral tends to
\[
hM_4\int_{\mathbb R}\frac{u^2}{(1+u^2)^2}\,du=\frac\pi2hM_4.
\]
Cross terms with \(y_1\) vanish on this scale by Cauchy–Schwarz, since \(\mathbb E y_1^2<\infty\). For symmetric ridge the singular denominator is \(D^2+2\lambda\) and the additional linear term in \(r_1\) is bounded; the same calculation replaces \(\lambda\) by \(2\lambda\), giving the factor \(1/\sqrt2\).

## Verification

The accompanying `verify.py` checks 375 rationally specified noisy oracle paths for the residual identities, exact unregularized image mixture whenever defined, and both ridge minimizers. It also checks the joint-Gaussian conditional mean/variance identities with exact fractions. For \(q=1/2\) and \(\sigma=1/2\), deterministic Gaussian quadrature at \(\lambda\in\{10^{-3},10^{-4},10^{-5},10^{-6}\}\) verifies convergence of the rescaled squared moments toward the two independently derived constants \(0.0721894693244\ldots\) and \(0.0510456632895\ldots\). The quadrature checks are corroboration, not a substitute for the infinite-horizon asymptotic proof. Run `python verify.py` with SciPy installed as listed in `requirements.txt`.

## Relationship to prior work

The 2021 analysis of stochastic Anderson acceleration by Lupo Pasini, Yin, Reshniak, and Stoyanov explicitly identifies noise-induced oscillations and motivates averaging; its formulation of depth-one residual least squares supports the algorithmic setup, but does not derive the Gaussian pole tail, the exact moment cutoff, or either weak-ridge constant. Scieur, d'Aspremont, and Bach (2017) prove bounds for a different regularized nonlinear extrapolation output that mixes *input iterates* rather than AA's *map images*; their positive-regularization estimates do not imply these sharp limits. Ouyang, Tao, Milzarek, and Deng study deterministic adaptive regularization with an acceptance test, and Pollock–Rebholz study deterministic filtering/conditioning. These safeguards deliberately change the random variable being analyzed. The generic pole mechanism is related to standard heavy-tail behavior of ratios of correlated Gaussian variables; the claimed contribution is the exact AA image update and its two explicit squared-risk constants, not a novel general Gaussian-ratio theorem.

## Limitations

This is a two-evaluation, scalar, zero-safeguard model. No claim concerns long-run convergence, any non-Gaussian noise law, finite-precision behavior, constrained AA coefficients, moving averages, restarts, clipped coefficients, or the adaptive algorithms in the cited papers. The parameter \(\sigma\) remains fixed and strictly positive as \(\lambda\downarrow0\); simultaneous limits may have other rates. Only the first accelerated output is assessed, not the stability of an entire trajectory. A search cannot exclude every unindexed equivalent calculation.

## References

1. M. Lupo Pasini, J. Yin, V. Reshniak, and M. Stoyanov, *Stable Anderson Acceleration for Deep Learning*, arXiv:2110.14813v1, first public 2021-10-26. https://arxiv.org/abs/2110.14813
2. D. Scieur, A. d'Aspremont, and F. Bach, *Nonlinear Acceleration of Stochastic Algorithms*, arXiv:1706.07270, 2017. https://arxiv.org/abs/1706.07270
3. W. Ouyang, J. Tao, A. Milzarek, and B. Deng, *Nonmonotone Globalization for Anderson Acceleration via Adaptive Regularization*, arXiv:2006.02559. https://arxiv.org/abs/2006.02559
4. S. Pollock and L. G. Rebholz, *Filtering for Anderson acceleration*, arXiv:2211.12953. https://arxiv.org/abs/2211.12953
