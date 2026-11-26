# One-quarter oscillation basins and a parity fracture in complete split-graph majority dynamics

## Finding

Let \(G_n=K_n\vee\overline{K}_n\), \(n\ge1\), be a labelled complete split graph with a clique \(C\) and an independent set \(I\), each of size \(n\). Under synchronous binary strict-neighbor majority with tie retention, let \(B_n\) count labelled initial configurations that eventually enter an orbit of primitive period two, including those already on such an orbit. Write \(A_n=\sum_{0\le c<n/2}\binom nc\) and \(Q_n=\sum_{0\le c<n/2}\binom nc^2\). Then

\[
B_n=\binom{2n}{n}+A_n^2-Q_n.
\]

For odd \(n\) this is \(4^{n-1}+\tfrac12\binom{2n}{n}\). For even \(n\), writing \(H_n=\binom n{n/2}\), it is \(4^{n-1}-2^{n-1}H_n+\tfrac34 H_n^2+\tfrac12\binom{2n}{n}\). Thus with independent unbiased initial bits,

\[
\Pr(\text{eventual primitive period two})=\frac{B_n}{4^n}=
\begin{cases}
\displaystyle \frac14+\frac{1}{2\sqrt{\pi n}}+O(n^{-3/2}), & n\text{ odd},\\[2mm]
\displaystyle \frac14+\frac{1-\sqrt2}{2\sqrt{\pi n}}+\frac{3}{2\pi n}+O(n^{-3/2}), & n\text{ even}.
\end{cases}
\]

Both subsequences tend to one quarter but approach it from opposite sides for all sufficiently large sizes. The claimed contribution is the closed basin enumeration and its finite-size parity corrections, not the recurrent-state census, the two-round convergence bound, or the general period-two principle.

## Assumptions and scope

All graphs are undirected, simple and loopless. The vertices update simultaneously using the strict majority of their open neighbors, retaining their own bit on a tie. Count labelled configurations, not orbits under graph automorphisms. Primitive period is the least period of the full labelled configuration; a stationary population count need not be a stationary configuration.

## Proof

Let \(c,s\) be the initial numbers of ones on \(C,I\), respectively. A clique vertex of current state \(x\) sees \(c+s-x\) ones among \(2n-1\) neighbors. Independent vertices see all \(n\) clique bits. Consequently the clique becomes all zero if \(c+s<n\), complements all its bits if \(c+s=n\), and becomes all one if \(c+s>n\). Independently, \(I\) becomes all zero if \(2c<n\), is retained if \(2c=n\), and becomes all one if \(2c>n\).

The two configurations with opposite constant shores exchange: the total is \(n\), so the clique flips, and the independent shore copies the old constant clique. If \(c+s>n\), the clique becomes all one. When \(2c<n\), the independent set simultaneously becomes all zero, giving that alternating pair. When \(2c>n\), both become all one. When \(2c=n\), the retained independent word has \(s>n/2\), so its count is positive and the next update gives all-one consensus. Bit complementation gives the corresponding conclusions for \(c+s<n\).

If \(c+s=n\), the endpoints \(c=0,n\) are already on the opposite-shore two-cycle. If \(2c=n\), each independent bit is retained and each clique bit flips at each update, so the labelled configuration has primitive period two. If \(0<c<n/2\), the next counts are \((n-c,0)\), whose total is below \(n\) and whose clique majority is one; a further update gives the opposite-shore pair. The case \(n/2<c<n\) is the complement. Therefore the basin is exactly the set of states with

\[
c+s=n,\qquad \text{or}\qquad c+s>n\ \text{and}\ 2c<n,\qquad \text{or}\qquad c+s<n\ \text{and}\ 2c>n.
\]

The first region contains \(\binom{2n}{n}\) states by counting all choices of \(n\) ones. The last two regions are exchanged by bit complementation. In the second put \(j=n-s\), making its inequalities \(0\le j<c<n/2\). The labelling weight is \(\binom nc\binom nj\). This product is symmetric in \(c,j\); the sum over the two strictly ordered triangles is the weight of the entire square of populations below \(n/2\) minus its diagonal, namely \(A_n^2-Q_n\). This gives the exact count for every \(n\), including \(n=1,2\).

By binomial symmetry and \(\sum_{c=0}^n\binom nc^2=\binom{2n}{n}\), for odd \(n\) we have \(A_n=2^{n-1}\) and \(Q_n=\tfrac12\binom{2n}{n}\). For even \(n\), \(A_n=(2^n-H_n)/2\) and \(Q_n=(\binom{2n}{n}-H_n^2)/2\). Substitution gives the two closed forms. Stirling's formula gives \(\binom{2n}{n}/4^n=(\pi n)^{-1/2}+O(n^{-3/2})\) and, for even \(n\), \(H_n/2^n=\sqrt{2/(\pi n)}+O(n^{-3/2})\). In the even formula the linear term contributes \(-\tfrac12\sqrt{2/(\pi n)}\) and the squared term contributes \(3/(2\pi n)+O(n^{-2})\). This yields the asserted expansions and the eventual signs of the deviations from one quarter.

## Verification

The standalone `verify_split_majority.py` uses explicit neighbor lists on all \(349{,}524\) labelled configurations for \(1\le n\le9\), determining the basin by testing whether the state at update two changes at update three, after independently checking periodic entry by update two. Its weighted population check compares the exact basin formulas for \(1\le n\le150\). The recorded output is `verification_output.txt`, with final marker `SPLIT_MAJORITY_VERIFY_OK`. The script also checks known recurrence and transient assertions. The finite checks do not prove the all-size enumeration or its asymptotics; the argument above does.

## Relationship to prior work and limitations

General finite-graph eventual period at most two is classical (Goles–Olivos; see also Tamuz–Tessler and Benjamini et al.). The complete-split classifications [Exact majority attractors and sharp convergence on complete split graphs](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-exact-majority-attractors-and-sharp-convergence-on-complete-spli--517ed2dd3465) and [A sharp three-round majority-relaxation phase on complete split graphs](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-a-sharp-three-round-majority-relaxation-phase-on-complete-split--46996c042071) already give the recurrent-state count in this subfamily and use the same local update and corner dynamics. Specializing gives one primitive two-cycle in odd sizes and \(1+\tfrac12 H_n^2\) in even sizes, as well as periodic entry by time two. Those results are background here. The distinct calculation is the weighted sum over *all initial states* classified by eventual outcome, giving the closed count and quantifying its parity corrections. In particular, the exponentially different orbit counts do not entail different limiting basin fractions.

The parity-sensitive one-quarter result for [triangular books](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-entrance-time-census-and-parity-law-for-majority-dynamics--260f52d7946d) concerns a different graph family and exact count. The [crown graph majority result](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-a-parity-fracture-in-synchronous-majority-dynamics-on-crown-grap--21b4ec9c390e) has different finite-size formulas and limit. No exact balanced complete-split basin formula was identified in the sources inspected; this is not a claim of historical priority. The full 1980 primary article was not available for comparison. No claim is made here for unequal sides, asynchronous updates, or another tie rule.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
2. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, https://arxiv.org/abs/1307.4035.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, https://arxiv.org/abs/1405.2486.
