# Folded-Gaussian dimer jamming at a balanced two-reservoir boundary

## Finding
Fix \(0<\alpha<1/2\), put \(\gamma=1-2\alpha\), and let \(N\) be even. Take integer class sizes \(0\le m_N\le N/2\) with \(m_N/N\to\alpha\) and \(\sqrt N(m_N/N-\alpha)\to0\). The graph is \(G_N=K_{N-2m_N}\vee K_{m_N,m_N}\), where \(\vee\) is graph join and \(K_{m_N,m_N}\) is complete bipartite. Thus the independent classes \(A,B\), each of size \(m_N\), have all edges between them, and the clique \(C\) of size \(N-2m_N\) is joined to both. Give the edges independent, identically distributed atomless priorities. In increasing-priority order, accept an edge if neither endpoint has been matched. Let \(U_N\) be the final number of unmatched vertices.

Then, along the even integers,
\[
\frac{U_N}{\sqrt N}\Longrightarrow |Z_\alpha|,\qquad
Z_\alpha\sim\mathcal N(0,\sigma_\alpha^2),\qquad
\sigma_\alpha^2=\frac{2\alpha^2}{\gamma}\bigl[e^{-\gamma/\alpha}-(1+\gamma/\alpha)e^{-2\gamma/\alpha}\bigr]>0.
\]
Also \(\mathbb E[U_N]/\sqrt N\to\sigma_\alpha\sqrt{2/\pi}\). Every graph in the sequence has a perfect matching: match \(A\) to \(B\) and pair the even number of vertices in \(C\). Nevertheless the greedy process leaves order \(\sqrt N\) vacancies with a folded-normal limit.

## Assumptions and scope
All pairs are edges except those inside \(A\) or inside \(B\). All accepted dimers are irreversible. The continuous independent priority law can be changed without changing the edge-order distribution. The quantity being scaled is the final unmatched count, not the number of accepted dimers or the vacancy count at a prescribed time.

## Proof
**1. Exact count process.** Independent exponential clocks of rate one give a uniform random priority order. Any edge with two unmatched endpoints has not yet rung. Conditional on the past, the clocks on such edges have independent exponential residual waiting times. In the rescaled time \(s=Nt\), where \(t\) is physical clock time, the four jump rates for counts \((A_s,B_s,C_s)=(A,B,C)\) are
\[
\begin{array}{c|c}
(-1,-1,0)&AB/N\\
(-1,0,-1)&AC/N\\
(0,-1,-1)&BC/N\\
(0,0,-2)&C(C-1)/(2N).
\end{array}
\]
Write \(a=A/N,b=B/N,c=C/N\), \(L=A+B\), and \(D=A-B\). The drift of \(D\) is \(-cD\). The bracket rate of the jump martingale of \(D/\sqrt N\) is \((a+b)c\). At jamming the unmatched set is independent and has even size. A vertex of \(C\) cannot occur in such a set, and the set cannot meet both \(A\) and \(B\). Thus \(U_N=|D_{\rm jam}|\) exactly.

**2. Fluid trajectory.** The normalized jumps are bounded by \(2/N\), their total rate is \(O(N)\), and the normalized drift is a Lipschitz polynomial on the fraction domain up to an \(O(1/N)\) term. The martingale maximal inequality and Grönwall's inequality give uniform convergence in probability on fixed time intervals to the fluid equations
\[
\dot a_*=-a_*(b_*+c_*),\quad \dot b_*=-b_*(a_*+c_*),\quad \dot c_*=-c_*(a_*+b_*+c_*),
\qquad (a_*,b_*,c_*)(0)=(\alpha,\alpha,\gamma).
\]
With \(\dot\tau=(1-\alpha\tau)^2e^{-\gamma\tau}\) and \(\tau(0)=0\), direct differentiation gives
\[
a_*=b_*=\alpha(1-\alpha\tau)e^{-\gamma\tau},\qquad c_*=\gamma(1-\alpha\tau)^2e^{-\gamma\tau}.
\]
As \(s\to\infty\), \(\tau\uparrow1/\alpha\), so \(\int_0^\infty c_*(s)\,ds=\gamma/\alpha\), and \(c_*/(a_*+b_*)\to0\).

**3. Cutoff estimates.** Let \(T_N=\inf\{s:L_s\le N^{2/3}\}\). We will use two generator bounds, for \(L\ge 10\) and \(0\le C\le L\):
\[
\mathcal L_N(2C/L)\le -C/(2N),\qquad
\mathcal L_N(NC/L^2)\le (NC/L^2)(C+7)/N.
\]
For \(C>0\), dividing the first generator by \(2C/(NL)\) gives \(2AB/(L-2)-L^2/(L-1)+C/(L-1)+1\). After replacing \(AB\) by \(L^2/4\) and \(C\) by \(L\), the deficit from \(-L/4\) is \((L^2-10L+8)/(4(L-2))\ge0\). For the second, dividing the generator by \(C/L^2\) and subtracting \(C\) gives
\[
\frac{4AB(L-1)}{(L-2)^2}-\frac{L^3}{(L-1)^2}+1+\frac{C(3L-2)}{(L-1)^2}.
\]
The same replacements give a deficit from \(7\) of \((2L-3)(L^2-8L+8)/((L-2)^2(L-1))\ge0\). Both bounds are immediate at \(C=0\).

The identity \(\mathcal L_N D^2=-2cD^2+Lc\) yields \(\mathbb E D_\theta^2\le C_0\) at any bounded stopping time \(\theta\): the expected integral of \(Lc\) is the expected number of \(A\)-\(C\) and \(B\)-\(C\) jumps through \(\theta\), at most \(C_0\). Stopping at the first crossing of \(|D|>N^{2/3}/3\) and then removing a deterministic time cap shows that its probability at any time is \(O(N^{-1/3})\).

Fix a sufficiently large deterministic \(T\). With probability tending to one, \(L_T>N^{2/3}\), \(C_T\le L_T\), and \(|D_T|\le L_T/3\) by convergence to the fluid path. On these initial states, stop at \(S\), the first of \(T_N\), \(C>L\), and \(|D|>L/3\) after \(T\). The first generator inequality gives, conditionally on the state at \(T\),
\[
\mathbb E\!\left[\int_T^S c(s)ds\mid\mathcal F_T\right]\le 4C_T/L_T,
\qquad
\mathbb P(C_S>L_S\mid\mathcal F_T)\le 2C_T/L_T.
\]
Here the exit values of \(2C/L\) are well defined for large \(N\), since \(L\) decreases by at most two at a jump. Before \(S\), both \(A,B\ge L/3\). At each level of \(L\), the rate of jumps decreasing it is at least \(L^2/(9N)\); changes of \(C\) alone do not reduce this lower bound. Summing the expected times at levels above \(N^{2/3}\) gives \(\mathbb E[S-T\mid\mathcal F_T]=O(N^{1/3})\) on those initial states. Thus the exponent \(\int_T^S(c+7/N)ds\) is tight. The second generator inequality makes \((NC/L^2)\exp(-\int_T^s(c+7/N)du)\), stopped at \(S\), a nonnegative supermartingale. Its initial value is tight by the fixed-time fluid limit (one can first condition on it being bounded). The stopped value of \(NC/L^2\) is therefore tight as well.

The probability of exiting at a side boundary before \(T_N\) can be made arbitrarily small by taking \(T\) large and then \(N\) large: for \(C>L\) use the ratio bound and \(c_*/(a_*+b_*)\to0\), and for \(|D|>L/3\) use the crossing bound. It follows that \(C_{T_N}=O_{\mathbb P}(N^{1/3})\) on the events that reach \(T_N\), up to a probability tending to zero. It also follows that the tail integral \(\int_T^{T_N}c(s)ds\) is negligible in the successive limits \(N\to\infty\), then \(T\to\infty\). On the event \(T_N=\infty\) the counts at \(T_N\) mean their absorbed values; this event has vanishing probability. Each future jump changing \(D\) consumes a vertex of \(C\). Consequently \((D_{\rm jam}-D_{T_N})/\sqrt N\to0\) in probability.

**4. Stopped martingale central limit theorem.** Put
\[
Q_N(s)=\exp\!\left(\int_0^{s\wedge T_N}c(u)du\right),\qquad
M_N(s)=Q_N(s)D_{s\wedge T_N}/\sqrt N.
\]
This integrating factor cancels the drift. Since \(D_0=0\), \(M_N\) is a zero-initial-value local martingale, with terminal bracket \(\int_0^{T_N}Q_N(s)^2(a+b)c\,ds\). The fixed-time and tail integral estimates give \(Q_N(T_N)\to e^{\gamma/\alpha}\) in probability. On fixed intervals the bracket converges by the fluid limit. For the tail, the compensator identity bounds \(\mathbb E\int_T^\infty(a+b)c\,ds\le\mathbb E[C_T]/N\), because each counted jump consumes one of the remaining \(C_T\) vertices. This bound tends to zero in the successive limits, and \(Q_N(T_N)^2\) is tight. The limiting bracket is
\[
V=2\alpha\gamma\int_0^{1/\alpha}(1-\alpha u)e^{\gamma u}\,du,
\]
using \(u=\tau(s)\). To apply the terminal martingale CLT, localize at a fixed bound on \(Q_N\) larger than \(e^{\gamma/\alpha}\); this changes the terminal value with probability tending to zero and bounds jumps by a constant times \(N^{-1/2}\). The bracket converges to \(V\) and the jump Lindeberg condition holds. Hence \(M_N(T_N)\Longrightarrow\mathcal N(0,V)\). Removing the integrating factor and applying the cutoff gives \(D_{\rm jam}/\sqrt N\Longrightarrow\mathcal N(0,e^{-2\gamma/\alpha}V)\). Evaluation of the positive integral gives \(e^{-2\gamma/\alpha}V=\sigma_\alpha^2\). Taking absolute values proves the law of \(U_N/\sqrt N\).

Finally, the same stopped second-moment estimate gives \(\mathbb E D_{\rm jam}^2/N\le C_0/N\) by Fatou's lemma. This implies uniform integrability of \(U_N/\sqrt N\) and gives the asserted convergence of its mean. No convergence of second moments is asserted.

## Verification
The accompanying `verify.py` compares exact small-graph absorption probabilities from the four-transition count chain with a recursion on labeled vertex subsets. It also checks rational identities for the generator bounds and uses midpoint quadrature for the limiting variance. Seeded finite-size simulations are sanity checks. None of these finite checks replaces the terminal martingale proof.

## Relationship to prior work
Classical work by Pippenger (1989), Dyer and Frieze (1991), and Gamarnik and Goldberg (2008) studies greedy matching or adsorption in other graph regimes. The regular-graph and bounded-degree results of Gamarnik and Goldberg do not give this terminal distribution for dense inhomogeneous graphs. Macroscopic fluid laws for complete-split graphs or multipartite graphs with a fixed number of parts do not determine fluctuations on the \(\sqrt N\) scale in this model. The comparisons do not establish exhaustive priority.

## Limitations
The result concerns exactly equally sized independent reservoirs and a clique of fixed positive limiting density. It does not treat independent reservoirs differing by order \(\sqrt N\), nonuniform edge orderings, or a time-dependent deposition rate.

## References
1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277v1 (2008), Sections 1–3.
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–45, doi:10.1002/rsa.3240020104.
3. N. Pippenger, *Random sequential adsorption on graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–401, doi:10.1137/0402034.
