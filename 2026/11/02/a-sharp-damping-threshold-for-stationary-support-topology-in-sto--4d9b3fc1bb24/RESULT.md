# A sharp damping threshold for stationary-support topology in stochastic Chebyshev descent

## Finding

An undamped Chebyshev stability interval contains internal neutral points. For the fixed-step, same-sample-per-stage stochastic Runge--Kutta--Chebyshev (SRKCD) method, damping removes these internal neutral points, but it also creates a sharp topological transition in the invariant error distribution. The two transitions are tied by an exact optimal noise-floor formula.

**Theorem.** Fix an **even** integer \(s\ge 2\), curvature \(a>0\), an offset \(b>0\), and damping \(\varepsilon>0\). Let \(T_s\) be the first-kind Chebyshev polynomial, and set
\[
\omega_0=1+\frac{\varepsilon}{s^2},\qquad
C=T_s(\omega_0)>1,\qquad
\omega_1=\frac{T_s(\omega_0)}{T_s'(\omega_0)}>0,\qquad
H=\frac{2\omega_0}{\omega_1}.
\]
Let the stochastic component objectives be \(f_\xi(x)=a(x-b\xi)^2/2\), where \(\xi\in\{-1,+1\}\) is fair. In each outer step draw an independent \(\xi\), reuse that one component throughout all \(s\) internal stages of first-order SRKCD with damping \(\varepsilon\), and use constant stepsize \(\eta=t/a\). For every \(0<t<H\), this method has a unique invariant probability law \(\mu_t\), approached in the \(1\)-Wasserstein metric from every initial distribution with finite first moment.

Writing
\[
r(t)=\frac{T_s(\omega_0-\omega_1t)}{C},
\]
the law has mean zero and exact stationary variance
\[
\operatorname{Var}_{\mu_t}(X)=b^2\frac{1-r(t)}{1+r(t)}.
\]
Its support is a **closed interval** exactly when \(|r(t)|\ge 1/2\); when \(0<|r(t)|<1/2\) it is a two-branch separated Cantor set of Hausdorff dimension \(\log 2/[-\log|r(t)|]\), and when \(r(t)=0\) it consists of exactly two atoms. At \(|r(t)|=1/2\), the invariant law is uniform on its support interval.

Let \(\mathcal N_{s,\varepsilon}\subset(0,H)\) be the set of stepsizes at which the support is **not** an interval, equivalently \(|r(t)|<1/2\). Then
\[
\boxed{\quad
\#\operatorname{components}(\mathcal N_{s,\varepsilon})=
\begin{cases}
s,&1<C\le2,\\
1,&C>2.
\end{cases}\quad}
\]
The exact worst stationary variance over all strictly stable stepsizes is attained and equals
\[
\boxed{\qquad\sup_{0<t<H}\operatorname{Var}_{\mu_t}(X)
=b^2\frac{C+1}{C-1}.\qquad}
\]
Consequently the **unique** damping threshold
\[
\boxed{\quad
\varepsilon_s=s^2\left[\cosh\!\left(\frac{\operatorname{arcosh}2}{s}\right)-1\right]\quad}
\]
separates \(s\) disjoint noninterval-support windows at \(0<\varepsilon\le\varepsilon_s\) from one merged window at \(\varepsilon>\varepsilon_s\). At exactly that same threshold, the maximum variance is \(3b^2\); it is **strictly below** \(3b^2\) exactly when the noninterval-support windows have merged. Moreover, \(\varepsilon_s\to(\operatorname{arcosh}2)^2/2\) as \(s\to\infty\).

Thus damping trades an all-steps stationary-noise bound against the topology of the attainable stationary errors: improving the sharp bound past \(3b^2\) forces a single contiguous band of noninterval stationary supports, for every even stage count.

## Assumptions and scope

The original deterministic objective is \(F(x)=\mathbb E_\xi f_\xi(x)=a(x^2+b^2)/2\), uniquely minimized at \(x=0\). Every outer step uses a fresh fair sign, independent between outer steps, and holds that sign **fixed across all internal stages**. This is not independently resampled-stage Runge--Kutta. We use exact arithmetic in the mathematical method, with no within-stage roundoff. Damping is strictly positive; stage count is any even integer at least two. The admissible interval \(0<t<H\) is open; no claims of uniqueness are made at its boundary. The invariant law need not possess a density when its support is an interval.

## Proof

**1. Exact Chebyshev recurrence.** The first-order RKC stage coefficients satisfy \(\omega_0=1+\varepsilon/s^2\), \(\omega_1=T_s(\omega_0)/T_s'(\omega_0)\). For a scalar linear equation \(y'=-ay\), its stage stability polynomial is
\[
R_s(-t)=\frac{T_s(\omega_0-\omega_1t)}{T_s(\omega_0)}.
\]
This follows directly from the three-term Chebyshev recurrence and the standard first-order RKC stage update: with \(Y_0=y\), \(Y_1=y-(\omega_1/\omega_0)t y\), and for \(2\le j\le s\),
\[
Y_j=\frac{2(\omega_0-\omega_1t)T_{j-1}(\omega_0)}{T_j(\omega_0)}Y_{j-1}
-\frac{T_{j-2}(\omega_0)}{T_j(\omega_0)}Y_{j-2}.
\]
Induction yields \(Y_j=T_j(\omega_0-\omega_1t)y/T_j(\omega_0)\). Because the sampled vector field is exactly \(-a(x-b\xi)\), translation by its equilibrium \(b\xi\) gives the **exact** stochastic outer update
\[
X_{n+1}=r(t)X_n+[1-r(t)]b\xi_{n+1}.
\]
No stochastic approximation is used in this reduction.

**2. Strict contraction and invariant law.** Since \(\omega_0>1\), \(C=T_s(\omega_0)>1\), and for even \(s\), \(|T_s(x)|<C\) whenever \(-\omega_0<x<\omega_0\). Hence \(|r(t)|<1\) for every \(0<t<H\). Coupling two iterations with the same signs shrinks their distance by \(|r(t)|\) each step. The unique invariant law is the absolutely convergent random series
\[
X_\infty=b[1-r(t)]\sum_{j=0}^\infty r(t)^j\xi_{-j}.
\]
Independence and symmetry give its mean and variance, and the common-sign coupling proves convergence in \(W_1\).

**3. Exact support.** Put \(q=|r(t)|<1\) and \(d=b[1-r(t)]>0\). The support of the series is the unique nonempty compact set \(K\) satisfying
\[
K=(rK+d)\cup(rK-d).
\]
Its convex hull is \([-M,M]\), with \(M=d/(1-q)\). The images of this hull have radius \(qM\), are centered at \(\pm d\), and cover the hull if and only if \(q\ge1/2\). In this case the contraction fixed-set uniqueness implies \(K=[-M,M]\). For \(0<q<1/2\), the image intervals are disjoint with a positive central gap; repeated construction gives a two-branch self-similar Cantor attractor with the stated Hausdorff dimension by the separated similarity theorem (or the elementary cylinder covering and mass-distribution argument). At \(q=0\) the support is precisely \(\{-b,+b\}\). For \(q=1/2\), rewriting each sign at alternating powers when \(r<0\) reduces the invariant law to a binary expansion with independent fair digits, so its distribution is uniform on \([-M,M]\). This proof classifies support, **not** absolute continuity for \(q>1/2\).

**4. Number of noninterval windows.** The map \(t\mapsto x=\omega_0-\omega_1t\) bijects \((0,H)\) with \((-\omega_0,\omega_0)\). Noninterval support means \(|T_s(x)|<C/2\). The \(s\) simple zeros of \(T_s\) are in \((-1,1)\), interlaced with its internal extrema \(x=\cos(j\pi/s)\) for \(1\le j<s\), where \(|T_s(x)|=1\). Outside \([-1,1]\), \(|T_s(x)|\) increases strictly with \(|x|\). Therefore, if \(1<C\le2\), the strict sublevel set has exactly one component around each of the \(s\) zeros, separated by all internal extrema (the equality extrema still separate components when \(C=2\)). If \(C>2\), the whole segment \([-1,1]\) lies in the strict sublevel set, which extends contiguously to one threshold point on each side and has exactly one component.

**5. Exact sharp bound and its coincidence with the merger.** The variance as a function of \(r\) is strictly decreasing, with derivative \(-2b^2/(1+r)^2\). For even \(s\), the smallest value of \(r(t)\) on the strict-stability interval is \(-1/C\), attained at every odd-indexed interior Chebyshev extremum. Hence the stated sharp supremum. It is less than \(3b^2\) if and only if \(C>2\), precisely the one-component case. Since \(T_s(x)=\cosh(s\operatorname{arcosh}x)\) is strictly increasing for \(x>1\), solving \(C=2\) gives the unique \(\varepsilon_s\). Finally \(s^2[\cosh(z/s)-1]\to z^2/2\) for fixed \(z=\operatorname{arcosh}2\).

## Verification

The standalone standard-library script `verify.py` uses independent direct RKC stage recurrences and Chebyshev-polynomial recurrences in exact rational arithmetic, exhaustive finite sign histories, and numerical checks of all extrema and damping thresholds. Executing `python verify.py` prints `CHECKS_PASS 25394`. The exact-rational checks confirm the stage polynomial, finite-time means and second moments; they are not substituted for the analytic infinite-series, Hausdorff-dimension, or all-step proof.

## Relationship to prior work

Stillfjord and Williamson, *SRKCD: a stabilized Runge--Kutta method for stochastic optimization* (arXiv:2201.12782, first posted January 30, 2022), define the same-sample-per-stage stabilized method, Chebyshev damping, and its stability interval, and prove diminishing-step convergence rates. Their discussion of \(\varepsilon>0\) removing stability degeneration motivates the present fixed-step stationary analysis. The first-order RKC polynomials and stable intervals themselves are **not** claimed as new. Classical Bernoulli-convolution literature already gives the interval/Cantor support criterion at contraction ratio \(1/2\); that criterion itself is also **not** claimed as new. The claimed contribution is their scheme-specific synthesis into a complete all-even-stage damping/stepsize phase diagram and the exact sharp equivalence of topology merger to a uniform stationary-variance threshold.

Relevant comparisons include Peres and Solomyak's Bernoulli-convolution theory; Jordan, Shmerkin and Solomyak's multifractal work; and general stochastic fixed-point iteration theory by Hermer, Luke and Sturm. These theories give ingredients but, in the inspected material, do not report the coupled Chebyshev damping threshold, number of stationary noninterval windows, or its coincidence with the all-step variance bound.

## Limitations

The proof is specific to one-dimensional quadratic component objectives with **identical curvature and opposite minimizers**, independent fair component selection between outer steps, stagewise sample reuse, strictly positive damping, even stage count, and a constant step in the full open Chebyshev stability interval. It does not characterize odd-stage endpoint behavior, the undamped internal-neutral cases, variable stepsizes, stagewise resampling, nonlinear losses, or floating-point effects. Full interval support for \(|r|>1/2\) does not imply an absolutely continuous invariant distribution; exceptional singular Bernoulli convolutions are possible. Publication-priority claims remain contingent on the reach of the available literature review and independent expert assessment.

## References

1. T. Stillfjord and M. Williamson, *SRKCD: a stabilized Runge--Kutta method for stochastic optimization*, arXiv:2201.12782, version 1 first posted 2022-01-30. https://arxiv.org/abs/2201.12782
2. Y. Peres and B. Solomyak, *Absolute continuity of Bernoulli convolutions, a simple proof*, Mathematical Research Letters 3 (1996), 231--239. https://www.microsoft.com/en-us/research/publication/absolute-continuity-bernoulli-convolutions-simple-proof/
3. T. Jordan, P. Shmerkin and B. Solomyak, *Multifractal structure of Bernoulli convolutions*, Mathematical Proceedings of the Cambridge Philosophical Society 151 (2011), 521--539. https://doi.org/10.1017/S0305004111000466
4. N. Hermer, D. R. Luke and A. Sturm, *Nonexpansive Markov operators and random function iterations for stochastic fixed point problems*, Journal of Convex Analysis 30 (2023), 1073--1114. https://journalofconvexanalysis.com/articles/jca30049/
5. S. Baker, H. Koivusalo, S. Troscheit and X. Zhang, *On the Fourier transform of random Bernoulli convolutions*, Journal of the London Mathematical Society 113 (2026), e70515. https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70515
