# The exact almost-sure stability frontier of planar Gaussian residual tracking

## Finding
For independent standard Gaussian columns \(u_k\in\mathbb R^2\) and \(0<b\le 1\), consider the homogeneous recursion
\[
 e_{k+1}=(I_2-bu_ku_k^{\mathsf T})e_k,\qquad e_0\ne0.
\]
The almost-sure logarithmic error rate exists, is independent of the starting direction, and equals
\[
\Lambda(b)=\lim_{k\to\infty}\frac1k\log\frac{\|e_k\|}{\|e_0\|}
=E_1\!\left(\frac1{2b}\right)-e^{-1/b}
\left[\operatorname{Ei}\!\left(\frac1b\right)-\operatorname{Ei}\!\left(\frac1{2b}\right)\right].
\]
The function has one positive global minimizer,
\(b_{\mathrm{opt}}=0.3244085176877795970\ldots\), where
\(\Lambda(b_{\mathrm{opt}})=-0.2303218640170102468\ldots\).
It has one positive zero,
\(b_{\mathrm{as}}=0.9370873719202791772\ldots\).
Almost-sure exponential decay occurs exactly for \(0<b<b_{\mathrm{as}}\); almost-sure exponential growth occurs for \(b>b_{\mathrm{as}}\), within the indicated domain. At the critical equality, the norm has almost-sure liminf zero and limsup infinity. By contrast,
\[
\mathbb E\|e_k\|^2=\left(1-2b+4b^2\right)^k\|e_0\|^2,
\]
so mean-square contraction requires \(0<b<1/2\). In particular, every \(1/2\le b<b_{\mathrm{as}}\) produces almost-sure exponential decay without mean-square decay. The mean-square optimal step is \(1/4\), strictly smaller than the almost-sure rate-optimal step.

## Assumptions and scope
All vectors are real and two-dimensional. The initial state is deterministic and nonzero, every \(u_k\) has independent standard normal coordinates, probes are mutually independent, and the coefficient \(b\) is fixed. All operations are exact, with a fixed target, no target drift, and no oracle noise. The standard exponential integral is \(E_1(z)=\int_z^\infty e^{-t}dt/t\) for positive \(z\); \(\operatorname{Ei}(z)\) denotes the ordinary real exponential integral. The original residual-tracking notation uses \(b=1-\rho\) with \(0\le\rho<1\). No convergence claim is made for the noisy, drifting, or nonlinear full optimization algorithm.

## Proof
**1. Every logarithmic increment has the same independent law.** For a nonzero current vector \(e\), rotate the coordinates to make \(e/\|e\|\) the first basis vector. Rotational invariance of a fresh \(u\) makes the conditional law of \(\log(\|(I_2-buu^{\mathsf T})e\|/\|e\|)\) independent of the past. By induction the sequence of log norm ratios is iid. The update is nonsingular almost surely because its exceptional determinant-zero event \(b\|u\|^2=1\) has probability zero. Each increment has finite positive variance: the only possible logarithmic singularity has locally integrable squared logarithm under a smooth two-dimensional Gaussian law, while the upper tail grows at most logarithmically in \(1+\|u\|^2\). Therefore the strong law of large numbers and, at zero drift, the law of the iterated logarithm apply.

**2. Exact rotation and radial averaging.** Conditional on \(S=\|u\|^2\), the projection direction is uniform on a circle. The update has radial-direction eigenvalues \(1-bS\) and \(1\). The elementary angular identity
\[
\frac1{2\pi}\int_0^{2\pi}
\log\sqrt{\cos^2\theta+a^2\sin^2\theta}\,d\theta
=\log\frac{1+|a|}2
\]
follows by factoring \(\cos\theta+i a\sin\theta\) into its two circle Fourier modes and applying the mean-value identity for \(\log|1+z e^{i\theta}|\). Since \(X=S/2\) is unit-mean exponential, the mean increment becomes
\[
\Lambda(b)=\int_0^{1/(2b)}e^{-x}\log(1-bx)\,dx
+\int_{1/(2b)}^\infty e^{-x}\log(bx)\,dx.
\]
The two pieces agree at their common endpoint. An integration by parts, followed by substitution \(t=bx\), gives
\[
\Lambda(b)= -\int_0^{1/2}\frac{e^{-t/b}}{1-t}\,dt
+\int_{1/2}^\infty\frac{e^{-t/b}}t\,dt.
\]
Evaluating these two integrals establishes the asserted real \(E_1\)/\(\operatorname{Ei}\) expression. The strong law proves the claimed pathwise exponent.

**3. One minimizer and one positive zero.** Differentiating the last two integrals yields
\[
b^2\Lambda'(b)=b e^{-1/(2b)}-\int_0^{1/2}\frac{t e^{-t/b}}{1-t}\,dt.
\]
The sign is the sign of \(1-R(b)\), where
\[
R(b)=\frac1b\int_0^{1/2}\frac t{1-t}
\exp\left(\frac{1/2-t}b\right)\,dt.
\]
For every fixed interior \(t\), both the prefactor and the exponential strictly decrease in \(b\); hence \(R\) strictly decreases from infinity to zero. Thus \(\Lambda'\) changes from negative to positive exactly once. Moreover \(\Lambda(b)=-b+O(b^2)\) as \(b\downarrow0\), while \(\Lambda(b)=\log b-\gamma_{\mathrm E}+o(1)\) as \(b\to\infty\), where \(\gamma_{\mathrm E}\) is Euler's constant. Hence there is exactly one positive zero on the increasing branch, and it exceeds the minimizer. The convergent quadrature reproduced in the accompanying checker brackets the minimizer in \((0.3244085,0.3244086)\) and the zero in \((0.9370873,0.9370875)\). A sign check at \(b=1\) may also be obtained without extrapolating: the increasing function \(e^{-t}/(1-t)\) on \([0,1/2]\) has its integral bounded above by its right-endpoint Riemann sum on 1000 cells; the decreasing function \(e^{-t}/t\) on \([1/2,10.5]\) has its integral bounded below by the right-endpoint sum on 1000 cells. The latter sum exceeds the former by more than \(0.023\), establishing \(\Lambda(1)>0\). These are finite inequalities of explicitly given elementary functions.

**4. Critical behavior and the mean-square criterion.** Strict positivity of increment variance at the unique zero makes the zero-mean log-error random walk oscillate infinitely in both directions by the law of the iterated logarithm. This yields the stated norm liminf/limsup and excludes critical convergence. The standard Gaussian fourth-moment identity \(\mathbb E[\|u\|^2( u^{\mathsf T}e)^2]=4\|e\|^2\), together with \(\mathbb E[(u^{\mathsf T}e)^2]=\|e\|^2\), yields the exact conditional squared-norm multiplier \(1-2b+4b^2\). Iteration gives the claimed mean-square formula and its sharp threshold.

## Verification
Run `python3 check.py` with Python 3.10 or later. It independently integrates both pieces of the logarithmic rate, locates the minimum and zero by bisection, checks the derivative sign, and simulates four 70,000-step iid Gaussian trajectories with normalization at each step. It also evaluates upper and lower monotone Riemann sums establishing a strictly positive numerical enclosure at the upper parameter endpoint. The algorithmic checks are corroborative; the continuum and almost-sure assertions follow from the preceding mathematical proof and standard probability limit laws. A finite experiment cannot establish infinite-time behavior.

## Relationship to prior work
Chayti–Mirrokni–Jaggi [1] derive precisely the stationary-sketch homogeneous error recursion (their Eq. (7)), the exact quadratic second-moment law (Eq. (8) for Gaussian probes), and the associated mean-square stability threshold (their Eq. (9) and Appendix I). The present contribution is the explicit *almost-sure* planar exponent, its unique minimizing parameter, the sharp planar pathwise stability threshold, and the critical oscillation law; it does not claim novelty of the underlying update or of the second-moment formula. Sayed–Nascimento [2], particularly Sections 3.8–3.9, already establish and illustrate that single-tap LMS can converge on typical trajectories beyond its mean-square stable window. This general distinction is therefore not claimed as new: the new calculation is the exact correlated, two-coordinate Gaussian rank-one dynamical exponent and its parameter boundaries for [1]. General Lyapunov-exponent research on products of rank-one matrices [3] concerns matrices that are themselves rank one, rather than the full-rank (almost surely) identity-minus-rank-one updates here. The full extent of coverage by other isotropic random-product results has not been exhaustively established.

## Limitations
This is a two-dimensional exact-noise-free fixed-target theorem, not a stability prescription for general dimensions, additive-noise stochastic optimization, moving targets, finite-precision iterations, or nonlinear models. The pathwise rates cannot be substituted for expected-error bounds in any theorem requiring moment control. Exact special-function constants were evaluated numerically for display; their unambiguous mathematical definitions are the displayed integrals and the uniquely specified roots. More broadly, conceptually related differences between pathwise and mean-square stability were known earlier; originality is restricted to the model-specific exact calculation.

## References
[1] E. M. Chayti, A. Mirrokni, M. Jaggi, *Partially Informed Stochastic Optimization via Zeroth-Order Residual Tracking*, arXiv:2610.13871v1 (first posted 2026-10-09), https://arxiv.org/html/2610.13871v1 .

[2] A. H. Sayed and V. H. Nascimento, *Energy Conservation and the Learning Ability of LMS Adaptive Filters*, in *Least-Mean-Square Adaptive Filters: New Insights*, Wiley (2003), pp. 79–104, https://asl.epfl.ch/wp-content/uploads/publications/book_chapters/wiley_2003_b.pdf .

[3] J. M. Altschuler and P. A. Parrilo, *Lyapunov Exponent of Rank-One Matrices: Ergodic Formula and Inapproximability of the Optimal Distribution*, SIAM J. Control Optim. 58 (2020), 510–528, arXiv:1905.07531, https://arxiv.org/abs/1905.07531 .
