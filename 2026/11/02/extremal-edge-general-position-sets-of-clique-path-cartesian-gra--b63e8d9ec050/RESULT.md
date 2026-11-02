# Extremal edge-general-position sets of clique-path Cartesian graphs

## Finding

**Theorem.** For all integers \(L,m\ge2\), let \(G=P_L\square K_m\). Then
\[
\operatorname{gp}_e(G)=L\binom{m}{2}+m.
\]
A set of edges of this maximum size is edge-general-position if and only if it consists of every edge contained in a complete-graph layer, together with every edge connecting layers \(i\) and \(i+1\), for a single \(i\in\{1,\ldots,L-1\}\). Therefore the number of maximum labeled sets is exactly \(L-1\).

## Assumptions and scope

The graphs are finite, simple and undirected. The path \(P_L\) has vertex set \(\{1,\ldots,L\}\) and the complete graph \(K_m\) has vertex set \(\{1,\ldots,m\}\). Product vertices are \((i,a)\). Two product vertices are adjacent if exactly one coordinate changes along an edge of its factor. An edge inside a fixed \(K_m\)-layer \(i\) is called a *clique edge*. An edge \((i,a)(i+1,a)\) is called a *path edge* in column \(a\) and cut \(i\). There are \(L\binom{m}{2}\) clique edges and \(m(L-1)\) path edges. A *geodesic* is a shortest path. An edge set \(S\subseteq E(G)\) is *edge-general-position* if every geodesic contains at most two edges of \(S\). A *maximum set* maximizes \(|S|\).

## Proof

**Construction.** Fix any cut \(i\in\{1,\ldots,L-1\}\), and select all clique edges and precisely the \(m\) path edges of cut \(i\). In a Cartesian product, every geodesic is monotone in the path coordinate and uses at most one clique edge, because the distance between any two vertices in \(K_m\) is at most one. It also crosses any fixed cut at most once. It therefore uses at most two selected edges. This gives \(\operatorname{gp}_e(G)\ge L\binom{m}{2}+m\).

**Upper bound.** Let \(S\) be any edge-general-position set. For each column \(a\), let \(h_a\) be the number of selected path edges. The entire column induces an isometric path, so \(h_a\le2\). Let \(t\) be the number of columns with \(h_a=2\), \(u\) the number with \(h_a=1\), and \(w\) the number with \(h_a=0\). Hence \(t+u+w=m\), and the number of selected path edges is \(2t+u\).

If \(t>0\), fix one of the \(t\) double-selected columns \(a\). For any different column \(b\), the clique edge \((1,a)(1,b)\) cannot be selected: the geodesic that begins with this edge and then proceeds along all of column \(a\) to layer \(L\) would contain it plus both selected column edges. Similarly \((L,a)(L,b)\) cannot be selected. Thus every clique edge at either endpoint layer with at least one endpoint in a double-selected column is absent. The total number of distinct absent clique edges is at least
\[
2\left(\binom m2-\binom{m-t}{2}\right)=t(2m-t-1).
\]
For \(m\ge3\), this number is at least \(2t>t\); for \(m=2,t=1\), it equals \(2>t\). The only remaining case is \(m=t=2\). Here the two endpoint clique edges are missing. If no further clique edge were missing, all interior clique edges would be selected. Choose a selected path edge in one column at cut \(r\) and a selected path edge in the other column at cut \(s\) with \(r<s\), swapping the roles of the two columns if necessary. Such a pair exists since each column has two distinct selected cuts. The geodesic that follows the first column from layer \(1\) through cut \(r\), switches columns using the selected interior clique edge at layer \(r+1\), and follows the second column through cut \(s\) to layer \(L\), would contain three selected edges. This is impossible. Consequently **in every case with \(t>0\)**, the number of absent clique edges is strictly greater than \(t\). Hence
\[
|S|<L\binom m2+(2t+u)-t
=L\binom m2+t+u
\le L\binom m2+m.
\]

If \(t=0\), at most one path edge is selected per column, so \(|S|\le L\binom m2+u\le L\binom m2+m\). Equality demands \(u=m\) and inclusion of **every** clique edge.

**Rigidity at equality.** Under equality, one path edge is selected in each of the \(m\) columns and every clique edge is selected. Suppose columns \(a\ne b\) use distinct cuts \(r<s\). The geodesic that runs along column \(a\) from layer \(1\) through cut \(r\), switches via the clique edge \((r+1,a)(r+1,b)\), and continues along column \(b\) through cut \(s\) to layer \(L\), uses three selected edges, a contradiction. Thus all columns select their path edge in the same cut. Conversely, the construction proves each such set valid. There are exactly \(L-1\) choices, as claimed. \(\square\)

## Verification

The accompanying standalone `verify.cpp` builds each Cartesian product from its adjacency lists, computes breadth-first-search distances, enumerates shortest paths and forbids every triple of edges that lies on one. An exact backtracking search finds every valid edge set of the claimed cardinality; the program checks these sets are exactly the claimed cut constructions, checks their validity and maximality, and thereby also excludes any larger valid set in the tested instances. Run `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`. Cases checked: \(m=2,3\), \(L=2,3,4,5\), and \(m=4\), \(L=2,3\), with all ten instances returning `OK` and terminal output `VERIFY_OK`. This finite exhaustive check is supplementary; the universal theorem follows from the proof above.

## Relationship to prior work

Manuel, Prabha and Klavžar introduced the edge-general-position parameter and determined it for trees, hypercubes and Cartesian products of two paths. Their subsequent generalized \(k\)-edge-geodesic paper studies tori, cubes and Benes networks, without deriving the present product formula. The present statement is instead a two-parameter *clique–path* product, where the non-bipartite clique factor changes both the optimum and its rigidity. Tian, Klavžar and Tan established extremal and block-graph results; when \(L\ge3\), this product contains induced squares and is not a block graph. Later work by Hamed-Labbafian, Henning and Tavakoli considers hierarchical and corona-type products in the accessible abstract, but its complete text was not available for a definitive comparison. No equivalent complete clique–path extremizer theorem was located in the inspected sources. This negative search is not a proof of publication priority.

## Limitations

The theorem concerns only Cartesian products of one path and one complete graph, with both factors having at least two vertices. It says nothing about other products or more general graph factors. The exhaustive computer checks cover only the listed ten finite instances. Earlier literature under alternate terminology or the inaccessible complete text of the 2026 graph-products paper might contain overlapping results; publication priority therefore remains uncertain. Independent validation has not been performed.

## References

1. P. Manuel, R. Prabha, S. Klavžar, *Edge General Position Problem*, 2021, arXiv:2105.04292v1, https://arxiv.org/abs/2105.04292 (first public version 2021-05-10).
2. J. Tian, S. Klavžar, E. Tan, *Extremal Edge General Position Sets in Some Graphs*, Graphs and Combinatorics 40 (2024), article 40, https://doi.org/10.1007/s00373-024-02770-z.
3. P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357v1, 2022, https://arxiv.org/html/2207.07357v1.
4. Z. Hamed-Labbafian, M. A. Henning, M. Tavakoli, *Edge general position in graphs: Graph products, integer linear programming and some applications*, Discrete Applied Mathematics 386 (2026), 1–8, https://doi.org/10.1016/j.dam.2026.01.008 (abstract consulted; full text unavailable).
