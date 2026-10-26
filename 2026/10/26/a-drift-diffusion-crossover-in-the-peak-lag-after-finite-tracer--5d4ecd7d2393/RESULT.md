# A drift–diffusion crossover in the peak lag after finite tracer shutoff

## Finding

Consider a constant-rate tracer release into a one-dimensional advection–dispersion channel for exactly \(\tau>0\) time units. At a perfectly absorbing downstream receiver, let \(t_*(\tau)\) be the time of maximum arriving mass flux and let \(\delta=t_* -\tau\) denote the time elapsed since source shutoff. Define \(c=L^2/(4D)>0\), \(b=v^2/(4D)\ge0\), \(T=\tau/c\), \(a=bc\), and \(w=c/\delta\). Then the arrival flux has exactly one strict global maximum, always after shutoff. Its lag decreases strictly with source duration and with drift parameter \(b\); the peak time increases strictly with source duration, with \(0<\partial t_*/\partial\tau<1\). The unique lag is specified by
\[
w=aT+\frac32\log(1+Tw)+\frac{w}{1+Tw}.
\]
The long-release limit has two genuinely different scales:
\[
\begin{aligned}
 b=0:\quad &w=\frac32\bigl(\log T+\log\log T+\log(3/2)\bigr)+o(1),\\
 b>0\ \text{fixed}:\quad &w=aT+3\log T+\frac32\log a+o(1).
\end{aligned}
\]
More generally, for any varying nonnegative drift satisfying \(aT/\log T\to\theta\in[0,\infty)\),
\[
\frac{w}{\log T}\longrightarrow\theta+\frac32.
\]
These are asymptotic claims as \(T\to\infty\). They quantify the transition from an inverse-logarithmic post-shutoff delay at zero drift to an inverse-duration delay at fixed positive drift.

## Assumptions and scope

Let \(L,D,\tau>0\), \(v\ge0\), and consider tracers obeying \(dX_t=v\,dt+\sqrt{2D}\,dB_t\), beginning at \(X_0=0\), with absorbing reception at \(L\). Ignore decay, adsorption, finite receiver capacity and recirculation. Each infinitesimal tracer input is independent; input mass rate is constant and positive throughout \([0,\tau]\), zero otherwise. The normalized first-arrival flux for one tracer, derived from the absorbing drift–diffusion equation, is
\[
f(t)=\frac{L}{\sqrt{4\pi Dt^3}}\exp\!\left(-\frac{(L-vt)^2}{4Dt}\right),\qquad t>0.
\]
Since \(v\ge0\), this is a probability density. For determining arrival-peak times, it is proportional to \(t^{-3/2}\exp(-c/t-bt)\); the discarded constant is independent of arrival time. The total absorbed flux under the finite source is proportional to
\[
Q_\tau(t)=\int_{\max(0,t-\tau)}^{t}f(u)\,du,\qquad t>0.
\]
The result concerns *absorbed first-passage mass flux*, not pointwise resident concentration or a constant-concentration inlet boundary condition. Those distinct observables have different kernels and need not satisfy the same formulas.

## Proof

**1. Global peak and its unique location.** Write \(\ell(u)=\log f(u)\) up to an additive constant, so \(\ell'(u)=c/u^2-3/(2u)-b\). This derivative vanishes exactly once, at the strict density mode
\[
m=\frac{2c}{3/2+\sqrt{9/4+4bc}}>0,
\]
and is positive below \(m\), negative above \(m\). On \(0<t\le\tau\), \(Q_\tau'(t)=f(t)>0\). For \(t=\tau+s\), \(s>0\),
\[
Q_\tau'(\tau+s)=f(s+\tau)-f(s).
\]
Define \(G(s)=\ell(s+\tau)-\ell(s)\). Directly,
\[
G(s)=\frac{c\tau}{s(s+\tau)}-\frac32\log(1+\tau/s)-b\tau,
\]
\[
G'(s)=\frac{\tau\bigl[\frac32s(s+\tau)-c(2s+\tau)\bigr]}{s^2(s+\tau)^2}.
\]
The bracket is a quadratic with positive leading coefficient and strictly negative constant term, so it has exactly one positive zero. Thus \(G\) first strictly decreases, then strictly increases. Moreover \(G(s)\to+\infty\) as \(s\downarrow0\); as \(s\to\infty\), it tends to \(-b\tau\), and when \(b=0\) it approaches zero from below because \(G(s)=-3\tau/(2s)+O(s^{-2})\). Therefore \(G\) crosses zero exactly once, on its decreasing branch. The signs of \(G\) and \(Q_\tau'\) coincide, proving a unique strict global peak \(t_*=\tau+\delta\), \(\delta>0\). Unimodality of \(f\) also gives \(\delta<m<\delta+\tau\).

**2. Strict parameter monotonicities.** The peak equation is \(\ell(t_*)=\ell(t_*-\tau)\). Its implicit derivative is nonzero because the root is on the descending branch of \(G\). Hence
\[
\frac{\partial t_*}{\partial\tau}=\frac{\ell'(\delta)}{\ell'(\delta)-\ell'(t_*)},\qquad 0<\frac{\partial t_*}{\partial\tau}<1.
\]
Consequently \(\partial\delta/\partial\tau<0\). Holding \(c,\tau\) fixed and varying \(b\), we have \(\partial_bG=-\tau\) and \(G'(\delta)<0\); thus \(\partial_b\delta=\tau/G'(\delta)<0\). Both assertions include the one-sided derivative at \(b=0\).

**3. Dimensionless equation.** Substitute \(s=\delta=c/w\), \(\tau=cT\), and \(b=a/c\) into \(G(\delta)=0\). The first rational term becomes \(Tw^2/(1+Tw)\) and the drift term becomes \(aT\). Dividing by \(T\) and rearranging yields
\[
w=aT+\frac32\log(1+Tw)+\frac{w}{1+Tw}.
\]
Its physically relevant positive root is unique by Step 1. In the short-release limit \(\tau\downarrow0\), the equality of density values across a symmetric interval around \(t_*-\tau/2\), together with \(\ell''(m)<0\), gives \(t_*=m+\tau/2+O(\tau^2)\).

**4. Long-release asymptotics with no drift.** For \(a=0\), the root equation implies \(w\to\infty\), \(w=O(\log T+\log w)\), and hence \(w\sim(3/2)\log T\). Consequently \(\log(1+Tw)=\log T+\log\log T+\log(3/2)+o(1)\), while \(w/(1+Tw)=o(1)\). Substitution proves the first displayed expansion.

**5. Fixed positive drift.** When \(a>0\) is fixed, the root equation gives \(w=aT+O(\log T)\). Then \(\log(1+Tw)=2\log T+\log a+o(1)\) and \(w/(1+Tw)=o(1)\), proving \(w=aT+3\log T+(3/2)\log a+o(1)\).

**6. Uniform crossover.** Suppose \(a=a(T)\ge0\) and \(aT/\log T\to\theta<\infty\). The root equation bounds \(w\) above by \(aT+(3/2)\log(1+Tw)+1\), which forces \(w=O(\log T)\); evaluation of the equation at any fixed positive \(w\) shows \(w\to\infty\). Hence \(\log(1+Tw)/\log T\to1\) and \(w/(1+Tw)/\log T\to0\). Divide the root equation by \(\log T\) to obtain \(w/\log T\to\theta+3/2\). All asymptotics concern positive roots, already proved unique, and do not rely on numerical enumeration.

## Verification

The included standard-library Python script `check_peak.py` deterministically reconstructs the scalar equation, checks the density-equality and derivative signs at 2,000 seeded parameter configurations, checks drift and pulse-duration ordering at 300 additional parameter pairs each, and evaluates asymptotic examples and the crossover. Run it with `python3 check_peak.py`. All checks passed on the delivered file. Finite floating-point experiments support but cannot establish the universal statements; Steps 1–6 supply the proof. For \(c=1\), \(\tau=100\), the script gives post-shutoff lag approximately \(0.09581063645\) at \(b=0\) and \(0.00877020045\) at \(b=1\).

## Relationship to prior work

The inverse-Gaussian first-passage kernel is classical; it is not claimed as new. Kreft and Zuber (1978) discuss flux and resident formulations of the dispersion equation. Yu, Warrick and Conklin (1999) examine breakthrough curves for step inputs and statistical moments; their abstract was accessible, but not their full paper. Kim, Eckford and Chae (2014) use the inverse-Gaussian hitting-time density for molecular communication with drift, focusing on impulse-release symbol intervals; its introductory sections and governing model were inspected. Haselmayr, Efrosinin and Guo (2018) analyze *differences of first-passage times*; their full article was inspected and does not treat the rectangular source peak lag. The present mathematical statement concerns a constant-rate finite input at an absorbing receiver, the unique post-shutoff maximum, and the drift–diffusion long-pulse crossover. Those precise statements were not located in the inspected material, but missing full historical texts remain a priority uncertainty.

## Limitations

The result is exact only for a homogeneous one-dimensional model with constant drift and dispersion, a perfectly absorbing endpoint, independent tracer particles, and a constant finite release. It does not apply unchanged to resident concentration, Robin/radiation boundaries, recycling, finite-volume receivers, reaction or sorption, variable flow, or noisy measurements. The logarithmic asymptotic requires \(T\to\infty\); using it at moderate durations can be inaccurate. It is a single-parameter-family theorem, not a claim about optimal environmental policy. A relevant historical step-input article and the original flux-concentration analysis were not obtainable in full; either could contain an unrecognized broader result.

## References

- Kreft, A. and Zuber, A. (1978). “On the physical meaning of the dispersion equation and its solutions for different initial and boundary conditions.” *Chemical Engineering Science*. DOI: 10.1016/0009-2509(78)85196-3.
- Yu, C., Warrick, A. W., and Conklin, M. H. (1999). “A moment method for analyzing breakthrough curves of step inputs.” *Water Resources Research*. DOI: 10.1029/1999WR900225. First published 1999-11-01.
- Kim, N., Eckford, A. W., and Chae, C.-B. (2014). “Symbol Interval Optimization for Molecular Communication with Drift.” arXiv:1407.5776v1 (2014-07-22).
- Haselmayr, W., Efrosinin, D., and Guo, W. (2018). Study of differences of molecular first-hitting times and inverse-Gaussian propagation, arXiv:1809.09995v1.
