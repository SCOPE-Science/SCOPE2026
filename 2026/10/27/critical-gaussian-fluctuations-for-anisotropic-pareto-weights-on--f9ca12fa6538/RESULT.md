# Critical Gaussian fluctuations for anisotropic Pareto weights on the range-two line

## Finding

Let the graph have vertex set \(\mathbb Z\) and edges joining vertices at distance one or two. Give each length-one edge an independent Pareto weight with tail \(\Pr(A>x)=x^{-\gamma_1}\) for \(x\ge1\), and each length-two edge an independent Pareto weight with tail \(\Pr(B>x)=x^{-\gamma_2}\) for \(x\ge1\). Assume all edge weights are independent and \(\gamma_1,\gamma_2>0\) satisfy

\[
\gamma_1+2\gamma_2=2.
\]

If \(T_n\) is the minimum total weight of a path from \(0\) to \(n\), and \(v\) is the regenerative time constant defined below, then

\[
\frac{T_n-vn}{\sqrt{n\log n}}\;\Rightarrow\;\mathcal N(0,1)\qquad(n\to\infty).
\]

The limiting variance is exactly one for every point on this critical exponent curve. The curve balances the one nearest-neighbor edge and the two length-two edges in the unique minimum cut across a unit boundary.

## Assumptions and scope

Write \(A_i\) for the weight of edge \(\{i,i+1\}\) and \(B_i\) for the weight of edge \(\{i,i+2\}\). The families \((A_i)_{i\in\mathbb Z}\) and \((B_i)_{i\in\mathbb Z}\) are independent, each family is identically distributed, and

\[
\Pr(A_i>x)=x^{-\gamma_1},\qquad \Pr(B_i>x)=x^{-\gamma_2}\quad(x\ge1).
\]

Let \(T(u,w)\) be the infimum of the sums of edge weights over paths from \(u\) to \(w\), and set \(T_n=T(0,n)\). For a threshold \(a>1\), call \(j\) a pivot if

\[
A_{j-1}<a,\quad A_j<a,\quad B_{j-2}<a,\quad B_j<a,\quad B_{j-1}>2a.
\]

A pivot forces every geodesic crossing from left to right of \(j\) to pass through \(j\): the only length-two bypass, \(\{j-1,j+1\}\), costs more than \(2a\), whereas the two nearest-neighbor edges through \(j\) cost less than \(2a\). The pivot event has positive probability. Pivot trials at sites spaced three apart use disjoint edge sets, so the gaps between pivots have exponential tails.

Let \(\rho_1<\rho_2<\cdots\) be the positive pivots, \(P_i=\rho_{i+1}-\rho_i\), and \(Q_i=T(\rho_i,\rho_{i+1})\). These regenerative blocks are independent and identically distributed. Fix any such threshold; the ratio below is intrinsic because it equals the renewal-reward limit of \(T_n/n\). Define

\[
\mu_P=\mathbb E P_1,\qquad \mu_Q=\mathbb E Q_1,\qquad v=\frac{\mu_Q}{\mu_P}.
\]

The proof below establishes \(\mu_Q<\infty\). The theorem concerns this fixed range-two graph and this independent, length-dependent Pareto family; it does not assert the same conclusion for dependent weights or arbitrary slowly varying tail factors.

## Proof

**1. Critical cut tail.** The edges crossing the boundary between \(u\) and \(u+1\) are exactly

\[
C_u=\bigl\{\{u,u+1\},\{u-1,u+1\},\{u,u+2\}\bigr\},
\]

with one length-one edge and two length-two edges. Hence, for \(x\ge1\),

\[
\Pr\{\min_{e\in C_u}\omega_e>x\}
=x^{-\gamma_1}x^{-2\gamma_2}=x^{-2}.
\]

**2. Weighted separator gap.** Consider any edge set separating a left endpoint window from a right endpoint window in a finite range-two block. It must contain at least one length-one edge and at least two length-two edges, because the nearest-neighbor chain and each of the two parity chains of length-two edges must be cut. If it contains exactly one length-one edge, the nearest-neighbor membership sequence changes only once; separation then requires the two length-two edges crossing that same unit boundary. Thus the only separator with one length-one edge and two length-two edges is a unit cut \(C_u\). Every other separator either has one length-one edge and at least three length-two edges, giving tail exponent at least \(\gamma_1+3\gamma_2=2+\gamma_2\), or at least two length-one edges and two length-two edges, giving exponent at least \(2\gamma_1+2\gamma_2=2+\gamma_1\). Put \(\delta=\min(\gamma_1,\gamma_2)>0\); every non-unit separator therefore has exponent at least \(2+\delta\).

For a block of fixed finite length, the event \(Q_i>x\) forces the set of edges with weight exceeding a fixed fraction of \(x\) to separate its endpoint windows: every simple path in the block has bounded length. If this separating set is not a unit cut, the preceding exponent gap makes its probability \(o(x^{-2})\). If it is a unit cut but one crossing edge is below \((1-\varepsilon)x\), a path using that edge must contain another edge of order \(x\); this also has probability \(o(x^{-2})\). For each edge of a unit cut there is a simple left-to-right path using that edge as its only cut-crossing edge. Consequently, if a unit cut is responsible for \(Q_i>x\) but one of its edges is below \((1-\varepsilon)x\), such a path must use an additional edge of order \(x\). Up to \(o(x^{-2})\), a large block reward is therefore caused by one unit cut whose three crossing edges all exceed \(x\), with an arbitrarily small relative relaxation of the threshold.

Let \(N_x\) count unit cuts with all three crossing edges above \(x\) between consecutive pivots. The stationary renewal identity gives

\[
\mathbb E N_x=\mu_P x^{-2}.
\]

Two adjacent unit-cut events have joint tail exponent \(2\gamma_1+3\gamma_2=2+\gamma_1+\gamma_2>2\); nonadjacent unit cuts use disjoint edges. Thus multiple high cuts contribute \(o(x^{-2})\). Truncating the geometric block length at a sufficiently large constant times \(\log x\) makes the discarded probability \(o(x^{-2})\). For the remaining blocks, the number of separator patterns with fixed counts of length-one and length-two edges grows polynomially in the block length, while their tail exponents grow linearly with those counts. The strict exponent gap therefore makes the sum of non-unit-separator probabilities \(o(x^{-2})\); removing the truncation yields the exact block tail

\[
\Pr(Q_1>x)\sim\mu_P x^{-2}.
\]

In particular, \(\mathbb E Q_1<\infty\), so \(v\) is finite and positive.

**3. Critical normal domain of attraction.** Set \(Y_i=Q_i-vP_i\). Then \(\mathbb E Y_i=0\). Since \(P_i\) has an exponential tail and \(\Pr(Q_i>x)\sim\mu_Px^{-2}\), a sandwich with \(\Pr(vP_i>\varepsilon x)\) shows

\[
\Pr(Y_i>x)\sim\mu_Px^{-2},\qquad
\Pr(Y_i<-x)\le\Pr(vP_i>x).
\]

Therefore the truncated second moment satisfies

\[
H(x):=\mathbb E\bigl[Y_i^2\mathbf 1_{\{|Y_i|\le x\}}\bigr]\sim2\mu_P\log x.
\]

The classical normal-domain-of-attraction criterion for independent identically distributed mean-zero variables now gives

\[
\frac{\sum_{i=1}^{m}Y_i}{\sqrt{m\mu_P\log m}}\Rightarrow\mathcal N(0,1).
\]

The renewal count up to spatial position \(n\) is asymptotic to \(n/\mu_P\); the renewal-index version of the same limit theorem consequently has normalization \(\sqrt{n\log n}\), since

\[
\frac{(n/\mu_P)\mu_P\log(n/\mu_P)}{n\log n}\longrightarrow1.
\]

Finally, the pivot decomposition writes \(T_n\) as the sum of the complete block rewards plus an initial and a terminal residual. The first pivot position and the gap containing \(n\) are tight, and the residual passage time within a tight finite window is tight. Thus

\[
T_n-vn=\sum_{i\le N(n)}Y_i+O_{\Pr}(1),
\]

where \(N(n)/n\to1/\mu_P\) in probability. The residual divided by \(\sqrt{n\log n}\) vanishes in probability. Slutsky's theorem completes the proof.

## Verification

The argument checks the exact unit-cut tail, the positive pivot probability, exponential pivot-gap control, the strict weighted-exponent gap for every non-unit separator, the block-tail constant, and the normalization in the normal domain of attraction. The tail constant \(\mu_P\) cancels against the asymptotic number \(n/\mu_P\) of blocks, producing variance one. No finite simulation is used as evidence for the limiting theorem. The key geometric step is restricted to the range-two graph and the independent length-dependent Pareto laws stated above.

## Relationship to prior work

Dey and Kim, *First-Passage Percolation on Spread-out line graphs: Microscopic Regime* (arXiv:2607.28865), establish a pivot decomposition, an exact one-block tail for identically distributed edge weights, a Gaussian regime above the critical exponent, and a stable regime below it. Their common-edge-law assumption does not include the length-dependent distributions here. The present proof redoes the cut-tail comparison for the range-two graph, where a unit cut has one edge of the first law and two edges of the second law, and derives the critical logarithmic Gaussian normalization.

Ahlberg, *Asymptotics of First-Passage Percolation on One-Dimensional Graphs*, *Advances in Applied Probability* 47 (2015), 182–209, develops regenerative FPP limits for essentially one-dimensional periodic graphs with identically distributed edge weights; its ordinary Gaussian passage-time theorem assumes a finite second moment. It does not cover this anisotropic infinite-variance model. The final probabilistic step is the classical normal-domain-of-attraction theorem for independent sums with slowly varying truncated second moment.

## Limitations

The result is for the range-two line and independent Pareto laws whose exponents lie on \(\gamma_1+2\gamma_2=2\). It does not establish a full stable/Gaussian phase diagram for arbitrary length-dependent exponents, dependent edge weights, slowly varying modifications, other graph ranges, or a functional limit theorem. The anisotropic block-tail estimate is proved from the explicit range-two separator structure; no external independent audit is claimed.

## References

1. P. S. Dey and D. Kim, “First-Passage Percolation on Spread-out line graphs: Microscopic Regime,” arXiv:2607.28865 (first public version: 2026-07-30).
2. D. Ahlberg, “Asymptotics of First-Passage Percolation on One-Dimensional Graphs,” *Advances in Applied Probability* 47 (2015), 182–209. DOI: 10.1239/aap/1427814587.
3. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II, 2nd ed., Wiley, 1971, normal domain of attraction of the Gaussian law.
