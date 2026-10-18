# Complete edge-general-position and facet enumerators for cliques with pendant bundles

## Finding
For every integer \(n\ge 3\) and every tuple of positive integers \(\mathbf b=(b_1,\ldots,b_n)\), let \(H_{n,\mathbf b}\) be obtained from a clique on hubs \(v_1,\ldots,v_n\) by attaching \(b_i\) distinct pendant leaves at hub \(v_i\). A selected-edge set is **edge-general-position** (EGP) when no three of its edges lie together on a shortest path. Let \(x\) record selected pendant edges and \(y\) record selected clique edges. The complete two-weight enumerator is
\[
F_{\mathbf b}(x,y)=\sum_{P\subseteq[n]}\left(\prod_{i\in P}\big((1+x)^{b_i}-1\big)\right)(1+y)^{\binom n2-\binom{|P|}{2}}.
\]
Every inclusion-maximal EGP set is obtained from a **unique nonempty** subset \(P\subseteq[n]\) by selecting all pendant edges at hubs indexed by \(P\), no pendant edges at the other hubs, and exactly all clique edges not having both endpoints in \(P\). Thus the complete maximal-set enumerator is
\[
M_{\mathbf b}(x,y)=\sum_{\varnothing\ne P\subseteq[n]}x^{\sum_{i\in P}b_i}y^{\binom n2-\binom{|P|}{2}},
\]
and the number of distinct inclusion-maximal EGP sets is exactly \(2^n-1\). If \(b_{(1)}\ge\cdots\ge b_{(n)}\) are the sorted multiplicities, the maximum size is
\[
\operatorname{gp}_e(H_{n,\mathbf b})=\binom n2+\max_{1\le s\le n}\left(\sum_{i=1}^s b_{(i)}-\binom s2\right).
\]
The EGP edge-subset complex is nonpure for **every** permitted \(n\) and \(\mathbf b\). For the one-leaf-per-hub corona \(H_{n,\mathbf1}\), its maximal-set enumerator is
\[
M_{\mathbf1}(z,z)=\sum_{s=1}^n\binom ns z^{\binom n2+s-\binom s2}.
\]
In particular, for every \(n\ge4\), there is no inclusion-maximal EGP set of any cardinality \(n+1,n+2,\ldots,2n-3\), giving \(n-3\) consecutive missing maximal cardinalities.

## Assumptions and scope
Graphs are simple and unweighted; shortest paths are graph-distance geodesics and distinct leaves are labeled. The parameters satisfy \(n\in\mathbb Z\), \(n\ge3\), and \(b_i\in\mathbb Z_{\ge1}\) for each index. An inclusion-maximal EGP set cannot be extended by even one additional edge while remaining feasible; this is distinct from a maximum-cardinality EGP set. In the enumerator \(F_{\mathbf b}\), the empty selected set is included. Every exponent and coefficient counts distinct **edge subsets**, not isomorphism types. All assertions hold simultaneously for every permitted parameter tuple.

## Proof
**Geodesic obstruction.** Every vertex belongs either to the hub clique or to a pendant leaf. Two hubs have distance one. A hub and any leaf have distance at most two. Two leaves on the same hub have distance two. Distinct leaves attached to different hubs \(i\ne j\) have the unique shortest path \(\ell_i,v_i,v_j,\ell_j\) of length three. There are no longer shortest paths. Therefore a selected set fails EGP precisely when it contains a pendant edge at hub \(i\), another pendant edge at distinct hub \(j\), and the clique edge \(v_iv_j\).

**All-set enumerator.** Given an EGP set, define its active hub set \(P\) as the indices of hubs carrying at least one selected pendant edge. For each \(i\in P\), the pendant-edge subset can be any nonempty subset of the \(b_i\) labeled edges and has weight polynomial \((1+x)^{b_i}-1\). For indices outside \(P\) no pendant edge is selected. The obstruction above prohibits exactly the \(\binom{|P|}{2}\) clique edges internal to \(P\), while each of the remaining \(\binom n2-\binom{|P|}{2}\) clique edges can be selected or omitted independently. The active set \(P\) is unique; multiplying choices and summing over \(P\) proves \(F_{\mathbf b}\).

**All maximal sets.** If \(P\ne\varnothing\), a feasible set can be extended whenever it omits a pendant edge at an active hub or omits an allowable clique edge. Hence maximality forces every available edge of these types to be selected. Such a saturated set is indeed maximal: choosing any previously unselected clique edge internal to \(P\) violates the geodesic obstruction; choosing a pendant edge at a formerly inactive hub \(j\notin P\) violates the obstruction together with the already selected clique edge \(v_iv_j\) and a selected pendant edge at any \(i\in P\). Thus all nonempty \(P\) give unique facets. When \(P=\varnothing\), one may always add a pendant edge without creating a triple, so this cannot be a facet. This proves \(M_{\mathbf b}\) and its value \(2^n-1\) at unit weights.

**Maximum cardinality.** For fixed active-set cardinality \(s\ge1\), the largest corresponding feasible set is a facet and has size \(\binom n2+\sum_{i\in P}b_i-\binom s2\). This is maximized by choosing the \(s\) largest multiplicities; maximizing over \(s\) gives the stated exact formula.

**Nonpurity.** Suppose all facets had the same size. The facet sizes for singleton active sets \(\{i\}\) force every \(b_i\) to be a common integer \(r\). Comparing singleton and two-element active sets yields \(r=1\). But for any three-element active set, its facet has size \(\binom n2+3-3=\binom n2\), whereas the singleton facet has size \(\binom n2+1\), a contradiction. Since \(n\ge3\), such a three-element set exists; no permitted complex is pure.

**Unbounded gaps.** When every \(b_i=1\), the facet size for an active set of size \(s\) is \(m(s)=\binom n2+s-\binom s2\). For \(s\ge2\), its consecutive differences are \(m(s+1)-m(s)=1-s<0\); in particular \(m(n)=n\), \(m(n-1)=2n-2\), and every other facet has size at least \(m(n-1)\). Therefore sizes strictly between \(n\) and \(2n-2\) do not occur; their number is \(n-3\) when \(n\ge4\). The binomial factor \(\binom ns\) counts active sets of each size, proving the last enumerator.

## Verification
The accompanying standalone `verify.py` constructs all graph edges and uses breadth-first search plus backtracking to enumerate **all shortest paths** independently of the structural criterion. It records every forbidden triple from those geodesics, then enumerates all edge subsets and separately tests all single-edge extensions for maximality. Exact bivariate coefficient dictionaries are compared to independently computed symbolic expansions of both displayed formulas. The scalar optimum and the total count of facets are also checked. It exhausted six positive-multiplicity parameter profiles, comprising 55,360 edge subsets in total; the exact command and observed output are included in `VERIFICATION.md` and `verify_output.txt`. Finite enumeration does not prove the assertions for unbounded parameters; the preceding geodesic and maximality arguments do.

## Relationship to prior work
Manuel, Prabha, and Klavžar introduced the edge-general-position problem (arXiv:2105.04292v1, 10 May 2021), including extremal counts for hypercubes, trees, and grids. Tian, Klavžar, and Tan (2024, Theorem 3.2 and its proof) establish the **already known** scalar \(\operatorname{gp}_e=\binom n2+1\) for a clique with at most one pendant path on each of certain hubs; for the one-leaf-per-hub case this follows from the present maximum formula and is **not new**. Their inspected results do not specify the all-edge-subset polynomial, the distinct facets, or the arbitrarily long gaps in facet cardinality, nor the heterogeneous positive leaf multiplicities.

The 2026 article by Hamed-Labbafian, Henning, and Tavakoli addresses edge-general-position numbers for graph products including coronas; accessible metadata indicate scalar extremal problems, but its full text was unavailable for theorem-by-theorem comparison. A related result on **vertex** general-position polynomials of complete-graph coronas concerns a different feasibility predicate and cannot imply the present edge-subset enumerators. Absence of an indexed formula does not establish priority.

## Limitations
The result concerns pendant edges of length one attached to a **complete** core and strictly positive multiplicities. Arbitrary core graphs, long pendant paths, or empty multiplicity classes are not covered by the stated proof. This finding does not establish any classification for those larger classes. The cited 2026 corona-product paper could conceal prior overlapping formulas in inaccessible full text. Independent scientific and bibliographic verification have not been performed. The finite checker verifies sampled parameter profiles exhaustively, not the universal claim.

## References
1. P. Manuel, R. Prabha, S. Klavžar, *Edge general position problem*, arXiv:2105.04292v1 (2021-05-10), https://arxiv.org/html/2105.04292v1 .
2. J. Tian, S. Klavžar, E. Tan, *Extremal Edge General Position Sets in Some Graphs*, Graphs and Combinatorics **40**, article 40 (2024), https://doi.org/10.1007/s00373-024-02770-z .
3. Z. Hamed-Labbafian, M. A. Henning, M. Tavakoli, *Edge general position in graphs: Graph products, integer linear programming and some applications*, Discrete Applied Mathematics (2026), https://doi.org/10.1016/j.dam.2026.01.008 (metadata and abstract checked; full text not inspected).
