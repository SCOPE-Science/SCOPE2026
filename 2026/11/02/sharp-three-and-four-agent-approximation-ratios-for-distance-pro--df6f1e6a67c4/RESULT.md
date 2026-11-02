# Sharp three- and four-agent approximation ratios for distance-proportional two-facility sampling

## Finding

For an arbitrary metric space \((X,d)\) with three or four agents, consider the randomized two-facility rule that selects an unordered pair of reports with probability proportional to their mutual distance and locates facilities at these two reports. The exact worst-case expected utilitarian social-cost approximation factors are
\[
\boxed{R_3=\tfrac32,\qquad R_4=2.}
\]
The denominator is the infimum cost of two freely located facilities in \(X\), not merely the best pair of reports. Both factors are sharp as suprema even with distinct reports on the real line. No Ptolemaic assumption is needed for these cost inequalities; incentive compatibility is a separate issue.

## Assumptions and scope

Let \(n\in\{3,4\}\), \(x_1,\ldots,x_n\in X\), with repetition allowed. For a facility pair \(F=\{f,g\}\subseteq X\), define
\[
C(F)=\sum_{i=1}^{n}\min\{d(x_i,f),d(x_i,g)\},\qquad
\mathrm{OPT}_2=\inf_{f,g\in X}C(\{f,g\}).
\]
Allow coinciding facility locations when needed; this makes no difference to the infimum. Set
\[
Z=\sum_{1\le i<j\le n}d(x_i,x_j),\qquad
C_{ij}=\sum_{k=1}^{n}\min\{d(x_k,x_i),d(x_k,x_j)\}.
\]
For \(Z>0\), the rule chooses \(\{i,j\}\) with probability \(d(x_i,x_j)/Z\), hence
\[
\mathbb E[C]=\frac{\sum_{i<j}d(x_i,x_j)C_{ij}}{Z}.
\]
For \(Z=0\), put the facilities at the common reported location and obtain zero cost. The comparison concerns truthful reports and cost efficiency, not strategic incentive guarantees on arbitrary metric spaces.

## Proof

**Three agents.** Write their three interreport distances in increasing order as \(u\le v\le w\). The cost of choosing the endpoints of the edge of length \(u\) is \(v\); for the edges of lengths \(v\) and \(w\), the costs are each \(u\). Thus the unnormalized expectation numerator and its denominator are
\[
N=u(2v+w),\qquad Z=u+v+w.
\]
For any two centres, at least two of the three clients are assigned to the same centre. For two clients at distance \(\delta\), the triangle inequality forces their sum of distances to that centre to be at least \(\delta\ge u\). Choosing facilities at the endpoints of an edge of length \(u\) achieves cost \(u\). Consequently \(\mathrm{OPT}_2=u\). Since \(v\le w\),
\[
2(2v+w)\le 3(u+v+w),
\]
and therefore \(N\le\tfrac32 Z\mathrm{OPT}_2\), including \(u=0\). For reports \((0,1,T+1)\) on the line, \(T\ge1\), the expected-cost ratio is \((3T+1)/(2(T+1))\), which increases to \(3/2\).

**Four agents: reduction to cluster sizes.** Fix arbitrary comparison centres \(f,g\in X\). Assign each report to a nearer comparison centre. If one centre has no assigned report, relocate that unused centre to a report and assign that report to it; this cannot increase the comparison cost. The resulting two nonempty clusters have sizes \((1,3)\) or \((2,2)\). Write \(N=\sum_{i<j}d(x_i,x_j)C_{ij}\) and \(Z=\sum_{i<j}d(x_i,x_j)\). We prove \(N\le2ZC(\{f,g\})\), with the inequality referring to the cost of the original comparison pair before any nonincreasing relocation.

**The \((1,3)\) case.** Denote the singleton by \(o\), and the other reports by \(p,q,r\). For \(i\in\{p,q,r\}\), write \(D_i=d(o,i)\), let \(e_i\) be the length of the edge opposite \(i\) in the triangle \(pqr\), and set \(P=e_p+e_q+e_r\) and \(D=D_p+D_q+D_r\). Then \(Z=D+P\). When a sampled facility pair consists of \(o\) and \(i\), the cost from the two unsampled triangle clients is at most the sum of their distances to \(i\), which is \(P-e_i\). Therefore the cross-pair contribution to \(N\) is at most
\[
N_{\rm cross}\le PD-\sum_iD_i e_i.
\]
When both sampled facilities lie in the triangle, the singleton incurs cost \(\min(D_i,D_j)\); the remaining triangle client incurs at most \(P\). Hence
\[
N_{\rm inside}\le\sum_{\{i,j\}\subset\{p,q,r\}}d(i,j)\min(D_i,D_j)+P^2.
\]
The following elementary **triangle-weight lemma** is critical:
\[
\sum_{i<j}d(i,j)\min(D_i,D_j)\le\sum_iD_i e_i.
\]
To prove it, relabel so that \(D_p\le D_q\le D_r\), and put \(u=d(p,q)\), \(v=d(p,r)\), \(w=d(q,r)\). The right side minus the left is exactly
\[
(v-w)(D_q-D_p)+u(D_r-D_p)
\ge(u+v-w)(D_q-D_p)\ge0,
\]
using \(u+v\ge w\). Adding the two contributions gives \(N\le P(D+P)=PZ\). If the three-client cluster is assigned to comparator centre \(f\), its three triangle edges each satisfy the triangle inequality through \(f\), so
\[
P\le2\sum_{i\in\{p,q,r\}}d(i,f)\le 2C(\{f,g\}).
\]
Consequently \(N\le2ZC(\{f,g\})\).

**The \((2,2)\) case.** Name the two clusters \(A=\{p,q\}\) and \(B=\{r,s\}\). Let \(u=d(p,q)\), \(v=d(r,s)\), and let \(H\) be the sum of all four distances between one report in \(A\) and one report in \(B\). Then \(Z=u+v+H\). A sampled cross-cluster facility pair costs at most \(u+v\), because the unsampled member of each cluster can use the chosen centre in the same cluster. The sum of its weighted contributions is at most \((u+v)H\). For sampled pair \(\{p,q\}\), the total cost of clients in \(B\) is at most \(H\), so this pair contributes at most \(uH\); analogously \(\{r,s\}\) contributes at most \(vH\). Therefore
\[
N\le 2(u+v)H\le2(u+v)Z.
\]
If the pair in \(A\) uses comparison centre \(f\) and the pair in \(B\) uses \(g\), triangle inequalities give \(u+v\le C(\{f,g\})\). Again \(N\le2ZC(\{f,g\})\).

Both cluster cases prove the bound for every comparison pair, and therefore, upon taking the infimum, \(\mathbb E[C]\le2\mathrm{OPT}_2\) for \(Z>0\). When \(Z=0\), both sides are zero by definition. This also covers \(\mathrm{OPT}_2=0\), without dividing by zero or assuming that the infimum is attained.

**Four-agent sharpness.** Take the real-line reports \((0,T,T+1,T+2)\) for integers \(T\ge2\). Direct enumeration of the six possible sampled pairs yields
\[
N=12T+13,\qquad Z=3T+7,\qquad \mathrm{OPT}_2=2.
\]
For the optimum, the three clustered points have one-facility median cost \(2\), and isolating the distant report costs zero; any grouping that places the leftmost report together with another incurs at least \(T\ge2\). The ratio is therefore
\[
\frac{12T+13}{2(3T+7)}\longrightarrow2
\quad\text{as }T\to\infty.
\]
The three- and four-agent inequalities and sharpness establish the stated exact worst-case suprema.

## Verification

A standalone integer-arithmetic checker, `check_pairwise_finite.py`, independently computes the rule's weighted expected cost and minimum cost over every candidate pair in finite metric spaces. It tests \(65\) valid integer-valued three-report pseudometrics and \(2371\) four-report pseudometrics with edge values in \(\{0,1,2,3,4\}\). It also constructs \(59049\) five-vertex shortest-path metrics from complete graphs with positive edge weights in \(\{1,2,3\}\), using only four vertices as reports and allowing the fifth as an additional comparator facility. All inequalities passed. Exact symbolic-integer checks confirm both sharpness families. These finite tests corroborate but do not replace the all-metric proof above. Run with `python3 check_pairwise_finite.py` using Python 3 and no third-party packages.

## Relationship to prior work

Ma and Peng (2026) introduced the Global Pair mechanism, proved the general factor-four approximation result, and studied strategyproofness and mixtures. Chan, Lin, and Wang (2026) independently studied the same rule under the name Pairwise-Distance, with a general factor-four bound that applies even to arbitrary metric spaces. Jia (2026) identifies the same two-facility rule as the \(k=2\) Product-Gap specialization and proves a \(2k\) bound for the general Product-Gap mechanism on the line. Those population-independent bounds do not imply the sharp three-agent factor \(3/2\) or the four-agent factor \(2\) by themselves. The result here is a small-population exact refinement for the unmodified mechanism, not a new mechanism or an improved strategyproofness theorem. The cited relevant main theorems and definitions were compared, although equivalent treatments elsewhere cannot be excluded.

## Limitations

The theorem concerns exactly three or four agents, utilitarian nearest-facility cost, two facilities, and the distance-proportional unordered-pair sampling rule. It does not determine the sharp approximation ratio at five or more agents. It does not assert incentive compatibility in arbitrary metrics; the source papers distinguish the metric conditions needed for strategyproofness. The equalities for the worst-case constants are suprema, with the displayed line families approaching the constants. The universal assertions rest on the triangle-inequality proof, not finite metric enumeration. Independent external validation and publication-priority certification have not been performed.

## References

1. M. Ma and B. Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, arXiv:2608.09061v1 (first public submission 2026-08-10), https://arxiv.org/abs/2608.09061.
2. H. Chan, J. Lin, and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484v1 (first public submission 2026-08-23), https://arxiv.org/abs/2608.22484.
3. J. Jia, *Product Gap Mechanisms for Multi-Facility Location*, arXiv:2608.19633v1 (first public submission 2026-08-20), https://arxiv.org/abs/2608.19633.
