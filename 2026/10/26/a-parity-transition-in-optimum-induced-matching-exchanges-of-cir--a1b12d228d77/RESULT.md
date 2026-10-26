# A parity transition in optimum induced-matching exchanges of circular ladders

## Finding

Let \(P_n=C_n\square K_2\) be the circular ladder with cyclic columns \(i\in\mathbb Z/n\mathbb Z\), top vertices \(u_i\), bottom vertices \(v_i\), rails \(u_iu_{i+1}\), \(v_iv_{i+1}\), and rungs \(u_iv_i\). Here and throughout, \(n\ge4\). An **induced matching** is an edge set whose endpoints span exactly its disjoint edges. Let \(\mathcal X_n\) have all **maximum** induced matchings as vertices, adjacent when precisely one chosen edge is removed and one different edge added, preserving inducedness and the maximum size. Thus adjacency means \(|M\triangle M'|=2\), not that one endpoint is moved.

The induced-matching number is
\[
\nu_s(P_n)=\left\lfloor\frac n2\right\rfloor.
\]
The complete optimum exchange classification is as follows.

* If \(n\equiv2\pmod4\), there are exactly two maximum induced matchings, and \(\mathcal X_n\cong2K_1\).
* If \(n\equiv0\pmod4\), there are exactly six maximum induced matchings, and \(\mathcal X_n\cong6K_1\).
* If \(n\) is odd (hence \(n\ge5\)), there are exactly \(n^2\) maximum induced matchings. Their exchange graph is connected, has \(2n(n+1)\) edges, and has exactly \(n(n-3)\) vertices of degree four, \(2n\) of degree five, and \(n\) of degree six.

A complete combinatorial presentation of the odd-order exchange graph is also given below. Hence the even-order optimal packings are entirely frozen under single-edge exchanges, whereas every pair of odd-order optimal packings can be connected by such exchanges.

## Assumptions and scope

All graphs are finite, simple, and labeled as above. The graphs \(C_n\) are ordinary simple cycles, with \(n\ge4\); the special triangular prism \(n=3\) is **not** covered. The exchange operation replaces one entire edge of an induced matching, not a vertex of its endpoint set. All counts are for labeled, distinct edge sets, not automorphism classes. Graph isomorphisms and congruences refer to the explicitly defined index \(n\).

For a given induced matching \(M\), let \(S(M)\) denote its endpoint set and put \(a_i=|S(M)\cap\{u_i,v_i\}|\). Each \(a_i\) lies in \(\{0,1,2\}\); value two means that the rung at column \(i\) belongs to \(M\). If \(a_i=2\), then \(a_{i-1}=a_{i+1}=0\). Therefore
\[
0\le a_i+a_{i+1}\le2
\quad(i\in\mathbb Z/n\mathbb Z).
\]

## Proof

**1. Optimal size and even orders.** Summing the preceding inequalities gives
\[
4|M|=2\sum_i a_i=\sum_i(a_i+a_{i+1})\le2n,
\]
so \(|M|\le\lfloor n/2\rfloor\). Choose rungs in every second column, with one additional zero column when \(n\) is odd; this attains the bound in all orders.

When \(n\) is even and \(|M|=n/2\), every consecutive-column inequality is an equality. Consequently \(a_{i+1}=2-a_i\) at every column. Either \(a_i\) alternates between zero and two, producing exactly the two rung configurations, or every \(a_i=1\). In the latter case each occupied vertex must be joined to its partner by a rail edge; the row sequence therefore consists of consecutive \(TT\) and \(BB\) pairs, alternately. Closing the cycle is possible precisely when \(4\mid n\), and produces exactly four configurations (two choices of the dimer boundary offset and two initial rows). This proves the even optimum counts. No two of these distinct optimum edge sets differ in just one edge: rung sets and rail sets are disjoint, distinct rung patterns are disjoint, and any two distinct full rail patterns either use disjoint rail edges or have different global phases. Thus every even optimum is isolated.

**2. Exhaustive odd-order parametrization.** Suppose \(n=2k+1\ge5\) and \(|M|=k\). Define \(d_i=2-a_i-a_{i+1}\ge0\). Since \(\sum_i a_i=2k=n-1\),
\[
\sum_i d_i=2.
\]
If one defect equals two, its two incident columns both have occupancy zero; all remaining consecutive occupancies sum to two. They consequently alternate \(2,0,2,0,\ldots,2\), giving a unique pattern of \(k\) rungs after the two zeros. For each \(i\in\mathbb Z/n\mathbb Z\), denote by \(R_i\) the matching of rungs at
\[
i+2,i+4,\ldots,i+2k\pmod n.
\]
These are exactly the \(n\) configurations with a defect equal to two.

Otherwise exactly two defects have value one. At a unit defect the two occupancies are zero and one; between defects, equality forces either a constant run of ones or an alternating run of zeros and twos. Therefore the cyclic occupancy sequence consists of one nonempty run of ones of even length \(2\ell\), followed by a run \(0,2,0,2,\ldots,0\) of odd length. Here \(1\le\ell\le k\). The even length is forced because the vertices of occupancy-one columns must be paired by horizontal rail edges. Within their run, the row labels necessarily alternate in pairs \(TT,BB,TT,BB,\ldots\). This permits exactly two row choices.

For \(i\in\mathbb Z/n\mathbb Z\), \(1\le\ell\le k\), and \(s\in\{0,1\}\), define \(F_{i,\ell,s}\) as follows. For \(0\le t<\ell\), choose the rail edge from column \(i+2t\) to column \(i+2t+1\) in row \(s+t\pmod2\), where row zero means the top rail. For \(0\le t<k-\ell\), also choose the rung at column \(i+2\ell+1+2t\). All column indices are taken modulo \(n\). The omitted columns are zero. All these matchings are induced. Every optimum with two unit defects arises uniquely in this way, because its maximal occupancy-one run determines \(i,\ell\), and the first selected rail determines \(s\). Therefore the total is
\[
n+\sum_{\ell=1}^k 2n=n+2nk=n^2.
\]

**3. Exact exchange rule for odd orders.** In the following display all first indices are reduced modulo \(n\), and \(\overline s=1-s\). The complete neighbor sets are
\[
\begin{aligned}
N(R_i)={}&\{R_{i-2},R_{i+2}\}\cup\{F_{i-1,1,s},F_{i+1,1,s}:s=0,1\},\\
N(F_{i,1,s})={}&\{F_{i,1,\overline s},F_{i,2,s},F_{i-2,2,\overline s},R_{i-1},R_{i+1}\},\\
N(F_{i,\ell,s})={}&\{F_{i,\ell-1,s},F_{i,\ell+1,s},F_{i+2,\ell-1,\overline s},F_{i-2,\ell+1,\overline s}\},\quad 1<\ell<k,\\
N(F_{i,k,s})={}&\{F_{i,k-1,s},F_{i+2,k-1,\overline s},F_{i-2,k,\overline s},F_{i+2,k,\overline s}\}.
\end{aligned}
\]
The last two lines are omitted when their index ranges are empty; \(k\ge2\) by hypothesis.

To verify exhaustiveness without assuming a reconfiguration theorem, compare edge subsets in the explicit families. Replacing one edge changes the number of horizontal edges by at most one. If this number increases or decreases by one, every unchanged horizontal edge must remain in the same alternating paired run; the only possible new or removed rail edge is at either end of that run. This gives precisely the two growth or shrinkage choices shown, including the rung-only boundary. If the number of horizontal edges is fixed, the unchanged edges force the matching except in three explicitly visible boundary cases: a rung-only configuration can shift its double-zero defect two columns; a run of one rail edge can switch rows; and a run occupying all but one column can move its sole zero column two positions, switching its starting row. Directly comparing the defining edge positions in these three cases yields the remaining displayed neighbors. Conversely, each displayed pair shares exactly \(k-1\) edges, hence differs by one legal exchange. No other exchange is possible.

The rule gives degrees six for the \(n\) vertices \(R_i\), five for the \(2n\) vertices \(F_{i,1,s}\), and four for all remaining \(2n(k-1)=n(n-3)\) vertices. The handshaking lemma yields
\[
|E(\mathcal X_n)|=\frac{6n+5(2n)+4n(n-3)}2=2n(n+1).
\]
The edges \(R_iR_{i+2}\) form an \(n\)-cycle, since \(n\) is odd. Every \(F_{i,\ell,s}\) admits a sequence of the displayed shrinkage exchanges decreasing \(\ell\) to one and then reaching an \(R_j\). Thus \(\mathcal X_n\) is connected. All asserted conclusions follow. \(\square\)

## Verification

The standalone `verify.py` constructs every edge and vertex neighborhood of \(P_n\), builds an induced-matching conflict graph, exhaustively enumerates the largest independent sets of that graph by a memoized branching recurrence, and independently constructs every displayed symbolic configuration and neighbor list. For every \(4\le n\le19\), it verifies equality of the two full families of edge subsets; the exact number of states, the exchange edge count, the connected-component sizes and the entire degree spectrum; and for odd orders, the displayed individual adjacency lists. Running `python verify.py` terminated with `ALL_VERIFY_OK`.

The infinite result is proved above from the occupancy inequalities and explicit family comparison, rather than inferred from the finite computation. The script requires only Python's standard library.

## Relationship to prior work

Cameron, Sritharan and Tang (2003) develop algorithms for maximum induced matchings in weakly chordal graph classes. The prisms here contain induced long outer cycles and need not belong to that class; their paper does not classify circular-ladder optimum exchanges. Dabrowski, Demange and Lozin (2013) prove complexity results for regular bipartite graphs and determine induced-matching sizes in hypercubes, not this prism family. Joos (2014) establishes general maximum-degree bounds, rather than enumerating minimum-gap optima or their exchange graph. Nakahata (2025) studies connected-component reconfiguration rules encompassing induced matching problems but derives its principal special-class results for paths, cographs and other restricted families; its inspected results do not imply this exact circular-ladder classification.

For context, an earlier exact strong-chromatic-index calculation on prism graphs concerns decomposing *all* graph edges into induced matchings, not the count or exchange adjacency of maximum individual induced matchings. Neither its value nor the general results above imply the \(n^2\) odd optimum count or the parity-dependent frozen-versus-connected phenomenon. This is a best-knowledge originality comparison, not a proof that no equivalent statement exists anywhere.

## Limitations

The triangular prism \(n=3\) is excluded; its small-order behavior differs. Only single **edge replacements** between maximum induced matchings are studied, not swaps of one matched endpoint, token sliding along the underlying graph, or moves among nonmaximum matchings. Numerical verification covers only \(4\le n\le19\), although the proof covers every integer \(n\ge4\). An equivalent theorem in unindexed or inaccessible literature is possible; novelty has not been independently certified.

## References

1. K. Cameron, R. Sritharan and Y. Tang, *Finding a maximum induced matching in weakly chordal graphs*, Discrete Mathematics **266** (2003), 133–142. DOI: `10.1016/S0012-365X(02)00803-8` (public date verified as 2003-05-06).
2. K. K. Dabrowski, M. Demange and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science **478** (2013), 33–40. DOI: `10.1016/j.tcs.2013.01.027`.
3. F. Joos, *Induced matchings in graphs of bounded maximum degree*, arXiv:`1406.2440` (first version 2014-06-10; later journal DOI `10.1137/16M1058078`).
4. Y. Nakahata, *Reconfiguring Multiple Connected Components with Size Multiset Constraints*, arXiv:`2505.07268` (2025).
