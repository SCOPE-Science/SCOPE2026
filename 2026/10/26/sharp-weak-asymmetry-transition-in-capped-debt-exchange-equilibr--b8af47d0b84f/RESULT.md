# Sharp weak-asymmetry transition in capped-debt exchange equilibria

## Finding
Fix \(\kappa,r>0\), \(\tau\in\mathbb R\), and \(N\geq2\). Put \(K_N=\lfloor\kappa N^2\rfloor\) and \(L_N=\lfloor rK_N\rfloor\). Consider an exchange process on an arbitrary connected undirected graph with \(N\) vertices: a symmetric irreducible directed-edge proposal transfers one coin from its tail to its head, subject to the total-debt ceiling \(L_N\); the transfer succeeds with probability
\[
g_N(k)=\begin{cases}\frac12e^{\tau/(2N)},&k\geq1,\\[2pt]\frac12e^{-\tau/(2N)},&k\leq0,\end{cases}
\]
when the donor has integer wealth \(k\). These are probabilities for all sufficiently large \(N\). Let \(X_N=(X_N(1),\ldots,X_N(N))\) have the unique stationary law on the configurations with total wealth \(K_N\) and total debt at most \(L_N\). Write \(D_N=\sum_i(-X_N(i))_+\).

Define
\[
\tau_c=\frac1{\kappa\sqrt{r(1+r)}},\qquad
\delta_\tau=\begin{cases}
 r\kappa,&\tau\leq\tau_c,\\[2pt]
 \dfrac{\sqrt{\kappa^2+4/\tau^2}-\kappa}{2},&\tau>\tau_c.
\end{cases}
\]
Then \(D_N/N^2\to\delta_\tau\) in probability. Put \(A=\sqrt{\kappa+\delta_\tau}\), \(B=\sqrt{\delta_\tau}\). For each fixed \(m\geq1\),
\[
\bigl(X_N(1)/N,\ldots,X_N(m)/N\bigr)
\ \Longrightarrow\ \mu_\tau^{\otimes m},
\]
where \(\mu_\tau\) has the continuous two-sided exponential density
\[
 f_\tau(x)=\frac1{(A+B)^2}
 \begin{cases}
 \exp\bigl(-x/[A(A+B)]\bigr),&x\geq0,\\[2pt]
 \exp\bigl(x/[B(A+B)]\bigr),&x<0.
 \end{cases}
\]
The empirical distribution \(N^{-1}\sum_{i=1}^N\delta_{X_N(i)/N}\) converges weakly in probability to \(\mu_\tau\). In particular, the negative-wealth proportion converges to \(B/(A+B)\), and the mean debt per agent after scaling converges to \(\delta_\tau\). The limiting debt has a genuine derivative discontinuity at \(\tau_c\): it is constant below \(\tau_c\), while for \(\tau>\tau_c\),
\[
\frac{d\delta_\tau}{d\tau}=-\frac{2}{\tau^3\sqrt{\kappa^2+4/\tau^2}}<0.
\]
For any fixed \(\tau>\tau_c\), debt remains macroscopically positive but strictly below the bank ceiling. This is a finite weak-asymmetry regime distinct from both fixed-rate limiting regimes.

## Assumptions and scope
All coordinates are integers, \(\sum_i X_N(i)=K_N\), and \(\sum_i(-X_N(i))_+\leq L_N\). The graph may depend on \(N\) but must be connected; the edge proposal \(p_N(i,j)\) is symmetric and irreducible on that graph. At each update an ordered edge is proposed, the donor decides with probability \(g_N\), and an inadmissible proposal is rejected. Fix \(\kappa,r,\tau\) before taking \(N\to\infty\); do not let \(\tau\) vary with \(N\). The scaling here is exactly \(K_N\asymp N^2\), so wealth per person is of order \(N\). No assumption is made on graph mixing times. The limiting law is a statement about equilibrium, not about the time to reach equilibrium.

## Proof
**1. Exact stationary weights.** Define \(P(\eta)=\sum_i(\eta_i)_+\) and \(D(\eta)=\sum_i(-\eta_i)_+\). Since \(P(\eta)-D(\eta)=K_N\), detailed balance for a legal transfer \(i\to j\) gives the stationary weight
\[
 w_N(\eta)=(g_N^+)^{-P(\eta)}(g_N^-)^{D(\eta)}
 =(g_N^+)^{-K_N}\exp(-\tau D(\eta)/N),
\]
where \(g_N^+=\tfrac12e^{\tau/(2N)}\) and \(g_N^-=\tfrac12e^{-\tau/(2N)}\). Indeed, for every integer \(k\) the single-site weight \(G(k)=(g_N^+)^{-k}\) for \(k\geq0\), and \(G(k)=(g_N^-)^{-k}\) for \(k<0\), satisfies \(G(k-1)/G(k)=g_N(k)\); hence the product weights balance each proposed move with its reverse. Connectivity and positive rates give irreducibility on the finite feasible state space, establishing uniqueness. Therefore
\[
 \Pr\{X_N=\eta\}=\frac{\exp(-\tau D(\eta)/N)}{Z_N},
 \qquad\eta\in\Omega_N^{K_N,L_N}.
\]
The graph disappears entirely from this distribution.

**2. Exact debt-sector counts.** Let \(J_N\) be the number of negative sites. For integers \(d\geq1\) and \(1\leq j\leq\min(d,N-1)\), the number of vectors with debt \(d\) and exactly \(j\) negative sites is
\[
 C_N(d,j)=\binom Nj\binom{d-1}{j-1}
 \binom{K_N+d+N-j-1}{N-j-1}.
\]
The factors choose negative locations, positive compositions of \(d\) among those locations, and weak compositions of \(K_N+d\) among the other locations. For \(d=0\) the count is \(\binom{K_N+N-1}{N-1}\). These identities count every feasible vector exactly once.

**3. Two-variable entropy and its maximum.** Set \(\delta=d/N^2\) and \(q=j/N\). Uniform Stirling estimates on each compact subinterval \(\delta\in[\varepsilon,r\kappa+1]\), including the boundary values \(q=0,1\) by continuity, yield
\[
 \frac1N\bigl(\log C_N(d,j)-N\log N\bigr)
 =1+2H(q)+q\log\delta+(1-q)\log(\kappa+\delta)+o(1),
\]
where \(H(q)=-q\log q-(1-q)\log(1-q)\) and \(0\log0=0\). Uniformity follows from \(d\asymp N^2\), \(K_N+d\asymp N^2\), \(j\leq N\), and the uniform factorial estimate \(\log(k!)=k\log k-k+O(\log(N+1))\) for \(0\leq k\leq N\). The maximizing sign fraction is uniquely
\[
 q_\delta=\frac{\sqrt\delta}{\sqrt{\kappa+\delta}+\sqrt\delta}.
\]
The maximized entropy is
\[
 \Phi(\delta)=1+2\log\bigl(\sqrt{\kappa+\delta}+\sqrt\delta\bigr).
\]
It has \(\Phi'(\delta)=1/\sqrt{\delta(\kappa+\delta)}\), strictly decreasing from infinity to zero. The exact weight in step 1 subtracts \(\tau\delta\) from the entropy per vertex. Therefore the unique maximizer of \(\Phi(\delta)-\tau\delta\) over \([0,r\kappa]\) is \(\delta_\tau\) as displayed. The equality \(\tau=\Phi'(r\kappa)\) gives the exact threshold \(\tau_c\). At \(\delta=0\) the sector has entropy \(\Phi(0)=1+\log\kappa\). To control \(0<\delta<\varepsilon\) uniformly, note that the positive-debt sector count \(\sum_j C_N(d,j)\) is nondecreasing in integer \(d\geq1\); compare it with the sector at \(\lceil\varepsilon N^2\rceil\), and include \(d=0\) separately. Since \(\Phi'(0+)=\infty\), these small sectors are exponentially negligible for sufficiently small \(\varepsilon\). The uniform entropy bounds and the fact that at most \(O(N^3)\) pairs \((d,j)\) occur imply exponential concentration of \((D_N/N^2,J_N/N)\) at \((\delta_\tau,q_{\delta_\tau})\).

**4. Conditional composition limit.** Conditional on \((D_N,J_N)=(d,j)\), the negative sites form a uniform \(j\)-subset. Independently, their debt magnitudes form a uniform positive composition of \(d\) into \(j\) parts, and the remaining wealth values form a uniform weak composition of \(K_N+d\) into \(N-j\) parts. For a uniform weak composition \((Z_1,\ldots,Z_s)\) of \(M\), its exact joint tail is
\[
 \Pr\{Z_1\geq h_1,\ldots,Z_\ell\geq h_\ell\}
 =\frac{\binom{M-\sum_{i=1}^{\ell}h_i+s-1}{s-1}}
 {\binom{M+s-1}{s-1}}
\]
when \(\sum h_i\leq M\). If \(M\asymp N^2\), \(s\asymp N\), and \(h_i=\lceil Nx_i\rceil\), the ratio tends to \(\exp(-\sum_i x_i\,sN/M)\). Uniform positive compositions have the same limit after subtracting one unit from every part. It follows jointly for any fixed number of coordinates that the sign indicators become independent Bernoulli indicators of parameter \(q_\delta\), the positive values divided by \(N\) become independent exponentials of mean \((\kappa+\delta)/(1-q_\delta)=A(A+B)\), and the negative magnitudes divided by \(N\) become independent exponentials of mean \(\delta/q_\delta=B(A+B)\). Mixture of these laws has the claimed density: the positive and negative mixture weights are respectively \(A/(A+B)\) and \(B/(A+B)\). The concentration in step 3 removes the conditioning, proving convergence of every fixed coordinate block.

**5. Empirical law and derivative jump.** Exchangeability and convergence of one- and two-coordinate marginals show that, for every bounded continuous \(h\), the mean of \(N^{-1}\sum_i h(X_N(i)/N)\) converges to \(\int h\,d\mu_\tau\), while its variance tends to zero. This proves empirical weak convergence in probability. The negative-site fraction follows from step 3, and the debt fraction from boundedness of \(D_N/N^2\). Differentiating the explicit interior solution yields the stated derivative and its one-sided jump at \(\tau_c\).

## Verification
The accompanying `wealth_phase_check.py` checks the exact sector-count formula against brute-force enumeration, exact detailed-balance identities over all allowable transitions in a finite example, and the threshold equations for several parameter choices. It also evaluates the complete finite debt-sector distribution for multiple \(N\) and \(\tau\) and compares its mean with the limiting formula. Run `python wealth_phase_check.py` with Python 3 and the standard library. It reports 278 exact combinatorial and rational assertions, plus 12 numerical critical-curve checks and a separate finite-size comparison table. Those finite checks do not establish the convergence proof, which is analytic.

## Relationship to prior work
Sakagawa, arXiv:2610.00901v1 (first public version 2026-10-01), gives the finite stationary product measure for a much broader debt-exchange process and proves limits with a **fixed** transfer function \(g\). In its theorem, fixed unequal positive/negative asymptotic rates select either a two-sided Gamma law or a one-sided Gamma law. The present result starts from that exact stationary structure but studies an \(N\)-dependent rate ratio \(g_N^+/g_N^-=e^{\tau/N}\), for which fixed-rate classification cannot select the limit. The resulting finite positive-debt regime above a computable saturation threshold, and the kink in limiting debt, are not stated in the inspected theorem. Cao and Reed (2025, arXiv:2311.07851) prove a general finite-system reversible product law in their Lemma 2.3 and stationary-coordinate formula in Theorem 2.4, which already subsume our finite-state detailed-balance step. Their Sections 2–3 were inspected: Section 2 then specializes to a wealth-dependent rational donor rate, Section 3 formally studies mean-field ODEs with fixed per-agent average wealth and debt ratio, and neither states the present joint large-wealth weak-bias limit or its threshold. This is a genuine same-object antecedent and is explicitly credited. Cao and Motsch (2023) cover the unbiased two-phase mean-field description at fixed parameters. Lanchier and Reed's earlier debt-exchange studies establish exact stationary laws or fixed-rule exponential limits; the selected accessible descriptions do not specify this near-equal-rate crossover. Classical equivalence-of-ensembles and Gibbs-conditioning methods provide general tools, but no directly covering statement with this constrained debt observable and exact threshold was identified in the checked material. This is a literature comparison, not a claim of exhaustive priority.

## Limitations
The claim concerns stationary states, symmetric connected interaction networks, a **specific two-rate donor rule**, fixed real \(\tau\), and the precise wealth scale \(K_N\asymp N^2\). It does not cover spatially asymmetric proposals, arbitrary wealth-dependent rates, transient mixing times, random \(\tau\), or a second critical fluctuation scaling at \(\tau_c\). The source's fixed-rate results do not by themselves yield uniformity in \(N\)-varying rates; conversely, this calculation does not contradict those results. Potential equivalent formulations in older ensemble or econophysics literature remain an originality risk.

## References
1. H. Sakagawa, *Convergence of stationary distributions for a class of zero-range processes and its application to a wealth distribution model with debt*, arXiv:2610.00901v1 (2026-10-01), https://arxiv.org/abs/2610.00901; especially Proposition 1.1 and Theorem 1.4.
2. N. Lanchier and S. Reed, *Rigorous results for the distribution of money on connected graphs (models with debts)*, arXiv:1812.10359 (2018), https://arxiv.org/abs/1812.10359.
3. N. Lanchier and S. Reed, *Distribution of money on connected graphs with multiple banks*, arXiv:2201.11930 (2022), https://arxiv.org/abs/2201.11930.
4. F. Cao and S. Reed, *A biased dollar exchange model involving bank and debt with discontinuous equilibrium*, Math. Model. Nat. Phenom. 20 (2025), article 5, https://doi.org/10.1051/mmnp/2025007; originally arXiv:2311.07851 (2023), https://arxiv.org/abs/2311.07851; especially Lemma 2.3, Theorem 2.4, Definition 2.5 and Section 3.
5. F. Cao and S. Motsch, *Uncovering a two-phase dynamics from a dollar exchange model with bank and debt*, SIAM J. Appl. Math. 83 (2023), 1872–1891, https://doi.org/10.1137/22M1518621.
6. H. Sakagawa, *Limiting distributions of generalized money exchange models*, arXiv:2501.02490 (2025), https://arxiv.org/abs/2501.02490.
