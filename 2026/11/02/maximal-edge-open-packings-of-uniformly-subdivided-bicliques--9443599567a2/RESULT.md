# Maximal edge-open packings of uniformly subdivided bicliques

## Finding

For every integer \(b\ge1\), let \(T_b=\operatorname{Sub}(K_{2,b})\) be the full edge subdivision of the complete bipartite graph with shores of sizes two and \(b\). Equivalently, \(T_b\) consists of \(b\) internally disjoint four-edge paths between two fixed poles. Let \(F_b(z)\) be the polynomial whose coefficient of \(z^j\) is the number of **inclusion-maximal edge-open packings** of cardinality \(j\), with vertex labels fixed.

**Theorem.** For \(b=1,2\), respectively, \(F_1(z)=4z^2\) and \(F_2(z)=4z^4\). For all integers \(b\ge3\),

\[
F_b(z)=2z^{2b}+b(b-1)z^4+4bz^{b+1}+2(2^b-2b-2)z^b.
\]

Contributions at the same exponent are added. Hence \(F_b(1)=2^{b+1}+b^2-b-2\) for \(b\ge3\). The minimum and maximum sizes are 4 and \(2b\), respectively, and exactly two maximal packings attain the maximum. For \(b\ge6\), the full cardinality support is \(\{4,b,b+1,2b\}\). Therefore the interval \(b+2,b+3,\ldots,2b-1\), of length \(b-2\), contains no maximal edge-open-packing cardinality for every \(b\ge3\). These connected bipartite graphs are \(2\)-degenerate, so the gaps occur within a natural sparse graph class.

## Assumptions and scope

All graphs are finite, simple, and labeled. An *edge-open packing* is a set \(D\subseteq E(G)\) such that no pair of distinct edges \(e,f\in D\) has a **third**, distinct graph edge joining an endpoint of \(e\) to an endpoint of \(f\). In particular, incident selected edges may be compatible. *Maximal* means inclusion-maximal, not maximum cardinality. The polynomial counts distinct edge subsets, not isomorphism types; the empty set is not maximal for these graphs. Set \([b]=\{1,\ldots,b\}\); all cardinality and parameter assertions quantify over the ranges explicitly indicated above.

Name the two original degree-\(b\) vertices \(u_0,u_1\), the other original vertices \(v_c\) for \(c\in[b]\), and each subdivision vertex \(s_{r,c}\) for \(r\in\{0,1\}\). Denote the four edges per column by \(L_{r,c}=u_rs_{r,c}\) and \(R_{r,c}=s_{r,c}v_c\). A packing has the unique form \(\{L_{r,c}:(r,c)\in A\}\cup\{R_{r,c}:(r,c)\in B\}\), where \(A,B\subseteq\{0,1\}\times[b]\).

## Proof

**1. Exact compatibility relation.** Every pair of distinct \(L\)-edges is compatible, as is every pair of distinct \(R\)-edges: there is no third edge connecting their endpoint sets. The cross pair \(L_{r,c},R_{q,d}\) is compatible if and only if

\[
(r,c)=(q,d)\quad\text{or}\quad r\ne q\ \text{and}\ c\ne d.
\]

Indeed, if the positions are distinct but share a row, the other \(L\)-edge in that row is a forbidden third edge; if they share a column, the other \(R\)-edge in that column is forbidden. If they differ in both coordinates, there is no connecting third edge. When the positions agree, their only connecting edges are the two selected edges themselves.

**2. Closure criterion for maximality.** For \(X\subseteq\{0,1\}\times[b]\) define

\[
N(X)=\{p: p\text{ is cross-compatible with every position in }X\}.
\]

The universal quantifier is vacuous for the empty set, so \(N(\varnothing)\) is the full \(2b\)-element position set. Since same-type edges never conflict, \((A,B)\) represents an inclusion-maximal edge-open packing if and only if

\[
A=N(B),\qquad B=N(A).
\]

This criterion proves both feasibility and maximality, because any excluded edge on either side is incompatible with at least one selected edge on the opposite side.

**3. Exhaustive closure classification for \(b\ge3\).** The mutually exclusive maximal pairs are as follows, with orientations distinguishing the \(L\) and \(R\) sides.

* **Pure:** \((A,B)=(\varnothing,\text{all})\) or \((\text{all},\varnothing)\). There are two choices, each of size \(2b\).
* **Transverse pairs:** choose different columns \(c\ne d\) and put \(A=B=\{(0,c),(1,d)\}\). There are \(b(b-1)\) choices, each of size four.
* **Singleton versus full compatible neighborhood:** choose a position \(p=(r,c)\). Put \(A=\{p\}\) and \(B=N(\{p\})=\{p\}\cup\{(1-r,d):d\ne c\}\), or swap \(A\) and \(B\). There are \(4b\) choices, each of size \(b+1\).
* **Complementary row blocks:** choose a row \(r\), and a subset \(X\subset[b]\) with \(2\le|X|\le b-2\). Put \(A=\{(r,c):c\in X\}\) and \(B=\{(1-r,c):c\notin X\}\). There are \(2\sum_{k=2}^{b-2}\binom bk=2(2^b-2b-2)\) choices, each of size \(b\). An empty summation equals zero.

For completeness, the closure criterion proves that the classification is exhaustive. If \(A=\varnothing\), then \(B\) is all positions. If \(A\) has one position, its compatible neighborhood is as displayed in the singleton case and closes back to \(A\) for \(b\ge3\). If \(A\) is contained in one row and has \(k\ge2\) positions of column set \(X\), then \(B=N(A)\) consists precisely of the positions in the other row and outside \(X\). If \(2\le b-k\le b-2\), the row-block case results. If \(b-k=1\), closing again adds the one opposite-row position to \(A\), giving the singleton case with sides reversed. If \(b-k=0\), closing gives all positions, yielding the pure case. Finally, if \(A\) meets both rows: when each row contains one position, their columns must be different to admit nonempty \(B\), and closure forces the transverse-pair case; if one row contains at least two positions, compatibility forces \(B\) to be a singleton in the other row, and closure forces the corresponding full-neighborhood singleton case. If \(B\) is empty instead, closure forces \(A\) to be all positions. These possibilities are exhaustive.

Summing the four disjoint types yields the displayed polynomial, since \(\sum_{k=2}^{b-2}\binom bk=2^b-2b-2\) for \(b\ge3\). When \(b=1\), direct application of \(A=N(B),B=N(A)\) gives four size-two packings; when \(b=2\), it gives four size-four packings. The extremal sizes, support and total count now follow by reading coefficients. For \(b\ge6\), all four exponent values are distinct and have positive coefficients, proving the exact four-point support. No inference from finite computation is involved.

## Verification

The standalone Python 3 program `verify.py` constructs \(T_b\) from its edge endpoints. It detects forbidden third-edge witnesses directly, without using the closure theorem. It checks that its resulting conflict graphs agree with the explicit incidence formula for all \(2\le b\le9\), enumerates all \(2^{4b}\) edge subsets for \(2\le b\le5\), and checks maximality by direct possible additions. It independently enumerates fixed points of the closure operation for \(2\le b\le9\). The observed output is

`VERIFY_OK direct_edge_subsets=1118464 incidence_edges=176 closure_parameters=8`

An additional direct check at \(b=1\) confirms the stated boundary polynomial. These finite checks independently corroborate the classifications, but the general proof is the closure argument above.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan introduced/studied the edge-open-packing framework and computed the maximum invariant for familiar graph families [1]. Brešar and Samadi studied complexity, algorithms and upper bounds [2]. Brešar, Dravec, Hedžet and Samadi studied the induced-matching relationship and graph products [3]. Pandey and Santra developed further extremal characterizations [4]. Their accessible full texts do not state the complete **inclusion-maximal edge-open-packing cardinality enumerator for full subdivisions of \(K_{2,b}\)** or its four-point support. The scalar upper bound \(2b\) follows from existing general edge-open-packing bounds on this family, so it is **not** separately asserted as new. The structural classification and distributional gap theorem are the contributions assessed here.

## Limitations

Publication priority is provisional: searches and selected full-text comparisons cannot exclude an unindexed equivalent treatment under another name, for example a maximal-biclique or complement conflict-graph formulation. The statement is exact only for the uniformly length-four theta family \(\operatorname{Sub}(K_{2,b})\); it does not claim the same polynomial for arbitrary theta graphs or arbitrary edge subdivisions. The numerical tests cover finite parameters and are not proofs for all \(b\). No independent mathematical audit has been performed.

## References

1. G. Chelladurai, K. Kalimuthu, and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776, doi:10.1051/ro/2022171. Full text: https://www.numdam.org/item/10.1051/ro/2022171.pdf.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (first posted 2024-03-01), https://arxiv.org/abs/2403.00750.
3. B. Brešar, K. Dravec, T. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first posted 2024-06-06), https://arxiv.org/abs/2406.04020.
4. S. Pandey and S. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935 (first posted 2025-08-03), https://arxiv.org/abs/2508.01935.
