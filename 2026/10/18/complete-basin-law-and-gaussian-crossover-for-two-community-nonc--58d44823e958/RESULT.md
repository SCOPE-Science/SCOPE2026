# Complete basin law and Gaussian crossover for two-community nonconsensus majority

## Finding
Let \(K_{m,n}\) be a complete bipartite graph with \(m,n\ge2\). In the synchronous binary nonconsensus opinion (NCO) model with fixed \(0<\varepsilon<1\), agents update by
\[
\sigma_v(t+1)=\operatorname{sign}\left((1+\varepsilon)\sigma_v(t)+\sum_{w\sim v}\sigma_w(t)\right),\qquad \sigma_v(t)\in\{-1,+1\}.
\]
Every initial state enters by time \(t=2\) exactly one of four types: all-plus consensus, all-minus consensus, a frozen nonunanimous fixed configuration, or the bipartition-swapping period-two orbit. A complete criterion and exact basin probabilities follow.

For each integer \(k\ge2\), put
\[
L_k=\left\lfloor\frac{k-2}{2}\right\rfloor,\qquad
H_k=\left\lfloor\frac{k+1}{2}\right\rfloor+1.
\]
Call an initial plus count in a part of size \(k\) **low** if it is at most \(L_k\), **high** if it is at least \(H_k\), and **central** otherwise. The phase diagram for the initial counts in the two parts is:

1. Both central: the original configuration is a frozen nonunanimous fixed point.
2. One low, the other high: the system enters the unique swapping two-cycle, in which one entire part is plus and the other minus, with their signs interchanged at each step.
3. At least one high and neither low: all-plus consensus by the second update.
4. At least one low and neither high: all-minus consensus by the second update.

Under independent initial plus spins with probability \(p\in[0,1]\), define
\[
\ell_k(p)=\sum_{j=0}^{L_k}\binom kj p^j(1-p)^{k-j},\quad
h_k(p)=\sum_{j=H_k}^{k}\binom kj p^j(1-p)^{k-j},\quad
g_k(p)=1-\ell_k(p)-h_k(p).
\]
Writing \(P_2,P_F,P_+,P_-\) respectively for the probability of the swapping cycle, frozen mixed state, plus consensus and minus consensus, the exact finite-size law is
\[
\begin{aligned}
P_2&=\ell_mh_n+h_m\ell_n,\\
P_F&=g_mg_n,\\
P_+&=h_mh_n+h_mg_n+g_mh_n,\\
P_-&=\ell_m\ell_n+\ell_mg_n+g_m\ell_n.
\end{aligned}
\]
All functions on the right are evaluated at \(p\). The four probabilities are disjoint and sum to one.

In particular at \(p=1/2\), set \(c_k=g_k(1/2)\), where
\[
c_k=\begin{cases}
\binom{k}{k/2}2^{-k},&k\text{ even},\\
2\binom{k}{(k-1)/2}2^{-k},&k\text{ odd}.
\end{cases}
\]
Then
\[
P_2=\frac{(1-c_m)(1-c_n)}2,\qquad P_F=c_mc_n,
\]
and \(P_+=P_-=(1-P_2-P_F)/2\). As \(m,n\to\infty\), the four probabilities converge to \((1/2,0,1/4,1/4)\) in the order \((P_2,P_F,P_+,P_-)\), regardless of relative part sizes. More precisely, writing \(\kappa_k=1\) for even \(k\) and \(\kappa_k=2\) for odd \(k\),
\[
P_F\sim\frac{2\kappa_m\kappa_n}{\pi\sqrt{mn}}.
\]
Thus even the leading finite-size correction distinguishes the parity of both communities.

Finally, let \(N=m+n\to\infty\), \(m/N\to\alpha\in(0,1)\), and set \(p_N=1/2+u/\sqrt N\) for any fixed real \(u\), with \(p_N\in[0,1]\) for large \(N\). With \(\beta=1-\alpha\) and the standard normal cumulative distribution function \(\Phi\), the exact critical-window limits are
\[
\begin{aligned}
P_2&\longrightarrow\Phi(2u\sqrt\alpha)\Phi(-2u\sqrt\beta)+\Phi(-2u\sqrt\alpha)\Phi(2u\sqrt\beta),\\
P_+&\longrightarrow\Phi(2u\sqrt\alpha)\Phi(2u\sqrt\beta),\\
P_-&\longrightarrow\Phi(-2u\sqrt\alpha)\Phi(-2u\sqrt\beta),\\
P_F&\longrightarrow0.
\end{aligned}
\]
For fixed \(p>1/2\), plus consensus has probability tending to one; for fixed \(p<1/2\), minus consensus does. This identifies the \(N^{-1/2}\) transition between the two deterministic consensus regimes and a high-probability switching regime.

## Assumptions and scope
The update is deterministic, simultaneous at every integer time, on the simple undirected complete bipartite graph. Each part has at least two vertices. The self-weight is exactly \(1+\varepsilon\) with one shared fixed \(\varepsilon\in(0,1)\). These assumptions implement the self-retention-on-local-tie convention in Equation (1) of Liu, Achterberg and Kooij (2024). The random initial configuration has mutually independent identically distributed spins with plus probability \(p\); randomness is not refreshed during dynamics. There is no claim for asynchronous updating, other self-weights, or arbitrary bipartite graphs. The central-limit statement requires both part sizes growing proportionally to total size. All finite-size formulas include boundary values \(p=0,1\).

## Proof
Let \(b\) be the number of plus spins in the second part of size \(n\). Every vertex in the first part sees the same neighbor spin sum \(d=2b-n\), an integer. If \(d\ge2\), even a vertex currently at minus experiences field \(d-(1+\varepsilon)\ge1-\varepsilon>0\), hence the entire first part becomes plus. If \(d\le-2\), the entire first part becomes minus. If \(-1\le d\le1\), the self-contribution strictly determines the sign and every vertex keeps its spin. These three alternatives are exactly \(b\ge H_n\), \(b\le L_n\), and the central range. The same argument with roles swapped controls the second part. These implications require only \(0<\varepsilon<1\), and never evaluate the sign at zero.

Now classify the two initial part labels. If they are both central, neither part changes and the state is fixed; because a central count is strictly between zero and its part size, this fixed state is mixed. If the first part is high and second low, their first updates make the second all plus and first all minus. Both are then extreme in the opposite directions, so each subsequent update swaps the signs of both parts. The low/high reversed case is symmetric, and these are the only two orientations of one primitive period-two orbit. If there is a high part and no low part, the opposite part becomes all plus after one update, while the first either stays put (central opposite count) or becomes all plus; in the next update the first part also becomes all plus. The low/no-high case is symmetric. These four mutually exclusive cases exhaust the nine ordered pairs of low/central/high labels, proving the complete deterministic classification and the upper bound of two updates. This bound is attained, for example, with \(m=n=4\), initial part counts \((3,2)\): one update is insufficient but two give plus consensus.

For independent initial spins, the two part counts are independent binomial random variables with the given parameters. Taking probabilities of the four disjoint label events yields the four exact expressions. At \(p=1/2\), symmetry identifies low and high mass as \((1-c_k)/2\); the central sets contain exactly one central count if \(k\) is even and two if \(k\) is odd. This proves the displayed central binomial formulas. Stirling's formula gives \(c_k\sim\kappa_k\sqrt{2/(\pi k)}\), yielding the stated leading correction and limiting four-outcome probabilities.

For the critical window, the de Moivre--Laplace triangular-array central limit theorem applied to independent \(\operatorname{Bin}(k,p_N)\) variables gives \(h_m(p_N)\to\Phi(2u\sqrt\alpha)\), \(\ell_m(p_N)\to\Phi(-2u\sqrt\alpha)\), and the analogous limits with \(n\) and \(\beta\). Indeed the standardized cutoff tends to \(-2u\sqrt\alpha\), and the bounded-width central mass tends to zero; endpoint parity does not alter this normal limit. Substitution into the exact finite expressions proves all four limits. If \(p\) is fixed away from \(1/2\), the law of large numbers makes each part's majority sign deterministic, and the same finite formulas give consensus of that sign with probability tending to one. No simulation is used to establish any limit.

## Verification
Run `python verify_nco_biclique.py` with the standard-library Python interpreter. It independently updates the literal \(1+\varepsilon=3/2\) spin rule and detects the eventual orbit for every \(2\le m,n\le7\) and every spin assignment, totaling 63,504 initial assignments. It compares each resulting basin with the paper's count criterion. Separately, for each of the 36 ordered pairs \((m,n)\), it checks exact rational basin probabilities at \(p=2/5\), normalization, and the unbiased swapping formula. All checks passed. The proof, not these finite tests, establishes the general bounds and asymptotics.

## Relationship to prior work
Liu, Achterberg and Kooij (2024), Equation (1), give the synchronous self-inclusive NCO rule and a mean-field treatment for networks with low degree correlation; their article does not supply an exact \(K_{m,n}\) all-state phase diagram or finite-size basin law. The original NCO works of Shao, Havlin and Stanley (2009) and the exact one-dimensional study of ben-Avraham (2011) study other network geometries, not this two-community classification. Fedrigo (2024), Theorem 3, treats complete bipartite graphs but under the threshold protocol game: a neighbor-fraction adoption rule lacking the NCO self-retention term. It therefore does not imply the NCO frozen central-central configurations or their exact probabilities. General results bounding periods of synchronous binary majority dynamics do not identify the present four basin probabilities, parity constants or critical-window law. An analogous classification in another threshold-dynamics literature cannot be ruled out without further review.

## Limitations
Only identical independent initial spin probabilities are used in the displayed distributions (though the deterministic basin criterion holds for every initial configuration). The graph is exactly complete bipartite, not a stochastic block graph. The swapping cycle is a deterministic dynamic attractor and is not stationary convergence of individual spins. The infinite-size limit assumes both parts diverge; the critical-window statement assumes a limiting positive part proportion. No claim of independent verification or comprehensive novelty across all mathematical literature is made.

## References
1. X. Liu, M. A. Achterberg and R. Kooij, *Mean-field dynamics of the non-consensus opinion model*, Applied Network Science **9**, article 47 (2024), first public 20 August 2024, DOI: 10.1007/s41109-024-00656-w. Full open article at https://link.springer.com/article/10.1007/s41109-024-00656-w.
2. J. Shao, S. Havlin and H. E. Stanley, *Dynamic Opinion Model and Invasion Percolation*, Physical Review Letters **103**, 018701 (2009), DOI: 10.1103/PhysRevLett.103.018701.
3. D. ben-Avraham, *Exact solution of the nonconsensus opinion model on the line*, Physical Review E **83**, 050101(R) (2011), arXiv:1101.3447.
4. A. Fedrigo, *End Behavior of the Threshold Protocol Game on Complete and Bipartite Graphs*, Games **15**(6), 41 (2024), DOI: 10.3390/g15060041.
