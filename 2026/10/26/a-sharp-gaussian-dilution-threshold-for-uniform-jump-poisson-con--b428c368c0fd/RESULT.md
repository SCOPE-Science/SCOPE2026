# A sharp Gaussian-dilution threshold for uniform-jump Poisson concentration

## Finding

Let \(J_1,J_2,\ldots\) be independent uniform random variables on \([1,2]\), let \(N\) be Poisson with intensity \(\lambda>0\), and let \(Z\) be standard normal, independently of everything else. For \(\sigma\geq0\), define
\[
X=\sigma Z+\sum_{j=1}^{N}J_j-\lambda\mathbb E J_1,
\qquad V=\operatorname{Var}(X)=\sigma^2+\frac73\lambda,
\qquad w=\frac{7\lambda}{3V}.
\]
Let \(c_*(X)\) denote the least \(c\geq0\) for which
\[
\log\mathbb E e^{tX}\leq\frac{Vt^2}{2(1-ct)}
\qquad (0\leq t<1/c),
\]
with \(1/0=\infty\). Set \(w_* =868/1125\). Then:

1. **Locally controlled regime.** If \(w_*\leq w\leq1\), equivalently \(0\leq\sigma^2\leq257\lambda/372\), then
\[
\boxed{c_*(X)=\frac{15w}{28}=\frac{\kappa_3(X)}{3V}.}
\]
The defining optimization is maximized only in the limiting sense as \(t\downarrow0\).

2. **Uniquely interior-controlled regime.** If \(0<w<w_*\), equivalently \(\sigma^2>257\lambda/372\), there is a **unique** \(t_w>0\) solving
\[
\frac{H'(t_w)}{H(t_w)^2}=w,
\qquad
H(t)=\int_0^2e^{tu}h(u)\,du,
\]
where
\[
h(u)=\frac37\begin{cases}
\frac73-3u+u^2,&0\leq u\leq1,\\
\frac{(2-u)^3}{3},&1\leq u\leq2,\\
0,&u>2.
\end{cases}
\]
The optimal scale is
\[
\boxed{c_*(X)=\frac{wH(t_w)}{1+wt_wH(t_w)}>\frac{15w}{28}.}
\]
The maximizing argument is unique on \((0,\infty)\).

3. **Quantitative onset.** Write \(\delta=w_*-w\downarrow0\). Then
\[
\boxed{t_w=\frac{84375}{9716}\delta+O(\delta^2),\qquad
c_*(X)-\frac{15w}{28}=\frac{523125}{544096}\delta^2+O(\delta^3).}
\]
In particular, the crossover is continuous in the scale and has quadratic contact with the third-cumulant lower bound.

More generally, for any positive, bounded jump law \(J\) with \(\mathbb E J^4<\infty\), put \(h_J(u)=\mathbb E[(J-u)_+^2]/\mathbb E J^2\). If \(h_J\) is log-concave on its positive support, the corresponding Gaussian-plus-compound-Poisson family exhibits the same *unique-local versus unique-interior* classification at
\[
\boxed{w_J^*=\frac{3\mathbb E J^4\,\mathbb E J^2}{4(\mathbb E J^3)^2},
\qquad w=\frac{\lambda\mathbb E J^2}{\sigma^2+\lambda\mathbb E J^2}.}
\]
If \(w_J^*\geq1\), the local regime has no interior \(w\)-values (or only the endpoint \(w=1\) when equality holds). This general criterion is the structural ingredient underlying the explicit uniform-jump threshold.

## Assumptions and scope

All random variables are real. The Poisson intensity is finite and positive; every jump is strictly positive. The Gaussian coefficient may vanish. For the general criterion, \(J\) has bounded support contained in \((0,\infty)\), and \(h_J\) is positive and log-concave on the interior of its support. The claim concerns the **right** moment-generating-function envelope with its quadratic parameter fixed to the **true variance**; it does not optimize a freely chosen variance proxy. All stated equalities and strict inequalities hold for every parameter in the specified intervals. The critical asymptotics are for fixed jump law as the variance fraction approaches its threshold.

## Proof

**(1) Exact transformation.** For a positive bounded jump \(J\), put \(m_2=\mathbb E J^2\) and \(V=\sigma^2+\lambda m_2\). The Lévy cumulant formula gives
\[
K_X(t)=\frac{\sigma^2t^2}{2}+\lambda\mathbb E(e^{tJ}-1-tJ).
\]
Integrating the remainder twice, or using \(e^{tJ}-1-tJ=t^2\int_0^J(J-u)e^{tu}\,du\), yields
\[
\frac{2K_X(t)}{Vt^2}=1+wtH_J(t),\quad
H_J(t)=\int_0^\infty e^{tu}h_J(u)\,du,\quad
h_J(u)=\frac{\mathbb E(J-u)_+^2}{m_2}.
\]
The identity follows because \(tH_J(t)\) is the excess over one in the moment generating function of the second-order equilibrium jump variable: explicitly, \(tH_J(t)=\frac{2}{m_2t^2}\mathbb E(e^{tJ}-1-tJ)-1\). The integrals are finite because jumps are bounded.

Set \(\phi_w(t)=wH_J(t)/(1+wtH_J(t))\). Algebra shows that the smallest feasible scale equals \(\sup_{t\geq0}\phi_w(t)\), with \(\phi_w(0)=wH_J(0)\): if a proposed \(c\) fails the inequality at a positive \(t\), then \(\phi_w(t)>c\); conversely, \(\phi_w(t)<1/t\), so any violation \(\phi_w(t)>c\) necessarily lies in the tested domain \(t<1/c\). Thus the full-range supremum and the envelope's restricted-domain optimization agree.

**(2) Strict unimodality from log-concavity.** Write \(H=H_J\) and define \(g(t)=H'(t)/H(t)^2\). Direct differentiation yields
\[
\phi_w'(t)=\frac{w\{H'(t)-wH(t)^2\}}{(1+wtH(t))^2},
\qquad
 g'(t)=\frac{H''(t)H(t)-2H'(t)^2}{H(t)^3}.
\]
The probability density \(f_t(u)=e^{tu}h_J(u)/H(t)\) is log-concave on a bounded interval. Its survival function \(S_t(s)\) has increasing hazard: log-concavity implies that \(f_t(s+v)/f_t(s)\) decreases as \(s\) grows, hence \(S_t(s)/f_t(s)\) decreases. Consequently \(S_t(r+s)\leq S_t(r)S_t(s)\) for nonnegative \(r,s\). The inequality is strict on a set of positive measure for a nondegenerate bounded-support density. Integrating the survival functions gives
\[
\mathbb E_tU^2=2\int_0^\infty\!\int_0^\infty S_t(r+s)\,dr\,ds
<2\left(\int_0^\infty S_t(r)\,dr\right)^2=2(\mathbb E_tU)^2.
\]
Therefore \(g'(t)<0\) for every finite \(t\geq0\). As \(t\to\infty\), \(H(t)\to\infty\) exponentially while \(0\leq H'(t)/H(t)\leq\sup\operatorname{supp}J\); hence \(g(t)\to0\). Thus \(\phi_w\) is strictly decreasing if \(w\geq g(0)\); otherwise it strictly increases until the sole solution of \(g(t)=w\), then strictly decreases. Because \(\phi_w(t)\to0\) as \(t\to\infty\), these are the global alternatives, with no hidden larger optimizer.

**(3) The universal threshold.** By Tonelli and the elementary beta integrals,
\[
H_J(0)=\frac{\mathbb E J^3}{3\mathbb E J^2},\qquad
H'_J(0)=\frac{\mathbb E J^4}{12\mathbb E J^2}.
\]
It follows that \(g(0)=3\mathbb E J^4\mathbb E J^2/[4(\mathbb E J^3)^2]\). This proves the general criterion. Notice that a Cauchy--Schwarz argument makes this critical variance fraction at least \(3/4\), with equality for deterministic jumps; the threshold can exceed one for broadly dispersed jump laws.

**(4) Uniform jumps and exact arithmetic.** For \(J\sim\operatorname{Uniform}[1,2]\), \(\mathbb E J^k=(2^{k+1}-1)/(k+1)\), so
\[
h_J(u)=\frac37\begin{cases}(2-u)^3/3-(1-u)^3/3,&0\leq u\leq1,\\\frac{(2-u)^3}{3},&1\leq u\leq2.\end{cases}
\]
For \(0\leq u\leq1\), the polynomial inside the positive factor is \(q(u)=u^2-3u+7/3\) and
\[
q''(u)q(u)-q'(u)^2=-2u^2+6u-\frac{13}{3}\leq-\frac13<0.
\]
For \(1<u<2\), \(\log h_J(u)\) differs by a constant from \(3\log(2-u)\), which is strictly concave; the first two derivatives match at \(u=1\). Thus the required log-concavity holds across the entire support. The first three derivative values are
\[
H(0)=\frac{15}{28},\quad H'(0)=\frac{31}{140},\quad H''(0)=\frac3{20}.
\]
Hence \(g(0)=868/1125\), and the equivalent Gaussian-to-Poisson intensity threshold is \(\sigma^2/\lambda=(7/3)(1-w_*)/w_*=257/372\). All three regimes and the exact scale formulas follow from (2).

**(5) Critical expansion.** Direct rational evaluation gives
\[
g'(0)=\frac{H''(0)H(0)-2H'(0)^2}{H(0)^3}=-\frac{9716}{84375}.
\]
The implicit function theorem applied to \(g(t_w)=w_*-\delta\) yields \(t_w=84375\delta/9716+O(\delta^2)\). Taylor expansion of \(\phi_w\) about \((t,w)=(0,w_*)\), using \(\partial_t\phi_w(0)=wH(0)^2(w_*-w)\), gives
\[
\phi_w(t_w)-\phi_w(0)=\frac{w_*H(0)^2}{-2g'(0)}\delta^2+O(\delta^3)
=\frac{523125}{544096}\delta^2+O(\delta^3).
\]
This proves the onset formulas, including the exact coefficients.

## Verification

The standalone standard-library script `checks/verify.py` reconstructs all rational constants directly from uniform-jump moments. It verifies the piecewise integrated-tail identity, log-concavity numerator, power-series coefficients, the variance threshold, several uniquely bracketed stationary points, original-cumulant-factorization cases, and the critical expansion numerically. Running `python checks/verify.py` produces `checks/verify_output.txt`; the accompanying finite checks passed. The complete all-parameter assertion rests on the analytic proof, **not** on finite sampling of arguments.

## Relationship to prior work

Chen's 2026 variational characterization of optimal variance-exact sub-gamma scales supplies the canonical second-order equilibrium transform and the general M-class interpretation. The theorem here does not claim those foundations: it proves a new strict single-crossing principle under log-concavity of the integrated jump tail and evaluates the sharp Gaussian smoothing threshold for a continuous, nondegenerate uniform jump law. Chen and Wang's signed-jump work classifies the different Skellam model, including a separate phase threshold, without the current uniform-jump and Gaussian-dilution classification. Leskelä and Välimaa study optimal **sub-Poisson variance proxies**, rather than the present fixed-variance, variable-pole sub-gamma problem. Standard increasing-failure-rate facts for log-concave densities are used with a proof in the present setting. The existence of the general variational formula means the present special value could in principle be computed from earlier implicit machinery; the distinct claim is global monotonicity, a unique optimizer, the explicit exact phase transition, and quantitative onset.

## Limitations

No claims concern arbitrary signed jumps, unbounded jump amplitudes, or general non-log-concave integrated tails. For an arbitrary bounded jump distribution the critical expression alone need not govern global optimality without the stated shape hypothesis. The left-side optimal scale and freely varying quadratic proxies are different questions. A comprehensive search cannot certify historical priority; an equivalent reliability-theoretic argument may exist under another terminology. The review and tests here are not independent external validation.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1, first public version 2026-09-02. https://arxiv.org/abs/2610.00032
2. Y. Chen and X. Wang, *Directional Optimal Sub-Gamma Scales for Infinitely Divisible Laws*, arXiv:2609.02590v1, first public version 2026-09-02. https://arxiv.org/abs/2609.02590
3. L. Leskelä and I. Välimaa, *Sub-Poisson Distributions: Concentration Inequalities, Optimal Variance Proxies, and Closure Properties*, arXiv:2508.12103v1, first public version 2025-08-16. https://arxiv.org/abs/2508.12103
4. B. Klar and A. Müller, *Characterizations of Classes of Lifetime Distributions Generalizing the NBUE Class*, Journal of Applied Probability 40 (2003), 20–32.
