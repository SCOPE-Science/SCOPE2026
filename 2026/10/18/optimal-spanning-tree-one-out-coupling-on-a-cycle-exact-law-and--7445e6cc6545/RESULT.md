# Optimal spanning-tree/one-out coupling on a cycle: exact law and Poisson–Gaussian regimes

## Finding
Let \(C_n\) be the simple cycle with \(n\ge3\) labeled edges, and let \(T_n\) be its uniform spanning tree. For any rotation-invariant random edge subset \(S\subseteq E(C_n)\), write \(M=|E(C_n)\setminus S|\). Among **all couplings** having the prescribed marginals for \(S\) and \(T_n\), the edge symmetric-difference distance \(\Delta=|S\triangle E(T_n)|\) is stochastically minimized by a coupling with
\[
\Delta=|M-1|\quad\text{almost surely}.
\]
In particular the exact unnormalized Hamming-\(1\)-Wasserstein distance is \(\mathbb E|M-1|=\mathbb EM-1+2\Pr(M=0)\), and the minimum of \(\mathbb E\varphi(\Delta)\) for every nondecreasing \(\varphi\) is \(\mathbb E\varphi(|M-1|)\).

Specialize to the independent one-out model in which vertex \(i\) chooses its clockwise neighbor with probability \(p\in(0,1)\), and its counterclockwise neighbor with probability \(q=1-p\), independently at all vertices; \(S\) is the undirected union of the selected edges. For every \(n\ge3\), the sharp expected distance is
\[
\boxed{W_{n,p}=npq-1+2(p^n+q^n).}
\]
The full optimal-distance law is the pushforward of the following exact missing-edge distribution under \(k\mapsto |k-1|\):
\[
\Pr(M=0)=p^n+q^n,
\qquad
\Pr(M=k)=\frac nk\sum_{a=k}^{n-k}\binom{a-1}{k-1}\binom{n-a-1}{k-1}p^a q^{n-a}
\quad(1\le k\le\lfloor n/2\rfloor).
\]
At \(p=1/2\), this simplifies to \(\Pr(M=k)=2^{1-n}\binom n{2k}\) for all \(0\le k\le\lfloor n/2\rfloor\). The maximum probability of an *exact match* \(S=E(T_n)\) under any coupling equals \(\Pr(M=1)\).

The law has two different asymptotic fluctuation regimes. For each fixed \(p\in(0,1)\), putting \(\mu=p(1-p)\),
\[
\frac{\Delta-n\mu}{\sqrt n}\ \Longrightarrow\ N(0,\mu(1-3\mu)).
\]
If instead \(p=p_n\to0\) with \(np_n\to\lambda\in[0,\infty)\), then
\[
\Delta\ \Longrightarrow\ |\operatorname{Pois}(\lambda)-1|,
\qquad \Pr(\Delta=0)\to\lambda e^{-\lambda}.
\]
The same assertion holds if \(p_n\to1\) and \(n(1-p_n)\to\lambda\). The unbiased specialization \(p=1/2\) is the usual uniform-neighbor one-out process; other \(p\) describe a rotation-invariant directional bias.

## Assumptions and scope
A spanning tree of \(C_n\) is obtained by deleting exactly one edge. The uniform law chooses that deleted edge uniformly among the \(n\) edges. Rotation invariance of \(S\) means its distribution is unchanged by cyclic shifts of edge labels; independence is **not** required for the general optimal-coupling statement. The one-out probabilities \(p,q\) are identical at each vertex, with vertex choices mutually independent. Distances count undirected edges belonging to exactly one set. The Wasserstein cost here is unnormalized symmetric-difference cardinality; divide \(W_{n,p}\) by \(n\) for the normalized Hamming metric.

## Proof
**Universal optimal coupling.** Let \(J\) denote the edge omitted by the spanning tree, and let \(A=E(C_n)\setminus S\) have size \(M\). As \(E(T_n)=E(C_n)\setminus\{J\}\), a direct set identity gives
\[
|S\triangle E(T_n)|=|A\triangle\{J\}|=
\begin{cases}
M-1,&J\in A,\\
M+1,&J\notin A.
\end{cases}
\]
If \(M=0\), this distance is necessarily \(1\); for \(M\ge1\), it is at least \(M-1\). Thus every possible coupling has \(\Delta\ge |M-1|\) pointwise. To attain equality, first sample \(S\) from its prescribed law. Conditional on \(S\), choose \(J\) uniformly from \(A\) if \(A\ne\varnothing\), otherwise uniformly among all cycle edges. This conditional rule is equivariant under every cyclic rotation. As the law of \(S\) is rotation invariant, \(J\) is rotation invariant, hence uniform among all \(n\) edges. Therefore \(E(C_n)\setminus\{J\}\) has the correct uniform-spanning-tree marginal, while \(\Delta=|M-1|\) pointwise. This proves the asserted stochastic minimality for **every** nondecreasing loss, and the expectation formula follows from \(|M-1|=M-1+2\mathbf{1}_{\{M=0\}}\).

**Missing edges under one-out orientations.** Label vertices cyclically. Let \(\xi_i=1\) mean vertex \(i\) chooses clockwise and \(\xi_i=0\) choose counterclockwise. The edge \(\{i,i+1\}\) is absent precisely when \((\xi_i,\xi_{i+1})=(0,1)\), so
\[
M=\sum_{i=1}^n\mathbf{1}_{\{\xi_i=0,\ \xi_{i+1}=1\}},\qquad \xi_{n+1}=\xi_1.
\]
A cyclic binary sequence has \(M=0\) if and only if it is constant. For \(M=k\ge1\), it has exactly \(k\) clockwise runs and \(k\) counterclockwise runs. If there are \(a\) clockwise choices, their ordered positive run lengths have \(\binom{a-1}{k-1}\) compositions; the other \(n-a\) choices yield \(\binom{n-a-1}{k-1}\) compositions. Mark a transition location and divide by the \(k\) possible marks per sequence to obtain the factor \(n/k\). Weighting by \(p^a q^{n-a}\) and summing proves the exact mass formula. When \(p=q=1/2\), specifying the \(2k\) change-point edges and one starting sign gives \(2\binom n{2k}\) equally likely configurations, also for \(k=0\).

Each missing-edge indicator has mean \(\mu=pq\), hence \(\mathbb EM=n\mu\). The two indicators sharing a vertex cannot both be one, so their covariance is \(-\mu^2\); nonneighboring indicators are independent. Every indicator has precisely two neighbors on a cycle of length \(n\ge3\). Therefore
\[
\operatorname{Var}(M)=n[\mu(1-\mu)-2\mu^2]=n\mu(1-3\mu).
\]
The constant-string probability is \(p^n+q^n\). Insert these identities in the universal expectation formula to obtain \(W_{n,p}\).

**Limits.** For fixed \(p\), the centered indicator sequence is stationary and \(1\)-dependent with positive asymptotic variance \(\mu(1-3\mu)>0\). The standard central limit theorem for bounded stationary \(1\)-dependent sequences, applied on a line, gives the displayed normal limit: the cyclic wrap term changes the line sum by at most \(1\). Because \(\Pr(M=0)=p^n+q^n\to0\), \(\Delta=M-1\) with probability tending to one and has the same centered \(\sqrt n\)-limit.

If \(p_n\to0\) and \(np_n\to\lambda<\infty\), the number \(N_n=\sum_i\xi_i\) of rare clockwise choices is \(\operatorname{Bin}(n,p_n)\), and \(N_n\Longrightarrow\operatorname{Pois}(\lambda)\). Except on the event of some cyclically adjacent clockwise choices, every clockwise symbol forms exactly one \((0,1)\) transition and hence \(M=N_n\); the exceptional probability is at most \(np_n^2\to0\), plus the negligible all-clockwise event. Thus \(M\Longrightarrow\operatorname{Pois}(\lambda)\) and \(\Delta=|M-1|\) has the asserted limit. The case \(p_n\to1\) follows by interchanging clockwise and counterclockwise orientations. Point probabilities also converge because the variables are integer-valued; in particular \(\Pr(M=1)\to\lambda e^{-\lambda}\). Finally, \(\Delta=0\) requires \(M=1\), since the universal pointwise bound is necessary and achieved by the stated coupling.

## Verification
A standalone exact-rational Python program enumerates every orientation word for \(3\le n\le10\) and four rational biases. It checks the conditional coupling's uniform omitted-edge marginal, optimal distance for every conditional pair, the entire run-count mass formula, the mean and variance identities, and the unbiased even-binomial simplification. It completed \(19{,}304\) exact rational assertions without failure. The universal statements and asymptotic limits rely on the analytical proof above, not on finite enumeration.

## Relationship to prior work
Mészáros and Peled (2026, arXiv:2610.11554v1, Theorem 1) construct couplings between uniform spanning trees and uniform-neighbor one-out graphs on any connected graph of minimum degree \(k\ge2\), with expected normalized symmetric-difference distance bounded by \(O(\log k/\sqrt{k})\). Their Section 3.1 uses an entropy comparison and Marton's coupling, and their Theorem 2 concerns local rooted neighborhoods. Their theorem applies to cycles with \(k=2\), but provides neither the cycle's **exact optimal** transportation cost nor its optimal-distance distribution or directional-bias crossover. The present result is an exact sparse-degree specialization and an independent extension to rotation-invariant input edge-set laws; it does not improve the high-degree uniform graph theorem.

Circular Bernoulli run-count identities have an earlier literature, including Makri and Philippou (1994) and Koutras, Papadopoulos, and Papastavridis (1995). The cyclic compositions and their Poisson asymptotics are **not claimed as new in isolation**. The claim concerns their combination with an optimal, marginal-preserving coupling of uniform spanning trees to one-out edge sets, yielding exact Wasserstein cost, a sharp stochastic comparison for every increasing loss, and the resulting two regimes. General graph-optimal-transport formulations and other spanning-tree overlap optimizations do not directly identify this cross-law cycle coupling.

## Limitations
The general optimality mechanism relies on transitivity of the cycle's rotations on edges and the fact that every spanning tree deletes one edge; it does not solve optimal coupling on arbitrary graphs. The biased model is not uniform-neighbor one-out unless \(p=1/2\). The fixed-bias Gaussian and rare-bias Poisson limits do not provide rates, and no statement is asserted for more general varying-bias intermediate regimes. The prior-art comparison supports originality against the inspected sources, not universal publication priority. Independent external validation has not been performed.

## References
- A. Mészáros and Y. Peled, *Product approximations for uniform spanning trees and determinantal processes*, arXiv:2610.11554v1 (first public 2026-10-08), especially Theorem 1 and Section 3.1. https://arxiv.org/pdf/2610.11554v1
- F. S. Makri and A. N. Philippou, *Binomial Distributions of Order K on the Circle*, in *Runs and Patterns in Probability* (1994), pp. 65–81. https://doi.org/10.1007/978-1-4613-3635-8_5
- M. V. Koutras, G. K. Papadopoulos and S. G. Papastavridis, *Runs on a Circle*, *Journal of Applied Probability* 32 (1995), 396–404. https://doi.org/10.2307/3215295
- N. Albin, J. Clemens, D. Hoare, P. Poggi-Corradini, B. Sit and S. Tymochko, *Fairest edge usage and minimum expected overlap for random spanning trees*, *Discrete Mathematics* 344 (2021), Article 112282. https://doi.org/10.1016/j.disc.2020.112282
