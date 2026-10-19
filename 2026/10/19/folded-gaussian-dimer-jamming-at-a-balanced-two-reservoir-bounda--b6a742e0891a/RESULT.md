# Folded-Gaussian dimer jamming at a balanced two-reservoir boundary

## Finding
Fix \(0<\alpha<1/2\), put \(\gamma=1-2\alpha\), and for each even integer \(N\) let \(m_N\) be an integer with \(m_N/N\to\alpha\) and \(\sqrt N(m_N/N-\alpha)\to0\). Form \(G_N=K_{N-2m_N}\vee(K_{m_N}^{\mathrm{ind}}\sqcup K_{m_N}^{\mathrm{ind}})\): two mutually joined independent classes \(A,B\), each of size \(m_N\), and a clique \(C\) of size \(N-2m_N\) joined to both. Independently assign every edge an atomless, identically distributed priority. Accept edges in increasing-priority order when neither endpoint has been matched. Let \(U_N\) be the number of unmatched vertices when no admissible edge remains.

Then, as \(N\to\infty\) through even integers,
\[
\frac{U_N}{\sqrt N}\ \Longrightarrow\ |Z_\alpha|,\qquad
Z_\alpha\sim\mathcal N(0,\sigma_\alpha^2),\quad
\sigma_\alpha^2=\frac{2\alpha^2}{\gamma}
\left[e^{-\gamma/\alpha}-(1+\gamma/\alpha)e^{-2\gamma/\alpha}\right]>0.
\]
Moreover \(\mathbb E[U_N]/\sqrt N\to\sigma_\alpha\sqrt{2/\pi}\). Every \(G_N\) has a perfect matching, yet uniform-priority irreversible matching leaves order \(\sqrt N\) vacancies, with a non-Gaussian, folded-normal law.

## Assumptions and scope
There are no edges inside \(A\) or inside \(B\); all other unordered pairs are edges, including all pairs inside \(C\). The classes \(A,B\) have the same integer size, and \(N\) is even, so \(|C|\) is even. All accepted dimers are irreversible. The priority distribution may be any continuous identically distributed law, independent over edges. The central limit theorem concerns the final count of *unmatched vertices*, not the number of accepted dimers or the trajectory at a prescribed physical time.

## Proof
**1. Exact jump chain.** Replacing random priorities by independent rate-one exponential clocks gives the same relative edge order. Speed up physical time by factor \(N\), and write \((A_s,B_s,C_s)\) for unmatched counts, \(a=A_s/N\), \(b=B_s/N\), \(c=C_s/N\). The four possible transitions and their rates in accelerated time are
\[
(A,B,C)\to(A-1,B-1,C):\ AB/N,\quad
(A-1,B,C-1):\ AC/N,\quad
(A,B-1,C-1):\ BC/N,\quad
(A,B,C-2):\ C(C-1)/(2N).
\]
Consequently \(D=A-B\) has drift \(-cD\), while its jump martingale has predictable squared-jump rate \((a+b)c\) after dividing \(D\) by \(\sqrt N\). Every jump involving \(C\) changes \(D\) by at most one and consumes at least one vertex of \(C\); all other jumps preserve \(D\). At a jammed state, unmatched vertices must be independent. Hence either they all lie in \(A\), all in \(B\), or comprise at most one vertex of \(C\). Parity rules out the last possibility, and thus \(U_N=|D_{\mathrm{jam}}|\) exactly.

**2. Fluid trajectory.** For fixed finite time intervals, the bounded-jump martingales are uniformly \(O_{\mathbb P}(N^{-1/2})\), so the density vector converges to
\[
\dot a=-a(b+c),\qquad \dot b=-b(a+c),\qquad \dot c=-c(a+b+c),
\qquad(a(0),b(0),c(0))=(\alpha,\alpha,\gamma).
\]
Introduce \(\tau\) by \(\dot\tau=(1-\alpha\tau)^2e^{-\gamma\tau}\), \(\tau(0)=0\). Direct differentiation gives
\[
a=b=\alpha(1-\alpha\tau)e^{-\gamma\tau},\qquad
c=\gamma(1-\alpha\tau)^2e^{-\gamma\tau}.
\]
The increasing parameter \(\tau\) tends to \(1/\alpha\). In particular \(\int_0^\infty c(s)\,ds=\gamma/\alpha\), while \(c/(a+b)\to0\).

**3. All-time cutoff lemma.** Write \(L=A+B\), and stop at \(T_N=\inf\{s:L_s\le N^{2/3}\}\). Two elementary generator inequalities make this growing-time cutoff rigorous. For \(L\ge10\) and \(0\le C\le L\), direct substitution of the four jump rates gives
\[
\mathcal L_N\frac{2C}{L}\le-\frac{C}{2N},\qquad
\mathcal L_N\frac{NC}{L^2}\le\frac{NC}{L^2}\left(\frac CN+\frac7N\right).
\tag{1}
\]
The algebra reduces respectively to the positive rational expressions
\[
\frac{L^2-10L+8}{4(L-2)}\ge0,
\quad\frac{(2L-3)(L^2-8L+8)}{(L-2)^2(L-1)}\ge0
\quad(L\ge10),
\]
by using \(AB\le L^2/4\) and \(C\le L\). These identities are checked independently in the verification script.

For clarity, here are the stopping arguments behind (1). Starting at a fixed large deterministic \(T\), stop also if \(C>L\) or \(|D|>L/3\). The first inequality and nonnegative-supermartingale stopping show that \(\mathbb E\int_T^{T_N}c(s)\,ds\) (on the unexceptional stopped path) is at most \(4\,\mathbb E[C_T/L_T]\), which tends to zero as \(T\to\infty\) after \(N\to\infty\). The chance of the boundary \(C>L\) is at most \(\mathbb E[2C_T/L_T]\), also vanishing in that order. The generator satisfies
\[
\mathcal L_N D^2=-2cD^2+(A+B)c,
\]
so optional stopping, together with at most \(C_0\) cross-to-\(C\) jumps, gives \(\sup_\theta\mathbb E D_\theta^2\le D_0^2+C_0\) for arbitrary bounded stopping times \(\theta\). Consequently \(\mathbb P(\sup_{s\le T_N}|D_s|>N^{2/3}/3)=O(N^{-1/3})\). On the remaining paths \(A,B\ge L/3\); the \(AB\) edge rate is at least \(L^2/(9N)\), which bounds the expected remaining accelerated time before \(L\le N^{2/3}\) by \(O(N^{1/3})\). Therefore \(\int_T^{T_N}7/N\,ds=o_{\mathbb P}(1)\). Applying the second inequality in (1) to the nonnegative process \(NC/L^2\), after multiplication by \(\exp[-\int(c+7/N)ds]\), and optional stopping, gives \(NC_{T_N}/L_{T_N}^2=O_{\mathbb P}(1)\). Thus \(C_{T_N}=O_{\mathbb P}(N^{1/3})=o_{\mathbb P}(\sqrt N)\). The probability of an exceptional stop goes to zero upon taking first \(N\to\infty\), then \(T\to\infty\).

In particular, at most \(C_{T_N}\) later changes of \(D\) are possible; hence \((D_{\mathrm{jam}}-D_{T_N})/\sqrt N\to0\) in probability.

**4. Stopped martingale central limit theorem.** Define
\[
Q_N(s)=\exp\left(\int_0^{s\wedge T_N}c(u)du\right),\qquad
M_N(s)=\frac{Q_N(s)D_{s\wedge T_N}}{\sqrt N}.
\]
This is a martingale (the initial value is zero), with bracket
\[
\langle M_N\rangle_{T_N}
=\int_0^{T_N}Q_N(s)^2(a(s)+b(s))c(s)ds.
\]
The preceding cutoff estimate implies \(Q_N(T_N)\to e^{\gamma/\alpha}\). On fixed intervals the bracket converges by the fluid limit; its remaining part is negligible because each cross-to-\(C\) jump consumes one of the \(C_T\) remaining vertices and \(C_T/N\to c(T)\to0\). Therefore the bracket tends to
\[
V=2\alpha\gamma\int_0^{1/\alpha}(1-\alpha u)e^{\gamma u}\,du.
\]
Jump sizes are at most \(Q_N(T_N)/\sqrt N=o_{\mathbb P}(1)\), so the martingale central limit theorem yields \(M_N(T_N)\Longrightarrow\mathcal N(0,V)\). Multiplying by \(Q_N(T_N)^{-1}\), then using the terminal cutoff and taking absolute values, proves the folded-normal claim, with variance \(e^{-2\gamma/\alpha}V\), algebraically equal to the displayed \(\sigma_\alpha^2\).

Finally \(\mathcal L_N D^2\le(A+B)c\). Since cross-to-\(C\) edges use at most \(C_0\) vertices, optional stopping gives \(\mathbb E D_{\mathrm{jam}}^2/N\le C_0/N\). This uniform second-moment bound implies uniform integrability of \(U_N/\sqrt N\) and convergence of its mean. No convergence of second moments is asserted.

## Verification
The accompanying `verify.py` enumerates exact small-graph absorption probabilities from the four-state jump chain and compares them with independent uniform-priority edge permutation enumeration; it also checks the rational generator inequalities, the fluid first integrals, and the folded-normal variance integral. Seeded finite-size simulations independently check the limiting magnitude. Finite enumeration is not a substitute for the all-size martingale proof.

## Relationship to prior work
Classical work by Pippenger (1989), Dyer and Frieze (1991), and Gamarnik and Goldberg (arXiv:0807.1277v1, 2008) studies greedy matching/adsorption in other graph regimes; in particular the 2008 full text concentrates on bounded-degree high-girth graphs and its concentration theorem assumes bounded degree. The present graph is dense and highly inhomogeneous. The known complete-split and fixed-number-of-partite-classes fluid laws concern *macroscopic* unmatched proportions, and their limiting laws do not determine this balanced, square-root-scale terminal distribution. The source comparisons do not establish priority over all unindexed literature.

## Limitations
The result concerns two exactly equally sized independent reservoirs; a nonzero order-\(\sqrt N\) imbalance is not included. It does not address other edge-priority distributions lacking independent identical continuity or the time-dependent physical deposition rate. The complete 1991 primary paper was not accessible for line-by-line examination; overlap with older special dense-graph studies cannot be categorically excluded. Independent assessment has not been performed.

## References
1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277v1 (public 2008-07-08), Sections 1–3 and the regular-tree comparisons.
2. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45, doi:10.1002/rsa.3240020104 (metadata/abstract consulted; full text unavailable).
3. N. Pippenger, *Random sequential adsorption on graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, doi:10.1137/0402034 (repository abstract consulted; full text unavailable).
