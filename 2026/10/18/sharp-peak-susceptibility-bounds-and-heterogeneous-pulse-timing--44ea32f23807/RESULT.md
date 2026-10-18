# Sharp peak-susceptibility bounds and heterogeneous pulse timing in a logistic vaccination model

## Finding
Fix a period \(T>0\), a logistic growth parameter \(A>0\), an integer \(m\geq1\), and prescribed vaccine-survival factors \(q_1,\ldots,q_m\in(0,1)\). Put \(Q=\prod_{i=1}^m q_i\). When \(e^{AT}Q>1\), every choice of positive inter-pulse gaps \(\tau_1,\ldots,\tau_m\) satisfying \(\sum_i\tau_i=T\) has a unique positive attracting disease-free periodic susceptible orbit. Its maximum susceptible density \(M(\boldsymbol\tau)\) satisfies the sharp envelope

\[
M_*\leq M(\boldsymbol\tau)\leq M_{\mathrm{cluster}}
=\frac{A(e^{AT}Q-1)}{Q(e^{AT}-1)},
\]

where \(M_*\in(0,A)\) is the unique solution of

\[
\prod_{i=1}^{m}\frac{A-q_iM_*}{A-M_*}=e^{AT}Q.
\]

The lower bound is attained at exactly one labeled cyclic schedule (up to a common phase shift):

\[
\boxed{\tau_i^*=\frac1A\log\frac{A-q_iM_*}{q_i(A-M_*)}}.
\]

Every pre-vaccination peak then equals \(M_*\). For \(m\geq2\) and strictly positive gaps, the **complete range** of attainable peaks is exactly \( [M_*,M_{\mathrm{cluster}})\): the upper endpoint is a sharp but unattained supremum as the pulses coalesce. For \(m=1\), both bounds coincide. For equal \(q_i\), the unique optimal gaps are equal; heterogeneous vaccination proportions generally require unequal gaps.

For the associated nonseasonal infection linearization \(\dot I=(\beta S-\gamma)I\) with \(\beta,\gamma>0\), the one-period rare-infection Floquet multiplier is exactly

\[
\boxed{\mathcal M_I=\exp\bigl(\beta(AT+\log Q)-\gamma T\bigr)},
\]

independent of all gaps. Thus periodic vaccination schedules with identical prescribed proportional pulse factors have the same linear invasion multiplier but different maximum instantaneous susceptible densities. This is an exact comparison of **proportional pulse factors**, not a claim of equal numbers of doses administered.

## Assumptions and scope
Between vaccination pulses the disease-free susceptible equation is \(\dot S=S(A-S)\), and at pulse \(i\), \(S^+=q_i S^-\). The \(m\) labeled pulse types recur each period in the fixed cyclic order \(1,\ldots,m\). Every inter-pulse interval \(\tau_i\) is strictly positive and sums to \(T\). The peak is the maximum of the disease-free susceptible orbit over a full period, including its left limits before pulses. All multipliers are strictly between zero and one. There is no seasonal variation in \(A\), \(\beta\), or \(\gamma\), no latency stage, and no disease-induced impulsive change in \(I\). The claim concerns the unique disease-free periodic orbit and its linear infection invasion, not the nonlinear endemic attractor.

When \(e^{AT}Q\leq1\), there is no strictly positive periodic disease-free susceptible orbit; the disease-free susceptible population tends to zero, so the positive-orbit peak optimization above is inapplicable.

## Proof
**Positive periodic orbit.** Write \(z=1/S\). A logistic flight of duration \(t\) transforms \(z\) to \(e^{-At}z+(1-e^{-At})/A\), and vaccination changes \(z\) to \(z/q_i\). The period map for \(z\) is affine with positive intercept and slope \(\kappa=e^{-AT}/Q\). If \(\kappa<1\), it has a unique positive fixed point and attracts all positive initial \(z\); if \(\kappa\geq1\), no finite positive fixed point exists. On a positive periodic orbit \(0<S<A\): a point at or above \(A\) cannot recur after a strict downward pulse because logistic flight never crosses \(A\). Therefore \(S\) increases strictly between pulses, and its period maximum is one of the pre-pulse values \(s_i=S(t_i^-)\).

**Invariant infection growth.** Away from pulses, \(d\log S/dt=A-S\); at a pulse the logarithm jumps by \(\log q_i\). Periodicity gives

\[
\int_0^T S(t)\,dt=AT+\sum_i\log q_i=AT+\log Q.
\]

Integrating the scalar infection variational equation yields the displayed \(\mathcal M_I\). This identity extends the known one-pulse expression to arbitrarily placed and unequally strong prescribed pulses; it is not presented as an independent novelty claim.

**Exact minimax lower bound.** Logistic flight from \(q_i s_i\) to \(s_{i+1}\) gives

\[
e^{A\tau_i}=\frac{s_{i+1}(A-q_i s_i)}{q_i s_i(A-s_{i+1})}.
\]

Multiplying over all \(i\) and using cyclic indexing gives

\[
AT+\log Q=\sum_{i=1}^{m}\phi_i(s_i),\qquad
\phi_i(s)=\log\frac{A-q_i s}{A-s}.
\]

For \(0<s<A\), \(\phi_i'(s)=(1-q_i)A/((A-s)(A-q_i s))>0\). Also \(\sum_i\phi_i(0)=0\) and \(\sum_i\phi_i(s)\to\infty\) as \(s\uparrow A\). Since \(AT+\log Q>0\), there is exactly one \(M_*\in(0,A)\) satisfying \(\sum_i\phi_i(M_*)=AT+\log Q\). If \(M=\max_i s_i\), then

\[
AT+\log Q=\sum_i\phi_i(s_i)\leq\sum_i\phi_i(M),
\]

so \(M\geq M_*\). Equality forces \(s_i=M_*\) for every \(i\). The uniquely prescribed recovery times from \(q_iM_*\) to \(M_*\) are precisely \(\tau_i^*\) above. Their sum is \(T\) by the defining equation, and each is positive. These gaps construct the unique schedule attaining the lower bound.

**Sharp clustered upper bound.** Define the logistic flight \(F_t(s)=Ae^{At}s/[A+(e^{At}-1)s]\). For any \(t>0\), \(q\in(0,1)\), and \(s>0\),

\[
qF_t(s)<F_t(qs).
\]

Moving an impulse earlier across a positive flight therefore strictly increases the period return map when measured just before an initial pulse. Moving every subsequent impulse next to the initial pulse bounds each pre-pulse return map above by \(s\mapsto F_T(Qs)\). At its positive fixed point \(s_i\), this comparison gives \(s_i\leq F_T(Qs_i)\). The right-hand map has its unique positive fixed point at \(M_{\mathrm{cluster}}\), and \(F_T(Qs)-s\) is positive below it and negative above it. Hence \(s_i\leq M_{\mathrm{cluster}}\) for every \(i\). For multiple positive gaps, at least one impulse must be moved through positive flight time, giving strictness. As all but one gaps tend to zero and one gap tends to \(T\), the maximal pre-pulse value approaches the fixed point of \(F_T(Q\cdot)\). This proves sharpness of the upper bound. The open positive-gap simplex is connected, and the unique periodic orbit and its peak depend continuously on its gaps. The attained minimum and limiting upper supremum therefore fill the entire interval \( [M_*,M_{\mathrm{cluster}})\) when \(m\geq2\).

## Verification
A standalone Python program, `verify_peak.py`, uses exact rational logistic Möbius maps. It independently reconstructs the positive periodic orbit from return-map coefficients, tests the strict peak envelope on a grid of unequal two- and three-pulse schedules, and checks an exact illustrative optimizer. The program completed 144 assertions. Its finite tests supplement, and do not replace, the proof above.

For the exact example \(A=1\), \(T=\log8\), \(m=2\), \(q_1=1/2\), \(q_2=3/4\), the defining equation has root \(M_*=2/3\) in \((0,1)\), with optimal gaps \((\log4,\log2)\), while \(M_{\mathrm{cluster}}=16/21\). If \(\beta=2\), \(\gamma=1\), every allowed spacing has infection Floquet multiplier \(9/8\), even though the peak varies over the stated nontrivial range.

## Relationship to prior work
Maurício de Carvalho and Rodrigues, arXiv:2312.02306 (first publicly submitted 4 December 2023), analyze the same logistic susceptible flight and a **single** periodically repeated proportional vaccine pulse; their Lemma 7 derives the one-pulse invasion formula and their Theorem A classifies epidemic regimes. Those prior results are not claimed as new here. This finding instead optimizes the maximum susceptible excursion over arbitrary placements of multiple **prescribed, possibly unequal proportional pulses**, proves uniqueness of the peak-equalizing gap vector, and identifies the sharp opposite clustered endpoint.

Browne, Smith and Bourouiba (arXiv:1309.0265; J. Math. Biol. 2015) study timing and synchronization in spatially coupled pulse-vaccination epidemics and analyze reproduction-number equivalence at **equal actual vaccination cost** for certain models. The present theorem is single-patch, has logistic rather than linear susceptible recruitment, fixes proportional pulse factors rather than actual dose cost, and has a different objective (worst instantaneous susceptible abundance). Gavish and Katriel (2026) optimize a transmission-based periodic vaccination functional in a model with seasonal infection and immunity decay, not the sharp, labeled, unequal-multiplier logistic peak envelope established here. Earlier impulsive-control work provides additional conceptual background but may contain a broader general equioscillation principle.

## Limitations
The theorem uses a single uncoupled population and constant between-pulse coefficients. It concerns the disease-free susceptible peak and the **linear** infection multiplier; it does not optimize actual infections, nonlinear endemic burden, seasonal transmission, or a fixed supply of physical doses. Prescribing \(q_i\) does not fix the count \(\sum_i(1-q_i)s_i\) of doses administered along the periodic orbit, which varies with timing. A pre-existing general minimax theorem for monotone impulsive flows might subsume the peak-equalization argument; priority beyond the inspected literature requires independent checking.

## References
- João P. S. Maurício de Carvalho and Alexandre A. Rodrigues, *Pulse vaccination in a SIR model: global dynamics, bifurcations and seasonality*, arXiv:2312.02306, first submitted 2023-12-04, https://arxiv.org/abs/2312.02306.
- Cameron J. Browne, Robert J. Smith, and Lydia Bourouiba, *From regional pulse vaccination to global disease eradication: insights from a mathematical model of poliomyelitis*, arXiv:1309.0265, https://arxiv.org/abs/1309.0265.
- Nir Gavish and Guy Katriel, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission*, Bull. Math. Biol. 88 (2026), article 170, https://doi.org/10.1007/s11538-026-01741-0.
- Imane Abouelkheir, Fadwa El Kihal, Mostafa Rachik, and Ilias Elmouki, *Optimal Impulse Vaccination Approach for an SIR Control Model with Short-Term Immunity*, Mathematics 7 (2019), 420, https://doi.org/10.3390/math7050420.
