# Sharp rare-curvature stability and extinction frontiers for stochastic Chebyshev descent

## Finding

The first-order, undamped stochastic Runge–Kutta–Chebyshev descent method admits an exact moment-stability classification under two-point positive random curvature, provided one sampled gradient is shared by all internal stages and new samples are independent across macrosteps. Its sharp high-curvature sampling threshold decreases **exponentially in the stage count**, in contrast to the quadratically expanding deterministic stability interval. At the Chebyshev zeros, almost-sure finite termination can coexist with exponential divergence of every sufficiently high moment.

Let \(s\ge1\) be an integer, \(\ell>0\), \(t\in(0,2)\), \(\kappa>2/t\), and \(p\in(0,1)\). Define

\[
\theta=\arccos(1-t),\quad
\gamma=\operatorname{arcosh}(\kappa t-1),\quad
 a_s=\cos(s\theta),\quad b_s=(-1)^s\cosh(s\gamma).
\]

For any nonzero starting point \(x_0\), any real \(q>0\), and every integer \(n\ge0\),

\[
\mathbb E|x_n|^q=|x_0|^q\bigl((1-p)|a_s|^q+p|b_s|^q\bigr)^n.
\]

Consequently, with

\[
p_q(s,t,\kappa)=\frac{1-|a_s|^q}{|b_s|^q-|a_s|^q},
\]

the \(q\)-moment tends geometrically to zero **if and only if** \(p<p_q\), remains equal to its initial value at \(p=p_q\), and diverges exponentially for \(p>p_q\). This statement includes \(p_q=0\), in which case no positive high-curvature sampling probability is moment-stable. The mean-square threshold is

\[
p_2=\frac{\sin^2(s\theta)}{\cosh^2(s\gamma)-\cos^2(s\theta)}
   =4\sin^2(s\theta)e^{-2s\gamma}\bigl(1+O(e^{-2s\gamma})\bigr)
\quad (s\to\infty),
\]

where the asymptotic holds for fixed \(t,\kappa\), uniformly in the phase \(s\theta\). In particular, stage counts satisfying \(s\theta\in\pi\mathbb Z\) have \(p_2=0\).

If \(0<|a_s|<1\), the almost-sure logarithmic growth exponent is

\[
\lim_{n\to\infty}\frac1n\log\left|\frac{x_n}{x_0}\right|
 =(1-p)\log|a_s|+p\log|b_s|\quad\text{almost surely}.
\]

Its zero occurs at

\[
p_{\mathrm{as}}=\frac{-\log|a_s|}{\log|b_s|-\log|a_s|}>p_2.
\]

Thus \(p_2<p<p_{\mathrm{as}}\) gives almost-sure exponential convergence but divergent mean square. For any Chebyshev zero \(a_s=0\), the first low-curvature sample sends the iterate exactly to the minimizer, and the survival probability after \(n\) macrosteps is \(p^n\); nevertheless \(q\)-moments diverge when \(p>\operatorname{sech}^q(s\gamma)\).

The especially natural central root \(t=1\) exists for every odd \(s\). For fixed \(\kappa>2\), it gives

\[
p_q=\operatorname{sech}^q\!\left(s\operatorname{arcosh}(\kappa-1)\right)
\sim 2^q e^{-q s\operatorname{arcosh}(\kappa-1)}
\quad (s\to\infty,\ s\text{ odd}).
\]

For \(\ell=1\), \(\kappa=3\), \(s=3\), \(t=1\), \(p=1/100\), and hence \(\alpha=9\), the low-curvature multiplier is \(0\) and the high-curvature multiplier is \(-26\). Therefore

\[
\mathbb E x_n=x_0\left(-\frac{13}{50}\right)^n,
\qquad
\mathbb E x_n^2=x_0^2\left(\frac{169}{25}\right)^n,
\qquad
\mathbb P(x_n\ne0)=100^{-n}.
\]

The signed mean converges, the second moment grows exponentially, and the method nevertheless reaches the exact minimizer after finitely many steps almost surely.

## Assumptions and scope

We minimize the strongly convex, one-dimensional expectation

\[
F(x)=\frac12\mathbb E[\lambda_\xi]x^2,
\quad
\mathbb P(\lambda_\xi=\ell)=1-p,
\quad
\mathbb P(\lambda_\xi=\kappa\ell)=p.
\]

The stochastic gradient \(g(\xi,x)=\lambda_\xi x\) is unbiased and vanishes at the exact minimizer \(x_*=0\). For every macrostep, the gradient sample \(\xi\) is drawn once and reused at **all** \(s\) stages; samples of different macrosteps are independent. The macrostep size is fixed as \(\alpha=s^2t/\ell\), and the damping parameter of SRKCD is exactly zero. All statements concern exact real arithmetic; the independent sampling and shared-within-step convention are essential.

## Proof

**1. Reduction to the actual stages.** The defining first-order SRKCD recursion has parameters \(\omega_0=1+\varepsilon/s^2\) and \(\omega_1=T_s(\omega_0)/T_s'(\omega_0)\), with stage coefficients \(\widetilde\mu_1=\omega_1/T_1(\omega_0)\), \(\widetilde\mu_j=2\omega_1T_{j-1}(\omega_0)/T_j(\omega_0)\), and \(\nu_j=-T_{j-2}(\omega_0)/T_j(\omega_0)\). At \(\varepsilon=0\), \(T_j(1)=1\) and \(T_s'(1)=s^2\), so \(\widetilde\mu_1=1/s^2\), \(\widetilde\mu_j=2/s^2\), and \(\nu_j=-1\). Holding the sampled \(\lambda\) constant through the stages gives

\[
y_0=x_n,\quad y_1=(1-\alpha\lambda/s^2)y_0,
\quad y_j=2(1-\alpha\lambda/s^2)y_{j-1}-y_{j-2}
\ (2\le j\le s).
\]

The Chebyshev recurrence, with \(T_0(u)=1\), \(T_1(u)=u\), proves inductively that \(x_{n+1}=y_s=T_s(1-\alpha\lambda/s^2)x_n\). For \(\lambda=\ell\), the multiplier is \(T_s(1-t)=\cos(s\theta)=a_s\). For \(\lambda=\kappa\ell\), it is \(T_s(1-\kappa t)=(-1)^s\cosh(s\gamma)=b_s\). The domain guarantees \(|a_s|\le1\) and \(|b_s|>1\).

**2. Sharp moments.** Independence across macrosteps yields \(x_n=x_0\prod_{j=1}^nM_j\) with iid \(M_j\in\{a_s,b_s\}\) of respective probabilities \(1-p,p\). Independence gives the exact formula for \(\mathbb E|x_n|^q\), for every \(q>0\). Since \(|b_s|^q>|a_s|^q\), the positive moment multiplier crosses \(1\) at precisely the stated \(p_q\). Below, at, and above this value it is respectively less than, equal to, and greater than \(1\); there are no unexamined boundary cases.

**3. Almost-sure behavior.** When \(a_s\ne0\), the logarithms \(\log|M_j|\) are integrable, so the strong law of large numbers gives the displayed logarithmic exponent. If \(0<|a_s|<1\), the exponent increases strictly with \(p\) and crosses zero at \(p_{\mathrm{as}}\). To prove \(p_2<p_{\mathrm{as}}\), evaluate at \(p=p_2\): strict Jensen for the nonconstant positive random variable \(|M|^2\) yields \(\mathbb E\log|M|^2<\log\mathbb E|M|^2=0\). Therefore the almost-sure exponent is negative at the mean-square threshold. If \(a_s=0\), the first low-curvature sample annihilates the iterate; the first occurrence is geometric with parameter \(1-p\), and \(\mathbb P(x_n\ne0)=p^n\) for \(x_0\ne0\). No use of the strong law with \(\log0\) is made in this case.

**4. Stage-count asymptotic and witness.** From \(\cosh(s\gamma)=\tfrac12e^{s\gamma}(1+e^{-2s\gamma})\) and \(\gamma>0\), substitution in the exact expression for \(p_2\) gives the uniform exponential formula. When \(t=1\) and \(s\) is odd, \(T_s(0)=0\), proving the central-root moments and extinction claims. Finally \(T_3(-2)=-26\) gives the rational witness exactly; \(p|b_s|=13/50<1\) while \(p|b_s|^2=169/25>1\).

**5. Perturbation robustness.** Strict mean-square instability \((1-p)a_s^2+pb_s^2>1\) persists on an open neighborhood in \((p,t,\kappa)\), by polynomial continuity of the multipliers. Exact finite-time extinction, by contrast, is tied to the Chebyshev roots and is not claimed away from them.

## Verification

Run `python3 verify.py` using only the Python standard library. The verifier evaluates the actual undamped stage recurrence independently from the Chebyshev polynomial recurrence for scalar rational curvatures and stages, checks the rational moment identity against finite binomial expansion, confirms boundary equalities, and reproduces the stated \(s=3\) rational witness. It also compares selected odd-stage exact thresholds with the asymptotic formula. The included script reports `VERIFY_OK 6099` when these finite checks succeed. The theorem for all real parameters and every horizon is proved analytically above; finite checks alone do not establish it.

## Relationship to prior work

Stillfjord and Williamson (2022, arXiv:2201.12782v1, especially §§2–3) introduced SRKCD with the same stochastic sample reused within the stages, and supplied general convergence estimates as well as the deterministic RKC stability-function discussion. They do not establish the exact random-curvature moment and almost-sure thresholds at an aggressive fixed macrostep. Eftekhari, Vandereycken, Vilmart and Zygalakis (2018, arXiv:1805.07199v1, §2 and Proposition 1) identify the Chebyshev polynomial and deterministic quadratic spectral-stability interval; their deterministic max-spectrum guarantee is not an expectation over iid batch curvatures. S-ROCK methods of Abdulle and Cirilli (2008) concern stochastic differential equations driven by time noise rather than this fixed-within-macrostep random-gradient oracle.

The general random-product moment factorization and strong law are classical tools. The contribution here is the **complete sharp SRKCD sampling-frequency frontier and its exponentially stage-dependent, almost-sure-versus-moment contrast** for the specified natural stochastic optimization model. No general priority claim beyond the inspected sources is made.

## Limitations

This is a one-dimensional, two-curvature, strongly convex quadratic model. It assumes iid batch choices across macrosteps, exactly one batch held for all internal stages, undamped SRKCD, a fixed step chosen by the low curvature, exact arithmetic, and no additive gradient noise. The chosen macrostep can exceed the deterministic worst-case stability limit for the high-curvature batch; the theorem does **not** contradict sufficient step-size restrictions based on maximum possible curvature or the source's diminishing-step convergence theorem. The exact hitting-zero phenomenon is resonance-sensitive; only the strict moment-instability region is open under parameter perturbation. There is no claim of higher-dimensional nonlinear stability, practical wall-clock speedup, or finite-precision exact extinction.

## References

1. T. Stillfjord and M. Williamson, *SRKCD: a stabilized Runge–Kutta method for stochastic optimization*, arXiv:2201.12782v1, first public 2022-01-30; §§2–3 and Appendix A. https://arxiv.org/html/2201.12782v1
2. A. Eftekhari, B. Vandereycken, G. Vilmart and K. C. Zygalakis, *Explicit stabilised gradient descent for faster strongly convex optimisation*, arXiv:1805.07199v1, first public 2018-05-18; open full text at https://link.springer.com/article/10.1007/s10543-020-00819-y
3. A. Abdulle and S. Cirilli, *S-ROCK: Chebyshev methods for stiff stochastic differential equations*, SIAM J. Sci. Comput. 30 (2008), 997–1014, DOI:10.1137/070679375; cited for the different SDE setting only.
