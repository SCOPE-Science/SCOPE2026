# Cover-endpoint tomography of conductance cycles: exact law and inverse rigidity

## Finding

For a reversible nearest-neighbor random walk on a known labelled cycle with arbitrary strictly positive edge conductances, the last newly visited vertex has an explicit two-arc resistance law. Moreover, observing only the probability that the clockwise neighbor is the last new vertex, once for each starting vertex, uniquely identifies all conductances up to a common multiplier. An explicit signed-product inverse, an exact feasibility criterion, a quantitative stability bound, and a rigidity characterization of uniform last coverage follow.

Write \(q_i\) for the probability that a walk starting at \(i\) visits \(i+1\) last, and \(\rho_i\) for the normalized resistance of edge \((i,i+1)\). Then

\[
q_i=\frac{\rho_i}{1-\rho_{i+1}},\qquad
\rho_i=\frac{\sum_{k=0}^{n-1}(-1)^k\prod_{h=0}^k q_{i+h}}{1-(-1)^n\prod_{h=0}^{n-1}q_h}.
\]

All subscripts are modulo \(n\). The inverse is unique for every \(n\ge3\), and the all-start last-vertex distributions are uniform precisely when the edge conductances are constant.

## Assumptions and scope

Fix an integer \(n\ge3\), with vertices \(0,1,\ldots,n-1\) arranged cyclically. Let \(c_i>0\) be the conductance of edge \(e_i=\{i,i+1\}\), and put \(r_i=c_i^{-1}\), \(R=\sum_{i=0}^{n-1}r_i\), and \(\rho_i=r_i/R\). The discrete-time Markov chain jumps according to

\[
P(i,i+1)=\frac{c_i}{c_{i-1}+c_i},\qquad
P(i,i-1)=\frac{c_{i-1}}{c_{i-1}+c_i}.
\]

The cover time \(\tau_{\mathrm{cov}}\) is the first time at which every vertex has been visited, including the initial vertex. The last newly visited vertex is \(J=X_{\tau_{\mathrm{cov}}}\). The chain is irreducible on a finite set, so this time is finite almost surely. We consider known cyclic labels, no self-loops, time-homogeneous jump probabilities, and strictly positive conductances. The overall conductance scale is unidentifiable by any discrete-time path observation.

For any start \(s\) and target \(j\ne s\), set \(L=j+1\), \(H=j-1\), and let \(\mathcal P_j\) be the path from \(L\) clockwise to \(H\) that avoids \(j\). Define \(T_j=R-r_j-r_{j-1}>0\), the total resistance of \(\mathcal P_j\), and \(d_{j,s}\in[0,T_j]\), the total resistance along \(\mathcal P_j\) from \(L\) clockwise to \(s\). Then

\[
\Pr_s(J=j)=\frac{T_j-d_{j,s}}{T_j}\frac{r_j}{T_j+r_j}
+\frac{d_{j,s}}{T_j}\frac{r_{j-1}}{T_j+r_{j-1}}.
\tag{1}
\]

In particular, with \(q_i=\Pr_i(J=i+1)\),

\[
q_i=\frac{r_i}{R-r_{i+1}}=\frac{\rho_i}{1-\rho_{i+1}}\in(0,1).
\tag{2}
\]

Let \(Q=\prod_{i=0}^{n-1}q_i\). The explicit reconstruction is

\[
\rho_i=\frac{\displaystyle\sum_{k=0}^{n-1}(-1)^k\prod_{h=0}^k q_{i+h}}{1-(-1)^nQ}.
\tag{3}
\]

A proposed vector \(q\in(0,1)^n\) is the clockwise-neighbor last-cover probability vector of some positive-conductance cycle if and only if the numbers reconstructed by (3) are all strictly positive and sum to one. In that case the compatible edge conductances are exactly the common positive multiples of \(\rho_i^{-1}\).

For any two realizable data vectors \(q,q'\), with reconstructed vectors \(\rho,\rho'\) and \(q_* = \max_i\max(q_i,q'_i)<1\),

\[
\|\rho-\rho'\|_\infty\le
\frac{\|q-q'\|_\infty}{1-q_*}.
\tag{4}
\]

Finally, the distributions of \(J\) are uniform over all \(j\ne s\), for every starting vertex \(s\), if and only if all \(c_i\) are equal.

## Proof

**Weighted path gambler's ruin.** On a path with positive edge resistances, the probability of hitting its right endpoint before its left endpoint, started at a vertex at resistance distance \(d\) from the left, is \(d/T\), where \(T\) is total path resistance. To check this directly, an interior harmonic function \(h\) satisfies \(c_{i-1}(h_{i-1}-h_i)+c_i(h_{i+1}-h_i)=0\). Hence the increments obey \(c_i(h_{i+1}-h_i)=c_{i-1}(h_i-h_{i-1})\), so increments are proportional to \(r_i\). The two boundary values determine the claimed linear resistance profile.

**Reduction of the last-new-vertex event.** Before \(j\) is visited, the walk lies on the path \(\mathcal P_j\). Because it moves only between neighbors, visiting both endpoints \(L\) and \(H\) before first hitting \(j\) is necessary and sufficient for every other vertex to have been visited. Thus \(J=j\) exactly when the walk reaches both \(L\) and \(H\) before hitting \(j\). Starting from \(s\), it first reaches \(L\) with probability \((T_j-d_{j,s})/T_j\), and first reaches \(H\) with probability \(d_{j,s}/T_j\). Conditional on the first endpoint \(L\), the strong Markov property and weighted gambler's ruin on the path \(j,L,\ldots,H\) give the probability \(r_j/(r_j+T_j)\) of hitting \(H\) before \(j\). Conditional on the first endpoint \(H\), the symmetric path calculation gives \(r_{j-1}/(r_{j-1}+T_j)\). The disjoint alternatives yield (1), including the boundary starts at either endpoint.

**Neighbor probabilities.** For target \(j=i+1\) and start \(s=i=H\), one has \(d_{j,s}=T_j\). Equation (1) becomes \(r_i/(T_j+r_i)=r_i/(R-r_{i+1})\), proving (2). Its strict upper bound follows from the presence of at least one other positive resistance when \(n\ge3\).

**Inverse and feasible data.** Rearrange (2) as \(\rho_i=q_i-q_i\rho_{i+1}\), and iterate it exactly \(n\) times. The right-hand side telescopes into the alternating partial products, while the terminal occurrence of \(\rho_{i+n}=\rho_i\) is multiplied by \((-1)^nQ\). This yields (3). Because \(0<Q<1\), the denominator \(1-(-1)^nQ\) is positive. Uniqueness also follows by subtracting two cyclic solutions: \(\delta_i=-q_i\delta_{i+1}\), so \(\delta_i=(-1)^nQ\delta_i\), and hence \(\delta_i=0\). Necessity of positivity and normalization is clear. Conversely, if (3) gives positive numbers summing to one, then \(\rho_i+\rho_{i+1}<1\) because \(n\ge3\). The defining cyclic equations imply \(q_i=\rho_i/(1-\rho_{i+1})\), so choosing \(c_i\) proportional to \(\rho_i^{-1}\) realizes exactly the stated data. The transition probabilities depend only on conductance ratios, proving identification up to a common scale and no more.

**Stability.** For two realizable inputs, subtract \(\rho_i=q_i(1-\rho_{i+1})\) and \(\rho'_i=q'_i(1-\rho'_{i+1})\) to obtain

\[
|\rho_i-\rho'_i|\le |q_i-q'_i|+q'_{i}|\rho_{i+1}-\rho'_{i+1}|.
\]

Take the maximum over \(i\) and absorb the contraction coefficient \(q_*<1\), proving (4).

**Uniformity rigidity.** If the last-cover distribution is uniform from every start, then \(q_i=1/(n-1)\) for every \(i\). Subtracting the common fixed-point solution of the cyclic recurrence, uniqueness gives \(\rho_i=1/n\), hence every resistance and every conductance is constant. Conversely, when all resistances equal \(r\), one has \(T_j=(n-2)r\) and both conditional hitting factors in (1) equal \(1/(n-1)\); their mixing weights sum to one. Every last-cover probability is therefore \(1/(n-1)\) regardless of the start and target.

## Verification

The included standalone Python checker `checker.py` uses exact rational arithmetic and an independently constructed absorbing Markov-state linear system. That system tracks the two neighbors of a proposed final vertex and computes the probability of visiting both before the target. Across twenty heterogeneous conductance instances of orders three through six, it exactly checks formula (1), normalization, the cyclic inverse, neighbor probabilities, consistency, stability, and constant-weight symmetry. The packaged run passed 801 assertions, including 340 independent first-step hitting-system comparisons. Finite checks do not establish the universal theorem; the proof above does.

For example, for a four-cycle with resistances \((1,1,1,2)\), the clockwise-neighbor last-cover vector is \((1/4,1/4,1/3,1/2)\); the inverse recovers the normalized profile \((1/5,1/5,1/5,2/5)\).

Reproduce with `python3 checker.py`. The expected canonical JSON output is included in `verification_output.json`.

## Relationship to prior work

Idnani and Salem (arXiv:2610.15115, first posted October 10, 2026) derive last-cover probabilities for symmetric and homogeneous biased cycle walks, and present a time-dependent homogeneous bias model. The present statement concerns arbitrarily varying *spatial* conductances with the associated site-dependent reversible transition probabilities, and particularly the inverse identification from one compressed cover endpoint probability per start. Its equal-conductance special case is classical; that special case is not asserted to be new. The accessible abstract of their work does not state this inverse result; the source's complete manuscript was not accessible for definitive appendix-level comparison.

Lovász and Winkler (1993) classify unweighted graphs with uniform last-cover laws, and Buchanan, Horn and Rombach (2022) extend such a graph classification to directed graphs. Those results do not recover weights of a fixed cycle from partial last-coverage data. Blåsten, Isozaki, Lassas and Lu (arXiv:2107.00494, Sections 1 and 4) recover weighted-graph parameters from time-indexed first-passage or heat observations under a geometric condition; those data and hypotheses are different from the present \(n\) scalar cover-endpoint observations, so their recovery theorem does not directly supply the formula or its inverse.

The weighted gambler's-ruin identity is standard and is used as a proof ingredient, not claimed as novel. The proposed contribution is the exact last-cover observable/inverse relationship and its realizability, stability, and rigidity consequences.

## Limitations

The topology and cyclic labelling are assumed known. The data concern independent repeated cover trials from each start, rather than a single observed walk. Uniformly positive *unknown* conductances are recovered only up to scale. No recovery is proved for nonreversible, long-range, directed or time-varying transition rules. The stability constant deteriorates as \(\max_i q_i\) approaches one. No independent historical-priority conclusion follows. The 2026 motivating paper was available by abstract but its full manuscript was inaccessible, leaving a specific residual historical-overlap risk.

## References

1. K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115v1 (2026), https://arxiv.org/abs/2610.15115.
2. L. Lovász and P. Winkler, *A note on the last new vertex visited by a random walk*, Journal of Graph Theory 17 (1993), 593–596, https://doi.org/10.1002/jgt.3190170505.
3. C. Buchanan, P. Horn, and P. Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079 (2022), https://arxiv.org/abs/2209.08079.
4. E. Blåsten, H. Isozaki, M. Lassas, and J. Lu, *Inverse problems for discrete heat equations and random walks for a class of graphs*, arXiv:2107.00494 (2021), https://arxiv.org/abs/2107.00494.
5. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch6.S1.html.
