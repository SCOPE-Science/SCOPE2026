# Sharp activity-dose placement for variance suppression in a harmonically trapped run-and-tumble particle

## Finding

For a stationary one-dimensional harmonic run-and-tumble particle, the best **weak, bounded tumbling-rate intervention with fixed integrated activity dose** is one interval of maximal extra tumbling. The interval need not begin at time zero or end at the observation time: once the horizon exceeds a specific relaxation lag, small doses are uniquely best in the **interior** of the protocol.

Precisely, let \(k,a,v>0\), \(T>0\), and \(0<m<T\). Let the orientation flip at rate \(\alpha_\varepsilon(t)/2\) with
\[
\alpha_\varepsilon(t)=a+\varepsilon u(t),\quad 0\leq u(t)\leq1,\quad \int_0^T u(t)\,dt=m,
\]
where \(u\) is any measurable control and \(\varepsilon\geq0\) is small. Write \(V_\varepsilon(T;u)=\operatorname{Var}(X_T)\). Then **uniformly over every admissible control**,
\[
V_\varepsilon(T;u)=\frac{v^2}{k(k+a)}-\varepsilon\int_0^T W(T-s)u(s)\,ds+R_\varepsilon(u),
\qquad 0\leq R_\varepsilon(u)\leq\frac{v^2\varepsilon^2}{k(k+a)^3},
\]
where the causal variance-reduction response kernel is
\[
W(z)=\frac{2v^2}{k+a}\begin{cases}
\dfrac{e^{-(k+a)z}-e^{-2kz}}{k-a},&k\ne a,\\[4pt]
z e^{-2kz},&k=a.
\end{cases}
\]
The kernel is positive for \(z>0\), vanishes at zero and infinity, and has exactly one maximum at the positive lag
\[
z_*=\begin{cases}
\dfrac{\log(2k/(k+a))}{k-a},&k\ne a,\\[4pt]
\dfrac1{2k},&k=a.
\end{cases}
\]
For each fixed \(T,m\), the unique, up to null sets, control maximizing the **first-order variance reduction** is \(u=\mathbf1_{[s_0,s_0+m]}\). The starting time \(s_0\) is characterized as follows.

If \(T\leq z_*\), then \(s_0=0\): front-loading all available activity is optimal. If \(T>z_*\), let \(r_T\in(0,z_*)\) be the unique solution \(W(r_T)=W(T)\), and put \(m_c(T)=T-r_T\). If \(m\geq m_c(T)\), then \(s_0=0\). If \(0<m<m_c(T)\), the optimizer is strictly interior, and \(s_0\in(0,T-m)\) is the unique solution
\[
W(T-s_0)=W(T-s_0-m).
\]
In particular, at every fixed \(T>z_*\), as the dose duration \(m\downarrow0\), the center of the optimal interval tends to the **delayed intervention time** \(T-z_*\), not either endpoint.

The optimization statements concern the derivative at \(\varepsilon=0\). They do **not** assert exact optimality of that same window for arbitrary finite intervention strength.

## Assumptions and scope

The particle follows the piecewise deterministic Markov dynamics
\[
\dot X_t=-kX_t+v\Sigma_t,
\quad\Sigma_t\in\{-1,+1\},
\]
with \(k,v>0\) constant. The flip clock is conditionally memoryless with rate \(\alpha_\varepsilon(t)/2\), independently of position. Before the intervention, \((X_0,\Sigma_0)\) has the symmetric stationary distribution for the constant baseline rate \(a>0\), giving \(\mathbb E X_t=0\), \(\mathbb E X_0^2=v^2/[k(k+a)]\), and \(\mathbb E[X_0\Sigma_0]=v/(k+a)\). There is no translational thermal noise, no position-dependent feedback, and no change in stiffness or propulsion speed. Controls are deterministic, measurable and obey the peak and integrated-dose constraints displayed above. The observation is made at a fixed finite \(T\).

## Proof

**1. Exact moment closure.** The generator acts on a function \(f(x,\sigma)\) as
\[
(\mathcal L_t f)(x,\sigma)=(-kx+v\sigma)\partial_xf(x,\sigma)+\frac{\alpha_\varepsilon(t)}2[f(x,-\sigma)-f(x,\sigma)].
\]
Consequently, putting \(A(t)=\mathbb E[X_t^2]\) and \(B(t)=\mathbb E[X_t\Sigma_t]\),
\[
A'=-2kA+2vB,\qquad B'=v-(k+a+\varepsilon u(t))B.
\]
The symmetry of the initial law is preserved; hence \(A(t)=\operatorname{Var}(X_t)\). With \(\delta=k+a\), the baseline equilibrium satisfies \(A_0=v^2/(k\delta)\), \(B_0=v/\delta\).

**2. Uniform linear response, including its error.** For \(\varepsilon\geq0\), the exact integral equation and scalar comparison give
\[
0<B_\varepsilon(t)\leq B_0,\quad
D(t):=B_0-B_\varepsilon(t)=\varepsilon\int_0^t e^{-\delta(t-s)}u(s)B_\varepsilon(s)\,ds.
\]
In particular \(0\leq D(t)\leq\varepsilon B_0/\delta\). Substituting \(B_\varepsilon(s)=B_0-D(s)\) into the integral expression yields
\[
0\leq \varepsilon B_0\int_0^t e^{-\delta(t-s)}u(s)\,ds-D(t)
\leq\varepsilon^2 B_0/\delta^2.
\]
The variance equation and initial stationarity give exactly
\[
A_\varepsilon(T)-A_0=-2v\int_0^T e^{-2k(T-t)}D(t)\,dt.
\]
Interchanging the deterministic integrals proves the stated kernel formula. The displayed error bound follows by \(\int_0^T e^{-2k(T-t)}dt\leq1/(2k)\), giving \(vB_0\varepsilon^2/(k\delta^2)=v^2\varepsilon^2/(k\delta^3)\). This bound is simultaneous for all measurable admissible schedules, so taking an infimum over schedules does not invalidate first-order optimality.

**3. Unique response maximum.** Apart from the positive constant \(2v^2/\delta\), for \(k\ne a\) the kernel has derivative
\[
W'(z)=\frac{2v^2}{\delta}\frac{-\delta e^{-\delta z}+2k e^{-2kz}}{k-a}.
\]
The numerator has one positive root: \(e^{(k-a)z}=2k/(k+a)\). Its sign on either side and the sign of \(k-a\) imply strict increase up to \(z_*\) and strict decrease afterward. At \(k=a\), \(W'(z)\) has the sign of \(1-2kz\). Thus the stated maximum is unique in all cases.

**4. Sharp fixed-dose placement.** Minimizing the variance to first order is maximizing the linear functional \(u\mapsto\int_0^T W(T-s)u(s)ds\) subject to \(0\leq u\leq1\) and \(\int u=m\). The elementary exchange principle implies that every maximizer fills precisely the \(m\) units of time having largest kernel values: if a lower-weight time receives control while a higher-weight time is unfilled, exchanging those values strictly improves the objective. Strict unimodality and the absence of positive-measure level sets make the optimizer unique almost everywhere, with support one interval. If \(T\leq z_*\), the weights decrease strictly with physical time, so this is \([0,m]\). If \(T>z_*\), there is exactly one \(r_T\in(0,z_*)\) with \(W(r_T)=W(T)\). As the selected interval expands through the increasing level sets, it first touches the initial-time boundary at length \(m_c(T)=T-r_T\), and thereafter equals \([0,m]\). Below that threshold it is interior, and continuity and strict unimodality force equality of the two endpoint weights. The sole peak implies convergence of the optimal interval center to \(T-z_*\) as \(m\downarrow0\). This completes the characterization.

## Verification

The accompanying standalone files `verify.py` and `verify_budget.py` can be run with Python, NumPy and SciPy using `python verify.py` and `python verify_budget.py`. The first reproduces the independent closed two-moment equations against adaptive ODE integration and checks sharp unrestricted variance envelopes. The second checks the kernel's unique maximum, the window's optimality against numerical quadrature on comparison windows, the uniform first-order approximation against exact time-dependent moment ODEs, and a genuinely interior protocol outperforming pulses at either endpoint. During preparation, 461 and 23 deterministic comparisons respectively passed. These are finite checks only; the proof above supplies the universal statements.

For \(k=1.2\), \(a=0.45\), \(v=1\), \(T=2\), \(m=0.25\), the predicted lag is \(z_*\approx0.4995912659\) and the optimal weak-dose pulse is \([1.3649081504,1.6149081504]\). Under \(\varepsilon=0.1\), independent moment integration gives endpoint variance approximately \(0.4996295196\) for this interior pulse, versus \(0.5036774237\) if applied at the start and \(0.5023481452\) if applied at the end. The finite-amplitude example illustrates the first-order prediction, not a global finite-amplitude optimality theorem.

## Relationship to prior work

Baldovin and Manacorda [1] develop the same harmonic RTP model with time-controlled trap stiffness and tumbling rate, describe distribution-level shortcuts and optimize work using a slow-protocol approximation. Their Section V discusses time-optimal bounded controls as a separate challenge. The present result does not solve their **full-distribution shortcut** problem: it fixes stiffness, starts in equilibrium, and optimizes the **endpoint position variance** to first order under a fixed total increase in tumbling intensity.

Frim and DeWeese [2] give exact RTP shortcuts and minimal-time protocols for another control arrangement (notably changing propulsion and stiffness with a fixed tumble rate). They do not provide the fixed-tumble-dose variance response kernel or its interior optimal timing phase. Davis, Proesmans and Fodor [3] derive a broad active-matter response framework for minimizing thermodynamic dissipation, mainly varying confining-potential controls; general linear-response principles are therefore prior art. The elementary moment equations and the exchange principle also are not independently claimed as novel. The assessed new statement is the combined model-specific, sharp dose-constrained timing classification, including the explicit transition lag, critical dose and uniform error bound. More general existing response/control theory may implicitly subsume it; that is an originality risk.

## Limitations

Only one-particle centered harmonic dynamics, constant stiffness and propulsion speed, stationary initial data, and a bounded nonnegative perturbation of the tumble rate are covered. The result is a sharp \(\varepsilon\downarrow0\) response-optimization statement, not a proof that the proposed windows are exactly optimal at all finite \(\varepsilon\). It controls one endpoint variance, not the complete non-Gaussian distribution or work/entropy costs. The peak/total-dose constraint permits measurable bang-bang controls; continuous-control constraints would change attainability. No claim is made for translational diffusion, interacting particles, feedback based on observations, or history-dependent tumbling.

## References

[1] M. Baldovin and A. Manacorda, *Control protocols for harmonically confined run-and-tumble particles*, arXiv:2602.04560v1 (first posted 2026-02-04); Phys. Rev. E **114**, 014112 (2026), DOI 10.1103/rspp-2334. https://arxiv.org/abs/2602.04560

[2] A. G. Frim and M. R. DeWeese, *Shortcut engineering of active matter: run-and-tumble particles*, arXiv:2304.06023 (2023). https://arxiv.org/abs/2304.06023

[3] L. K. Davis, K. Proesmans and É. Fodor, *Active Matter under Control: Insights from Response Theory*, Phys. Rev. X **14**, 011012 (2024); arXiv:2305.11078. https://arxiv.org/abs/2305.11078
