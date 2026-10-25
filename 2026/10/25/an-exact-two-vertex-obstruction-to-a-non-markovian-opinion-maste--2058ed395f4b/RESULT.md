# An exact two-vertex obstruction to a non-Markovian opinion master equation

## Finding
Consider a two-agent asynchronous neighbor-copying process with one undirected edge and no self-copying: at a ring of agent \(i\)'s private renewal clock, \(X_i\) is replaced by the other agent's opinion. The clocks have mutually independent, strictly positive, continuous interevent distributions; their first-event survival functions are \(S_1,S_2\). If \(X_1(0)=a\) and \(X_2(0)=b\), then for every \(t\ge0\)
\[
\mathbb E[X_1(t)-X_2(t)]=(a-b)S_1(t)S_2(t).
\]
For the common waiting-time density \(T(u)=\tfrac12\mathbf1_{[0,2]}(u)\), and \(a\ne b\), the expected difference computed from the stochastic update rule contradicts the asserted exact renewal master equation (2.9) of Chu and Porter: when its genuine expected difference is substituted into the claimed equation at \(t=2\), the right-hand side is \(-(a-b)(11-4e)\), while the left-hand side is \(0\). Because \(11-4e>0\), this is a strict failure of the purported exact marginal identity.

## Assumptions and scope
The two clocks run independently and restart after each of their own events; interevent laws are independent of their opinions. Each ring unidirectionally copies the other agent's opinion without altering the neighbor's clock. The original network has normalized adjacency \(P=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Assume continuous waiting-time densities so simultaneous events have probability zero. The initial opinions are deterministic with \(a\ne b\). This is an instance of the stochastic event description in Section 2, pp. 2626–2627 of the cited paper, and uses its definitions \(\phi\) (first-wait survival) and \(\theta\) (renewal-event density).

## Proof
Let \(F_i\) be the first ring time of vertex \(i\). The first ring causes consensus: after either vertex copies its only neighbor, the two opinions agree and never separate. Until that first ring they remain \(a,b\). Consequently the random difference is exactly
\[
X_1(t)-X_2(t)=(a-b)\mathbf 1_{\{F_1>t,F_2>t\}},
\]
and independence yields the stated product formula. More explicitly, for \(i=1,2\), the marginal opinions satisfy
\[
\begin{aligned}
\mathbb E X_1(t)&=a+(b-a)\int_0^t T_1(u)S_2(u)\,du,\\
\mathbb E X_2(t)&=b+(a-b)\int_0^t T_2(u)S_1(u)\,du.
\end{aligned}
\]
For identical uniform \([0,2]\) waits, \(S(t)=1-t/2\) for \(0\le t\le2\), and hence the genuine mean difference is \(y_{\mathrm{true}}(t)=(a-b)(1-t/2)^2\) on this interval and zero at \(t=2\).

Equation (2.9) in the source asserts, for the two-agent antisymmetric mode,
\[
y(t)=S(t)(a-b)-\int_0^t S(t-u)\theta(u)y(u)\,du.
\]
On \(0<u<2\), the renewal density is
\[
\theta(u)=\sum_{k\ge1}T^{*k}(u)
=\sum_{k\ge1}\frac{u^{k-1}}{2^k(k-1)!}
=\frac12 e^{u/2}.
\]
(The finite-time convolutions are elementary because for \(u<2\) the convolution of \(k\) uniform densities equals the corresponding polynomial simplex density.) At \(t=2\), inserting the **actual** trajectory into the right side gives
\[
-\frac{a-b}{4}\int_0^2 u e^{u/2}(1-u/2)^2\,du
=-(a-b)\int_0^1 v e^v(1-v)^2\,dv
=-(a-b)(11-4e).
\]
The integral is strictly positive and equals \(11-4e\) by the antiderivative \(e^v(v^3-5v^2+11v-11)\). The left side is zero, so the purported identity fails for \(a\ne b\). The source's intermediate factorization (2.4) treats the neighbor's state distribution at a renewal event as the unconditional neighbor marginal. Independence of primitive clocks does not give this state-event independence: the neighbor's opinion can depend on earlier updates by the very agent whose clock rings later.

## Verification
Run \(\texttt{python verify.py}\) from the extracted package; it uses only the Python standard library and checks the polynomial antiderivative, exact renewal coefficients, the order-four Taylor mismatch, and a separate finite-state first-event probability identity. The proof is analytic; the program checks explicit formulas rather than replacing the proof.

## Relationship to prior work
The source's Section 2.1, equations (2.4), (2.6), and (2.9), supplies the concrete comparison target. It describes an event-driven stochastic copying process and presents the resulting renewal relation as the exact equation for the mean. The present calculation demonstrates a discrepancy for the specific two-agent stochastic process. The 2021 tie-decay opinion paper studies an evolving-weight Laplacian and DeGroot evolution, not this renewal-clock stochastic marginal assertion. General moment-closure literature already warns that state correlations obstruct naive closure; the contribution here is the exact identification of the discrepancy in this particular published non-Markovian derivation, including a closed-form witness \(11-4e\).

## Limitations
This finding does **not** claim that the printed renewal integral equation is ill-defined, that its spectral properties are false when treated as a **separately defined** deterministic model, or that any particular published numerical simulation is wrong. The counterexample applies to interpreting that equation as the **exact ensemble expectation** of the specified independent-clock copying process. It does not assert an infinite-network approximation error or classify all waiting-time laws permitting exact closure. A mean-field approximation may be useful, but its accuracy is a separate question. Independent scientific assessment and complete publication-priority clearance remain outstanding.

## References
- Chu, W. and Porter, M. A., Non-Markovian Models of Opinion Dynamics on Temporal Networks, SIAM J. Appl. Dyn. Syst. 22 (2023), 2624–2647; arXiv:2208.12787, first public 2022-08-26; DOI:10.1137/22M151858X.
- Sugishita, K., Porter, M. A., Beguerisse-Díaz, M., and Masuda, N., Opinion dynamics on tie-decay networks, Phys. Rev. Research 3 (2021), 023249, DOI:10.1103/PhysRevResearch.3.023249 (distinct interaction mechanism).
- Demirel, G., Vázquez, F., Böhme, G. A., and Gross, T., Moment-closure approximations for discrete adaptive networks, Physica D 267 (2014), 68–80, DOI:10.1016/j.physd.2013.07.003 (general correlation-closure context, not claimed as a direct source of this example).
