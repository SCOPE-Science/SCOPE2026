# Universal age–transverse fluctuation correlation in extreme sheared reset excursions

## Finding

A planar Brownian particle simultaneously reset to the origin at independent Poisson times and advected between resets by a nonzero linear shear has an explicit **universal extreme-excursion history**. For each fixed diffusivity \(D>0\), reset rate \(r>0\), and signed shear \(\gamma\in\mathbb R\setminus\{0\}\), define
\[
 a=\left(\frac{9}{4D\gamma^2r}\right)^{1/4},\qquad c=\frac{3}{2\gamma a},\qquad \lambda=\frac{4ra}{3}.
\]
Let \(A\) be the age of the current reset-free excursion at a stationary observation time \(0\). Given a large positive observed longitudinal displacement \(X_0>x\), the reset-free path on normalized age \(u\in[0,1]\) satisfies
\[
\sup_{0\le u\le1}\left|\frac{X_{-A+uA}}{x}-\frac{3u^2-u^3}{2}\right|\ \xrightarrow[x\to\infty]{\mathbb P(\cdot\mid X_0>x)}\ 0,
\]
\[
\sup_{0\le u\le1}\left|\frac{Y_{-A+uA}}{c\sqrt{x}}-(2u-u^2)\right|\ \xrightarrow[x\to\infty]{\mathbb P(\cdot\mid X_0>x)}\ 0.
\]
The main new assertion concerns fluctuations **jointly** in excursion age and transverse endpoint, not the individual fixed-duration Gaussian-bridge profiles. The excursion age concentrates at \(a\sqrt{x}\), but its fluctuations and the transverse endpoint fluctuations remain correlated. Specifically, with
\[
 U_x=\frac{A-a\sqrt{x}}{\sqrt{a/(4r)}\,x^{1/4}},\qquad
 W_x=\frac{Y_0-c\sqrt{x}}{\sqrt{3Da/4}\,x^{1/4}},
\]
one has the joint weak limit
\[
(U_x,W_x)\mid\{X_0>x\}\ \Longrightarrow\
\mathcal N_2\!\left(0,
\begin{pmatrix}
1&-\operatorname{sgn}(\gamma)/\sqrt3\\
-\operatorname{sgn}(\gamma)/\sqrt3&1
\end{pmatrix}\right).
\]
The magnitude of the limiting age--transverse-coordinate correlation is exactly \(1/\sqrt3\), independent of diffusivity, resetting rate, and shear magnitude. In addition, the stationary longitudinal tail has the sharp form
\[
\mathbb P(X_0>x)\sim\frac{\sqrt6}{4}\exp(-\lambda\sqrt{x}).
\]
The marginal stretched-exponential tail belongs to the known random-acceleration resetting class, and the cubic shape is equivalent to a familiar integrated-Brownian optimal bridge shape. The contribution assessed here is the **Poisson-age-conditioned joint Gaussian fluctuation law with a parameter-free cross-correlation**, together with its uniform path-level interpretation, not those antecedents in isolation.

## Assumptions and scope

Use independent standard one-dimensional Brownian motions \(B^x,B^y\), independent of a rate-\(r\) Poisson clock. Between clock rings, evolve
\[
 dX_t=\gamma Y_t\,dt+\sqrt{2D}\,dB^x_t,\qquad
 dY_t=\sqrt{2D}\,dB^y_t.
\]
At each Poisson event reset **both** coordinates instantaneously to \((0,0)\); restart from fresh Brownian increments. The unique stationary regenerative version is considered, and \(A>0\) denotes time elapsed since the last reset before observation at time zero. Write \(X_{-A+uA},Y_{-A+uA}\) for the actual path *after* that reset, with \(u\in[0,1]\). All limits fix the three parameters before sending the positive threshold \(x\to\infty\). The joint Gaussian limit is weak convergence on \(\mathbb R^2\), and both path limits are convergence in probability in the uniform norm on continuous functions.

## Proof

**1. Exact regeneration and Gaussian covariance.** In stationarity \(A\sim\mathrm{Exp}(r)\). Conditional on \(A=t\), the most recent excursion has exactly the same law as a process started at the origin and run for time \(t\), with
\[
Y_s=\sqrt{2D}B^y_s,\qquad
X_s=\sqrt{2D}B^x_s+\gamma\sqrt{2D}\int_0^s B^y_v\,dv.
\]
For \(0\le u\le1\), write \(V(t)=\operatorname{Var}(X_t)\), \(C_Y(u,t)=\operatorname{Cov}(Y_{ut},X_t)\), and \(C_X(u,t)=\operatorname{Cov}(X_{ut},X_t)\). Integration of Brownian covariance yields the **exact** identities
\[
 V(t)=2D\left(t+\frac{\gamma^2t^3}{3}\right),
\quad C_Y(u,t)=2D\gamma t^2\left(u-\frac{u^2}{2}\right),
\]
\[
 C_X(u,t)=2Dut+2D\gamma^2t^3\left(\frac{u^2}{2}-\frac{u^3}{6}\right).
\]
In particular, \(\operatorname{Cov}(Y_t,X_t)=D\gamma t^2\) and \(\operatorname{Var}(Y_t)=2Dt\). Consequently
\[
\mathbb P(X_0>x)=r\int_0^\infty e^{-rt}\overline\Phi\!\left(\frac{x}{\sqrt{V(t)}}\right)\,dt,
\]
where \(\overline\Phi\) is the survival function of a standard normal random variable. This identity is exact for every \(x>0\).

**2. Uniform saddle and excursion-age Gaussian law.** Write \(t=z\sqrt{x}\). On every compact subinterval of \((0,\infty)\), the Gaussian tail argument tends uniformly to infinity and Mills' ratio applies. The leading exponent is
\[
 rt+\frac{x^2}{2V(t)}
 =\sqrt{x}\,f(z)+o(1),\qquad
 f(z)=rz+\frac{3}{4D\gamma^2z^3}.
\]
The function \(f\) diverges at both endpoints and has a single global minimizer \(z=a\), because
\[
 f'(z)=r-\frac{9}{4D\gamma^2z^4},\quad
 f''(a)=\frac{4r}{a}>0,\quad
 f(a)=\lambda.
\]
For rigor in the Laplace localization, outside a fixed compact neighborhood of \(a\), the exact nonnegative exponent \(rt+x^2/[2V(t)]\) is separated from its minimum by a positive multiple of \(\sqrt{x}\) on compact \(z\)-sets. For very large \(z\), the term \(rt\) supplies exponential domination. For very small \(z\), the term \(x^2/[2V(t)]\) supplies exponential domination (including the regime where \(t\) is bounded); standard normal tail bounds make these statements uniform. Thus no omitted age regime contributes at leading order.

Mills' ratio and the one-dimensional Laplace formula now yield
\[
\mathbb P(X_0>x)\sim
 \frac{r\sqrt{2D\gamma^2/3}\,a^{3/2}}{\sqrt{f''(a)}}
 e^{-\lambda\sqrt{x}}
 =\frac{\sqrt6}{4}e^{-\lambda\sqrt{x}}.
\]
Expanding \(f\) at its nondegenerate minimum on the scale \(t=a\sqrt{x}+v x^{1/4}\) gives
\[
 \frac{A-a\sqrt{x}}{x^{1/4}}\;\bigg|\;X_0>x
 \ \Longrightarrow\ N\!\left(0,\frac{a}{4r}\right).
\]
The same tail asymptotic at \(x+h\sqrt{x}\), for any fixed \(h\ge0\), shows that
\[
\frac{X_0-x}{\sqrt{x}}\;\bigg|\;X_0>x
 \ \Longrightarrow\ \mathrm{Exp}(\lambda/2).
\]
Only the consequence \(X_0=x+O_{\mathbb P}(\sqrt{x})\) is needed below; no independence of this overshoot and other fluctuations is asserted.

**3. Uniform path concentration.** Conditional on age \(A=t\), Gaussian regression on the final coordinate \(X_t\) gives
\[
X_{ut}=\frac{C_X(u,t)}{V(t)}X_t+R_X(u,t),\qquad
Y_{ut}=\frac{C_Y(u,t)}{V(t)}X_t+R_Y(u,t),
\]
where each centered residual Gaussian process is independent of \(X_t\) conditional on \(t\). The exact covariances above imply uniformly for \(0\le u\le1\), as \(t\to\infty\),
\[
\frac{C_X(u,t)}{V(t)}\longrightarrow\frac{3u^2-u^3}{2},\qquad
\frac{t\,C_Y(u,t)}{V(t)}\longrightarrow\frac3\gamma\left(u-\frac{u^2}{2}\right).
\]
The Burkholder/Doob maximal bound for Brownian motion and direct integration give \(\mathbb E\sup_u|R_X(u,t)|^2=O(t^3+t)\) and \(\mathbb E\sup_u|R_Y(u,t)|^2=O(t)\), with constants uniform for \(t\ge1\). These follow by subtracting the Gaussian projections from the explicit Brownian path representation, bounding projection coefficients uniformly, and using \(\mathbb E\sup_{s\le t}|B_s|^2\le4t\). Because the residuals are independent of the conditioning coordinate and the tilted age satisfies \(A=O_{\mathbb P}(\sqrt{x})\), the normalized residuals vanish: \(\sup|R_X|/x\to0\) and \(\sup|R_Y|/\sqrt{x}\to0\), conditionally in probability. Combining regression, age concentration, and \(X_0/x\to1\) proves both asserted uniform polynomial path laws.

**4. Joint endpoint fluctuation law.** At \(u=1\), the conditional Gaussian regression is
\[
 Y_0=\frac{D\gamma A^2}{V(A)}X_0+
 \sqrt{2DA-\frac{D^2\gamma^2 A^4}{V(A)}}\,Z,
\]
where \(Z\sim N(0,1)\) can be chosen independent of \((A,X_0)\). Uniformly over ages in the saddle window, the regression coefficient is \(3/(2\gamma A)+O(A^{-3})\), while the residual variance is \(DA/2+O(A^{-1})\). Insert \(A=a\sqrt{x}+O_{\mathbb P}(x^{1/4})\) and \(X_0=x+O_{\mathbb P}(\sqrt{x})\) to obtain
\[
\frac{Y_0-c\sqrt{x}}{x^{1/4}}
 =-\frac ca\frac{A-a\sqrt{x}}{x^{1/4}}
 +\sqrt{\frac{Da}{2}}\,Z+o_{\mathbb P}(1).
\]
The first term has limiting variance \(c^2/(4ra)=Da/4\), using \(a^4=9/(4D\gamma^2r)\). The second contributes \(Da/2\), giving total variance \(3Da/4\). After standardization, the covariance is \(-\operatorname{sgn}(\gamma)/\sqrt3\), which proves the bivariate Gaussian limit. Nonzero shear is indispensable: taking \(\gamma\to0\) before \(x\to\infty\) changes the tail and path scaling.

## Verification

The standalone `CHECK.py` uses independent numerical integration of Gaussian covariance kernels and of the exact stationary renewal/tail integrals, at three parameter triples of both shear signs and two large thresholds. It checks the marginal tail coefficient, conditional age and transverse endpoint means, convergence of the conditional endpoint correlation, and the two projected path shapes. Running `python CHECK.py` (with NumPy and SciPy installed) reports `PASS: 177 deterministic assertions`. These finite-threshold checks support, but cannot establish, the infinite-threshold claims; the proof above supplies the latter.

## Relationship to prior work

Abdoli, Olsen, and Löwen, *Shear-Driven Diffusion with Stochastic Resetting* (arXiv:2410.10333v1, first submitted 2024-10-14), study precisely the simultaneous-reset planar shear model, derive its Gaussian free propagator, perturbative stationary density, moments, skewness, kurtosis, and energetic cost. Their renewal kernel supplies the starting model, but the large-positive-longitudinal-displacement posterior *path* and its joint endpoint-age law are not stated there.

Singh, *Random acceleration process under stochastic resetting* (arXiv:2007.05576v1, 2020), derives the stationary joint position/velocity law and the leading stretched-exponential stationary position tail for complete random-acceleration resetting. The shear model's dominant large-excursion longitudinal component reduces to that integrated-Brownian class, so the displayed marginal tail exponent and prefactor **alone must not be regarded as a new result**. The independent direct longitudinal Brownian noise makes the full model different, and the present conditioned shear-plane excursion law, polynomial path shapes, and universal age--transverse-endpoint Gaussian correlation require the additional posterior analysis.

Meerson, *Geometrical optics of first-passage functionals of random acceleration* (arXiv:2302.04029), studies short-first-passage optimal trajectories and gives the cubic bridge \(1-3u^2/2+u^3/2\) for a trajectory from a positive point to zero. Its complement is exactly the longitudinal cubic displayed here; that **fixed-duration path shape is not claimed as original on its own**. The first-passage optimization has neither stationary Poisson-reset age conditioning nor the joint Gaussian age–transverse endpoint correlation. Generic Gaussian regression and Laplace's method are established tools; novelty, if independently sustained, lies in the specific joint posterior fluctuation theorem with universal correlation, not those methods or isolated polynomials.

## Limitations

The statement is for complete simultaneous resets to the origin, linear homogeneous shear, independent Gaussian translational noises, fixed nonzero shear, and a stationary Poisson clock. It concerns the conditional distribution given an unusually large longitudinal *position*, not a maximum-over-time or first-passage event. No inference guarantee at finite threshold, experiment-level sampling optimality, uniqueness of the result in all existing literature, independent mathematical validation, or uniformity as \(\gamma\to0\) is claimed. The available exact random-acceleration mixture formula is a significant priority antecedent, and independent priority review remains necessary.

## References

- I. Abdoli, K. Stølevik Olsen, H. Löwen, *Shear-Driven Diffusion with Stochastic Resetting*, arXiv:2410.10333v1, 2024-10-14, https://arxiv.org/html/2410.10333v1.
- P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576v1, 2020-07-10, https://arxiv.org/pdf/2007.05576.
- B. Meerson, *Geometrical optics of first-passage functionals of random acceleration*, arXiv:2302.04029, 2023-02-08, https://arxiv.org/pdf/2302.04029.
