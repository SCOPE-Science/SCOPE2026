# Sharp \(2/n\) rare-jamming law for random dimers on crown graphs

## Finding
For every integer \(n\ge2\), let \(G_n\) be the crown graph obtained from the complete bipartite graph on vertex sets \(\{a_i:1\le i\le n\}\) and \(\{b_i:1\le i\le n\}\) by deleting exactly the diagonal edges \(a_ib_i\). Independently assign every surviving edge a continuous random priority, and irreversibly deposit a dimer on that edge, in priority order, precisely when both endpoints remain vacant. Let \(P_n\) be the probability of incomplete final coverage, and set \(H_{n-1}=\sum_{j=1}^{n-1}1/j\).

**Theorem.** The jammed state contains either no vacancies or exactly two, the latter being the two endpoints of one deleted diagonal edge. For all \(n\ge2\),
\[
\max\!\left\{0,\frac{2}{n+1}-\frac{4H_{n-1}}{n(n+1)}\right\}
\le P_n\le\frac{2}{n+1}.
\]
In particular,
\[
0\le\frac2n-P_n\le\frac{2+4H_{n-1}}{n(n+1)},
\qquad\lim_{n\to\infty}nP_n=2.
\]
The expectation of the number of empty sites is \(2P_n\); its expected fraction of empty sites is \(P_n/n\sim2/n^2\). One has \(P_2=0\) and \(P_n>0\) for \(n\ge3\).

## Assumptions and scope
This concerns an unweighted, finite graph with exactly \(n(n-1)\) permitted edges, one forbidden perfect matching, independent continuous random edge arrival times and irreversible two-site adsorption. There is no desorption, diffusion or resampling of previously rejected edges. Uniform random edge permutations and independent continuous priorities induce the same law. The event of jamming without perfect coverage is an event about the *greedy adsorption process*, not nonexistence of a perfect matching: for \(n\ge2\) the crown graph does have perfect matchings.

## Proof
At any intermediate stage the unoccupied index sets on the left and right are \(A_k,B_k\subseteq\{1,\ldots,n\}\), both of cardinality \(k\). Write \(T_k=|A_k\cap B_k|\). Initially \(T_n=n\). Every available edge connects one index in \(A_k\) to a **different** index in \(B_k\), so there are \(k^2-T_k\) eligible edges. The next accepted edge is uniform among these, by the uniform random order of the still-eligible edges.

For \(k\ge2\), since \(0\le T_k\le k\), at least one edge is eligible. Hence adsorption always continues until \(k=1\), where it succeeds exactly when the two remaining indices are different. Thus \(P_n=\Pr(T_1=1)=\mathbb E[T_1]\). Removal of one left and one right index gives, conditionally on \(T_k=t\),
\[
\begin{aligned}
\Pr(T_{k-1}=t-2\mid T_k=t)&=\frac{t(t-1)}{k^2-t},\\
\Pr(T_{k-1}=t-1\mid T_k=t)&=\frac{2t(k-t)}{k^2-t},\\
\Pr(T_{k-1}=t\mid T_k=t)&=\frac{(k-t)^2}{k^2-t}.
\end{aligned}
\]
Terms with zero numerators are interpreted as zero. This also supplies an exact finite-state recursion for \(P_n\).

The first conditional moment is
\[
\mathbb E[T_{k-1}\mid T_k=t]
=t\left(1-\frac{2(k-1)}{k^2-t}\right)
=\frac{k-1}{k+1}t-\frac{2t(t-1)}{(k+1)(k^2-t)}.
\]
Introduce \(m_k=\mathbb E[T_k]/[k(k+1)]\). For \(2\le k\le n\), this gives the exact defect identity
\[
m_k-m_{k-1}=
\frac{2}{(k-1)k(k+1)}
\mathbb E\left[\frac{T_k(T_k-1)}{k^2-T_k}\right]\ge0.
\tag{1}
\]
In particular, \(m_n=1/(n+1)\), \(m_1=P_n/2\), so \(P_n\le2/(n+1)\).

For a bound on the defect in (1), use the falling factorial \((t)_2=t(t-1)\). If two prescribed common indices are to remain common after one adsorption event, the selected edge must avoid their two left and two right endpoints. Precisely \(4k-6\) of the \(k^2-t\) eligible edges meet this set. Thus
\[
\mathbb E[(T_{k-1})_2\mid T_k=t]
=(t)_2\left(1-\frac{4k-6}{k^2-t}\right).
\]
For \(t\ge2\) this factor is at most \((k-2)^2/(k^2-2)\), which is at most \((k-2)(k-1)/[k(k+1)]\) for \(k\ge2\). The second inequality follows after clearing positive denominators from the identity \((k-1)(k^2-2)-k(k+1)(k-2)=2\). For \(t<2\), the falling factorial vanishes, so the same upper bound holds. Iterating from \(\mathbb E[(T_n)_2]=n(n-1)\) yields, for \(2\le k\le n\),
\[
\mathbb E[(T_k)_2]\le\frac{k^2(k^2-1)}{n(n+1)}.
\tag{2}
\]
Because \(T_k\le k\), one has \(k^2-T_k\ge k(k-1)\), and (1) and (2) imply
\[
0\le m_k-m_{k-1}
\le\frac{2\,\mathbb E[(T_k)_2]}{(k-1)^2k^2(k+1)}
\le\frac{2}{n(n+1)(k-1)}.
\]
Summing from \(k=2\) through \(n\) shows
\[
0\le\frac1{n+1}-\frac{P_n}{2}
\le\frac{2H_{n-1}}{n(n+1)},
\]
which proves both finite-size bounds and the \(2/n\) asymptotic. Exactly two sites are vacant on failure, so the coverage statements follow. For \(n=2\), two disjoint edges are necessarily accepted. For \(n\ge3\), a permissible matching among the first \(n-1\) index pairs can be chosen as a derangement of those \(n-1\) labels, leaving the same index free on both sides; the corresponding accepted-edge order has positive probability and jams with two vacancies. \(\square\)

## Verification
The standalone standard-library checker `verify_crown_jamming.py` independently computes the law using all subsets of unmatched left/right vertices for \(n=2,\ldots,7\), and compares it with the reduced two-parameter rational recurrence. It separately enumerates all \(6!=720\) orders of the six edges for \(n=3\), checks the stated finite bounds exactly for \(n=2,\ldots,17\), and verifies the second-factorial-moment inequality on those finite instances. It prints `PASS` on success. These checks only test finite cases; the proof above covers all \(n\ge2\).

## Relationship to prior work
Dyer and Frieze (1991) introduce and analyze random-edge greedy matching on general graphs. Pippenger (1989) treats random sequential adsorption and edge occupation on graphs, chiefly regular graphs with long cycles or restricted short-cycle overlap. Evans (1993) surveys irreversible adsorption and jamming. The present statement isolates a dense, highly four-cycle-rich crown graph and proves its *specific rare failure probability* with an explicit harmonic error, rather than a general approximation ratio or coverage-density limit.

Mendonça (2018), Section 4, studies a sequential importance sampler for derangements in which input rows are processed in a predetermined order. Its transition kernel is different from the present process, which chooses uniformly from **all** currently eligible edges; the fixed-row results do not determine \(P_n\). Other nearby graph results address combinatorial domination on crown graphs and unweighted counts of maximal matchings, not random-priority adsorption probabilities.

## Limitations
This is a strict, unweighted crown-graph theorem. It does not establish the same prefactor for arbitrary dense bipartite defects, nonsymmetric missing edges, preferential edge rates or cooperative adsorption. Literature equivalence under a different formulation remains possible; in particular, accessible publisher descriptions were available for some older general matching papers but their full texts could not be inspected. No independent external scientific audit has been performed.

## References
1. M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* **2** (1991), 29–45. DOI: 10.1002/rsa.3240020104.
2. N. Pippenger, “Random sequential adsorption on graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401. DOI: 10.1137/0402034.
3. J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* **65** (1993), 1281–1329. DOI: 10.1103/RevModPhys.65.1281.
4. J. R. G. Mendonça, “Efficient generation of random derangements with the expected distribution of cycle lengths,” arXiv:1809.04571 (2018), especially Section 4.
