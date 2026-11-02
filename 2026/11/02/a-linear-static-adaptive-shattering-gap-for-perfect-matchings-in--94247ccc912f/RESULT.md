# A linear static–adaptive shattering gap for perfect matchings in connected subcubic planar graphs

## Finding
For every integer \(m\ge1\), there is an explicitly described connected, planar, bipartite graph \(G_m\) on \(10m\) vertices, with maximum degree three, whose perfect-matching edge-membership concept family \(\mathcal P(G_m)\) satisfies
\[
\operatorname{VCdim}(\mathcal P(G_m))=2m,\qquad
\operatorname{Ldim}(\mathcal P(G_m))=3m.
\]
Thus the adaptive-minus-static dimension gap equals \(m\), even under all four graph restrictions. The building block is the two-row, five-column ladder \(B=P_2\mathbin{\square}P_5\), for which the dimensions are exactly \(2\) and \(3\).

## Assumptions and scope
Graphs are finite, simple and undirected. Let \(B\) have vertices \(u_i,v_i\) for \(1\le i\le5\), vertical edges \(u_iv_i\), and horizontal edges \(u_iu_{i+1},v_iv_{i+1}\) for \(1\le i<5\). A hypothesis is an entire perfect matching \(M\), evaluated by \(h_M(e)=1\) if \(e\in M\) and zero otherwise. VC dimension uses one fixed set of distinct edge queries. Littlestone dimension uses a complete adaptively edge-labeled binary tree, with each root-to-leaf sequence realized by some perfect matching.

Form \(G_m\) from disjoint labeled copies \(B_1,\ldots,B_m\) by adjoining exactly the bridge \(u_5^{(j)}v_1^{(j+1)}\) for \(1\le j<m\), with no other interblock edges. The row/column checkerboard coloring makes each bridge bipartite. Each used corner has degree two inside its block, so the joined graph is connected, planar and has maximum degree three.

## Proof
**1. Eight local concepts.** A perfect matching of \(B\) decomposes uniquely into vertical columns (denoted \(1\)) and pairs of adjacent columns spanned by both horizontal edges (denoted \(2\)). Hence its perfect matchings correspond bijectively to the eight compositions of five with parts one or two:
`11111, 1112, 1121, 1211, 2111, 122, 212, 221`.

**2. Static dimension of one block.** The two vertical-edge queries \(u_1v_1\) and \(u_4v_4\) realize all four binary patterns in those eight matchings, so the VC dimension is at least two. A shattered three-query support would require eight distinct concepts, one per pattern. Thus every one of its three queries would be positive on exactly four of the eight matchings. Directly from the eight compositions, the five vertical-edge positive counts (in column order) are \(5,3,4,3,5\), and the eight horizontal-edge positive counts (two edges at each of four positions) are \(3,3,2,2,2,2,3,3\). Only the central vertical edge occurs in exactly four concepts, so no three distinct edges can be shattered. The VC dimension is exactly two.

**3. Adaptive dimension of one block.** A depth-three shattered tree is explicit. At the root query the vertical edge in column three. On a positive response, query the vertical edge in column one, then the vertical edge in column four on either branch. On a negative response, query the top horizontal edge joining columns two and three; if positive, query the vertical edge in column four, and if negative, query the vertical edge in column one. All eight answer words of length three occur, and they correspond to eight distinct compositions listed above. Hence the Littlestone dimension is at least three. Eight concepts cannot realize all leaves of a tree of depth four, so the dimension is exactly three.

**4. Bridges cannot lie in perfect matchings.** Each joining edge is a bridge. Deleting the bridge between blocks \(j\) and \(j+1\) separates vertex sets of sizes \(10j\) and \(10(m-j)\), both even. If the bridge belonged to a perfect matching, deleting its endpoints would leave an odd number of unmatched vertices on either side with no other crossing edge, a contradiction. Consequently every perfect matching of \(G_m\) is precisely a freely chosen perfect matching from each of its \(m\) blocks, and each bridge query is constantly false. There are exactly \(8^m\) hypotheses.

**5. Exact dimensions of the connected graph.** The two local VC queries in each block combine to shatter \(2m\) queries. Conversely, any shattered query set cannot contain a constant bridge query, and its restriction to each block must be shattered by that block's eight-concept family; therefore it contains at most two queries per block. This gives VC dimension \(2m\). Concatenating the explicit depth-three tree of each block, proceeding to the next block after each leaf of the previous, gives a complete depth-\(3m\) tree with all \(8^m\) distinct product witnesses. The cardinality bound \(2^d\le|\mathcal P(G_m)|=8^m\) for any shattered depth \(d\) gives the reverse inequality. Thus Littlestone dimension is \(3m\).

## Verification
The accompanying dependency-free `check.py` independently enumerates all perfect matchings from the graph's edge list, checks the local VC supports, realizes all eight adaptive answer words, and confirms that two connected copies have exactly \(64\) perfect matchings with the bridge absent. Its recorded output is in `check_output.txt`. The infinite result follows from the bridge parity and product arguments above, not from finite extrapolation.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805, first publicly posted September 10, 2021) calculate equal VC and Littlestone dimensions for zero sets of linear combinations; those zero-set families are not perfect-matchings of ladder graphs. Ghazi, Golowich, Kumar and Manurangsi (PMLR 132, 2021) obtain general aggregation closure bounds, not exact edge-membership dimensions of matching families. Classical Fibonacci enumeration of ladder domino tilings supplies the local composition correspondence but not this dimension computation. The claim here is the concrete connected-graph separation, not the standard concepts of VC/Littlestone dimension, the general cardinality bound, or general product additivity.

## Limitations
No formula is asserted for arbitrary perfect-matching graphs or ordinary uninterrupted ladders of every length. This particular bridge-connected family is not two-vertex-connected. Searches do not establish complete historical novelty; equivalent results under dimer-tiling or online matching terminology may exist.

## References
1. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (2021), https://arxiv.org/abs/2109.04805 .
2. B. Ghazi, N. Golowich, R. Kumar and P. Manurangsi, *Near-tight closure bounds for the Littlestone and threshold dimensions*, PMLR 132 (2021), 686–696, https://proceedings.mlr.press/v132/ghazi21a.html .
