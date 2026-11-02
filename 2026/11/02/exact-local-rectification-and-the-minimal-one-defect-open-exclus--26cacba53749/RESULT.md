# Exact local rectification and the minimal one-defect open exclusion chain

## Finding

Consider a four-site continuous-time symmetric exclusion chain with clean boundary sites and one defective interior departure rate. With site-departure rates \((1,t,1,1)\), \(t>0\), left and right reservoir densities \(\rho_L=(1+\delta)/2\) and \(\rho_R=(1-\delta)/2\), and unit total exchange rate at either end, write \(J_t(\delta)\) for the stationary particle current from left to right. The hopping rate for an allowed jump from site \(i\) to a vacant neighboring site is the departure rate at \(i\). The reservoir density difference is \(\delta\), with \(-1<\delta<1\).

The exact analytic expansion at the equal half-density reservoir point \(\delta=0\) is

\[
J_t(\delta)=C_1(t)\delta+C_2(t)\delta^2+O_t(\delta^3),
\]

where

\[
\boxed{C_1(t)=\frac{2tR(t)}{D(t)},\qquad
C_2(t)=\frac{2t(t-1)P(t)}{(1+t)D(t)^2}.}
\]

The polynomials, written in ascending powers, are

\[
\begin{aligned}
R(t)&=9975+17100t+10365t^2+2642t^3+238t^4,\\
D(t)&=27685+108535t+149179t^2+90837t^3+24584t^4+2380t^5,\\
P(t)&=15612625+155893675t+411771380t^2+510425170t^3\\
&\quad+351379457t^4+142316303t^5+33739658t^6\\
&\quad+4331572t^7+232560t^8.
\end{aligned}
\]

In particular \(C_1(t)>0\) for every \(t>0\), while \(C_2(t)<0\) for \(0<t<1\), \(C_2(1)=0\), and \(C_2(t)>0\) for \(t>1\). Thus the sign of the leading current-magnitude asymmetry is completely determined by whether the interior defect is a slow trap or a fast site:

\[
\boxed{J_t(\delta)+J_t(-\delta)=2C_2(t)\delta^2+O_t(\delta^4).}
\]

For each fixed \(t\ne1\), this even current component is strictly nonzero for all sufficiently small nonzero \(\delta\). Reflecting the defect to site three changes its sign exactly. Four is the **minimum chain length** in the same clean-boundary, one-interior-defect family for which such local rectification is possible: a two-site chain is homogeneous, and a three-site chain with its sole possible bulk defect is reflection-symmetric.

## Assumptions and scope

The state space is \(\{0,1\}^4\). A particle at an occupied site \(i\) may jump to an empty adjacent site at rate \(a_i\), where \((a_1,a_2,a_3,a_4)=(1,t,1,1)\). At the left boundary a vacant site is filled at rate \((1+\delta)/2\) and an occupied site is emptied at rate \((1-\delta)/2\). At the right boundary the corresponding rates are \((1-\delta)/2\) and \((1+\delta)/2\). No other transitions occur. All rates are in a fixed common inverse-time unit. The current is the left-reservoir particle influx, equivalently the steady current through each interior bond.

For \(t>0\) and \(|\delta|<1\), all configurations communicate, so a unique stationary distribution exists. The result concerns the coefficient at symmetric average reservoir density \(1/2\), not a theorem about arbitrary mean density, arbitrary chain lengths, or arbitrary large density differences. No thermodynamic or continuum limit is asserted.

## Proof

**Stationarity and analytic expansion.** Index the sixteen configurations lexicographically, let \(Q_t(\delta)\) be the column generator, and write

\[
Q_t(\delta)=Q_0(t)+\delta Q_1,
\qquad
Q_t(\delta)p(\delta)=0,
\qquad
\mathbf1^{\mathsf T}p(\delta)=1.
\]

Finite-state irreducibility makes the normalized stationary solution real-analytic near \(\delta=0\). Its coefficient vectors \(p_0,p_1,p_2\), defined by \(p(\delta)=p_0+\delta p_1+\delta^2p_2+O_t(\delta^3)\), satisfy

\[
Q_0p_0=0,\quad
Q_0p_1=-Q_1p_0,\quad
Q_0p_2=-Q_1p_1,
\]

with \(\sum p_0=1\) and \(\sum p_1=\sum p_2=0\). At equilibrium \(\delta=0\), detailed balance gives the explicit product distribution

\[
p_0(\eta)=\frac{t^{1-\eta_2}}{8(1+t)}.
\]

In particular the boundary sites and site three are independently fair and the defect site has occupation probability \(1/(1+t)\).

**Exact finite polynomial certificate.** The included `certificate.json` supplies three sixteen-component integer-polynomial vectors \(v_0,v_1,v_2\), each in lexicographic configuration order, with

\[
p_k(t)=\frac{v_k(t)}{8(1+t)^{k+1}D(t)^k},\qquad k=0,1,2.
\]

The included standalone `verify.py` constructs the generator from the physical transition rules, with integer-polynomial matrices \(A=2Q_0\) and \(B=2Q_1\), and verifies the following *exact polynomial identities*, coefficient by coefficient:

\[
\begin{aligned}
Av_0&=0,\\
Av_1+(1+t)DBv_0&=0,\\
Av_2+(1+t)DBv_1&=0,\\
\sum_\eta v_0(\eta)&=8(1+t),\\
\sum_\eta v_1(\eta)&=\sum_\eta v_2(\eta)=0.
\end{aligned}
\]

These are finite identities in \(\mathbb Z[t]\), not sampled numerical agreements. The two stationary-response equations and uniqueness identify the displayed rational vectors with the actual Taylor coefficients for every positive \(t\).

**Current extraction.** Since the net influx across the left boundary equals its injection density minus the stationary occupancy of site one,

\[
J_t(\delta)=\frac{1+\delta}{2}-\sum_{\eta:\eta_1=1}p(\delta;\eta).
\]

The same certificate checks exact polynomial identities for the coefficients of this expression, giving precisely the displayed rational expressions for \(C_1\) and \(C_2\). The linear numerator \(R\), common denominator \(D\), and nonlinear numerator \(P\) all have strictly positive integer coefficients. As \(t>0\), they are strictly positive, proving the global-in-\(t\) sign statement. Analyticity implies the asserted small-driving rectification for each fixed \(t\ne1\), and shows that the next correction to the even part starts at order \(\delta^4\).

**Minimality and reflection.** Reflection of a chain exchanges its reservoirs and negates the signed stationary current. A two-site chain with two clean boundaries, or a three-site chain with one interior defect, is itself reflection-invariant. Its current must therefore be exactly odd in \(\delta\), not merely to second order. For the four-site chain with its defect on site two, \(C_2\) is nonzero whenever \(t\ne1\), exhibiting a reflection-asymmetric instance. The reflected site-three defect has the opposite even current component. This proves the sharp minimum of four sites.

## Verification

Run `python verify.py` from the directory containing `verify.py` and `certificate.json`. The program uses the Python standard library only. It reconstructs every state transition, checks the three polynomial stationary balances and their normalizations, checks both current-coefficient identities, and confirms the strict positivity of all coefficients of \(D\), \(R\), and \(P\). Each polynomial operation uses arbitrary-precision integer arithmetic, so the identities are exact for all formal \(t\). A successful replay printed `PASS: exact polynomial balances at orders 0, 1, 2; normalization; exact current coefficients; positive-coefficient sign certificate.`

As a separate numerical orientation check, direct stationary linear solves at \(t=1/2\), \(\delta=\pm0.1\) give a negative even current component approximately \(-1.0953\times10^{-4}\), agreeing with the sign and leading coefficient. This finite check is not the proof of the sign statement.

## Relationship to prior work

Sakai and Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process* (arXiv:2609.03560, first posted 2026-09-03), introduced and analyzed the open site-disordered exclusion setting, established reflection-based necessary conditions, and studied nonlinear current response using approximations. The model and broad rectification mechanism are prior work. The contribution here is an **exact** smallest-chain, one-defect, half-density-reservoir quadratic coefficient whose strict sign is proved for every positive departure rate, without a closure assumption.

Their earlier *Symmetry Breaking of Current Response in Disordered Exclusion Processes* (arXiv:2512.03316, 2025) studies reversal of a **bulk external field** in disordered exclusion dynamics; the present reversal exchanges **reservoir densities** in a bulk-symmetric open chain. Their *Unexpected Effects of Disorder on Current Fluctuations in the Symmetric Simple Exclusion Process* (arXiv:2408.11364, 2024) studies exact second current moments with a defect under periodic boundary conditions, not this open stationary current coefficient. Homogeneous open exclusion theory already gives \(J_1(\delta)=\delta/5\); it is recovered at \(t=1\).

## Limitations

The claim is only a near-equilibrium expansion about mean reservoir density \(1/2\) in the specified four-site model; no global-in-\(\delta\) sign, random-disorder-ensemble limit, or arbitrary-size formula is claimed. The full remaining sections and appendices of the most closely matching 2026 preprint could not be inspected through the available access routes. Their possible exact finite-chain calculations are a residual priority risk. A general finite-state response theorem may imply the formal coefficient recurrence, but does not by itself give this model-specific positive numerator and sharp sign. The exact polynomial certificate is independently replayable, but an external mathematical or publication-priority audit has not been performed.

## References

- I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (first posted 2026-09-03), https://arxiv.org/abs/2609.03560.
- I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (first posted 2025-12-03), https://arxiv.org/abs/2512.03316.
- I. Sakai and T. Akimoto, *Unexpected Effects of Disorder on Current Fluctuations in the Symmetric Simple Exclusion Process*, arXiv:2408.11364v1 (first posted 2024-08-21), https://arxiv.org/abs/2408.11364.
- B. Derrida, B. Douçot, and P.-E. Roche, *Current fluctuations in the one-dimensional symmetric exclusion process with open boundaries*, J. Stat. Phys. 115 (2004), 717–748.
