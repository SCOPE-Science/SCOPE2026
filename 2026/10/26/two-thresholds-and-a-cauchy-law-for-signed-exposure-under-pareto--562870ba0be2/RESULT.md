# Two thresholds and a Cauchy law for signed exposure under Pareto resetting

## Finding
For fully renewed scaled Brownian motion subjected to independent Pareto renewal resets, the **signed** accumulated displacement has a symmetric stable limit and two distinct notions of long-time averaging. A Cauchy law occurs at \(\alpha=1+\beta/2\), while the *mean-square* threshold, when accessible, is \(\alpha=1+\beta\). In between, the signed time average converges to zero in probability although its variance diverges. This separates typical signed-exposure statistics from rare, very long excursions.

Write \(\gamma=1+\beta/2\), \(p=\alpha/\gamma\) and \(v=4K/((\beta+1)(\beta+2))\). For every \(0<\beta<2\), \(1<\alpha<2\), and \(K,t_0>0\),
\[
 t^{-1/p}S(t)\;\Longrightarrow\;Z_p,\qquad
 \mathbb E[e^{iuZ_p}]=\exp(-\lambda|u|^p),
\]
where
\[
 m=\frac{\alpha t_0}{\alpha-1},\qquad
 M_p=v^{p/2}\frac{2^{p/2}\Gamma((p+1)/2)}{\sqrt{\pi}},
\]
\[
 \lambda=\frac{t_0^\alpha M_p}{m}
 \begin{cases}
 \Gamma(1-p)\cos(\pi p/2),&p\ne1,\\
 \pi/2,&p=1.
 \end{cases}
\]
The formula is positive throughout \(0<p<2\); its expression at \(p=1\) is the continuous extension. In particular,
\[
 \frac{S(t)}t\Longrightarrow
 \operatorname{Cauchy}\!\left(0,\frac{\pi t_0^\alpha M_1}{2m}\right)
 \quad\text{if }\alpha=1+\beta/2.
\]
If \(\alpha<\gamma\) then \(|S(t)|/t\to\infty\) in probability; if \(\alpha>\gamma\), \(S(t)/t\to0\) in probability.

The exact second-moment leading term is
\[
 \mathbb E[S(t)^2]\sim Vt^{3+\beta-\alpha},\qquad
 V=\frac{2\gamma v t_0^\alpha}{m(2\gamma-\alpha)(2\gamma-\alpha+1)}.
\]
Thus \(\operatorname{Var}(S(t)/t)\sim Vt^{1+\beta-\alpha}\). For \(0<\beta<1\), the interval \(\gamma<\alpha<1+\beta\) has probability convergence to zero together with divergent variance; the variance tends to \(V\) at \(\alpha=1+\beta\), and mean-square convergence holds for \(\alpha>1+\beta\). For \(1\le\beta<2\), mean-square convergence does not occur within \(1<\alpha<2\). All finite-time signed means are exactly zero.

## Assumptions and scope
Let \((\tau_j)_{j\ge1}\) be i.i.d., independent of the Brownian drivers, with \(\mathbb P(\tau_j>u)=1\) for \(0\le u<t_0\) and \((t_0/u)^\alpha\) for \(u\ge t_0\). Start at the origin. On each renewal interval, use an independent standard Brownian motion \(W_j\) and the process \(X(T_{j-1}+a)=\sqrt{2K}\,W_j(a^\beta)\), \(0\le a<\tau_j\), with \(T_j=\sum_{i=1}^j\tau_i\). Every reset restarts both position and the time-dependent diffusivity clock. Define the **signed**, not absolute, integrated displacement \(S(t)=\int_0^t X(s)\,ds\). Parameters satisfy \(0<\beta<2\), \(1<\alpha<2\), \(K>0\) and \(t_0>0\). The fixed lower Pareto cutoff is part of the stated model. The primary setting is anomalous diffusion/renewal resetting in statistical mechanics (MSC2020 82C31).

## Proof
**1. Gaussian reward inside one excursion.** For a deterministic duration \(u>0\), define \(J(u)=\int_0^u\sqrt{2K}W(s^\beta)\,ds\). Gaussian covariance gives
\[
 \operatorname{Var}(J(u))=2K\int_0^u\!\int_0^u\min(s,a)^\beta\,ds\,da
 =vu^{2\gamma},\quad v=\frac{4K}{(\beta+1)(\beta+2)}.
\]
A completed cycle therefore produces the reward \(J_j=\tau_j^\gamma\xi_j\), where the \(\xi_j\) are i.i.d. centered Gaussian with variance \(v\), independent of all cycle lengths. This representation is equality in joint distribution with the renewal times, and gives \(\mathbb E|\xi_j|^p=M_p\).

**2. Tail and stable attraction.** Put \(p=\alpha/\gamma\), which lies strictly between zero and two. Pareto regular variation, Gaussian moments and the product-tail lemma imply
\[
 \mathbb P(J_j>x)\sim\mathbb P(J_j<-x)
 \sim\tfrac12 t_0^\alpha M_p\,x^{-p}.
\]
The centered, symmetric variables \(J_j\) thus lie in the normal domain of attraction of a symmetric \(p\)-stable distribution. The standard Lévy–Khintchine tail-to-characteristic-function integral yields
\[
 n^{-1/p}\sum_{j=1}^{n}J_j\Longrightarrow Y_p,
 \quad\mathbb E e^{iuY_p}=
 \exp[-t_0^\alpha M_p\,\Gamma(1-p)\cos(\pi p/2)|u|^p],
\]
with the continuous value \(\pi/2\) when \(p=1\). Exact sign symmetry removes centering even at the critical index.

**3. Renewal random index and last excursion.** Write \(N(t)=\max\{n:T_n\le t\}\). As \(m=\mathbb E\tau_j<\infty\), the renewal strong law gives \(N(t)/t\to1/m\). Joint functional stable convergence for the i.i.d. rewards and the deterministic-limit random time change gives \(t^{-1/p}\sum_{j=1}^{N(t)}J_j\Longrightarrow Z_p\) with exponent multiplied by \(1/m\). This does not assume independence of \(J_j\) and \(\tau_j\): dependence is allowed because the limiting renewal time change is deterministic. The backward recurrence age \(A_t=t-T_{N(t)}\) is tight for the nonlattice finite-mean Pareto renewal process. Conditional on the ages, the remaining incomplete excursion has centered normal signed area with variance \(v A_t^{2\gamma}\); consequently it is tight and divided by \(t^{1/p}\) tends to zero in probability. Together these prove the stated stable law. Since a nondegenerate symmetric stable law has no atom at zero, multiplying the limit by \(t^{1/p-1}\) proves all three typical-time-average alternatives, including divergence in absolute value for \(p<1\).

**4. Sharp second moment.** Let \(h(t)=\mathbb E[S(t)^2]\), \(q=2\gamma=2+\beta\), \(\Psi(t)=\mathbb P(\tau>t)\), and \(f\) its density. Independence and zero mean across excursions yield the exact renewal equation
\[
 h(t)=vt^q\Psi(t)+v\int_0^t u^qf(u)\,du+\int_0^t h(t-u)f(u)\,du.
\]
Its Laplace transform is
\[
 \widehat h(s)=\frac{v}{1-\widehat f(s)}\left[
 \int_0^\infty e^{-st}t^q\Psi(t)\,dt
 +\frac1s\int_0^\infty e^{-su}u^qf(u)\,du\right].
\]
Because \(q>\alpha\), the two bracketed terms together are asymptotic to \(q t_0^\alpha\Gamma(q-\alpha)s^{-(q-\alpha+1)}\). Moreover \(1-\widehat f(s)\sim ms\). A monotone Tauberian theorem applies: conditional on the renewal times, \(h(t)\) is \(v\) times the expected sum of nondecreasing completed-excursion powers and current-age power, which increases continuously across completed cycles. Hence
\[
 h(t)\sim \frac{vq t_0^\alpha}{m(q-\alpha)(q-\alpha+1)}t^{q-\alpha+1}
 =Vt^{3+\beta-\alpha}.
\]
As \(\mathbb ES(t)=0\), dividing by \(t^2\) gives the variance classification. The inequality \(\gamma<1+\beta\) is strict when \(\beta>0\). For \(\beta\ge1\), the constraint \(\alpha<2\) prevents access to the mean-square convergent regime.

## Verification
The accompanying standalone `signed_area_verify.py` implements the cycle constants, an independent analytic Laplace-transform evaluation of the exact renewal second moment, and direct finite-horizon renewal-clock Monte Carlo using conditional Gaussian integration. It checks three regimes: a Cauchy point \((\beta,\alpha)=(0.5,1.25)\), probability convergence with mean-square convergence \((0.5,1.7)\), and a non-self-averaging stable index below one \((1.2,1.4)\). In total **43 numerical assertions passed**. The Laplace-transform ratios approach unity at small transform parameters, and conditional-Gaussian simulated characteristic functions agree with stable predictions within the script's declared finite-time tolerance. These finite calculations support but do not establish the infinite-time assertions; those follow from the proof above. Run `python signed_area_verify.py` with NumPy, SciPy and mpmath.

## Relationship to prior work
Méndez and Cristín (2026, arXiv:2610.19985v1) analyze the **absolute** area of renewed scaled Brownian motion with exponential and heavy-tailed resetting, deriving lower moments and an ergodicity boundary at \(\alpha=1+\beta\). The present theorem retains their physical reset framework but concerns the **signed** area and gives an explicit stable limit, a Cauchy crossover at the strictly smaller \(\alpha=1+\beta/2\), and a separate sharp signed-variance asymptotic. These are different random functionals; one cannot infer their stable laws merely by deleting absolute values. The earlier Méndez–Flaquer-Galmés–Cristín (2026, arXiv:2602.04342v1) derives the variance and Gaussian distribution for the signed area of *unreset* scaled Brownian motion, providing the single-cycle input used here. Smith and Majumdar (2022, arXiv:2202.03546v1) study the signed area under **Poisson**, not Pareto, resetting, and Gaussian typical limits in that setting. General renewal-reward stable-limit results (e.g. Levy–Taqqu, 2000) supply classical probabilistic machinery but do not, in the examined accessible material, state this physical Pareto-SBM model's explicit constants or its separated in-probability/mean-square threshold classification. Earlier power-law resetting of continuous-time random walks (Bodrova–Sokolov, 2020) addresses position distributions, not this signed integrated-displacement limit. These distinctions are conclusions from examined material, not an exhaustive proof of research priority.

## Limitations
The result assumes a *fully renewed* diffusivity clock, exact Pareto waiting times with a fixed positive cutoff, independent Brownian paths, centered Gaussian fluctuations, and \(1<\alpha<2\). It does not cover \(\alpha\le1\), tempering, nonrenewal diffusivity protocols, higher-dimensional fields, or a fluctuating reset location. The stable law is a weak limit; no local limit or convergence-rate theorem is claimed. The second-moment asymptotic does not imply convergence of moments of the stable limit (which has infinite variance). The standard stable domain-of-attraction and renewal theorems are used as established mathematical results, not claimed as new. Independent assessment of mathematical priority and verification has not been performed.

## References
1. V. Méndez and J. Cristín, *Absolute area under a scaled Brownian motion with resetting*, arXiv:2610.19985v1 (first posted 2026-10-14), https://arxiv.org/abs/2610.19985.
2. V. Méndez, R. Flaquer-Galmés and J. Cristín, *Area under subdiffusive random walks*, arXiv:2602.04342v1 (first posted 2026-02-04), https://arxiv.org/abs/2602.04342.
3. N. R. Smith and S. N. Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting*, arXiv:2202.03546v1 (2022), https://arxiv.org/abs/2202.03546.
4. A. S. Bodrova and I. M. Sokolov, *Continuous-time random walks under power-law resetting*, Physical Review E 101, 062117 (2020), arXiv:2001.01350, https://arxiv.org/abs/2001.01350.
5. J. B. Levy and M. S. Taqqu, *Renewal reward processes with heavy-tailed inter-renewal times and heavy-tailed rewards*, 2000 (general probabilistic background).
