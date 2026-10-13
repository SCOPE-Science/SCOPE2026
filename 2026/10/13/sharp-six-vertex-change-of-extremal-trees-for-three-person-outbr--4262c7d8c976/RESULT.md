# Sharp six-vertex change of extremal trees for three-person outbreak risk

## Finding

The probability that an epidemic initiated at a uniformly random site reaches at least three sites does not have the same extremal contact trees at every transmissibility. At orders \(2\le n\le5\), the star uniquely maximizes and the path uniquely minimizes this probability whenever they are nonisomorphic (hence \(n\ge4\)), for every edge-opening probability \(p\in(0,1)\). At order \(n=6\) both identities change at exact, distinct values:

\[
\begin{array}{c|ccc}
\text{extremum}&\text{before transition}&\text{tie}&\text{after transition}\\
\hline
\max F_T(p)&S_6&p=6/7&D_6\\
\min F_T(p)&P_6&p=3/4&T_6
\end{array}
\]

Here \(S_6\) is the six-vertex star; \(D_6\) is the balanced double star formed by joining two degree-three vertices; \(P_6\) is the six-vertex path; and \(T_6\) has a degree-three center with three arms of lengths \((2,2,1)\). At either tie exactly the two displayed trees share the extremum. For every \(n\ge6\), neither the star nor the path is extremal in its former direction for all \(p\) sufficiently close to one: explicit double stars beat the star, and explicit two-length-two-arm trees beat the path.

## Assumptions and scope

Let \(T=(V,E)\) be a finite simple connected acyclic undirected graph with \(|V|=n\ge2\). Independently retain every edge with probability \(0<p<1\). Choose \(U\) uniformly from \(V\), independently of all edge choices, and let \(C_T(U)\) be its connected component in the retained-edge graph, counting \(U\) itself. The only risk measure here is

\[
F_T(p)=\mathbb P\bigl(|C_T(U)|\ge3\bigr).
\]

Tree isomorphism classes, not labelled realizations, are compared. The epidemic interpretation is an independent-bond transmission proxy; no claim is made for arbitrary continuous-time SIR dynamics, dependent edge transmissions, heterogeneous edge probabilities, vaccination decisions, multiple seeding, or populations with cycles. The endpoint values \(p=0\) and \(p=1\) are excluded from uniqueness assertions: all trees share \(F_T(0)=0\) and \(F_T(1)=1\) for \(n\ge3\).

## Proof

**Exact connected-subtree formula.** Every nonempty connected vertex set \(A\subseteq V\) is an induced subtree. Its being a *whole retained-edge component* requires its \(|A|-1\) internal edges to be open and all edges in the edge boundary \(\partial_T A\) to be closed. All other edges are unrestricted. Each such component contributes \(|A|/n\) to the conditional chance of a uniformly selected seed lying in it, so by linearity

\[
nF_T(p)=\sum_{\substack{A\subseteq V,\ |A|\ge3\\T[A]\text{ connected}}}|A|\,p^{|A|-1}(1-p)^{|\partial_T A|}.
\tag{1}
\]

The sum counts components by disjoint events for each fixed seed, or equivalently by the size-biased component census, and therefore has no overcounting problem. Formula (1) produces exact integer-coefficient polynomials for \(nF_T\).

**All trees through order five.** Every unlabelled tree of order \(n=2\) or \(n=3\) has only one shape. For \(n=4\), the star and path are the only shapes, with

\[
4F_{S_4}=9p^2-5p^3,\qquad 4F_{P_4}=6p^2-2p^3.
\]

Their difference equals \(3p^2(1-p)>0\). At \(n=5\) the three shapes are star, path, and the intermediate one-arm-subdivided star \(B_5\). Their exact polynomial numerators are

\[
\begin{aligned}
5F_{S_5}&=18p^2-20p^3+7p^4,\\
5F_{B_5}&=12p^2-9p^3+2p^4,\\
5F_{P_5}&=9p^2-4p^3.
\end{aligned}
\]

Indeed \(5(F_{S_5}-F_{B_5})=p^2(1-p)(6-5p)>0\) and \(5(F_{B_5}-F_{P_5})=p^2(1-p)(3-2p)>0\) for \(0<p<1\). This proves the universal small-order statement.

**Complete six-vertex census.** There are precisely six nonisomorphic trees, distinguished in the table by structure. In addition to the four shapes defined above, let \(B_6\) be the star with one edge subdivided, and \(H_6\) the three-arm tree with arm lengths \((3,1,1)\). The table lists the coefficients of \(6F_T(p)/p^2\) in descending powers of \(p\), so these are polynomial *identities*, not fitted approximations.

| Tree | \(6F_T(p)/p^2\) |
|---|---|
| \(S_6\) | \(-9p^3+35p^2-50p+30\) |
| \(B_6\) | \(-2p^3+13p^2-26p+21\) |
| \(D_6\) | \(-2p^3+8p^2-18p+18\) |
| \(H_6\) | \(2p^2-11p+15\) |
| \(T_6\) | \(4p^2-13p+15\) |
| \(P_6\) | \(12-6p\) |

Completeness can be derived by classifying the possible maximal degrees \(5,4,3,2\): these give one star, one subdivided star, three degree-three types (two adjacent degree-three centers or the two distinct three-arm splits), and one path. Alternatively, Prüfer-word generation and canonical isomorphism encoding in the included checker gives exactly six classes.

Elementary exact factorizations from the table show that \(F_{S_6}\) exceeds \(F_{B_6},F_{H_6},F_{T_6},F_{P_6}\) throughout \((0,1)\), while \(F_{D_6}\) exceeds \(F_{H_6},F_{T_6},F_{P_6}\) throughout \((0,1)\), and \(F_{D_6}>F_{B_6}\) whenever \(p>3/5\). For example,

\[
\begin{aligned}
6(F_{S_6}-F_{B_6})&=p^2(1-p)(7p^2-15p+9),\\
6(F_{D_6}-F_{H_6})&=p^2(1-p)(2p^2-4p+3).
\end{aligned}
\]

Both displayed quadratics are strictly positive for real \(p\); remaining differences factor into \(p^2(1-p)\) times positive polynomials or immediate positive linear factors, as checked exactly in the standalone file. Thus the maximum must be \(S_6\) or \(D_6\). Their sharp difference is

\[
6(F_{S_6}-F_{D_6})=p^2(1-p)(2-p)(6-7p).
\tag{2}
\]

Similarly, \(F_{T_6}\) and \(F_{P_6}\) each lie strictly below each of \(F_{S_6},F_{B_6},F_{D_6},F_{H_6}\) for every \(0<p<1\), so the minimum is one of those two, and

\[
6(F_{T_6}-F_{P_6})=p^2(1-p)(3-4p).
\tag{3}
\]

Equations (2)--(3) prove the complete phase diagram and the exact tie sets.

**The bridge-loss mechanism at every order.** Fix \(n\ge6\), write \(q=1-p\), and remove an edge \(e\), obtaining tree components of respective orders \(a_e\) and \(b_e\) with \(a_e+b_e=n\). If just this edge is closed, the number of vertices in open components of size at most two is exactly \(a_e\mathbf1_{a_e\le2}+b_e\mathbf1_{b_e\le2}\). The all-open configuration has none, the probability that a *particular* edge is the only closed edge is \(q(1-q)^{n-2}=q+O(q^2)\), and the total probability of at least two closed edges is \(O(q^2)\) for each fixed tree. Therefore

\[
F_T(1-q)=1-\frac{L(T)}{n}q+O(q^2),\qquad
L(T)=\sum_{e\in E}\left(a_e\mathbf1_{a_e\le2}+b_e\mathbf1_{b_e\le2}\right).
\tag{4}
\]

The star \(S_n\) has \(L(S_n)=n-1\). Define \(D_n\) by joining two star centers so that the resulting hub-side orders on removing their joining edge are \(3\) and \(n-3\), both at least three. Its other \(n-2\) edges isolate leaves, giving \(L(D_n)=n-2\). Thus \(F_{D_n}(p)>F_{S_n}(p)\) for all \(p<1\) sufficiently close to one.

The path \(P_n\) has two leaf cuts of loss one and two cuts isolating a two-vertex end segment of loss two; all other cuts have zero loss, so \(L(P_n)=6\). Let \(T_n\) have a center with exactly two arms of length two and \(n-5\) arms of length one. Its leaf cuts have total loss \(n-3\), and the two length-two arm-base cuts each contribute two, giving \(L(T_n)=n+1>6\). Hence \(F_{T_n}(p)<F_{P_n}(p)\) for \(p<1\) sufficiently close to one. Since the small-order extremality holds for every \(p\), order six is sharp.

## Verification

The accompanying `verify.py` uses only the Python standard library. Run `python3 verify.py`. It enumerates all Prüfer words through order six, canonically encodes each unrooted tree, obtains each polynomial independently (a) from all open/closed edge configurations and (b) from the connected-subtree identity (1), checks the exact six-vertex table, verifies fourteen symbolic factor identities, and checks the bridge-loss indices for orders 6 through 17. Expected output begins with `VERIFY_OK`. The unlimited-order conclusions follow from the proof of (4), not from the finite checks.

## Relationship to prior work

Newman (2002, first public preprint 30 April 2002) uses percolation to analyze network disease propagation; the present claim takes independent edge opening as its *definition* and compares the chance of an at-least-three-vertex outbreak among fixed finite tree shapes. Jevtić, Lanchier and La Salle (2020) examine first and second moments of the typical percolation-cluster size on paths, rings and stars, while Lanchier and La Salle (2021) establish moment bounds on regular graphs. Neither the accessible 2021 full text nor Newman's full preprint provides the six-vertex probability-tail phase diagram or the bridge-loss extremality obstruction. The 2020 paper's full text was not available in this inspection, so potential stronger prior coverage remains a specific uncertainty. Existing work on near-certain transmission does not automatically settle the exact \(3/4\) and \(6/7\) comparisons.

## Limitations

The risk threshold is fixed at three vertices. No analogous extremal classification is claimed for larger outbreak cutoffs, other graph classes, temporally correlated transmissions, or arbitrary SIR disease processes. The explicit all-order counterfamilies only yield a neighborhood of full transmission depending on \(n\), not a uniform critical probability or global optimizer for all orders. Exact counts and proof establish a combinatorial model result; they do not estimate human or animal disease risks, intervention costs, or confidence bounds for observed transmission probabilities. An inaccessible relevant 2020 paper leaves residual originality risk; an absence of search hits does not demonstrate absolute novelty.

## References

1. M. E. J. Newman, *The spread of epidemic disease on networks*, arXiv:cond-mat/0205009v1 (first public 2002-04-30); subsequent Phys. Rev. E 66, 016128 (2002). https://arxiv.org/pdf/cond-mat/0205009
2. P. Jevtić, N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on rings, paths and stars*, Statistics & Probability Letters 161 (2020), 108714. https://doi.org/10.1016/j.spl.2020.108714
3. N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on regular graphs*, arXiv:2111.01982v1 (2021). https://arxiv.org/pdf/2111.01982
4. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, Phys. Rev. E 76, 036113 (2007). https://doi.org/10.1103/PhysRevE.76.036113
