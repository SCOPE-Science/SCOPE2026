# Quadratic-accuracy logarithmic localization in a three-state trapped active particle

## Finding
Consider a stationary athermal run-and-tumble particle with a finite-duration nonpropulsive state in a one-dimensional harmonic trap, with independent microscopic run-termination and tumble-termination rates. In the rare-switching regime, the logarithmic distance to the deterministic attractor of the currently occupied internal state has an exponential law with an explicitly **quadratic**, rather than merely linear, total-variation error. The first nonzero corrections to the conditional means distinguish the running and tumbling states and contain two different exact dilogarithmic constants.

Precisely, under the definitions below, write \(Z_{\varepsilon,j}=-\varepsilon\log|Y-s_j|\). For every \(\varepsilon>0\),
\[
 d_{\rm TV}\bigl(\mathcal L(Z_{\varepsilon,+}\mid J=+),\operatorname{Exp}(a/b)\bigr)
 \le {ac\over b^2}\left({\pi^2\over6}+(\log2)^2+1\right)\varepsilon^2,
\]
with the same statement for \(J=-\), and
\[
 d_{\rm TV}\bigl(\mathcal L(Z_{\varepsilon,0}\mid J=0),\operatorname{Exp}(c/b)\bigr)
 \le {ac\pi^2\over3b^2}\varepsilon^2.
\]
Here \(\operatorname{Exp}(r)\) means the exponential probability law with rate \(r\), and total variation is the supremum of differences of event probabilities. In addition, as \(\varepsilon\downarrow0\),
\[
 \mathbb E[Z_{\varepsilon,+}\mid J=+]
 = {b\over a}+{c\pi^2\over24b}\varepsilon^2+o(\varepsilon^2),
 \qquad
 \mathbb E[Z_{\varepsilon,0}\mid J=0]
 = {b\over c}+{a\pi^2\over6b}\varepsilon^2+o(\varepsilon^2).
\]
The formula for \(J=-\) equals that for \(J=+\) by reflection symmetry. The conditional peak laws identify the two switching-rate coefficients \(a\) and \(c\), if the trap rate \(b\) and common small factor \(\varepsilon\) are calibrated, even though the unscaled weak positional limit only records their ratio.

## Assumptions and scope
Fix \(a,c,b>0\) and \(\varepsilon>0\). The internal state \(J_t\in\{+,0,-\}\) jumps from either running state to state \(0\) at rate \(\varepsilon a\) and from state \(0\) to either sign at rate \(\varepsilon c/2\). The dimensionless position solves
\[
 \dot Y_t=-b(Y_t-s_{J_t}),\qquad s_+=1,\quad s_0=0,\quad s_-=-1.
\]
There is no Brownian noise, direct reversal while running, or positional feedback in the transition rates. The physical position is recovered from \(Y=bX/v\) for propulsion speed \(v>0\). The stationary process is constructed from a bilateral stationary internal-state chain and the unique exponentially stable forced solution, and satisfies \(|Y|\le1\) almost surely.

The state weights are exactly \(\Pr(J=0)=a/(a+c)\) and \(\Pr(J=\pm)=c/[2(a+c)]\). All probabilities and means in this result refer to this stationary joint law; no finite-time transient assertion is made.

## Proof
**1. Stationary age decomposition.** When observed in an internal state \(j\), the time \(A_j\) elapsed since entering that state is exponential with rate \(\varepsilon\lambda_j\), where \(\lambda_+=\lambda_-=a\) and \(\lambda_0=c\), and is independent of the position \(Y_j^{\rm in}\) at entry. This follows either from the stationary Palm occupation formula \(\varepsilon\lambda_j e^{-\varepsilon\lambda_j t}\,dt\) or directly from exponential holding times and the state-independent exit hazard. Along the holding interval,
\[
 |Y-s_j|=D_j e^{-b A_j},\qquad
 D_j=|Y_j^{\rm in}-s_j|,
 \qquad
 Z_{\varepsilon,j}=b\varepsilon A_j-\varepsilon\log D_j.
\]
The first term \(E_j=b\varepsilon A_j\) has **exactly** law \(\operatorname{Exp}(\lambda_j/b)\), for every \(\varepsilon>0\), independently of \(D_j\).

**2. Quantitative logarithmic entry bounds.** Define \(h(t)=-\log(1-e^{-bt})\) for \(t>0\). Its integral is \(\int_0^\infty h(t)\,dt=\pi^2/(6b)\), by expanding \(-\log(1-z)=\sum_{n\ge1}z^n/n\).

For an entry into running state \(+\), the preceding state is \(0\), of independent duration \(T_0\sim\operatorname{Exp}(\varepsilon c)\). Its entry position \(V\) satisfies \(|V|\le1\). Thus \(D_+=|1-Ve^{-bT_0}|\). For \(0<t<\log2/b\), uniformly in \(|V|\le1\),
\[
 |\log|1-Ve^{-bt}||\le h(t)+\log2.
\]
For \(t\ge\log2/b\) the same absolute logarithm is at most \(2e^{-bt}\). Bounding the exponential density by \(\varepsilon c\) and integrating gives
\[
 \mathbb E|\log D_+|\le {\varepsilon c\over b}
 \left({\pi^2\over6}+(\log2)^2+1\right).
\]
Reflection gives the same result for \(J=-\).

For an entry into tumble state \(0\), the preceding sign \(s\) is \(+1\) or \(-1\), each with probability one half. Its duration \(T_R\) is independent exponential with rate \(\varepsilon a\). The preceding entry position \(V\in[-1,1]\) yields
\[
 D_0=|s+(V-s)e^{-bT_R}|\le1.
\]
For \(s=+1\), when \(V<1\), put \(t_*=b^{-1}\log(1-V)\le\log2/b\). Then \(D_0=|1-e^{-b(T_R-t_*)}|\), and \(-\log D_0\le h(|T_R-t_*|)\). The bound remains true for the limiting case \(V=1\) by continuity. With the same argument for \(s=-1\),
\[
 \int_0^\infty h(|t-t_*|)\,dt\le2\int_0^\infty h(t)\,dt={\pi^2\over3b},
\]
so \(\mathbb E|\log D_0|\le\varepsilon a\pi^2/(3b)\).

Translation of an exponential random variable of rate \(r\) by any constant \(u\) changes its distribution in total variation by \(1-e^{-r|u|}\le r|u|\). Convexity of total variation under mixing and independence of \(E_j,D_j\) therefore yield
\[
 d_{\rm TV}(\mathcal L(Z_{\varepsilon,j}),\mathcal L(E_j))
 \le {\lambda_j\over b}\varepsilon\,\mathbb E|\log D_j|.
\]
Inserting the preceding bounds proves both stated \(O(\varepsilon^2)\) inequalities, **globally for positive \(\varepsilon\)**.

**3. Sharp mean corrections.** At the entry to a tumble, the preceding running state has sign \(S\in\{-1,+1\}\), equally likely, and the last running duration is exponential with rate \(\varepsilon a\). Since the duration tends to infinity in probability, the end-of-run position converges in probability to \(S\) (all entry positions lie in \([-1,1]\)). Hence at the next entry into state \(+\), the position \(V\) at entry to the preceding tumble converges in law to the equiprobable pair \(\pm1\). For fixed positive \(t\),
\[
 \mathbb E_V\log|1-Ve^{-bt}|\longrightarrow
 \tfrac12\log(1-e^{-2bt}).
\]
The pointwise logarithmic bounds in step 2 give an integrable majorant in \(t\), so dominated convergence applied to the preceding tumble duration yields
\[
 \lim_{\varepsilon\downarrow0}{\mathbb E\log D_+\over\varepsilon}
 = {c\over2}\int_0^\infty\log(1-e^{-2bt})\,dt
 =-{c\pi^2\over24b}.
\]
Similarly, the position at entry to a running interval converges in probability to zero, since it follows an independent long tumble. Therefore, at the end of a running interval, the integrand for \(\log D_0\) converges for fixed \(t>0\) to \(\log(1-e^{-bt})\). The translated-integrable-\(h\) majorant in step 2 also makes these integrals continuous in the running entry location at zero. Consequently,
\[
 \lim_{\varepsilon\downarrow0}{\mathbb E\log D_0\over\varepsilon}
 =a\int_0^\infty\log(1-e^{-bt})\,dt
 =-{a\pi^2\over6b}.
\]
Taking means in the exact age decomposition gives \(\mathbb E Z_{\varepsilon,j}=b/\lambda_j-\varepsilon\mathbb E\log D_j\), and proves the two displayed expansions. The full proof is analytical; the finite numerical checks below are supplementary.

**4. Identifiability and the unscaled limit.** Exponentially long holding times force the stationary position to the attractor of its current state in probability as \(\varepsilon\to0\). Thus \(Y\) converges weakly to \(a\delta_0/(a+c)+c(\delta_{-1}+\delta_{+1})/[2(a+c)]\), which depends on \(a,c\) only through their ratio. The conditioned logarithmic layers instead have rates \(a/b\) and \(c/b\). Their distinct limiting laws recover both coefficients when the common slowdown \(\varepsilon\) and trap parameter \(b\) are calibrated.

## Verification
The accompanying `verify.py` independently checks the convergent series for \(\pi^2/6\), the stationary transition balance, the predicted two coefficients, and the analytic absolute-logarithm bounds against independent finite-state renewal simulations using a reproducible seed. The simulator propagates the exact solution of each deterministic holding segment; it does not approximate the full infinite-time stationary distribution by solving a discretized Fokker–Planck equation. Simulation agreement at several finite rare-switching scales is supportive and **does not** establish any infinite-parameter limit or total-variation bound. Run with `python verify.py` using the Python standard library.

## Relationship to prior work
Sun, Ye and Chen (2026, arXiv:2610.24961v1) establish conditional position densities and a path-integrated moment approach for a harmonically trapped run-and-tumble particle with a finite tumble interval. Those finite-rate densities and the three-state model are prior work. Basu, Majumdar, Rosso, Sabhapandit and Schehr (2019, arXiv:1910.10083v1) obtain exact stationary distributions and boundary singularities for a related equal-rate three-state trap. Guéneau, Majumdar and Schehr (2026, arXiv:2602.08436) give a broad stick-breaking representation for a different instantaneous-refresh harmonic run-and-tumble model.

The present assertion is the **two-rate rare-switching quantitative logarithmic limit**, including an all-parameter quadratic total-variation estimate and unequal first nonzero mean corrections. It does not claim discovery of the stationary distribution, its edge singularities, or the ordinary Markov holding-age formula.

## Limitations
The result requires constant, position-independent, memoryless switching; deterministic linear confinement; no thermal diffusion; a strictly positive run and tumble termination rate; and stationarity. It does not treat nonlinear confinement, orientation persistence across the tumble beyond an independent symmetric choice, translational measurement noise, or finite observation statistics. Exact finite-rate formulas in earlier work may allow additional derived asymptotics, so priority for the present quantitative formulation requires independent assessment. No independent audit has been performed.

## References
1. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1 (first public 2026-10-18), https://arxiv.org/abs/2610.24961.
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083v1 (2019), https://arxiv.org/abs/1910.10083.
3. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (2026), https://arxiv.org/abs/2602.08436.
4. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578v2 (2025), https://arxiv.org/html/2409.00578v2.
5. P. C. Bressloff, *Truncated stochastically switching processes*, Phys. Rev. E 109, 024103 (2024), https://doi.org/10.1103/PhysRevE.109.024103.
