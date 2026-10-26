# A dyadic half-edge theorem and optimal online shattering for bipartite edge concepts through 31 edges

## Finding

**Theorem.** Every finite simple bipartite graph with exactly \(16\) edges has a vertex subset \(U\) for which its induced subgraph has exactly \(8\) edges. Consequently, for every finite simple bipartite graph \(G=(V,E)\) with \(1\le |E|\le31\), the Boolean concept class
\[
\mathcal H_G=\{h_e:e\in E\},\qquad h_e(U)=\mathbf1[e\subseteq U]\quad (U\subseteq V),
\]
has exact Littlestone dimension
\[
\operatorname{Ldim}(\mathcal H_G)=\lfloor\log_2|E|\rfloor.
\]
The bounds include disconnected graphs and graphs with arbitrarily many isolated vertices. This is a finite dyadic threshold, **not** a claim for graphs with \(32\) or more edges.

## Assumptions and scope

Graphs are finite, simple, undirected, and bipartite. Isolated vertices can be discarded for the induced-edge argument. A query is *any* vertex subset \(U\subseteq V\); hypotheses correspond to *edges*, not vertices. Distinct edges give distinct functions because querying the two endpoints of one edge distinguishes it from all other edges. Littlestone dimension is the greatest depth of a fully shattered adaptive binary membership-query tree, with a single hypothesis of dimension zero.

## Proof

**Lemma 1 (two-row interpolation).** Fix two vertices \(u,v\) in the same side of a bipartition, and let \(s=\deg(u)+\deg(v)\). If \(s\ge t\), for a positive even integer \(t\), then some subset of the opposite bipartition, together with \(u,v\), induces exactly \(t\) edges. Indeed, each opposite vertex contributes weight \(0,1\), or \(2\); write \(a\) for the number of weight-two columns. If \(a\ge t/2\), select exactly \(t/2\) such columns. Otherwise select all \(a\) columns of weight two and \(t-2a\) weight-one columns, available because \(s-2a\ge t-2a\). A one-vertex star with degree at least \(t\) also admits exactly \(t\) induced edges.

**Lemma 2 (half-edge splits for \(2,4,8\) edges).** Every bipartite graph with \(2,4\), or \(8\) edges has an induced subgraph with half that many edges. For two edges select their endpoints on one edge. For four edges, either a vertex has degree at least two and gives a two-edge star, or all active degrees are one and two edges can be selected by choosing their endpoints. For eight edges, a vertex of degree at least four gives a four-edge star. Otherwise inspect the positive degrees on one side. If a subset sums to four, taking exactly those vertices and all opposite vertices gives four induced edges. If not, the only integer partition of eight with parts at most three and no submultiset summing to four is \((3,3,2)\): this follows by the finite partition generation in `verify_half16_independent.py`, and can alternatively be checked by listing the partitions of eight. The first two vertices then have degree sum six, so Lemma 1 with \(t=4\) applies.

**Lemma 3 (the 16-edge half-edge split).** Let \(G\) have \(16\) edges. A vertex of degree at least eight or two vertices on the same bipartition side with degree sum at least eight yields eight induced edges, by Lemma 1 or the star case. A subset of degrees on either side summing to eight also yields eight induced edges. It remains to consider the case where neither side has such a subset or a pair of degrees summing to eight. The positive degrees on either side form a nonincreasing integer partition of 16 with largest part at most seven, largest two parts summing to at most seven, and no submultiset summing to eight. Exhaustive generation of these integer partitions gives exactly
\[
P=(4,3,3,3,3),\qquad Q=(3,3,3,3,3,1).
\]
Thus, up to relabeling the nonisolated vertices within each side, any outstanding graph has one of four ordered pairs of degree lists \((P,P),(P,Q),(Q,P),(Q,Q)\). The complete, finite residual verification uses `verify_half16.cpp` and the separately implemented `verify_half16_independent.py`. Each program enumerates every binary adjacency matrix with those *ordered row and column degree lists*, checking for each row subset whether a column subset contains exactly eight ones. Their corresponding matrix counts are \(906,6720,6720,43440\), totaling \(57\,786\). Every one has a suitable submatrix; the programs print the same counts and no exceptions. The generators are exhaustive because they list every permitted fixed-weight row mask and retain exactly those assignments satisfying every prescribed column sum. The subset-sum test is equivalent to searching all subsets of opposite vertices for a given selected row subset. This proves the residual case and hence Lemma 3 for graphs of **arbitrary vertex order**, not merely graphs with at most six vertices.

**Lemma 4 (dyadic shattering).** Suppose every bipartite graph with exactly \(2^r\) edges has an induced subgraph with exactly \(2^{r-1}\) edges for \(1\le r\le k\). Then every such graph with \(2^r\) edges, \(0\le r\le k\), has a shattered tree of depth \(r\). The proof is by induction. For \(r\ge1\), query the witnessing vertex subset \(U\); the edges contained in \(U\) and edges not contained in \(U\) form two disjoint families of \(2^{r-1}\) edge hypotheses. Both are themselves the edge sets of bipartite graphs (with possibly isolated vertices), so by induction each branch admits a shattered tree of depth \(r-1\). Adjoin those trees below the query. The case \(r=0\) is a single hypothesis.

By Lemmas 2 and 3, Lemma 4 applies for \(r\le4\). Given any bipartite graph with \(m\) edges, \(1\le m\le31\), take an arbitrary subset of exactly \(2^{\lfloor\log_2m\rfloor}\) edges; by Lemma 4 its concept class has dimension at least \(\lfloor\log_2m\rfloor\), and adding further hypotheses cannot decrease Littlestone dimension. Conversely, every shattered depth-\(r\) binary tree requires at least \(2^r\) distinct hypotheses, proving the sharp opposite inequality.

## Verification

The package includes two standalone programs requiring only C++17 standard libraries or Python standard libraries. Run `g++ -O3 -std=c++17 verify_half16.cpp -o half16 && ./half16`, and run `python3 verify_half16_independent.py`. Exact saved stdout for the two programs appears consecutively in `verification_output.txt`. The C++ implementation enumerates allowed adjacency matrices recursively and tests row-subset/column-subset sums by bitset; the Python implementation independently enumerates fixed-weight row combinations and uses explicit sets of attainable column sums. Both produce the ordered counts \((906,6720,6720,43440)\), verify all \(57\,786\) matrices, and find zero exceptions. The Python implementation also independently generates the two exceptional degree partitions \(P,Q\). The unbounded-vertex reduction is mathematical; no unbounded graph enumeration is claimed.

## Relationship to prior work

Ghazi, Golowich, Kumar, and Manurangsi (arXiv:2007.03668, first posted July 7, 2020) establish general closure bounds for Littlestone and threshold dimension under Boolean aggregation, not the present exact edge-indexed result. Alon, Krivelevich, and Sudakov (2003), *Induced Subgraphs of Prescribed Size*, prove a different general interpolation statement; their Lemma 4.1 guarantees edge counts through the size of one positive-degree bipartition side, which need not reach eight in the remaining \(P,Q\) cases. A MathOverflow question posed November 6, 2012 asks about induced half-edge subgraphs of bipartite graphs with dyadic edge counts, illustrating that the present 16-edge conclusion is a particular finite case of a broader longstanding question. The question and its visible answers do not establish this 16-edge case. An earlier finite classification of arbitrary graph edge-conjunction classes through seven vertices found nonbipartite obstructions already at 16 edges; it does not imply the present theorem for unrestricted bipartite graphs of arbitrarily large order and up to 31 edges.

## Limitations

The theorem only covers \(1\le |E|\le31\), and claims no splitting or optimal Littlestone dimension at \(32\) edges. The key 16-edge assertion is established via a proved degree reduction plus an exhaustive finite computation over \(57\,786\) residual adjacency matrices, rather than by a purely symbolic classification of those matrices. The broader dyadic induced-subgraph problem remains outside the claim. Historical publication priority beyond the inspected sources is not guaranteed.

## References

1. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1, July 7, 2020. https://arxiv.org/abs/2007.03668
2. N. Alon, M. Krivelevich, B. Sudakov, *Induced Subgraphs of Prescribed Size*, Journal of Graph Theory (2003), section 4, Lemma 4.1. https://people.math.ethz.ch/~sudakovb/aks-induced.pdf
3. *Does every bipartite graph with 512 edges have an induced subgraph with 256 edges?*, MathOverflow question 111684, November 6, 2012. https://mathoverflow.net/questions/111684/
