# Cubic-root rounding of the drift-controlled optimal-resetting transition at a partially reactive point trap

## Finding

Let a Brownian particle diffuse on the full real line with diffusion coefficient \(D>0\), constant drift \(v\), initial position \(x_0>0\), and a reactive point trap at the origin of killing strength \(k>0\). Independently of the diffusion, the surviving particle is reset to \(x_0\) at Poisson rate \(r>0\). Write
\[
a=\frac{vx_0}{2D},\qquad K=\frac{kx_0}{2D},\qquad \rho=\frac{rx_0^2}{D},\qquad u=\sqrt{a^2+\rho}.
\]
Then the mean absorption time \(M(r)\) obeys the exact law
\[
\frac{D}{x_0^2}M(r)=m_{a,K}(\rho)=\frac{e^{a+u}(1+u/K)-1}{\rho}.
\]
For **every real drift** \(a\) and **every finite** \(K>0\), this function has exactly one minimizer \(\rho_*(a,K)>0\). It is strictly decreasing before, and strictly increasing after, that minimizer.

For drift toward the trap, write \(a=-b\), \(b>0\). The perfectly absorbing limit \(K=\infty\) has an optimal *zero* reset rate exactly when \(b\ge1\) (and a unique positive optimal rate when \(0<b<1\)). The finite-reactivity optimum is therefore a singular perturbation of that threshold. At fixed \(b>1\),
\[
\rho_*(-b,K)=\sqrt{\frac{8b^4}{(b-1)K}}\,[1+o(1)]\qquad(K\to\infty).
\]
At the threshold \(b=1\),
\[
\rho_*(-1,K)=\left(\frac{24}{K}\right)^{1/3}[1+o(1)].
\]
More sharply, for every fixed \(\lambda\in\mathbb R\), put \(b_K=1+\lambda K^{-1/3}\) (which is positive for sufficiently large \(K\)). Then
\[
K^{1/3}\rho_*(-b_K,K)\longrightarrow t_\lambda,
\qquad t_\lambda^3+3\lambda t_\lambda^2=24,
\]
where \(t_\lambda\) is the **unique positive solution**, and the optimal dimensionless mean satisfies
\[
\min_{\rho>0}m_{-b_K,K}(\rho)=\frac1{2b_K}
+K^{-2/3}\left(\frac1{t_\lambda}+\frac{\lambda t_\lambda}{8}+\frac{t_\lambda^2}{48}\right)
+o(K^{-2/3}).
\]
At \(\lambda=0\), the excess is \(\frac32 24^{-1/3}K^{-2/3}+o(K^{-2/3})\).

## Assumptions and scope

The underlying free process solves \(dX_t=v\,dt+\sqrt{2D}\,dB_t\) on \(\mathbb R\). While alive, its forward density obeys \(\partial_t p=D\partial_{xx}p-v\partial_xp-k\delta_0p(0,t)\). Equivalently, killing is induced by an exponential clock in the local time at the origin, using the normalization dictated by this delta-sink generator. The initial and resetting position is \(x_0>0\). Absorption terminates the entire experiment, whereas a reset acts only on surviving paths. All stated asymptotics hold with \(b\) or \(\lambda\) fixed as indicated and \(K\to\infty\); no uniform assertion over unbounded drifts is made. All rates are continuous-time Poisson rates.

## Proof

**1. Free killing transform.** For \(s>0\), write \(w=\sqrt{v^2+4Ds}\). The drifted Gaussian resolvent at the trap is
\[
G_s(0,x_0)=\int_0^\infty\frac{\exp[-(x_0+vt)^2/(4Dt)-st]}{\sqrt{4\pi Dt}}\,dt
=\frac{\exp[-(v+w)x_0/(2D)]}{w},\qquad G_s(0,0)=\frac1w.
\]
The rank-one resolvent identity for the sink \(k\delta_0\) gives its killing-time Laplace transform, including the event of never being killed,
\[
F_0(s)=\mathbb E_{x_0}[e^{-sT_0};T_0<\infty]
=\frac{kG_s(0,x_0)}{1+kG_s(0,0)}
=\frac{k}{k+w}\exp\!\left[-\frac{(v+w)x_0}{2D}\right].
\]
The density Laplace transform and the sink flux are related by \(\widetilde f_0(s)=k\widetilde p(0,s)\), which fixes the normalization without an appeal to a heuristic radiation boundary.

**2. Renewal under complete resetting.** Independence of the reset clock gives the total absorption-time mean as \(M(r)=(1-F_0(r))/(rF_0(r))\). Substitution of \(F_0(r)=e^{-(a+u)}/(1+u/K)\) proves the displayed dimensionless formula. For every finite \(K\), the mean diverges at \(\rho\downarrow0\): when \(a\ne0\), its numerator has a strictly positive finite limit, and when \(a=0\) that numerator is \((1+K^{-1})\sqrt\rho+O(\rho)\). It also diverges as \(\rho\to\infty\).

**3. Global uniqueness.** Set \(H(\rho)=e^{a+u}(1+u/K)-1\) and \(J(\rho)=\rho H'(\rho)-H(\rho)\). Then \(m'=J/\rho^2\) and
\[
J'(\rho)=\rho H''(\rho),\qquad
H''(\rho)=\frac{e^{a+u}}{4Ku^3}\bigl[u^2+(K+1)u-(K+1)\bigr].
\]
The bracketed quadratic has one positive zero and changes sign only from negative to positive. Thus \(J\) first decreases and then increases, or increases throughout its physical domain. For \(a\ne0\), \(J(0+)=-H(0+)<0\). For \(a=0\), \(J(\rho)\sim-\frac12(1+K^{-1})\sqrt\rho<0\) at small positive \(\rho\). Finally \(J(\rho)>0\) for all sufficiently large \(\rho\), since \(\rho H'/H\sim\sqrt\rho/2\). Therefore \(J\) crosses zero **exactly once**, from negative to positive, proving global uniqueness and strict monotonicity on the two sides.

**4. Perfect-reactivity boundary.** At \(K=\infty\) and \(a=-b<0\), the mean is \([e^{\sqrt{b^2+\rho}-b}-1]/\rho\). Its small-rate expansion is
\[
m_{-b,\infty}(\rho)=\frac1{2b}+\frac{b-1}{8b^3}\rho
+\frac{b^2-3b+3}{48b^5}\rho^2+O(\rho^3).
\]
For \(b\ge1\), \(H''\ge0\) on the entire physical range and \(J(0+)=0\), hence the strict infimum occurs at \(\rho=0\). For \(0<b<1\), \(H''<0\) initially and changes sign once; the resulting \(J\) has exactly one positive root. Thus the perfect-sink threshold is precisely \(b=1\).

**5. Singular optimum and crossover.** Write \(\varepsilon=K^{-1}\). Direct uniform Taylor expansion for \(b\) in a fixed neighborhood of one and \(\rho\downarrow0\) gives
\[
 m_{-b,K}(\rho)=\frac1{2b}+\frac{\varepsilon b}{\rho}
 +\frac{b-1}{8b^3}\rho
 +\frac{b^2-3b+3}{48b^5}\rho^2
 +O(\rho^3+\varepsilon).
\]
At fixed \(b>1\), balance the positive terms \(\varepsilon b/\rho\) and \((b-1)\rho/(8b^3)\) to obtain the square-root constant. The unique optimum necessarily converges to zero, because \(m_{-b,K}\ge m_{-b,\infty}\) and evaluating at a test scale \(\rho\asymp\sqrt\varepsilon\) approaches the perfect-sink minimum. The same comparison, combined with the displayed expansion, confines the minimizer to the square-root scale.

For \(b_K=1+\lambda\varepsilon^{1/3}\), put \(\rho=\varepsilon^{1/3}t\). Uniformly for \(t\) in compact subsets of \((0,\infty)\),
\[
\varepsilon^{-2/3}\left[m_{-b_K,K}(\varepsilon^{1/3}t)-\frac1{2b_K}\right]
\longrightarrow \Phi_\lambda(t)=\frac1t+\frac{\lambda t}{8}+\frac{t^2}{48}.
\]
A small-rate lower bound of the form \(c\rho^2-C\varepsilon^{1/3}\rho+c\varepsilon/\rho\), valid near the origin with positive constants, together with a test value \(t=1\) and the strict perfect-sink gap away from the origin, confines rescaled minimizers to a compact subset of \((0,\infty)\). Since \(\Phi_\lambda''(t)=2/t^3+1/24>0\), it has a unique minimizer characterized by \(t^3+3\lambda t^2=24\). Compactness and uniform convergence then imply convergence of the minimizers and their values. The special case \(\lambda=0\) yields the two stated critical coefficients. This completes the proof.

## Verification

The standalone `verify.py` checks 235 derivative/root/asymptotic assertions over positive and negative drifts, finite sink strengths, square-root and cubic-root regimes, and the two-sided crossover. Forty-five additional checks reconstruct the drifted Brownian trap resolvent by independent numerical quadrature of its Gaussian transition density. The script uses Python 3, SciPy and NumPy-free standard math routines; it does not prove the theorems for infinitely many parameter values. Analytic results above provide the proof.

## Relationship to prior work

Mazzolo's 2026 work on exactly this drifted delta-trap restarting model obtains exact Laplace-space survival and resolvent formulas and the survival-decay regimes [1]. Its accessible abstract does not state the uniqueness theorem, square-root/cubic-root asymptotics or the two-sided critical crossover; **the full primary article could not be inspected**, so noncoverage of all its appendices is not asserted. Evans, Majumdar and Schehr [2, §3.8, especially Eq. (3.58)] explicitly derive a driftless point-sink reset transform. Whitehouse, Evans and Majumdar [3] analyze driftless partial absorption and optimal resetting. Biswas and collaborators [4] treat optimal resetting with drift and a *stochastically gated target*, a different mechanism; perfect-absorber drift thresholds are established ingredients, not claimed as a new general idea. Bressloff [5] covers partially absorbing half-line targets. The new claim here is the full-line drifted delta-trap global uniqueness and its explicit **finite-reactivity rounding crossover**, not the underlying renewal identity, point-sink resolvent, or perfect-sink threshold alone.

## Limitations

The model uses a single delta trap, constant drift, full-line diffusion, instantaneous complete Poisson resets and a fixed reset site. The minimization concerns **mean absorption time**, not the large-time survival exponent or a finite-time success probability. The asymptotic results are pointwise in their displayed parameters. Although literature comparisons and direct proof checks support the claim, the motivating full primary article was not accessible for a complete all-sections comparison and a broader unpublished optimization result remains possible. No independent scientific audit is claimed.

## References

1. A. Mazzolo, *Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes* (first public preprint 2026-09-18), arXiv:2609.22527; Phys. Rev. E 114, 044105 (2026), DOI: 10.1103/3s1c-k5vg.
2. M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, J. Phys. A 53, 193001 (2020), DOI: 10.1088/1751-8121/ab7cfe; accessible peer-reviewed manuscript: https://www.pure.ed.ac.uk/ws/portalfiles/portal/139969031/1910.07993.pdf.
3. J. Whitehouse, M. R. Evans and S. N. Majumdar, *Effect of partial absorption on diffusion with resetting*, Phys. Rev. E 87, 022118 (2013), DOI: 10.1103/PhysRevE.87.022118; arXiv:1301.2489.
4. A. Biswas, A. Pal, D. Mondal and S. Ray, *Rate enhancement of gated drift-diffusion process by optimal resetting*, J. Chem. Phys. 158 (2023), DOI: 10.1063/5.0154210; arXiv:2304.10605.
5. P. C. Bressloff, *Probabilistic formulations of diffusive search processes with stochastic resetting*, in *The Mathematics of Movement* (2026), DOI: 10.1007/978-3-032-00873-2_4.
