# A strict mean–variance resetting-rate separation for inverse boundary local time

## Finding

A reflecting Brownian particle repeatedly reset **in position but not in accumulated boundary local time** admits an exact, universal reliability–speed tradeoff for a large boundary-reaction budget. In the dimensionless resetting variable \(z=a\sqrt{r/D}\), the unique asymptotic mean-optimal value is \(z=1\), whereas the unique asymptotic absolute-variance optimum is \(z_*=1.330917894\ldots>1\). The ratio between corresponding optimal physical resetting rates is \(z_*^2=1.771342441\ldots\). The leading squared-coefficient-of-variation factor is strictly decreasing with \(z\), so absolute and relative notions of reliability favor different rates.

## Assumptions and scope

Let \(X_t\) be reflecting Brownian motion with generator \(D\partial_{xx}\) on \([0,\infty)\), starting at \(X_0=a>0\). Independently, a Poisson process of rate \(r>0\) resets **only the position** to \(a\), without resetting the boundary local time
\[
L_t=\lim_{\epsilon\downarrow0}\frac D\epsilon\int_0^t\mathbf 1_{\{0\le X_s<\epsilon\}}\,ds.
\]
All limits are in the conventional boundary-local-time sense. For a fixed deterministic length budget \(\ell>0\), set \(\tau_\ell=\inf\{t\ge0:L_t>\ell\}\). Define \(z=a\sqrt{r/D}\), \(\xi=\ell/a\), and \(T_\xi=D\tau_\ell/a^2\). The dimensionless resetting rate equals \(z^2\). All assertions below hold for every \(z,\xi>0\) unless a limit is specified.

## Proof

**1. Exact threshold-time transform.** Write \(s\ge0\), \(q(s)=\sqrt{(r+s)/D}\), and \(w(s)=e^{-a q(s)}\). The Laplace transform of the first visit \(H\) to zero under position-only Poisson resetting is the standard renewal expression
\[
\mathbb E_a e^{-sH}=\frac{(r+s)w(s)}{s+r w(s)}.
\]
For completeness, introduce an independent exponential boundary-local-time budget of parameter \(\theta>0\) per unit length. The transform \(f(x)\) of absorption time solves \(Df''-(r+s)f+rf(a)=0\) for \(x>0\), with \(f'(0)=\theta[f(0)-1]\). Its bounded solution is \(f(x)=rf(a)/(r+s)+Be^{-q(s)x}\). Evaluating at \(a\) and imposing the boundary condition gives
\[
f(a)=\frac{(r+s)w(s)}{s+rw(s)}\frac{\theta}{\theta+\psi(s)},\qquad
\psi(s)=\frac{s q(s)}{s+rw(s)}.
\]
Inverting the elementary Laplace transform in the exponential-budget parameter identifies the fixed-budget transform:
\[
\boxed{\mathbb E_a e^{-s\tau_\ell}=\frac{(r+s)w(s)}{s+rw(s)}\exp\!\left[-\ell\frac{s q(s)}{s+rw(s)}\right].}\tag{1}
\]
This calculation relies on the known position-resetting/local-time-accumulation model and is not claimed as an independent novelty result. It also follows from the existing double-transform formalism for the process.

**2. Independent decomposition, moments, Gaussian limit.** At every positive local-time level the position is at zero. The strong Markov property of the spatial process with position-only resetting implies that the inverse local-time increments after the first boundary hit are stationary and independent. Their Laplace exponent is \(\psi\) from (1). Thus \(\tau_\ell=H+S_\ell\), with \(H\) independent of a subordinator \(S\) satisfying \(\mathbb E e^{-sS_\ell}=e^{-\ell\psi(s)}\). Differentiating the logarithm of (1) at \(s=0\), then rescaling length and time, yields the **exact** formulas
\[
\boxed{\mathbb E T_\xi=\frac{e^z-1}{z^2}+\xi\frac{e^z}{z},}\tag{2}
\]
\[
\boxed{\operatorname{Var} T_\xi=\frac{e^{2z}-ze^z-1}{z^4}+\xi\,B(z),\quad B(z)=\frac{e^z(2e^z-1-z)}{z^3}.}\tag{3}
\]
The first terms in (2) and (3) are the first-passage mean and variance; the terms linear in \(\xi\) come from the inverse-local-time subordinator. Because \(\psi\) is analytic in a neighborhood of zero for each \(r>0\), \(S_1\) has finite variance \(B(z)>0\). Ordinary independent-increment central limit theory, with the independent \(H\) negligible on the square-root threshold scale, gives, for each **fixed** \(z>0\),
\[
\frac{T_\xi-\xi e^z/z}{\sqrt{\xi B(z)}}\ \Longrightarrow\ \mathcal N(0,1)\quad(\xi\to\infty).\tag{4}
\]
The exact mean could equally be used in the centering.

**3. Strict separation of globally optimal rates.** Let \(M(z)=e^z/z\). Then \(M'(z)=e^z(z-1)/z^2\), so \(M\) has exactly one global minimizer \(z=1\). For \(B\), direct differentiation and positive-factor extraction give
\[
B'(z)=\frac{e^z}{z^4}F(z),\quad F(z)=2e^z(2z-3)-z^2+z+3.
\]
Crucially, \(F'(z)=(2z-1)(2e^z-1)\). Hence \(F\) decreases on \((0,1/2)\), increases on \((1/2,\infty)\), satisfies \(F(0)=-3\), \(F(1)=3-2e<0\), and \(F(3/2)=9/4>0\). It therefore has exactly one positive root \(z_*\in(1,3/2)\). Also \(B(z)\to\infty\) both as \(z\downarrow0\) and \(z\to\infty\), proving that \(z_*\) is the unique **global** variance-coefficient minimizer.

For every \(\xi>0\), both exact functions (2) and (3) are continuous and coercive as \(z\downarrow0\) or \(z\to\infty\), and hence possess global minimizers. Their nonnegative first-passage terms give the inequalities
\[
M(z_{\xi,\mathrm{mean}})\le M(1)+\frac{(e-1)}{\xi},\qquad
B(z_{\xi,\mathrm{var}})\le B(z_*)+\frac{e^{2z_*}-z_*e^{z_*}-1}{\xi z_*^4}.
\]
Coercivity of \(M,B\) and uniqueness of their minima imply \(z_{\xi,\mathrm{mean}}\to1\) and \(z_{\xi,\mathrm{var}}\to z_*\), for **every choice** of respective global minimizers. Therefore for all sufficiently large budgets every globally variance-optimal resetting rate exceeds every globally mean-optimal rate. The limiting physical-rate ratio is \(z_*^2=1.771342441\ldots\), independently of \(a,D\). No claim of uniqueness of finite-budget minimizers is needed.

**4. Relative reliability has no finite optimal rate in the large-budget coefficient.** Combining (2)–(3) gives
\[
C(z)=\lim_{\xi\to\infty}\xi\frac{\operatorname{Var}T_\xi}{(\mathbb ET_\xi)^2}=\frac{2-(1+z)e^{-z}}{z}.
\]
Its derivative equals \(C'(z)=[e^{-z}(z^2+z+1)-2]/z^2\). For \(z>0\), the exponential-series lower bound \(2e^z\ge2+2z+z^2>1+z+z^2\) shows \(C'(z)<0\). Moreover \(C(z)\downarrow0\) as \(z\to\infty\). This establishes three distinct asymptotic optimization principles: the mean has a finite optimum at \(z=1\), absolute variance at \(z=z_*\), and normalized relative variance coefficient has no finite minimizer.

## Verification

The standalone file `verify.py` independently differentiates the Laplace expression at zero at 80-digit precision and checks the moment formulas (2)–(3) over a positive-parameter grid. It also checks the sign structure of \(F\), the root bracket and high-precision root, and the decreasing relative-variance coefficient on sampled values. The analytic proof, not the finite checks, establishes the global signs, uniqueness, and convergence. Run with `python verify.py` after installing `mpmath` (declared in `requirements.txt`).

## Relationship to prior work

Bressloff's *Threshold surface reactions and local time resetting* (arXiv:2203.04868, 2022) **already establishes this exact half-line position-only-resetting model and its mean threshold absorption time**, including formula (2) after scaling (see Eq. (3.17)). Its broader Laplace-domain propagator encompasses the ingredients used to derive (1). Neither the mean formula nor the reset/local-time distinction is claimed here as new. Bressloff's *Diffusion-mediated surface reactions and stochastic resetting* (arXiv:2202.01119, 2022) develops the underlying encounter-based framework. Benkhadaj and Grebenkov's *Encounter-based approach to diffusion with resetting* (arXiv:2209.00947, 2022) gives a general position-resetting encounter approach for **bounded** domains, but the inspected position-resetting results do not evaluate this half-line variance minimizer. Pal, Chatterjee, Reuveni, and Kundu, *Local time of diffusion with stochastic resetting* (arXiv:1902.00907, 2019), treats forward local-time fluctuations, not the inverse boundary-local-time threshold problem. The narrowly assessed addition is the exact variance-rate law coupled to the **unique global optimal-rate separation and strict relative-reliability monotonicity**.

## Limitations

The findings assume Poisson **position-only** resetting and accumulation (not resetting) of the boundary local time. They do not apply to complete resetting of the local-time budget, to general reaction-threshold distributions, or to bounded/multidimensional domains without further analysis. The large-budget optimization limits hold with \(z\) varying through global minimizers; the coefficient-of-variation limit is for each fixed \(z\), so no interchange of \(z\to\infty\) and \(\xi\to\infty\) is asserted. The conclusions have not been independently audited, and the priority search cannot exclude an equivalent unlocated derivation in broader inverse-local-time or stochastic-restart literature.

## References

1. P. C. Bressloff, *Threshold surface reactions and local time resetting*, arXiv:2203.04868 (first posted 2022-03-09), especially Secs. 2–3 and Eq. (3.17).
2. P. C. Bressloff, *Diffusion-mediated surface reactions and stochastic resetting*, arXiv:2202.01119 (first posted 2022-02-02).
3. Z. Benkhadaj and D. S. Grebenkov, *Encounter-based approach to diffusion with resetting*, arXiv:2209.00947 (first posted 2022-09-02), especially Sec. II.2 and Appendix A.
4. A. Pal, R. Chatterjee, S. Reuveni, A. Kundu, *Local time of diffusion with stochastic resetting*, arXiv:1902.00907 (2019).
