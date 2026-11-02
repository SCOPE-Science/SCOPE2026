# Weibull edge extremes with a Gamma-function clock for a harmonically confined run–rest–run particle

## Finding

**Theorem (rare near-edge hits and temporal extremes).** Let the internal state \(S_t\in\{-1,0,+1\}\) jump at rates \(+1\to0\) and \(-1\to0\) equal to \(\gamma_R>0\), and \(0\to\pm1\) equal to \(\gamma_T/2>0\) each. Between jumps let the particle obey \(\dot X_t=-bX_t+vS_t\), with \(b,v>0\). Initialize the joint process in its unique stationary law, and put

\[
\alpha=\frac{\gamma_R}{b},\quad \beta=\frac{\gamma_T}{b},\quad
\delta=1-\frac{b a}{v},\quad
\Lambda=b\frac{\alpha\beta}{2(\alpha+\beta)}
\frac{\Gamma(1+(\alpha+\beta)/2)}
{\Gamma(1+\alpha/2)\Gamma(1+\beta/2)}.
\]

For the first time \(T_a=\inf\{t\ge0:X_t\ge a\}\), with \(a=(v/b)(1-\delta)\) and \(\delta\downarrow0\),

\[
\Lambda\delta^\alpha T_a\ \Longrightarrow\ \operatorname{Exp}(1),
\qquad
\mathbb E T_a\sim\frac{1}{\Lambda\delta^\alpha}.
\]

Consequently, for \(M_t=\sup_{0\le s\le t}(bX_s/v)\), the edge deficit converges to an exact Weibull law:

\[
\lim_{t\to\infty}\Pr\{t^{1/\alpha}(1-M_t)\le z\}
=1-\exp(-\Lambda z^\alpha),\qquad z\ge0.
\]

Here \(t\) is physical time and \(\Lambda\) is a physical inverse-time rate. Thus the Weibull shape is the dimensionless run-termination rate \(\alpha\); the finite tumble duration modifies the exact scale through \(\beta\). In the symmetric case \(\gamma_R=\gamma_T=b\), \(\Lambda=b/\pi\). The theorem is for the temporal maximum along a single trajectory, not an independent sample from the stationary position distribution.

## Assumptions and scope

The internal chain has the *alternating run/rest structure* above; direct jumps \(+1\leftrightarrow-1\) are absent. Runs and rests are exponential and independent after each transition. The restoring field is linear, and no translational Brownian noise is added. Stationary positions satisfy \(|bX_t/v|<1\) almost surely. The theorem holds for every fixed strictly positive \(b,v,\gamma_R,\gamma_T\), without an ordering assumption on the rates. An initial state sampled at a stationary \(0\to+1\) entrance satisfies the same two limits. Time-dependent parameters and joint limits in which rates vary with \(\delta\) are not asserted.

## Proof

**1. Normalize and identify the stationary entry distribution.** Rescale \(Y_s=bX_{s/b}/v\); time \(s=bt\) makes its dynamics \(\dot Y=-Y+S\) with transition rates \(\alpha,\beta\). Denote the stationary unnormalized moments \(m_n^+=\mathbb E[Y^n\mathbf1_{S=+1}]\) and \(m_n^0=\mathbb E[Y^n\mathbf1_{S=0}]\). Symmetry under \((Y,S)\mapsto(-Y,-S)\) gives \(m_{2k}^-=m_{2k}^+\) and \(m_{2k+1}^0=0\). The stationary generator identity, applied to monomials, gives

\[
(n+\alpha)m_n^+=nm_{n-1}^++\frac\beta2m_n^0,
\quad(n+\beta)m_n^0=\alpha(m_n^++m_n^-).
\]

For odd \(n\), \(m_n^0=0\); eliminating it at even \(n=2k\) yields

\[
\frac{m_{2k}^+}{m_{2k-2}^+}=
\frac{(2k-1)(2k+\beta)}{(2k-1+\alpha)(2k+\alpha+\beta)},
\qquad m_0^+=\frac\beta{2(\alpha+\beta)}.
\]

At each stationary \(0\to+1\) entry, the position has the same distribution \(\mu_0\) as the stationary position conditional on \(S=0\), since the transition hazard \(\beta/2\) is position-independent. With \(U\sim\operatorname{Beta}(1/2,\alpha/2)\), \(V\sim\operatorname{Beta}(\beta/2,1+\alpha/2)\), and an independent fair sign \(\epsilon\in\{-1,+1\}\), the exact entrance law is

\[
Y_{\mathrm{entry}}\ \stackrel d=\ \epsilon\sqrt{UV}.
\]

Indeed the stationary recurrence gives precisely

\[
\mathbb E_{\mu_0}Y^{2k}=
\frac{(1/2)_k(\beta/2)_k}{((1+\alpha)/2)_k(1+(\alpha+\beta)/2)_k},
\]

while odd moments vanish; compact support makes these moments distribution-determining. Expanding the symmetric part of \((1-Y)^{-\alpha}\) into nonnegative even powers and applying the Gauss summation identity (whose excess is exactly \(1\)) gives the **finite exact entrance moment**

\[
H_{\alpha,\beta}:=\mathbb E_{\mu_0}(1-Y)^{-\alpha}
={}_2F_1\left(\frac\alpha2,\frac\beta2;1+\frac{\alpha+\beta}{2};1\right)
=\frac{\Gamma(1+(\alpha+\beta)/2)}{\Gamma(1+\alpha/2)\Gamma(1+\beta/2)}.
\]

**2. Exact run-start success probability.** Number successive \(+1\) runs and call their entrance positions \(Z_n\). A run begins at \(x\in(-1,1)\); it reaches \(1-\delta\) if its independent exponential duration of rate \(\alpha\) exceeds \(\log((1-x)/\delta)\), provided \(x<1-\delta\). Thus its mark-success probability is

\[
h_\delta(x)=\min\{1,[\delta/(1-x)]^\alpha\}.
\]

Under the stationary entrance distribution, dominated convergence (dominating \(h_\delta/\delta^\alpha\) by \((1-x)^{-\alpha}\)) yields

\[
p_\delta:=\mathbb E_{\mu_0}h_\delta(Z)
\sim H_{\alpha,\beta}\delta^\alpha.
\]

Entries above the target, which are counted by the mark but need not be fresh upward crossings, have probability \(o(\delta^\alpha)\): integrability of \((1-Z)^{-\alpha}\) implies \(\mu_0\{Z\ge1-\delta\}=o(\delta^\alpha)\). They therefore cannot alter the limiting first-hit law.

**3. Rare marked runs obey an exponential clock.** The entrance chain \((Z_n)\) is an affine random recursion \(Z_{n+1}=A_nZ_n+B_n\) with independent cycle coefficients and \(0<A_n<1\). More importantly, it obeys a *one-step Doeblin minorization* on \((-1,1)\): require a short initial \(+1\) run, a long rest that brings every starting location uniformly near zero, a run in state \(-1\) of duration in a fixed nondegenerate interval, a short final rest, and then entry to \(+1\). Each stipulated transition and duration interval has probability bounded below independent of the starting position. Varying the \(-1\) duration smoothly gives a common nondegenerate interval of new entrance positions with a density bounded below uniformly in the old position. Consequently the entrance chain is uniformly geometrically mixing in total variation; the run-success marks inherit exponential mixing at separated episode indices.

Clustering is ruled out quantitatively. Between *any* two consecutive \(+1\) entries there is a fresh independent rest of duration \(T\sim\operatorname{Exp}(\beta)\). The next entrance position cannot exceed \(e^{-T}\), because during the intervening states \(0\) and \(-1\) the position never increases beyond that upper bound. Hence the conditional success probability for the next \(+1\) run is at most

\[
\kappa_\delta=
\mathbb E\min\left\{1,\left[\frac\delta{1-e^{-T}}\right]^\alpha\right\}
=O\!\left(\delta^{\min(\alpha,1)}[1+|\log\delta|]\right)\longrightarrow0.
\]

In particular \(\Pr(A_{n+j}\mid A_n)\le\kappa_\delta\) for every fixed or varying positive index lag \(j\), where \(A_n\) means that run \(n\) is marked. For a direct Poisson blocking argument, take gaps \(g_\delta=K|\log\delta|\) sufficiently large that the total-variation mixing error is \(o(p_\delta^2)\), and blocks of \(\lfloor p_\delta^{-1/2}\rfloor\) successive runs. Short-lag joint-mark contributions are \(O(\text{block length}\cdot p_\delta g_\delta\kappa_\delta)=o(\text{block length}\cdot p_\delta)\); long-lag pairs contribute \(O((\text{block length}\cdot p_\delta)^2)\). Discarded gaps occupy a vanishing fraction of runs. Independent-block approximation therefore proves

\[
p_\delta N_\delta\Longrightarrow\operatorname{Exp}(1),
\qquad \mathbb E N_\delta\sim p_\delta^{-1},
\]

for the index of the first marked run, also from any fixed initial entrance state. The expectation follows by uniform integrability: at *every* entrance position \(x\in[-1,1]\), the next-run success probability is at least \((\delta/2)^\alpha\), giving a uniform geometric upper tail for \(\delta^\alpha N_\delta\).

**4. Convert runs into physical time and maxima.** The mean normalized time between \(+1\) entries is

\[
\bar L=\frac1\alpha+\frac1\alpha+\frac2\beta
=\frac{2(\alpha+\beta)}{\alpha\beta},
\qquad \nu:=\bar L^{-1}=\frac{\alpha\beta}{2(\alpha+\beta)}.
\]

The cycle lengths form an iid finite-mean sequence and their strong law remains valid at the random first-mark index, which diverges in probability. For expectations, Wald's identity gives the mean full-cycle time through the marked cycle as \(\bar L\mathbb E N_\delta\). The portion of that final cycle after the threshold hit has expectation \(O(1+|\log\delta|)\): a successful run requires at most \(\log(2/\delta)\) time to reach the target, followed by an independent exponential remainder and a finite-mean interval to the next entry. This correction is \(o(\delta^{-\alpha})\). A stationary-time start instead of an entrance start adds a finite-mean residual wait and changes the immediate-hit event by a probability tending to zero, hence the limits are unchanged. Thus \(\nu H_{\alpha,\beta}\delta^\alpha\) is the normalized-time rare-hit rate. Restoring physical time multiplies the rate by \(b\), giving exactly \(\Lambda\). Finally \(\{M_t<1-z t^{-1/\alpha}\}=\{T_{(v/b)(1-zt^{-1/\alpha})}>t\}\); the exponential survival limit proves the Weibull formula.

## Verification

The standalone `verify.py` recomputes exact stationary-generator moment identities using rational arithmetic at five distinct positive rate pairs through moment order \(40\), checks the Gauss formula numerically at high precision, verifies \(\Lambda/b=1/\pi\) for equal normalized rates and \(\Lambda/b=1/2\) for normalized rates \((2,1)\), and performs bounded Monte Carlo checks on the run-start success probability. Run: `python verify.py` (Python 3 with `mpmath`). These tests are finite checks; the infinite-time exponential and Weibull statements are established by the analytic Doeblin-and-blocking proof, not by simulation.

## Relationship to prior work

Sun, Ye and Chen (2026) give the joint stationary position–velocity distribution for the finite-tumble harmonic model and report stationary edge singularities; Sun, Ye and Podgornik (2024) give the position moments and finite-tumble steady state. Basu et al. (2019) solve the stationary distribution of the one-rate three-state special case. None of those stationary results alone yields an exponential *trajectory-level first-hit* law: the dependence between successive near-edge visits and the entry clock must also be controlled. Guéneau, Majumdar and Schehr (2024) derive first-passage formulas for a two-state process in general potentials, including a harmonic-trap application; Grange and Yuan (2025) treat positive tumble times but a spatially constant drift, not a harmonic restoring force. The new statement combines the exact two-parameter amplitude with a trajectory-maximum limit for positive-duration rests. Standard mixing-based extreme-value principles inform the proof, and a broader unseen theorem for rare events in piecewise-deterministic Markov processes may imply the abstract limit without this model-specific prefactor.

## Limitations

This concerns a *single* stationary trajectory and its one-sided upper maximum, not extrema of independent particles, transient nonstationary large deviations, finite observation times, or finite-tumble laws with added Gaussian noise. Rate parameters remain fixed as the target approaches the hard edge. The generic blocking argument uses uniform Doeblin mixing and negligible short-lag clustering; the explicit Gauss prefactor applies only to the stated exponential three-state protocol. No independent audit or priority certification is asserted.

## References

1. A. Sun, F. Ye, and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1, publicly posted 2026-10-18. https://arxiv.org/html/2610.24961
2. A. Sun, F. Ye, and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, 2024-09-01. https://arxiv.org/abs/2409.00578
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083, 2019-10-22. https://arxiv.org/pdf/1910.10083
4. M. Guéneau, S. N. Majumdar, and G. Schehr, *Run-and-tumble particle in one-dimensional potentials: mean first-passage time and applications*, arXiv:2409.16951, 2024-09-25. https://arxiv.org/pdf/2409.16951
5. P. Grange and L. Yuan, *Mean first-passage time of a run-and-tumble particle with exponentially-distributed tumble duration in the presence of a drift*, arXiv:2509.11308, 2025-09-14. https://arxiv.org/abs/2509.11308
