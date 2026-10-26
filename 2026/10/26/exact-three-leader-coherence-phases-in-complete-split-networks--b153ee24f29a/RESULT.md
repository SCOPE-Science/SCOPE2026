# Exact three-leader coherence phases in complete split networks

## Finding
Let \(G_{r,m}=K_r\vee\overline{K_m}\) be the unweighted complete split graph, with \(r\ge4\) clique vertices and \(m\ge3\) mutually nonadjacent peripheral vertices. Exactly three distinct vertices are designated noise-free leaders. For any leader set \(S\), let \(L_{FF}\) denote the principal submatrix of the combinatorial Laplacian obtained by retaining the follower vertices, and define the unnormalized coherence \(J(S)=\operatorname{tr}(L_{FF}^{-1})\).

Write \(a=|S\cap K_r|\), the number of leaders selected from the clique. Every optimal leader set has an allocation \(a\) in the following **complete and exact** phase table; conversely, **every** choice of three distinct leaders with one of the listed allocations is optimal.

| Peripheral count | Clique count | Exactly optimal allocations \(a\) |
| --- | --- | --- |
| \(m=3\) | \(r\ge4\) | \(0\) |
| \(m=4\) | \(4\le r<20\) | \(0\) |
| \(m=4\) | \(r=20\) | \(0,3\) |
| \(m=4\) | \(r>20\) | \(3\) |
| \(m=5\) | \(4\le r<10\) | \(0\) |
| \(m=5\) | \(r=10\) | \(0,3\) |
| \(m=5\) | \(r>10\) | \(3\) |
| \(m=6\) | \(4\le r<6\) | \(0\) |
| \(m=6\) | \(r=6\) | \(0,2,3\) |
| \(m=6\) | \(r>6\) | \(3\) |
| \(m\ge7\) | \(4\le r<6\) | \(2\) |
| \(m\ge7\) | \(r=6\) | \(2,3\) |
| \(m\ge7\) | \(r>6\) | \(3\) |

For \(a\in\{0,1,2,3\}\), set \(u=r-a\), \(v=m-3+a\). The exact objective is
\[
J_a=\frac{u-1}{r+m}+\frac{v-1}{r}+\frac{r+m+a}{3r+a(m-3)+a^2}.
\]
This formula is also valid at \(v=0\) by cancellation; in that case it reduces to \((u-1)/(r+m)+1/(m+a)\). Thus \(J_{\min}=\min_{0\le a\le3}J_a\), with the minimizing indices completely resolved in the table. The exact number of optimal three-vertex subsets is
\[
\sum_{a\in A_{r,m}}\binom ra\binom m{3-a},
\]
where \(A_{r,m}\) is the table entry for \((r,m)\). There are no other tie parameters.

## Assumptions and scope
All edges have unit conductance, there are no peripheral-to-peripheral edges, all \(r+m\) vertices are distinguishable, and there are exactly three **noise-free** leaders. Here \(r\) and \(m\) are integers with \(r\ge4\), \(m\ge3\). Follower disturbances are independent with equal intensities; the standard total stationary variance for unit-intensity continuous-time white noise is \(J/2\). Minimizers are unchanged by this factor. Neither other leader budgets nor weighted edges are covered.

## Proof
**Symmetry reduction and exact objective.** Permutations of the clique and of the independent vertices act transitively on three-leader sets with a fixed allocation \(a\). Because \(r\ge4\), at least one clique follower remains: \(u=r-a\ge1\). The grounded Laplacian, in clique-follower/peripheral-follower order, is
\[
L_{FF}=\begin{pmatrix}(r+m)I_u-\mathbf1_u\mathbf1_u^{\mathsf T}&-\mathbf1_u\mathbf1_v^{\mathsf T}\\
-\mathbf1_v\mathbf1_u^{\mathsf T}&rI_v\end{pmatrix}.
\]
When \(v\ge1\), the clique-sum-zero eigenspace has eigenvalue \(r+m\) with multiplicity \(u-1\), and the peripheral-sum-zero eigenspace has eigenvalue \(r\) with multiplicity \(v-1\). On normalized class indicators, the remaining symmetric block is
\[
B=\begin{pmatrix}m+a&-\sqrt{uv}\\-\sqrt{uv}&r\end{pmatrix},\qquad
\det B=r(m+a)-uv=3r+a(m-3)+a^2>0.
\]
Its inverse trace is \((r+m+a)/\det B\), giving the displayed \(J_a\). For \(v=0\), direct diagonalization yields \((u-1)/(r+m)+1/(m+a)\), the same rational expression. This proves that four values exhaust all leader choices and establishes the formula at every boundary.

**Finite peripheral counts.** All denominators below are strictly positive in the stated domain. For \(m=3\), direct simplification gives
\[
J_1-J_0=\frac{2(r+15)}{3(r+3)(3r+1)},\quad
J_2-J_0=\frac{2(r^2+24r+18)}{3r(r+3)(3r+4)},\quad
J_3-J_0=\frac6{r(r+3)}.
\]
All three are positive.

For \(m=4\), the differences \(J_1-J_0=(r^2+32r-8)/[3r(r+4)(3r+2)]\) and \(J_2-J_0=16(r+1)/[3r(r+2)(r+4)]\) are positive, while
\[
J_3-J_0=\frac{20-r}{3r(r+4)}.
\]
If \(r\ge20\), the additional exact comparisons \(J_1-J_3=2(r-8)(2r+3)/[3r(r+4)(3r+2)]>0\) and \(J_2-J_3=(r-6)/[3r(r+2)]>0\) establish the winner and the unique tie at \(r=20\).

For \(m=5\), \(J_1-J_0=10(r-1)/[3r(r+1)(r+5)]>0\), and
\[
J_2-J_0=\frac{-2(r^2-20r-20)}{3r(r+5)(3r+8)},\qquad
J_3-J_0=\frac{-2(r-10)}{3r(r+5)}.
\]
For \(4\le r\le10\), \(J_2-J_0>0\). For \(r\ge10\), \(J_1-J_3=2(r^2-4r-15)/[3r(r+1)(r+5)]>0\) and \(J_2-J_3=4(r-6)/[3r(3r+8)]>0\). Hence the stated unique tie at \(r=10\).

For \(m=6\), the exact comparisons are
\[
J_1-J_0=\frac{-(r^2-24r+72)}{3r(r+6)(3r+4)},\quad
J_2-J_0=\frac{-4(r-6)}{3(r+6)(3r+10)},\quad
J_3-J_0=\frac{-(r-6)}{r(r+6)}.
\]
For \(4\le r\le6\), the first is strictly positive and the other two are nonnegative, with equality in the latter two exactly at \(r=6\). For \(r\ge6\), \(J_1-J_3=2(4r^2-9r-72)/[3r(r+6)(3r+4)]>0\) and \(J_2-J_3=5(r-6)/[3r(3r+10)]\ge0\); comparison with \(J_0\) above completes this case.

**All \(m\ge7\).** Put \(P=r-4\ge0\) and \(Q=m-7\ge0\). Clearing the strictly positive denominators gives
\[
J_0-J_2=\frac{2N_{02}}{3r(r+m)(3r+2m-2)},\qquad
J_1-J_2=\frac{N_{12}}{r(r+m)(3r+m-2)(3r+2m-2)},
\]
where the numerator polynomials have the explicit positive-coefficient expansions
\[
\begin{aligned}
N_{02}&=P^2(Q+3)+P(2Q^2+22Q+24)+Q^3+22Q^2+127Q+90,\\
N_{12}&=P^3(Q+4)+P^2(2Q^2+28Q+64)\\
&\quad+P(Q^3+28Q^2+211Q+320)+2Q^3+44Q^2+246Q+92.
\end{aligned}
\]
Thus both \(J_0\) and \(J_1\) are strictly worse than \(J_2\). The remaining comparison is
\[
J_2-J_3=\frac{(r-6)(m-1)}{3r(3r+2m-2)},
\]
which is negative when \(r<6\), zero at \(r=6\), and positive when \(r>6\). This yields exactly the claimed alternatives and proves there are no other optimal allocations or ties.

## Verification
The standalone `verify.py` uses exact symbolic rational simplifications to check the difference identities and the two positive-coefficient certificates. It evaluates \(45{,}746\) parameter pairs with exact rational arithmetic and compares \(140\) small instances against direct exact grounded-Laplacian inverses built independently from adjacency. Its recorded output is in `verification_output.txt`. The analytical proof above, rather than these finite checks, establishes the universally quantified phase classification.

## Relationship to prior work
Fitch and Leonard introduced the joint-centrality framework for selecting noise-free leaders to minimize variance on arbitrary connected graphs and solved particular path/cycle cases [1]. Patterson, Yi and Zhang extended resistance-distance treatments to selected graph classes, including cycles, paths and trees [2]. The complete split graph is also a complete multipartite graph with one nonsingleton part and the remaining parts singleton, as well as a threshold graph. The present result does not claim the general coherence objective, the grounded-inverse formula, graph symmetry reduction, or general algorithms as new. It provides an exact phase diagram and complete optimizer/tie classification for **three** leaders on unweighted split networks, beyond the separately examined two-leader split-network problem. The related three-leader calculation on complete bipartite graphs concerns a different edge set and does not imply the split-network thresholds \(20\), \(10\), and \(6\).

## Limitations
The classification assumes a complete unit-conductance clique, complete unit-conductance clique-to-periphery connections, independent peripheral vertices, exactly three noise-free leaders, and \(r\ge4,m\ge3\). It does not imply comparable thresholds for finite leader measurement gains, noise-corrupted leaders, other leader counts, or nonuniform conductances. Searches and source inspections do not establish mathematical uniqueness in the wider literature; specialized work not found by the searches may overlap. 

## References
[1] K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (initial public version 2014-07-07), https://arxiv.org/abs/1407.1569.

[2] S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017), https://arxiv.org/abs/1708.06873.
