# Exact logarithmic extremes and duration selection for Poisson-reset scaled Brownian area

## Finding

For independent fully renewed scaled-Brownian excursions separated by Poisson resets, the largest **absolute area accumulated in a single completed reset interval** has a sharp logarithmic scale. More surprisingly, with probability tending to one, its winning interval is **not** the longest reset interval: the winning duration is asymptotically a strict, universal fraction of the longest duration.

Let \(0<\beta<2\), \(K>0\), and \(r>0\). For each completed cycle \(i\), let \(T_i\) be exponential with rate \(r\) and let \(B_i\) be a fresh standard Brownian motion independent of all durations and other Brownian paths. Within that cycle, the displacement at age \(a\) is \(X_i(a)=\sqrt{2K}\,B_i(a^\beta)\), and its nonnegative absolute-area reward is

\[
A_i=\int_0^{T_i}|X_i(a)|\,da.
\]

Put

\[
m=\beta+2,\qquad q=\frac{2}{m+1},\qquad
v=\frac{4K}{(\beta+1)(\beta+2)},
\]
\[
u_* = \left(\frac{m}{2vr}\right)^{1/(m+1)},\qquad
C=\frac{m+1}{m}r u_*,\qquad
b_n=\left(\frac{\log n}{C}\right)^{1/q}.
\]

The one-cycle area has the **sharp logarithmic Weibull tail**

\[
\boxed{\lim_{x\to\infty}x^{-q}\log\mathbb P(A_1>x)=-C.}
\]

Let \(J_n\) be the index of the largest area among the first \(n\) completed cycles, and \(I_n\) the index of the longest duration, with any deterministic tie rule. Then, as \(n\to\infty\),

\[
\boxed{\frac{A_{J_n}}{b_n}\xrightarrow{\mathbb P}1,\qquad
\frac{rT_{J_n}}{\log n}\xrightarrow{\mathbb P}\frac{m}{m+1},\qquad
\frac{rT_{I_n}}{\log n}\xrightarrow{\mathbb P}1.}
\]

In particular,

\[
\boxed{\mathbb P(J_n=I_n)\longrightarrow0,\qquad
\frac{A_{I_n}}{b_n}\xrightarrow{\mathbb P}0.}
\]

These limits remain true for the maximum over **all completed reset intervals before a physical observation time** \(t\), replacing \(n\) by \(rt\) in the logarithmic normalizers as \(t\to\infty\). The unfinished final interval is not included in this corollary.

For ordinary Brownian diffusion with \(\beta=K=r=1\), the constants simplify to

\[
\boxed{\frac{\max_{1\le i\le n}A_i}{(\log n)^2}
\xrightarrow{\mathbb P}\frac38,\qquad
\frac{T_{J_n}}{\log n}\xrightarrow{\mathbb P}\frac34,
\qquad \frac{T_{I_n}}{\log n}\xrightarrow{\mathbb P}1.}
\]

## Assumptions and scope

The diffusivity clock is **restarted** with the position at every Poisson event. Each excursion is an independent copy of scaled Brownian motion \(\sqrt{2K}B(a^\beta)\); the argument is not for position-only resets that preserve a globally aging diffusivity clock. The reset waiting times are i.i.d. exponential with fixed positive rate, independent of the paths. The theorem concerns the absolute area **of individual complete cycles**, rather than the distribution of the total accumulated area or the maximum of the position process.

## Proof

**1. Gaussian excursion-area tail.** By Brownian scaling,

\[
A_i\overset d=T_i^pY_i,\qquad
p=1+\frac\beta2=\frac m2,
\quad Y_i=\sqrt{2K}\int_0^1|B_i(u^\beta)|\,du,
\]

where \(Y_i\) is independent of \(T_i\). Define the centered Gaussian signed area \(G=\sqrt{2K}\int_0^1B(u^\beta)\,du\). Its covariance calculation gives

\[
\operatorname{Var}G=2K\int_0^1\int_0^1
\min(s^\beta,t^\beta)\,ds\,dt=v.
\]

Because \(Y\ge G\), the Gaussian tail lower bound implies
\(\liminf_{y\to\infty}y^{-2}\log\mathbb P(Y>y)\ge-1/(2v)\).
For the upper bound, write \(Y\) as the supremum, over measurable \(|h|\le1\), of the centered Gaussian linear forms \(\sqrt{2K}\int_0^1h(u)B(u^\beta)\,du\). This family has a separable version; all its variances are at most \(v\), since the Brownian covariance kernel is nonnegative, and the choice \(h\equiv1\) attains \(v\). Its supremum has finite mean because continuous Brownian paths have integrable suprema. The Borell–Tsirelson–Ibragimov–Sudakov Gaussian concentration bound therefore gives

\[
\mathbb P(Y>y)\le
\exp\!\left(-\frac{(y-\mathbb EY)^2}{2v}\right)
\quad\text{for }y>\mathbb EY.
\]

Together these estimates yield

\[
\lim_{y\to\infty}y^{-2}\log\mathbb P(Y>y)=-\frac1{2v}.
\]

**2. The single-cycle saddle.** Independence and the exponential waiting-time density imply

\[
\mathbb P(A_1>x)=\int_0^\infty re^{-rt}
\mathbb P(Y>x/t^p)\,dt.
\]

Set \(t=x^q u\), with \(q=2/(m+1)\). On any fixed compact subset of \((0,\infty)\), step 1 gives the integrand's logarithmic cost at speed \(x^q\) as

\[
h(u)=ru+\frac1{2vu^m}.
\]

The same Gaussian concentration bound controls the \(u\downarrow0\) contribution. The independent exponential density controls \(u\to\infty\), while the region in which \(x/t^p\) remains bounded begins at durations of order \(x^{1/p}\), which is larger than \(x^q\) and is exponentially negligible at speed \(x^q\). Hence elementary upper/lower Laplace bounds apply. The function \(h\) is strictly convex, diverges at both endpoints, and has its unique minimum at \(u_*=(m/(2vr))^{1/(m+1)}\). Its minimum equals \(C=r u_*(m+1)/m\), proving the displayed sharp tail. The same estimates provide a constrained Laplace upper bound when the cycle duration is restricted to a closed set after rescaling.

**3. Size of the maximal reward.** Write \(M_n=\max_{1\le i\le n}A_i\). The cycles are i.i.d., so \(\mathbb P(M_n\le x)=(1-\mathbb P(A_1>x))^n\). Taking \(x=a b_n\), the preceding limit gives

\[
\mathbb P(A_1>a b_n)=n^{-a^q+o(1)}
\qquad(a>0).
\]

For \(a<1\) the expected count of exceedances diverges; for \(a>1\) it tends to zero. Thus \(M_n/b_n\to1\) in probability. This first-order limit does not assert a centered Gumbel law.

**4. The duration of the winning area.** Set \(z=rT_1/\log n\). For fixed \(a>0\), the joint rare-event cost for \(A_1>a b_n\) and \(z\) near a positive number is \((\log n)\,H_a(z)\), with

\[
H_a(z)=z+\frac{m^m}{(m+1)^{m+1}}\frac{a^2}{z^m}.
\]

This is the same Laplace bound as step 2 after a change of scale. It has a unique minimizer at \(z_a=\frac{m}{m+1}a^q\) and minimum \(a^q\). Put \(\theta=m/(m+1)\). For each \(\delta>0\), strictness of the minimizer gives \(\inf_{|z-\theta|\ge\delta}H_1(z)>1\). Choose \(a<1\) sufficiently close to one so that also \(\inf_{|z-\theta|\ge\delta}H_a(z)>1\). The constrained Laplace upper bound and a union bound over \(n\) cycles show that with probability tending to one no cycle with \(A_i>a b_n\) has \(|rT_i/\log n-\theta|\ge\delta\). Step 3 guarantees that at least one such high-area cycle exists with probability tending to one. Therefore \(rT_{J_n}/\log n\to\theta\) in probability.

**5. The longest-duration mismatch.** Elementary exponential order statistics give \(rT_{I_n}/\log n\to1\) in probability. Since \(\theta<1\), the two maximizing indices coincide with probability tending to zero. Conditional on all durations, the Brownian shape factor \(Y_{I_n}\) still has the fixed distribution of \(Y\), because the longest-duration index is chosen using durations alone. As \(T_{I_n}=O_{\mathbb P}(\log n)\) and \(b_n\) grows as \((\log n)^{p+1/2}\), the ratio \(T_{I_n}^{p}Y_{I_n}/b_n\) tends to zero in probability.

**6. Physical-time version.** Let \(N(t)=\max\{n:\sum_{i=1}^nT_i\le t\}\). Renewal theory (or the Poisson strong law) gives \(N(t)/(rt)\to1\) almost surely. The maximum of the first \(N(t)\) rewards is bounded between the maxima of deterministic groups of \((1\pm\varepsilon)rt\) cycles with high probability, yielding the same logarithmic reward scaling. For the winning duration, apply the union bound of step 4 over the first \(\lceil2rt\rceil\) cycles and the lower bound from the first \(\lfloor rt/2\rfloor\) cycles. The longest completed waiting time is similarly sandwiched. This proves the time-indexed corollary.

## Verification

The included standard-library program \(`check_extremes.py`\) independently computes the covariance-kernel integral by midpoint quadrature and checks the tail-saddle, optimizer, normalization and elementary Brownian special-case identities for fifteen parameter combinations. Its deterministic test run passed 276 checks. These checks support the displayed algebra; Gaussian concentration and the constrained Laplace principle are analytic arguments, not finite experiments.

## Relationship to prior work

Méndez and Cristín (2026) introduce the renewed scaled-Brownian absolute-area functional, develop its low-order moments under Poisson resetting, and analyze largest-cycle areas principally in power-law resetting regimes. Their cited maximum-waiting-period results do not supply the present Poisson tail constant or selected-duration law. Den Hollander, Majumdar, Meylahn and Touchette (2019) establish resetting-based functional large-deviation results for ordinary Brownian absolute area, including a flat upper rate at speed equal to observation time; that does not specify the present single-cycle logarithmic tail or its joint duration law. Smith and Majumdar (2022) derive condensate costs for **signed** areas of general self-similar Gaussian processes; the Gaussian time-area saddle is closely related, but the present assertion concerns the absolute-area maximum with a selected-cycle duration among many reset intervals. Smith, Majumdar and Schehr (2023) establish ordering-event universalities for arbitrary reset-cycle observables, not their absolute scales or comparison with the longest waiting time.

The novelty claim is deliberately confined to the **combined marked Poisson-cycle theorem**: sharp area-tail constant, maximal-area scale and a limiting selected-duration fraction strictly below the longest-duration fraction. General Gaussian-extremes theorems and broader marked-renewal results may imply parts of its proof; priority beyond the inspected material is not certified.

## Limitations

All limits are asymptotic with fixed \(\beta,K,r\). No finite-number convergence rates or second-order centered extreme-value distribution are claimed. The absolute area of the incomplete current interval is excluded. The result neither describes upper tails of the **total** time-integrated absolute area nor covers power-law reset waiting times, nonrenewal diffusivity clocks, or non-Gaussian excursion processes. The review recorded here is not an independent audit.

## References

1. V. Méndez and J. Cristín, *Absolute area under a scaled Brownian motion with resetting* (2026), arXiv:2610.19985, first submitted 14 October 2026; relevant material: Sections II, IV.1 and VI.1. https://arxiv.org/abs/2610.19985
2. F. den Hollander, S. N. Majumdar, J. M. Meylahn and H. Touchette, *Properties of additive functionals of Brownian motion with resetting* (2019), arXiv:1801.09909; Sections III and VI. https://arxiv.org/abs/1801.09909
3. N. R. Smith and S. N. Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting* (2022), arXiv:2202.03546; Section II and Appendix B. https://arxiv.org/abs/2202.03546
4. N. R. Smith, S. N. Majumdar and G. Schehr, *Striking universalities in stochastic resetting processes* (2023), arXiv:2301.11026. https://arxiv.org/abs/2301.11026
5. Standard Gaussian concentration (Borell–Tsirelson–Ibragimov–Sudakov inequality), classical theorem used with the explicitly computed maximal Gaussian variance.
