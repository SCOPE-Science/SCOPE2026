# Maximum Grundy total dominating sequences of book graphs
## Finding
For every integer \(n\ge1\), let the \(n\)-page book graph be
\[
B_n=K_{1,n}\mathbin{\square}P_2.
\]
Write its vertices as spine vertices \(u,v\) and page vertices \(a_i,b_i\), \(1\le i\le n\), with edges \(uv\), \(ua_i\), \(a_ib_i\), and \(b_iv\). Then
\[
\gamma_{\mathrm{gr}}^t(B_n)=2n.
\]
Moreover, with the natural bipartition
\[
L=\{u,b_1,\ldots,b_n\},\qquad R=\{v,a_1,\ldots,a_n\},
\]
a set is the underlying set of a maximum Grundy total dominating sequence if and only if its complement contains exactly one vertex of \(L\) and exactly one vertex of \(R\). Therefore the number of distinct maximum sets is
\[
(n+1)^2,
\]
and the number of ordered maximum Grundy total dominating sequences is
\[
4(2n)!.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A sequence \((x_1,\ldots,x_k)\) of distinct vertices is a legal open-neighborhood sequence when
\[
N(x_i)\setminus\bigcup_{j<i}N(x_j)\ne\varnothing
\]
for every \(i\). If its selected vertices totally dominate the graph, it is a total dominating sequence. A maximum-length such sequence is a Grundy total dominating sequence, and its length is \(\gamma_{\mathrm{gr}}^t\).

The theorem concerns all labeled book graphs \(B_n\) for \(n\ge1\). It counts both underlying maximum vertex sets and ordered maximum sequences. No claim is made about arbitrary Cartesian products or arbitrary bipartite graphs.

## Proof
The graph is bipartite with parts
\[
L=\{u,b_1,\ldots,b_n\},\qquad R=\{v,a_1,\ldots,a_n\}.
\]
Its open neighborhoods are
\[
N(u)=R,\qquad N(b_i)=\{v,a_i\},
\]
and symmetrically
\[
N(v)=L,\qquad N(a_i)=\{u,b_i\}.
\]

Take any legal open-neighborhood sequence \(S\), and retain only its vertices from \(L\). Whether a chosen vertex of \(L\) is legal depends only on earlier chosen vertices of \(L\), because every neighborhood of an \(L\)-vertex lies in \(R\), whereas neighborhoods of chosen \(R\)-vertices lie in \(L\). The same separation holds on the other side. Thus the two side-subsequences can be analyzed independently, and any interleaving of legal side-subsequences remains legal.

Consider the \(L\)-subsequence. If \(u\) is omitted, there are only \(n\) available vertices \(b_i\), and all \(n\) can be chosen in arbitrary order: the first footprints \(v\) and its private \(a_i\), and each later \(b_i\) footprints its still-new \(a_i\). If \(u\) is used, then \(u\) must be last among the chosen \(L\)-vertices, since choosing \(u\) dominates all of \(R\) and makes every later \(L\)-choice illegal. Also, at most \(n-1\) of the \(b_i\) may precede it; if all \(n\) did, they would already dominate all of \(R\), so \(u\) would not be legal. Hence every legal \(L\)-subsequence has length at most \(n\), and equality occurs exactly in one of two forms:

1. all \(b_1,\ldots,b_n\), in arbitrary order; or
2. for some \(j\), all \(b_i\) with \(i\ne j\), in arbitrary order, followed by \(u\).

The same statement, with \(a_i\) and \(v\), holds for the \(R\)-subsequence. Therefore every legal sequence has length at most \(2n\). Choosing a maximum side-subsequence on each side and interleaving them gives a total dominating sequence of length \(2n\), proving \(\gamma_{\mathrm{gr}}^t(B_n)=2n\).

Equality forces both side-subsequences to have length \(n\). On side \(L\), a maximum subsequence omits exactly one vertex of \(L\): either \(u\), or one \(b_j\). Conversely every such omission occurs. The same is true on \(R\). Thus a maximum underlying set is exactly
\[
V(B_n)\setminus\{\ell,r\},\qquad \ell\in L,\ r\in R,
\]
which gives \((n+1)^2\) maximum sets.

For ordered sequences, the number of maximum legal \(L\)-subsequences is
\[
n!+n(n-1)!=2n!.
\]
The first term orders all \(b_i\); the second chooses the omitted \(b_j\), orders the other \(n-1\) vertices, and places \(u\) last. The \(R\)-side contributes another \(2n!\). For each ordered pair of side-subsequences, any choice of the \(n\) positions occupied by the \(L\)-subsequence gives a legal interleaving, so the total is
\[
\binom{2n}{n}(2n!)(2n!)=4(2n)!.
\]
This proves all assertions.

## Verification
The standalone checker `verify.py` reconstructs the graph from the edge definition and computes the maximum legal open-neighborhood length by dynamic programming on the already dominated vertex set. It independently counts all maximum sequences and reconstructs all underlying maximum sets. For every \(1\le n\le7\), it checks \(\gamma_{\mathrm{gr}}^t(B_n)=2n\), the complement classification, the count \((n+1)^2\), and the ordered count \(4(2n)!\). A finite check does not prove the infinite theorem; the proof above supplies the all-\(n\) argument.

## Relationship to prior work
Brešar, Henning, and Rall introduced Grundy total domination and the open-neighborhood sequence definition used here. Their foundational work studies extremal values, trees, regular graphs, and the hypergraph connection, but targeted full-text searches found no book-graph statement.

Brešar et al. later studied Grundy total domination in graph products. Their Cartesian-product section gives bounds for products whose factors are paths and cycles. The book graph \(K_{1,n}\mathbin{\square}P_2\) has a star factor, and targeted full-text searches found no occurrence of “book” or “star” in that paper. In addition, that work concerns the scalar parameter rather than an enumeration of all maximum sets and ordered maximum sequences.

The later identity \(\gamma_{\mathrm{gr}}^t(G)=|V(G)|-Z_-(G)\) links the scalar parameter to skew zero forcing. Searches under that equivalent terminology did not locate a book-graph minimum-set classification or a result that implies the ordered count above. The scalar identity alone does not determine the number of maximum legal sequences.

## Limitations
The theorem is specific to the open-neighborhood Grundy total domination process on book graphs. The exact sequence count uses the special decomposition of the two bipartition sides into independent neighborhood-cover processes and should not be extrapolated to general Cartesian products. Novelty searches reduce but do not eliminate the possibility of an unindexed or differently named equivalent result, especially through skew zero forcing terminology.

## References
1. B. Brešar, M. A. Henning, and D. F. Rall, “Total Dominating Sequences in Graphs,” arXiv:1601.07525, first posted 2016-01-27; later Discrete Mathematics 339 (2016), 1665–1676, DOI:10.1016/j.disc.2016.01.017.
2. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, T. Marc, B. Patkós, Z. Tuza, and M. Vizer, “On Grundy total domination number in product graphs,” arXiv:1712.08780, first posted 2017-12-23.
