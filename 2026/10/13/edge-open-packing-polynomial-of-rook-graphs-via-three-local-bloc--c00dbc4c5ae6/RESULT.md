# Edge-open-packing polynomial of rook graphs via three local blocks

## Finding

For nonnegative integers \(m,n\), let \(R_{m,n}=K_m\square K_n\), with vertices the cells of an \(m\)-by-\(n\) board and adjacency between distinct cells in a common row or column. Define
\[
\mathcal E_{m,n}(z)=\sum_{S\subseteq E(R_{m,n}),\ S\ \mathrm{edge\ open\ packing}}z^{|S|}.
\]
The empty edge set is included. An edge set is an edge-open packing when no edge different from two selected edges joins an endpoint of one to an endpoint of the other.

**Classification.** Every nonempty edge-open packing is a disjoint collection of precisely three possible block types: a horizontal one-edge block using one row and two columns, a vertical one-edge block using two rows and one column, and a two-edge right-angle block using two rows and two columns. Different blocks use disjoint row labels **and** disjoint column labels. Conversely, every such block collection is an edge-open packing.

**Full enumerator.** In the ring of formal power series in \(u,v\) with polynomial coefficients in \(z\),
\[
\boxed{\sum_{m,n\ge0}\mathcal E_{m,n}(z)\frac{u^m v^n}{m!n!}
=\exp\!\left(u+v+\frac{uv^2z}{2}+\frac{u^2vz}{2}+u^2v^2z^2\right).}
\]
Equivalently, for all \(m,n\ge0\),
\[
\boxed{\mathcal E_{m,n}(z)=
\sum_{\substack{a,b,c\ge0\\a+2b+2c\le m\\2a+b+2c\le n}}
\frac{m!n!\,z^{a+b+2c}}{
(m-a-2b-2c)!\,(n-2a-b-2c)!\,a!\,b!\,c!\,2^{a+b}}.}
\]
Here \(a,b,c\) count the horizontal, vertical and right-angle blocks, respectively. A useful distinguished-row recurrence is
\[
\begin{aligned}
\mathcal E_{m+1,n}(z)={}&\mathcal E_{m,n}(z)
+\binom n2z\mathcal E_{m,n-2}(z)
+mnz\mathcal E_{m-1,n-1}(z)\\
&+2mn(n-1)z^2\mathcal E_{m-1,n-2}(z),
\end{aligned}
\]
where \(\mathcal E_{m,n}=0\) for a negative index, and \(\mathcal E_{0,n}=\mathcal E_{m,0}=1\) for nonnegative indices.

**Extremal consequence.** For positive integers \(m,n\), the maximum number of edges in an edge-open packing satisfies
\[
\boxed{\rho_e^o(R_{m,n})=\min\{m,n\}-\mathbf 1_{\{m=n\ \mathrm{odd}\}}.}
\]
Thus the only loss from the smaller side length is one edge when the board is an odd square; the one-cell graph has maximum zero.

## Assumptions and scope

Graphs are finite, simple and undirected. Rows and columns are separately labeled. The case of a board with zero rows or columns is an empty graph included solely for the generating function and recurrence. Unlike the original nonempty-set convention for edge-open packings, the enumerator includes the empty set as its constant term. The proofs apply without asymptotics or randomness.

## Proof

**Lemma 1 (induced stars).** For any simple graph, an edge set \(S\) is an edge-open packing if and only if the subgraph induced on the endpoints of \(S\) is a disjoint union of induced stars and \(S\) comprises exactly their edges. Indeed, two selected incident edges cannot have adjacent other endpoints, since that connecting edge would be common to them. Three selected edges along a path cannot occur, since its middle edge would be common to the first and third. Therefore each component of the selected-edge subgraph is a star, and there can be no other graph edge between or within those components: any such extra edge joins endpoints of two selected edges and witnesses a forbidden pair. Conversely, any union of isolated induced stars has no third edge linking two selected edges.

**Lemma 2 (three block types).** Every vertex \((i,j)\) of \(R_{m,n}\) has a neighborhood consisting of the same-row cells and the same-column cells, each a clique. Consequently, no vertex has three pairwise nonadjacent neighbors; every induced star has one or two edges. A one-edge star is horizontal or vertical. An induced two-edge star has one horizontal and one vertical edge at its center, thus occupies exactly two rows and two columns. The latter shape has four choices of center on any labeled \(2\)-by-\(2\) subboard. If two distinct stars used a common row, an endpoint of one and a different endpoint of the other in that row would be adjacent; the same applies to a shared column. Lemma 1 therefore forces row-and-column disjointness. Conversely, stars on disjoint row and column sets have no edges between them. This proves the classification.

**Lemma 3 (enumeration).** Treat unused rows and unused columns as singleton labeled species with weights \(u\) and \(v\). A horizontal block has \(1\) row and \(2\) columns, hence weight \(uv^2z/2\) in a bivariate labeled exponential series. A vertical block has weight \(u^2vz/2\). A right-angle block has \(2\) rows, \(2\) columns, two selected edges, and four possible centers, so its weight is \(4u^2v^2z^2/(2!2!)=u^2v^2z^2\). Every packing decomposes uniquely into an unordered family of disjoint labeled components of these five sorts (two unused-label sorts and three selected-edge sorts). The exponential formula yields the displayed generating function. Expanding each component exponential and extracting \(m!n![u^mv^n]\) yields the finite triple sum, with unused row and column counts as shown. Alternatively distinguish one of \(m+1\) rows. It is unused or belongs to exactly one of the three block types; choosing its partner row and/or columns, and the four possible right-angle centers, gives the stated recurrence.

**Lemma 4 (maximum).** If a packing contains \(a,b,c\) blocks of the three types, it uses \(a+2b+2c\) rows, \(2a+b+2c\) columns, and \(a+b+2c\) edges. Each resource count is at least the edge count, so \(\rho_e^o\le\min\{m,n\}\). If an odd square achieved exactly \(m=n\) edges, both resource inequalities would be equalities; hence \(a=b=0\), and the number of edges would equal \(2c\), contradicting oddness. Therefore the odd-square upper bound improves by one.

The bounds are attained as follows. If \(s=\min\{m,n\}\) is even, choose \(s/2\) disjoint right-angle blocks. If \(s\) is odd and the board is nonsquare, use \((s-1)/2\) right-angle blocks and one horizontal block when rows are fewer, or one vertical block when columns are fewer; the longer side has at least \(s+1\) labels. If the board is an odd square, use \((s-1)/2\) right-angle blocks. The constructions also cover \(s=1\). This proves the extremal formula. \(\square\)

## Verification

The included standard-library script `eop_rook_verify.py` independently builds the rook graph's edge set, tests each edge subset by searching for an explicit forbidden third edge, and compares its full cardinality histogram with the factorial coefficient formula. It exhaustively checks \(328221\) candidate edge subsets on nine boards, including the empty board and all rectangle sizes up to \(3\)-by-\(3\) that fit the exhaustive budget. On \(3\)-by-\(4\) and \(4\)-by-\(4\) boards it additionally checks \(217579\) subsets with size at most the proved maximum. For \(225\) pairs of side lengths with \(0\le m,n\le14\), it additionally compares the factorial formula against the distinguished-row recurrence, verifies transpose symmetry, checks the one-edge coefficient and the exact extremal degree. The script output is included separately. This finite verification is not a proof for unbounded parameters; Lemmas 1–4 provide that proof.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan (2022) introduced edge-open packing, gave the basic induced-star observation, and computed the maximum for several standard graph families including paths, cycles, complete multipartite graphs, wheels and the Petersen graph. Brešar and Samadi (2024) studied complexity, bounds, and a tree algorithm. Brešar, Dravec, Hedžet and Samadi (2024) studied EOP in graph products and proved general sharp lower bounds for Cartesian and strong products. Those general bounds do not state the rook-graph size distribution, and the family \(K_m\square K_n\) is not among their exact complete polynomial evaluations. Bhanupriya, Dominic and Sunitha (2023) treated injective edge chromatic indices, a related but different invariant; its Cartesian-product formulas concern paths and cycles rather than a polynomial enumerating individual color classes on rook graphs. Pandey and Santra (2025) characterize values of the EOP number on broad graph classes but do not enumerate these rook-graph edge subsets. The present statement refines EOP from a maximum parameter to the complete distribution on an infinite two-parameter graph family.

## Limitations

The theorem concerns only rectangular rook graphs, not arbitrary Cartesian products or arbitrary line graphs. No formula for injective edge chromatic index, for multicolor partitions into EOP sets, or for asymptotic coefficient profiles is asserted. The literature comparison is based on the named examined sources and targeted searches; an equivalent formula under other terminology in older induced-star enumeration literature remains a residual novelty risk. 
## References

1. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, https://doi.org/10.1051/ro/2022171 (published online 2022-11-01).
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (2024), https://arxiv.org/abs/2403.00750.
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (2024), https://arxiv.org/abs/2406.04020.
4. C. K. Bhanupriya, C. Dominic and M. S. Sunitha, *Injective edge coloring of product graphs and some complexity results*, Filomat 37 (2023), 3963–3983, https://www.pmf.ni.ac.rs/filomat-content/2023/37-12/37-12-20-18771.pdf.
5. A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935 (2025), https://arxiv.org/abs/2508.01935.
