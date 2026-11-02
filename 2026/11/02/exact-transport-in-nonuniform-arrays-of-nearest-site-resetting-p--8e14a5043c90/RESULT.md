# Exact transport in nonuniform arrays of nearest-site resetting points

## Finding

Let \(N\geq2\) distinct resetting sites repeat periodically on the real line with period \(L>0\), and let their successive cyclic gaps be \(\ell_1,\ldots,\ell_N>0\), \(\sum_i\ell_i=L\). Between independent rate-\(r>0\) Poisson events, the particle is ordinary Brownian motion with generator \(D\partial_x^2\), \(D>0\). At each event it is instantaneously moved to the nearest resetting site. Write
\[
q=\sqrt{r/D},\quad a_i=q\ell_i/2,\quad
S=\sum_{i=1}^{N}\sinh a_i,\quad T=\sum_{i=1}^{N}\tanh a_i.
\]
Then the lifted particle has zero effective drift, satisfies
\[
\frac{X_t-X_0}{\sqrt t}\ \Longrightarrow\
\mathcal N\!\left(0,2D_{\rm eff}\right),\qquad
\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}
=D_{\rm eff}=\boxed{\frac{rL^2}{4ST}},
\]
for every deterministic starting point. The unique invariant density of position modulo \(L\) is explicitly, on the open gap \((x_i,x_{i+1})\),
\[
p(x)=\frac{q}{2T}\frac{\cosh(q[x-(x_i+x_{i+1})/2])}{\cosh a_i}.
\]
At stationary Poisson times, the probability of resetting to site \(x_i\) is
\[
\pi_i^{\rm reset}=\frac{\tanh a_{i-1}+\tanh a_i}{2T},
\]
where indices are cyclic. These probabilities refer to sites selected **at Poisson resetting events**, not to occupation fractions of a different first-exit skeleton.

For fixed \(N,L,D\) and gaps, the small-rate expansion is
\[
\frac{D_{\rm eff}}{D}=1+\frac{r}{24DL}\sum_i\ell_i^3+O(r^2),\quad r\downarrow0.
\]
Consequently, at every sufficiently small **fixed** positive rate, any nonuniform array has strictly larger effective diffusion than the equal-gap array with the same \(N,L,D,r\). This does not contradict the already known **rate-optimized** superiority of the regular array. At high resetting rate, if \(\ell_{\max}\) occurs with multiplicity \(k\),
\[
D_{\rm eff}\sim \frac{rL^2}{2Nk}
\exp\!\left(-\frac{\ell_{\max}}{2}\sqrt{\frac rD}\right).
\]
Thus the largest gap is a sharp high-rate transport bottleneck. The exact all-gap diffusivity, stationary law, fixed-rate reversal and largest-gap asymptotics form one linked transport theorem.

## Assumptions and scope

Choose \(0=x_1<x_2<\cdots<x_N<L\), with \(x_{N+1}=x_1+L\), extended by \(x_{i+N}=x_i+L\). The nearest-site map \(Q:\mathbb R\to\{x_i+mL\}\) chooses the closest site, breaking midpoint ties arbitrarily. Ties have probability zero at Poisson times. All sites are static. Resets are instantaneous and do not interrupt the Brownian clock except for the jump. There is no attraction force between events and no independent reset-location sampling. The infinitesimal generator is
\[
(\mathcal Lf)(x)=Df''(x)+r\{f(Q(x))-f(x)\}.
\]
The process is observed on the unwrapped line for transport, and modulo \(L\) for its invariant density. The \(O(r^2)\) remainder is for a fixed positive finite gap configuration, with \(D\) fixed. The high-rate asymptotic holds for fixed gaps and \(D\) as \(r\to\infty\).

## Proof

**Invariant law.** On a gap, the invariant forward equation away from resetting sites is \(Dp''-rp=0\). The displayed density \(p\) is positive, periodic, continuous, and has the same value \(c=q/(2T)\) at every resetting site. Its integral on the full gap \((x_i,x_{i+1})\) equals \(2c\tanh(a_i)/q\), so its total mass is one. The reset destination \(x_i\) owns the Voronoi interval from the previous gap's midpoint to the next gap's midpoint. Integrating \(p\) on its two half-gaps gives \(\pi_i^{\rm reset}=c(\tanh a_{i-1}+\tanh a_i)/q\). Across site \(x_i\), the derivative jump is
\[
D[p'(x_i+)-p'(x_i-)]=-Dcq(\tanh a_i+\tanh a_{i-1})=-r\pi_i^{\rm reset}.
\]
Therefore the distributional forward equation \(Dp''-rp+r\sum_i\pi_i^{\rm reset}\delta_{x_i}=0\) holds. Periodic uniformly elliptic Brownian motion with bounded Poisson jump intensity has an irreducible transition density on the circle, so this invariant probability is unique and the stationary ergodic theorem applies.

**Harmonic coordinate and drift.** Put \(A=L/(2S)\), select \(h_1=0\), and impose \(h_{i+1}-h_i=2A\sinh a_i\) (also \(h_{i+N}=h_i+L\)). On the Voronoi interval of site \(x_i\) define
\[
H(x)=h_i+A\sinh[q(x-x_i)].
\]
At the common boundary of two Voronoi cells, the left and right values agree because their difference is \(h_{i+1}-h_i-2A\sinh a_i=0\). The derivatives agree there because both equal \(Aq\cosh a_i\). Thus \(H\) is continuously differentiable and piecewise twice continuously differentiable, with bounded derivative and bounded jumps under resets. Since \(H(Q(x))=h_i\) within cell \(i\),
\[
DH''(x)+r(H(Q(x))-H(x))=DAq^2\sinh[q(x-x_i)]-rA\sinh[q(x-x_i)]=0,
\]
using \(Dq^2=r\). The derivative is continuous at all cell boundaries, so the generalized Itô formula has no local-time term. Hence \(M_t=H(X_t)-H(X_0)\) is a square-integrable martingale. Because \(H(x+L)=H(x)+L\), the function \(H(x)-x\) is bounded. It follows that the physical effective drift is zero; the bounded correction does not change the limiting diffusive variance or weak limit.

**Exact quadratic variation.** If \(z=x-Q(x)\), the predictable quadratic-variation rate of \(H(X_t)\) is
\[
2D A^2q^2\cosh^2(qz)+rA^2\sinh^2(qz).
\]
Under the invariant law above, the half-gaps contribute symmetrically. In particular,
\[
\mathbb E_p[\cosh^2(qz)]
=\frac1T\sum_i\int_0^{a_i}\frac{\cosh(a_i-u)\cosh^2u}{\cosh a_i}\,du
=\frac{T+2S}{3T};
\]
the elementary integral is \((2\sinh a+\tanh a)/3\). Consequently \(\mathbb E_p[\sinh^2(qz)]=2(S/T-1)/3\) and
\[
\frac12\mathbb E_p\left[\frac{d\langle M\rangle_t}{dt}\right]
=rA^2\left[\mathbb E_p\cosh^2(qz)+\frac12\mathbb E_p\sinh^2(qz)\right]
=rA^2S/T=\frac{rL^2}{4ST}.
\]
The circle process is ergodic, so the time-averaged bracket converges to this constant. All martingale jumps are bounded by \(A\max_i\sinh a_i\), and the Brownian coefficient is bounded. The martingale central limit theorem gives the stated Gaussian law. The martingale isometry yields its variance rate; a bounded corrector changes this variance by only \(O(\sqrt t)\) and therefore leaves the limiting rate unchanged.

**Disorder comparison.** Set \(A_0=\sum_i a_i=qL/2\) and \(C_3=\sum_i a_i^3\). The series \(S=A_0+C_3/6+O(q^5)\) and \(T=A_0-C_3/3+O(q^5)\) imply \(ST=A_0^2-A_0C_3/6+O(q^6)\). Using \(r=Dq^2\) gives the stated small-rate expansion. Strict convexity of \(u\mapsto u^3\) shows \(\sum_i\ell_i^3>N(L/N)^3\) for any unequal positive gaps. The first-order difference is positive, hence so is the exact difference for all sufficiently small rates. For the largest-gap law, \(S\sim(k/2)e^{q\ell_{\max}/2}\) and \(T\to N\), immediately giving the result.

**Relationship to the known rate-optimized ceiling.** Writing \(f(a)=a^2/(\sinh a\tanh a)\), the source paper already identifies \(\sup_{a>0}f(a)\approx1.169\) as the regular-array optimum. Cauchy–Schwarz and \(f(a)\le \sup f\) yield
\[
ST\ge\left(\sum_i\frac{\sinh a_i}{\sqrt{\cosh a_i}}\right)^2
\ge\frac{(\sum_i a_i)^2}{\sup_{a>0}f(a)}.
\]
Hence \(D_{\rm eff}/D\le\sup f\), with the regular array attaining the known ceiling after rate optimization. This last ceiling is not presented as novel; it provides a consistency check on the new all-gap identity.

## Verification

Run `python checker.py` from the directory containing this result and the included checker, with NumPy available. The checker evaluates an **independent** description of the process: at each Poisson reset, the displacement accumulated since the previous reset has a symmetric two-sided exponential density \(q e^{-q|y|}/2\). Exact integrals over translated Voronoi cells produce a finite-state tilted generator recording period windings. Its first two eigenvalue derivatives yield drift and diffusivity independently of the harmonic-coordinate calculation. The checker compares six nonuniform/regular configurations at several parameter values, normalizes site probabilities, and tests small-rate and large-rate consequences and the Cauchy inequality. It reports 235 finite checks. Infinite claims depend on the analytic proof, not these finite calculations.

For example, at \(D=1,r=9,L=1\) and gaps \((0.2,0.3,0.5)\), both independent expressions give \(D_{\rm eff}=1.048056198935\ldots\). At \(D=r=L=1\), gaps \((0.3,0.7)\) give \(1.0146414895\ldots\) versus \(1.0101912826\ldots\) for \((0.5,0.5)\); at \(r=100\) the ordering reverses to \(0.7034579212\ldots\) versus \(1.0470382788\ldots\).

## Relationship to prior work

Alston and Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1, introduce exactly this nearest-site Poisson resetting model. Their equation (17) supplies the **regular-array** diffusivity \(D\,a^2\operatorname{csch}(a)\coth(a)\), and their equations (18)–(20) discuss maximal rate-optimized diffusion over arbitrary configurations. The same source's main text states that an analytic expression for arbitrary arrays is unavailable through its site-exit stationary weights, and its Supplementary Section IV proves a weaker generic weak-rate enhancement inequality. The present statement does **not** claim novelty for the regular formula, generic enhancement at small reset rate, or globally optimized regular-site superiority. The new result instead supplies the exact **nonuniform** closed form, its stationary distribution and selected-reset-site weights, and the sharp fixed-rate disorder reversal and largest-gap high-rate law. Its Poisson-event weights are not assumed equivalent to the paper's site-exit residence fractions.

A related earlier item concerning the **uniform** nearest-site model evaluates higher cumulants of physical displacement, but does not cover nonuniform gaps or the all-gap closed form. Other general renewal, cell-problem, or periodic-jump-diffusion methods could potentially imply this formula without displaying it; publication-priority assessment therefore remains qualified.

## Limitations

The theorem is for one-dimensional instantaneous nearest-site **Poisson** resetting to a fixed periodic array, with homogeneous Brownian diffusion between resets. It does not give the finite-time displacement distribution or treat arbitrary renewal clocks, multidimensional Voronoi tessellations, mobile sites, finite reset durations, or random nonperiodic media. Its Gaussian limit and exact effective diffusivity are mathematical population asymptotics; finite trajectories need not identify them accurately. The global rate-optimized regular-array ceiling was already established in the motivating literature. No independent validation or exhaustive literature uniqueness claim is made.

## References

1. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1 (first public January 23, 2024), https://arxiv.org/abs/2401.12772. Open preprint and accompanying supplementary material: https://thibaultbertrand.com/assets/pdf/2024_arxiv_a.pdf.
2. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, Physical Review E **111**, 034114 (2025), DOI:10.1103/PhysRevE.111.034114. This is a later journal version of reference 1, not a later first-public date.
3. M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A **53**, 193001 (2020), general background on resetting; no coverage of the derived nonuniform-array theorem is claimed or assumed.
