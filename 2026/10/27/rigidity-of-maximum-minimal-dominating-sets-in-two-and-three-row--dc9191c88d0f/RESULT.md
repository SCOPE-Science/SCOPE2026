# Rigidity of maximum minimal dominating sets in two- and three-row grids

## Finding
Let \(G_{h,n}=P_h\square P_n\), with \(h\in\{2,3\}\) and \(n\ge2\). A set \(D\subseteq V(G_{h,n})\) is *minimal dominating* if it dominates every vertex and deletion of any one of its vertices destroys domination. Write \(U_h(n)\) for the number of these sets having the largest possible size. Then
\[
\Gamma(G_{h,n})=\left\lceil\frac{hn}{2}\right\rceil,
\qquad
U_2(n)=\begin{cases}4&n\text{ odd},\\6&n\text{ even},\end{cases}
\qquad
U_3(n)=\begin{cases}1&n\text{ odd},\\4&n\text{ even}.\end{cases}
\]
Moreover, *every* such set is one of the following explicitly described sets, taking only the cases of the correct cardinality:

1. A checkerboard parity class \(\{(i,j):(i+j)\equiv p\pmod2\}\) of cardinality \(\lceil hn/2\rceil\).
2. If \(h=2\), either complete horizontal row \(\{(i,j):j=p\}\), for \(p\in\{0,1\}\).
3. If \(n\) is even, either of the two period-four full-column patterns: take every row in columns \(i\equiv0,3\pmod4\), or every row in columns \(i\equiv1,2\pmod4\).

The coordinates are \(0\le i<n\) and \(0\le j<h\). All listed sets are distinct when \(n\ge2\); there are exactly the asserted numbers of them.

## Assumptions and scope
Graphs are finite, undirected, and simple; Cartesian adjacency means that vertices differing by one in exactly one coordinate are adjacent. An external or self-private neighbor of a selected vertex \(v\) is a vertex \(u\in N[v]\) for which \(N[u]\cap D=\{v\}\). A dominating set is inclusion-minimal if and only if each selected vertex has such a witness. The finding concerns maximum *cardinality among inclusion-minimal* dominating sets, not minimum-cardinality dominating sets, and covers all \(n\ge2\) for the two fixed heights.

## Proof
First, each listed set has size \(\lceil hn/2\rceil\) and is minimal dominating. A checkerboard class is a maximal independent set. In a full horizontal row when \(h=2\), the opposite-row vertex in each column is a private witness. In either full-column pattern, adjacent omitted columns come in pairs, except possibly at an endpoint: every selected vertex has a horizontally adjacent omitted vertex whose other horizontal neighbor, when present, is also omitted. This vertex is its private witness, and all omitted vertices are dominated. The existing bipartite-grid upper-domination theorem gives \(\Gamma(G_{h,n})=\lceil hn/2\rceil\); the finite-state argument below also proves this value directly.

For completeness, here is an exact finite-state induction proving that the displayed list is exhaustive for every \(n\). Encode column \(i\) by a bitmask \(v_i\in\{0,\ldots,2^h-1\}\), with one bit per selected row, and use a special symbol \(\bot\) for the nonexistent columns outside the graph. The condition that both vertices (when \(h=2\)), or all three vertices (when \(h=3\)), of column \(i\) are dominated and that each selected one has a private witness is determined by the five masks
\[
(v_{i-2},v_{i-1},v_i,v_{i+1},v_{i+2}).
\]
Indeed, domination depends only on adjacent columns, while a private witness lies in the closed neighborhood of its selected vertex and the witness's own closed neighborhood lies within distance two. The predicate `good` in `verify.py` is precisely this local test, with nonexistent vertices excluded from the witness search.

Maintain a state of four consecutive masks, initialized to \((\bot,\bot,\bot,\bot)\). When appending a real mask \(v\), inspect the five-mask word consisting of the state followed by \(v\); validate its middle mask if real, shift left, and add \(\operatorname{popcount}(v)\) to the selected cardinality. For each state \(s\) and length \(k\), retain the maximum weight \(M_k(s)\) of admissible prefixes and the number \(C_k(s)\) of prefixes attaining that weight. These data evolve by an exact integer max-plus recurrence: a higher weight replaces the previous value and its count; tied higher weights add counts. After the last real mask, append \(\bot\) twice, which validates the final two columns without counting extra vertices. Discarding suboptimal prefixes at a fixed state is lossless because every possible continuation and its added weight depend only on that state.

The finite, exhaustive transition computation included in `verify.py` establishes the following identities for every reachable state \(s\), including equality of the state supports at the three displayed lengths:
\[
\begin{array}{c|c|c|c}
h&k_0&\text{number of states}&M_{k_0+4}(s)-M_{k_0}(s)\\\hline
2&12&123&4\\
3&16&1285&6
\end{array}
\]
and, for both heights,
\[
M_{k_0+8}(s)-M_{k_0}(s)=4h,
\qquad C_{k_0+8}(s)-2C_{k_0+4}(s)+C_{k_0}(s)=0.
\]
These are identities over all states, not sampled initial graph orders. Let \(T\) denote four successive real-column transitions. The displayed weight-translation identity ensures that the maximizing transitions forming \(T\) are identical on the translated weight vectors at \(k_0\) and \(k_0+4\). Consequently, on their associated count vectors, \(T\) acts as one fixed integer linear transformation. Writing \(d=C_{k_0+4}-C_{k_0}\), the second-difference identity is exactly \(T(d)=d\). Inductively, for every \(q\ge0\),
\[
M_{k_0+4q}=M_{k_0}+2hq,
\qquad C_{k_0+4q}=C_{k_0}+qd.
\]
The same reasoning after zero, one, two or three more real-column transitions applies in each residue class modulo four, and the final two \(\bot\)-transitions are also a fixed linear operation on counts once their maximizing transitions are determined. The program checks that the final maximal-cardinality counts at \(k_0+r\) and \(k_0+r+4\) are equal for \(r=0,1,2,3\). Thus their affine slope is zero, proving eventual period four; the explicit counts in those four residues are actually period two. The same exact recurrence checks all \(2\le n<k_0\). It also proves directly that the largest weight is \(\lceil hn/2\rceil\). This yields the displayed formulas for every \(n\ge2\).

Finally, the explicit listed constructions give exactly the same number of distinct sets as the proved total \(U_h(n)\), so no other maximal-cardinality minimal dominating set exists. This completes the classification.

## Verification
Run `python3 verify.py` using Python 3.10 or later. The script has no external dependencies. It checks all claimed five-mask local tests, all max-plus transitions and state supports, the full period-four induction certificate, and the terminal count equalities, using exact unbounded integers. Separately, it directly examines original vertex subsets of the indicated extremal cardinality for \(2\le n\le8\) in both heights, and directly tests every listed pattern. Successful output ends with `VERIFY_OK`. These small enumerations are cross-checks, not the justification for the infinite claim: the induction is supplied by the statewise vector identities and linearity argument above.

## Relationship to prior work
Sahbi's arXiv:2610.03785 establishes the largest cardinality \(\Gamma(G_{m,n})=\lceil mn/2\rceil\) for all rectangular grids, but does not enumerate or classify the maximizers. Burdett, Haythorpe and Newcombe (2023) study upper domination formulations and grids computationally, without this classification. OEIS A286847 and A290379 record the *total* number of minimal dominating sets of grids and ladders, respectively, summed over all sizes; those counts are not the top-cardinality coefficient or its structural description. The 2003 unique-independence/upper-domination theorem for bipartite graphs covers the uniqueness *aspect* of certain odd-area cases, not the nonunique enumerations or full two-height classification. The earlier upper-domination classification of circular ladders concerns \(C_n\square K_2\), where the cyclic boundary changes the classification: it does not imply the open-ladder results here.

## Limitations
Only heights two and three are classified. Experiments with taller grids are not theorems about their infinite families. The proof is a reproducible finite-state induction, not a hand classification of all local configurations; computational transcription and independent-review risks remain. The literature search cannot establish absolute historical priority, and the full text of every older related publication was not inspected. No independent audit is claimed.

## References
- R. Sahbi, *Upper Domination in Rectangular Grid Graphs and Its Relation to Sub-Quorum Colorings*, arXiv:2610.03785, first posted 2026-09-30, https://arxiv.org/abs/2610.03785.
- R. Burdett, M. Haythorpe, and A. Newcombe, *Binary programming formulations for the upper domination problem*, Mathematical Methods of Operations Research 98 (2023), 155–168, https://doi.org/10.1007/s00186-023-00831-2.
- A. Howroyd and E. W. Weisstein, OEIS A290379, *Number of minimal dominating sets in the n-ladder graph*, https://oeis.org/A290379.
- A. Howroyd, OEIS A286847, *Number of minimal dominating sets in the grid graph*, https://oeis.org/A286847.
- *Unique Independence, Upper Domination and Upper Irredundance in Graphs*, J. Combin. Math. Combin. Comput. 47 (2003), 237–249, https://combinatorialpress.com/jcmcc-articles/volume-047/unique-independence-upper-domination-and-upper-irredundance-in-graphs/.
