# Paired Poisson thresholds for random total domination on rook graphs

## Finding

Fix an integer \(r\ge1\) and a real number \(c\). On the square rook graph \(R_N=K_N\square K_N\), independently select every vertex with probability
\[
p_N(c)=\frac{\log N+(r-1)\log\log N+c}{N}.
\]
For sufficiently large \(N\) this probability lies in \((0,1)\). Denote the random selected set by \(S_N\). A set is *total \(k\)-dominating* when each vertex, whether selected or not, has at least \(k\) **other selected neighbors**. Put \(\lambda=e^{-c}/(r-1)!\).

The two consecutive total-domination properties exhibit different limiting probabilities in the *same* sampling window:
\[
\begin{aligned}
\lim_{N\to\infty}\Pr(S_N\text{ is total }(2r-1)\text{-dominating})
 &=2e^{-\lambda}-e^{-2\lambda},\\
\lim_{N\to\infty}\Pr(S_N\text{ is total }2r\text{-dominating})
 &=e^{-2\lambda}.
\end{aligned}
\]
In fact, let \(X_N\) and \(Y_N\) count rows and columns, respectively, containing exactly \(r-1\) selected cells. The pair \((X_N,Y_N)\) converges jointly in law to two **independent** Poisson random variables of mean \(\lambda\). With probability tending to one, the odd requirement succeeds precisely when \(X_N=0\) *or* \(Y_N=0\), whereas the even requirement succeeds precisely when \(X_N=Y_N=0\). Therefore the limiting probabilities of the joint outcomes (both succeed, only odd succeeds, neither succeeds) are
\[
\left(e^{-2\lambda},\ 2e^{-\lambda}(1-e^{-\lambda}),\ (1-e^{-\lambda})^2\right).
\]
The odd-even success-probability gap reaches its possible maximum \(1/2\) at \(\lambda=\log 2\).

The same limits hold when exactly
\[
 m_N(c)=\left\lfloor N\bigl(\log N+(r-1)\log\log N+c\bigr)\right\rfloor
\]
cells are selected uniformly. Consequently, for a uniformly random ordering of the \(N^2\) vertices, if \(T_{k,N}\) is the first number of exposed vertices whose set is total \(k\)-dominating, then
\[
\begin{aligned}
\Pr\!\left(\frac{T_{2r-1,N}-N(\log N+(r-1)\log\log N)}{N}\le c\right)
 &\longrightarrow 2e^{-\lambda}-e^{-2\lambda},\\
\Pr\!\left(\frac{T_{2r,N}-N(\log N+(r-1)\log\log N)}{N}\le c\right)
 &\longrightarrow e^{-2\lambda}.
\end{aligned}
\]
All claims concern fixed \(r\) as \(N\to\infty\). In particular, neither formula is claimed uniformly in a growing domination requirement.

## Assumptions and scope

The vertices of \(R_N\) are pairs \((i,j)\) with \(1\le i,j\le N\). Distinct pairs are adjacent when they share a row or column. The graph product is Cartesian, not categorical. Each vertex has \(2(N-1)\) neighbors. Define \(A_{ij}=\mathbf1_{\{(i,j)\in S_N\}}\), row occupancies \(d_i=\sum_j A_{ij}\), and column occupancies \(e_j=\sum_i A_{ij}\). The number of selected *open* neighbors of \((i,j)\) equals
\[
 d_i+e_j-2A_{ij}.
\]
This standard occupancy identity is not asserted to be new; it is consistent with the rook-graph total-domination formulations in the references. The new assertion is the paired Poisson/odd-even random-placement law and its fixed-budget and hitting-time consequences.

## Proof

**1. Small row and column degrees.** Put \(a=r-1\) and \(\mu_N=Np_N=\log N+a\log\log N+c\). For each fixed nonnegative integer \(j\), a binomial calculation gives
\[
 N\Pr(\operatorname{Bin}(N,p_N)=j)
 =\frac{e^{-c}}{j!}(\log N)^{j-a}(1+o(1)).
\]
Indeed, \(Np_N^2=O((\log N)^2/N)=o(1)\), so the binomial mass is asymptotic to \(e^{-\mu_N}\mu_N^j/j!\). It follows by a union bound that every row and column has at least \(a\) selected cells with probability tending to one. The number of rows of degree \(a+1\) is binomial with mean asymptotic to \(\lambda\log N/(a+1)\) (and likewise for columns); hence each side has at least one degree-\((a+1)\) class member with probability tending to one.

Because different rows are disjoint, \(X_N\) converges marginally to Poisson\((\lambda)\). The same is true of \(Y_N\). Their *joint* convergence requires accounting for row/column crossings. For any fixed collection of \(s\) rows and \(t\) columns, condition on the \(st\) intersection cells. If they are all absent, the remaining selected counts across these rows and columns are independent binomials on \(N-t\) and \(N-s\) trials; their degree-\(a\) probabilities are each asymptotic to \(q_N=\Pr(\operatorname{Bin}(N,p_N)=a)\). A prescribed crossing is occupied with probability \(p_N=O(\log N/N)\), and imposing that crossing while retaining total degree \(a\) changes the corresponding row and column degree probabilities by factors \(O(1/\log N)\) each (or makes them zero when \(a=0\)). Since only \(st\) crossings exist, all configurations with an occupied crossing contribute \(o(q_N^{s+t})\). Thus the mixed factorial moments obey
\[
 \mathbb E[(X_N)_s(Y_N)_t]
 =(N)_s(N)_t q_N^{s+t}(1+o(1))\longrightarrow\lambda^{s+t}.
\]
These are exactly the mixed factorial moments of two independent Poisson variables; the standard factorial-moment criterion proves the joint convergence.

**2. Exclusion of the occupied-cell correction.** Call an occupied cell *critical* if its row and column degrees are both at most \(r+1\). Conditional on occupancy of a particular cell, the remaining entries of its row and column are disjoint independent binomial variables on \(N-1\) trials. Therefore the expected number of critical cells is at most
\[
 N^2p_N\Pr(\operatorname{Bin}(N-1,p_N)\le r)^2
 =O_r\!\left(\frac{(\log N)^3}{N}\right)=o(1).
\]
To obtain the bound, use \(\Pr(\operatorname{Bin}(N-1,p_N)\le r)=O_r(\log N/N)\). Markov's inequality excludes critical cells with probability tending to one.

**3. Exact forcing of both truth values on the high-probability event.** Work where all row and column degrees are at least \(a\), where each side possesses a degree-\((a+1)\) class member, and where no occupied cell is critical.

For \(2r\)-total domination, if \(X_N>0\) choose a degree-\(a\) row and any degree-\((a+1)\) column. At their intersection, the open-neighbor count is at most \(a+(a+1)=2r-1\), so the even property fails. The same holds when \(Y_N>0\). Conversely, if \(X_N=Y_N=0\), all rows and columns have degree at least \(r\); every unoccupied cell then has at least \(2r\) selected neighbors. A selected cell could fail only if its row and column degrees sum to at most \(2r+1\), forcing each to be at most \(r+1\). Such a critical cell was excluded. Therefore the even property holds exactly when \(X_N=Y_N=0\).

For \((2r-1)\)-total domination, if both \(X_N,Y_N>0\), intersect a degree-\(a\) row with a degree-\(a\) column. That cell has at most \(2a=2r-2\) selected neighbors, so the odd property fails. If \(X_N=0\), every row has degree at least \(r\) and every column at least \(r-1\). Thus every unoccupied cell meets the odd requirement. A violating occupied cell must have degree sum at most \(2r\), again implying both degrees at most \(r+1\), which was excluded. The same reasoning holds if \(Y_N=0\). Hence the odd property holds precisely when \(X_N=0\) or \(Y_N=0\).

**4. Limits and fixed-size transfer.** The Poisson convergence and the preceding high-probability equivalences yield the probability and joint-outcome formulas. Put \(h_N=\log N+(r-1)\log\log N\). Couple Bernoulli selection at probabilities \((h_N+c\pm\varepsilon)/N\) to the first \(m_N(c)\) members of a uniformly random permutation. At either probability the number selected is binomial with mean \(N(h_N+c\pm\varepsilon)\) and standard deviation \(O(\sqrt{N\log N})=o(N)\). For any fixed \(\varepsilon>0\), with probability tending to one the smaller Bernoulli set is contained in the uniform fixed-size set, itself contained in the larger Bernoulli set. Total \(k\)-domination is monotone under selection of additional vertices. Sandwich the success probabilities and then send \(\varepsilon\downarrow0\) to obtain the fixed-size formulas by continuity. The hitting-time assertions follow because \(T_{k,N}\le m\) exactly when the first \(m\) vertices constitute a total \(k\)-dominating set.

## Verification

The independently programmed open-neighbor predicate in `verify.py` agrees with the row/column occupancy formula for **2,608** exhaustive small-board configurations and eligible domination requirements at orders \(2\) and \(3\). A seeded finite Bernoulli simulation samples boards of orders \(80\) and \(180\) with \(r=1,2\), reporting empirical success frequencies, limiting predictions, and occasional finite-size disagreement with the asymptotic degree-count surrogates. Run `python3 verify.py` with the Python 3 standard library. These tests validate definitions and implementations, **not** the infinite limiting theorems, which are established by the preceding proof. No computational certificate is needed for an unbounded parameter claim.

## Relationship to prior work

Carballosa and Wisby investigate deterministic minimum total \(k\)-domination of Cartesian products of complete graphs, including asymptotics of the *minimum cardinality* at fixed \(k\). Pahlavsay, Palezzato and Torielli likewise use rook occupancies to analyze minimum total \(3\)-domination. These works provide the natural model and already contain the underlying row/column neighbor-count viewpoint; no novelty is claimed for that identity or for their extremal minimum-size results. The new assertions concern independent random placements, **joint** independent-Poisson row/column deficiency counts, an odd/even pair of different limit laws at a common threshold, and uniform-cardinality/hitting-time transfer. Standard Poisson laws for rare low-degree vertices in random graphs provide methodological context, not a direct rook-domination statement. The earlier articles and available mathematical-record searches inspected did not supply the displayed paired law; see the scientific comparison details and access caveats in the accompanying review.

## Limitations

The result assumes a square rook graph, fixed integer \(r\), and a fixed real window parameter \(c\), with \(N\to\infty\). It does not establish an analogous window for rectangular boards whose aspect ratio diverges, or for domination requirement growing with \(N\). The fixed-size law is an asymptotic statement, not a finite-board exact polynomial. Independent publication-priority checking beyond the inspected material may reveal an equivalent theorem formulated as random bipartite incidence domination; related literature in this formulation remains a residual risk.

## References

1. W. Carballosa and J. Wisby, *Total k-domination in Cartesian product of complete graphs*, arXiv:2001.07850, first publicly submitted January 22, 2020; https://arxiv.org/abs/2001.07850 .
2. B. Pahlavsay, E. Palezzato and M. Torielli, *3-Tuple Total Domination Number of Rook's Graphs*, arXiv:1807.08104, 2018; https://arxiv.org/abs/1807.08104 .
3. A. P. Kazemi, B. Pahlavsay and R. J. Stones, *Cartesian product graphs and k-tuple total domination*, arXiv:1509.08208, 2015; https://arxiv.org/abs/1509.08208 .
4. M. A. Henning and A. P. Kazemi, *k-tuple total domination in graphs*, Discrete Applied Mathematics **158** (2010), 1006–1011; https://doi.org/10.1016/j.dam.2010.01.009 .
