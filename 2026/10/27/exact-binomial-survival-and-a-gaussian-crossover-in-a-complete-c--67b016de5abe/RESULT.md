# Exact binomial survival and a Gaussian crossover in a complete competitive ecological sign map

## Finding

Consider the homogeneous, synchronous discrete generalized Lotka–Volterra update with carrying capacity \(\(K=2\)\) on the complete graph with \(n\geq3\) sites. Start every biomass independently and uniformly at \(1\) or \(2\). For \(0<\alpha<1\), set
\[
T_n(\alpha)=(n-1)(\alpha^{-1}-1).
\]
When \(T_n(\alpha)\notin\mathbb Z\), the number \(S_n\) of eventual occupied sites is determined **exactly** by the initial count \(B_n\sim\operatorname{Bin}(n,1/2)\) of sites initially at biomass two:
\[
 S_n=\begin{cases}
 B_n,&B_n>T_n,\\
 n-B_n,&B_n<T_n<n-B_n,\\
 n,&B_n<T_n\text{ and }n-B_n<T_n.
 \end{cases}
\]
Every orbit enters a fixed point or a period-two orbit after at most two updates. In particular, the exact complete-survival probability is
\[
 \Pr(S_n=n)=2^{1-n}+2^{-n}\!\sum_{\substack{1\le k\le n-1\\n-T_n<k<T_n}}\binom nk.
\]
The sum is interpreted as zero if its index set is empty.

There is a **one-sided Gaussian finite-size crossover** at the already-known complete-graph extinction threshold \(\alpha_c=2/3\). For each real \(s\), take
\[
 \alpha_n(s)=\frac{n-1}{\frac32 n-1+s\sqrt n},
 \qquad T_n(\alpha_n)=\frac n2+s\sqrt n.
\]
For all sufficiently large \(n\), these interactions lie in \((0,1)\). Define \(p(s)=\max\{0,2\Phi(2s)-1\}\), where \(\Phi\) is the standard-normal cumulative distribution function. Then, including exceptional values where \(T_n\) is an integer,
\[
 \Pr(S_n=n)\longrightarrow p(s),\qquad
 S_n/n\ \Longrightarrow\ p(s)\,\delta_1+(1-p(s))\,\delta_{1/2},
\]
and
\[
 \lim_{n\to\infty}\mathbb E[S_n/n]=\tfrac12(1+p(s)).
\]
For every fixed \(0<\alpha<2/3\), \(S_n/n\to1\) in probability. For each fixed \(2/3\le\alpha<1\), \(S_n/n\to1/2\) in probability. Thus the thermodynamic occupied fraction has an exact jump from one to one half at the threshold; the Gaussian crossover resolves its finite-size window of order \(n^{-1/2}\).

## Assumptions and scope

The site set is \(\{1,\ldots,n\}\) with every pair linked and no self-loops. For \(x(t)\in\{0,1,2\}^n\), the update is
\[
 x_i(t+1)=x_i(t)+\operatorname{sgn}\left[x_i(t)\left(2-x_i(t)-\frac{\alpha}{n-1}\sum_{j\ne i}x_j(t)\right)\right],
\]
with \(\operatorname{sgn}(0)=0\). Zero is absorbing. Initial abundances are independent with \(\Pr(x_i(0)=1)=\Pr(x_i(0)=2)=1/2\); the dynamic is deterministic thereafter. The exact finite-\(n\) formulas assume the nonresonant condition \(T_n\notin\mathbb Z\). The limiting statements permit resonant parameter values because their contribution is asymptotically negligible. Neither arbitrary graphs nor \(K>2\) are covered.

## Proof

Write \(k\) for the number of sites initially at biomass two, and let \(H\) be these sites, \(L\) their complement. At time zero, every site of \(H\) falls from two to one (every site has a positive neighbor since \(n\ge3\)). A site of \(L\) has total neighboring biomass \(n+k-1\), so its sign of growth is the sign of
\[
1-\alpha\frac{n+k-1}{n-1}.
\]
Under the nonresonance assumption this is positive exactly when \(k<T_n\), and negative exactly when \(k>T_n\).

If \(k>T_n\), every site of \(L\) becomes extinct at the first update, leaving \(k\) sites at one. On this surviving complete graph a site at one grows, since \(1-\alpha(k-1)/(n-1)>0\). If \(k\ge2\), all survivors subsequently alternate between biomass one and biomass two; if \(k=1\), the unique survivor reaches the fixed biomass two. The eventual occupied count is \(k\).

If \(k<T_n\), sites of \(L\) increase from one to two and those of \(H\) decrease from two to one. At the next update each site of \(L\) drops to one. A site of \(H\), now at one, sees neighboring biomass \(2(n-k)+k-1=n+(n-k)-1\), and hence either grows to two when \(n-k<T_n\) or becomes extinct when \(n-k>T_n\). In the first case the initial state is recovered at time two, giving a full-support two-cycle. In the second case only the \(n-k\) sites of \(L\) remain, and they alternate between one and two (as \(n-k\ge2\) in this case). This proves the piecewise formula, including the cases \(k=0\) and \(k=n\), which both yield full survival. It also proves entry into the final orbit by the second update.

Since \(k\) has probability \(2^{-n}\binom nk\), full survival occurs precisely for \(k=0,n\) and the interior integer values strictly between \(n-T_n\) and \(T_n\). Summing their probabilities gives the finite-\(n\) formula.

For the critical scaling, set \(Z_n=(2B_n-n)/\sqrt n\). The binomial central limit theorem gives \(Z_n\Rightarrow N(0,1)\). If \(s>0\), full survival away from the two boundary counts is exactly \(|Z_n|<2s\); if \(s\le0\), the interior full-survival event is empty. The two endpoints contribute \(2^{1-n}\). If \(T_n\) is an integer, only the initial counts \(k=T_n\) and \(k=n-T_n\) can fail the nonresonant case distinction. Their total probability is at most \(2^{1-n}\binom n{\lfloor n/2\rfloor}=O(n^{-1/2})\). Thus the full-survival limit is \(p(s)\) for every real \(s\), regardless of resonances.

On the complementary event, the exact nonresonant survivor count equals either \(B_n\) or \(n-B_n\), so \(|S_n/n-1/2|\le|B_n/n-1/2|\to0\) in probability there. Exceptional boundary events have vanishing probability. This proves the stated weak mixture. Boundedness of \(S_n/n\) then gives convergence of expectations. Finally, for fixed \(\alpha<2/3\), \(T_n/n\to(1-\alpha)/\alpha>1/2\), placing the binomial center in the full-survival interval with exponentially high probability. For fixed \(\alpha>2/3\) the interval is eventually empty and the surviving fraction tends to one half. At equality the center is within \(O(1)\) of the boundary, and the same limit holds.

## Verification

The standalone `verify.py` re-solves the original synchronized update using exact rational arithmetic and enumerates every initial state for \(3\le n\le11\) at nine prescribed rational interaction strengths, skipping only resonant pairs. It checks the predicted occupied-site count, the complete-survival binomial census and eventual fixed/period-two entry after two updates. It reports 25,560 checked initial-state cases. The infinite-population mixture follows from the displayed proof, not from this finite enumeration.

For instance, for \(n=6\) and \(\alpha=3/5\), the threshold is \(T_n=10/3\); exactly the all-one, all-two, and three-two initial groups coexist completely, with probability \((1+20+1)/64=11/32\).

## Relationship to prior work

Sergo, Koller, Erba, and Zdeborová (2026), arXiv:2606.09494v1, introduced this discrete ecological update, proved that symmetric interactions have no cycles longer than two (Appendix C), and determined the thermodynamic complete-graph extinction threshold \(2/3\) for \(\(K=2\)\) using their high-degree theory (Appendix F.2 and Table 1). Those are antecedents, not new claims here. The present result supplies the finite-population conditional survivor law and its exact binomial distribution, and identifies the associated Gaussian transition profile and limiting mixture at the critical scale; neither follows from the value of the thermodynamic threshold alone.

Goles and Olivos (1980, 1981) established general period-at-most-two behavior for symmetric threshold networks. That background does not alone determine the conditional extinction sizes or probabilities in this particular ecological map. Abramson and Zanette (1998) study extinction statistics for continuous competitive systems with random matrices rather than this specific synchronous sign map. A previously documented calculation for the same ecological model on cycle graphs concerns bounded-degree geometries and does not imply the complete-graph binomial law. The relation to all broader threshold-process literature has not been exhaustively settled.

## Limitations

Only the homogeneous complete-graph \(\(K=2\)\) update with initial abundance in \(\{1,2\}\) is treated. Exact finite-size formulas exclude the finitely many tie parameter values for each \(n\); limiting statements do not, as justified in the proof. Results are about deterministic sign updates from random initial states, not demographic noise, continuous gLV solutions, ecological viability under arbitrary heterogeneity, or random sparse graphs. The proof establishes this narrow model's crossover, not a universal scaling law. Historical priority against differently named threshold-network results requires independent review.

## References

1. D. Sergo, C. Koller, V. Erba, L. Zdeborová, *Percolation and clustering in ecological communities: A dynamical theory*, arXiv:2606.09494v1 (first public June 8, 2026), https://arxiv.org/html/2606.09494.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI:10.1016/0012-365X(80)90121-1.
3. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics 3 (1981), 93–105. DOI:10.1016/0166-218X(81)90034-2.
4. G. Abramson and D. H. Zanette, *Statistics of extinction and survival in Lotka–Volterra systems*, Physical Review E 57 (1998), 4572–4577. DOI:10.1103/PhysRevE.57.4572.
