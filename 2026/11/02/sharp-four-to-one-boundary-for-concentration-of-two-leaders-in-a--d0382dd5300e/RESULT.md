# Sharp four-to-one boundary for concentration of two leaders in a weighted two-clique network

## Finding

Consider two disjoint complete graphs of orders \(p,q\ge3\). Every internal edge of the first clique has conductance \(a>0\), every internal edge of the second has conductance \(b>0\), and precisely one interclique bridge, joining designated gateways, has conductance \(t>0\). Choose exactly two distinct vertices as perfectly grounded, noise-free leaders. With \(F\) the remaining follower set, minimize
\[
J(S)=\operatorname{tr}\bigl(L_{FF}^{-1}\bigr).
\]
Here \(L\) is the combinatorial weighted Laplacian and \(L_{FF}\) is its principal grounded submatrix. For independent unit-intensity Brownian disturbances on followers, stationary total tracking variance equals \(J(S)/2\).

Define the positive quantities
\[
J_0=\frac{2(p-1)}{ap}+\frac{2(q-1)}{bq},\quad
 d_p=\frac{2}{ap},\quad d_q=\frac{2}{bq},\quad
 z_p=\frac{p+2}{a^2p^2},\quad z_q=\frac{q+2}{b^2q^2}.
\]
The global optimum is the minimum of exactly five explicit rational expressions:
\[
\begin{aligned}
J_{PP}&=J_0-\frac{t(z_p+z_q)}{1+t(d_p+d_q)},\\
J_{PG}&=J_0-\frac{tz_p}{1+td_p},\\
J_{GP}&=J_0-\frac{tz_q}{1+td_q},\\
J_{SS}&=\frac{3(p-2)}{2ap}+\frac{2(q-1)}{bq}+\frac qt,\\
J_{TT}&=\frac{3(q-2)}{2bq}+\frac{2(p-1)}{ap}+\frac pt.
\end{aligned}
\]
Their corresponding two-leader patterns are, respectively: (PP) one non-gateway in each clique; (PG) a non-gateway of the first clique and the gateway of the second; (GP) the first gateway and a non-gateway of the second; (SS) the first gateway and a non-gateway in the first clique; (TT) the second gateway and a non-gateway in the second clique. **Every** globally optimal pair belongs to a pattern attaining the minimum; every pair in a minimum-attaining pattern is globally optimal. Thus all ties and the full optimizer set are determined by five constant-time evaluations, independent of network order.

The reduction has the following sharp parameter-independent structural consequence:
\[
\boxed{\text{A two-leader optimum can put both leaders in the first clique for some }a,b,t>0\quad\Longleftrightarrow\quad p>4q-2.}
\]
There is an analogous criterion \(q>4p-2\) for both leaders in the second clique. In particular, when both \(p\le4q-2\) and \(q\le4p-2\), **every** optimum splits the leaders between the cliques at every positive choice of the three conductances. At least one whole-clique concentration regime becomes possible only beyond the sharp size-imbalance boundary.

For an explicit three-phase example, take \(p=16\), \(q=3\), \(a=1/10\), \(b=1\). When \(0<t<16/115\) the optimal pattern is PP; at \(t=16/115\), PP and PG tie; for \(16/115<t<8/5\), PG is optimal; at \(t=8/5\), PG and SS tie; and for \(t>8/5\), SS is optimal. These are the only optimizer patterns throughout that example.

## Assumptions and scope

The graph is simple, finite, undirected and connected; both clique orders are integers at least three; all internal clique edges are present at their specified uniform positive conductance; there is exactly one bridge and no other cross-clique edge. There are exactly two distinct perfectly grounded leaders. The grounded objective is unnormalized \(\operatorname{tr}(L_{FF}^{-1})\), so the factor of two converting it to stationary variance is not included in \(J\). No claims are made for directed, multi-bridge, nonuniform-within-clique, noisy-leader or more-than-two-leader models.

## Proof

**Step 1: a grounded clique identity.** For a complete graph on \(m\) vertices with internal conductance \(c>0\), ground any \(k\) of its vertices, where \(1\le k<m\), and put \(f=m-k\). Its grounded Laplacian is \(c(mI_f-\mathbf1_f\mathbf1_f^{\mathsf T})\), whose inverse is
\[
\frac{1}{cm}\left(I_f+\frac1k\mathbf1_f\mathbf1_f^{\mathsf T}\right).
\]
Consequently its inverse trace is \(f(k+1)/(cmk)\). If a designated gateway remains a follower, the corresponding inverse diagonal for \(k=1\) is \(2/(cm)\), and the squared norm of the corresponding inverse column is \((m+2)/(c^2m^2)\). These are exactly \(d_p,z_p\) and \(d_q,z_q\) for the two cliques.

**Step 2: one leader in each clique.** Without the bridge, the grounded operator is a direct sum of two invertible one-leader clique operators, with trace \(J_0\). The bridge adds the positive rank-one form \(tuu^{\mathsf T}\), where \(u\) has a gateway coordinate in any clique whose gateway remains a follower and has zero coordinate for a grounded gateway. Sherman--Morrison gives
\[
\operatorname{tr}(A+tuu^{\mathsf T})^{-1}
=\operatorname{tr}(A^{-1})-
\frac{t\|A^{-1}u\|_2^2}{1+t u^{\mathsf T}A^{-1}u}.
\]
For non-gateways on both sides, the denominator contribution is \(d_p+d_q\) and the squared-column contribution is \(z_p+z_q\), giving PP. If the second gateway is grounded only \(d_p,z_p\) remain, giving PG; the reverse gives GP. If both gateways are grounded the bridge has no follower coordinate, giving \(J_0\), which is strictly greater than PP since \(t,z_p,z_q>0\). Thus the two-gateway pattern is never optimal.

**Step 3: both leaders in one clique.** Suppose both leaders are in the first clique. Removing the bridge separates an internally grounded first clique from a second clique without any grounded vertex. The first clique's follower inverse trace is \(3(p-2)/(2ap)\). The bridge is a cut-edge, so the grounded effective resistance from each vertex of the second clique to the leader set is the sum of its internal resistance to the second gateway, \(1/t\), and the first gateway's effective resistance to the grounded leaders. The sum of internal resistances to the second gateway in a unit-conductance \(K_q\) is \(2(q-1)/q\); at conductance \(b\) it is \(2(q-1)/(bq)\). If the first gateway is a leader, its effective resistance to the grounded set is zero, hence the displayed \(J_{SS}\). If it is not, the grounded-clique inverse identity with two non-gateway leaders gives the strictly positive gateway resistance \(3/(2ap)\), adding \(3q/(2ap)>0\) to \(J_{SS}\). Therefore two non-gateway leaders of that clique cannot minimize. Swapping the cliques gives \(J_{TT}\) and the strict analogous comparison. This exhausts every possible two-vertex choice and proves the five-value classification, including all ties.

**Step 4: sharp boundary for concentrating leaders.** Put \(\alpha_p=z_p/d_p=(p+2)/(2ap)\) and \(\alpha_q=z_q/d_q=(q+2)/(2bq)\). By direct subtraction,
\[
J_{SS}-J_{PG}=\frac qt-\frac{\alpha_p}{1+td_p},
\qquad \frac{\alpha_p}{d_p}=\frac{p+2}{4}.
\]
If \(p\le4q-2\), then for every finite \(t>0\),
\[
\frac{\alpha_p}{1+td_p}<\frac{\alpha_p}{td_p}=\frac{p+2}{4t}\le\frac qt,
\]
so SS is strictly inferior to PG for every positive \(a,b,t\). Conversely, if \(p>4q-2\), select \(a/b\) sufficiently small that \(\alpha_p>\alpha_q\). As \(t\to\infty\), the limits of SS and PG both equal \(J_0-\alpha_p\), whereas GP and TT tend to \(J_0-\alpha_q\), strictly larger, and PP tends to
\[
J_0-\frac{d_p\alpha_p+d_q\alpha_q}{d_p+d_q},
\]
which is also strictly larger. The first-order terms in the two tied limits are \(q/t\) for SS and \((p+2)/(4t)+O(t^{-2})\) for PG. Since \(q<(p+2)/4\), SS strictly wins for every sufficiently large finite \(t\). Exchanging clique labels proves the symmetric criterion. These comparisons also show that whenever both size inequalities hold, colocation cannot be optimal in either clique.

**Step 5: the explicit double transition.** Substituting \((p,q,a,b)=(16,3,1/10,1)\) yields \(d_p=5/4\), \(d_q=2/3\), \(z_p=225/32\) and \(z_q=5/9\). Algebraic comparison of PP with PG gives a sign change exactly at \(t=16/115\); comparison of PG with SS gives a sign change exactly at \(t=8/5\). Here PG strictly beats GP because both \(z_p>z_q\) and \(z_p d_q>z_q d_p\). Also TT is strictly above GP: \(J_{TT}-J_{GP}=p/t-\alpha_q/(1+td_q)>0\). The five-pattern classification therefore gives exactly the five intervals and boundary ties stated in the finding.

## Verification

The included standalone `verify_weighted.py` uses exact rational Gaussian elimination for grounded Laplacians, independently computes every unordered leader pair for \(300\) combinations of clique sizes and positive weights, and checks each value against the appropriate formula and the minimum of the five candidates. It performed \(9000\) exact grounded inversions, checked \(2400\) strict exclusions of same-clique non-gateway pairs, and verified the two rational transition points and sharp-size-bound inequalities. `verification_output.txt` contains the successful direct execution output. These finite checks corroborate the algebra but do not prove its infinite quantifiers; Steps 1--5 do.

## Relationship to prior work

Lin, Fardad and Jovanović (2013) formulate leader selection under stochastic disturbances and develop optimization relaxations and algorithms. Fitch and Leonard (first posted 2014) express noisy-network tracking performance through joint centrality and give explicit cycle/path leader placements. Patterson, Yi and Zhang (first posted 2017) develop resistance-based leader coherence formulas and analyze paths, cycles and certain trees. None of the materially inspected results states the five-candidate solution and the sharp size-only four-to-one colocation boundary for two differently weighted bridge-connected cliques. General grounded-Laplacian inverse identities underlie the calculation, and this result does not claim those methods as new.

An earlier narrow equal-strength construction with a two-vertex clique and one larger clique already has a one-transition placement rule. The present finding contains such a special case algebraically but requires new coverage for independent clique strengths, arbitrary sizes at least three, five competing patterns, and the genuine two-transition/leader-colocation phenomenon. A general exact solver can of course evaluate all \(\binom{p+q}{2}\) pairs; the claim is the analytic five-candidate reduction and sharp parametric structural criteria, not an assertion that the underlying optimization problem was previously unknown.

## Limitations

The classification assumes internally uniform clique conductances and a single bridge. The five rational values determine ties exactly, but no claim is made that every possible ordering of their transition curves has been tabulated. The example is an exact corollary, not representative of every parameter configuration. No independent audit or external formal proof has been obtained. The literature comparison is bounded and does not establish absolute publication priority, particularly against unindexed specialized community-control calculations or general formulas specialized without explicit statement.

## References

1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, initially posted 2013-02-03. https://arxiv.org/abs/1302.0450
2. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, initially posted 2014-07-07. https://arxiv.org/abs/1407.1569
3. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, initially posted 2017-08-23. https://arxiv.org/abs/1708.06873
