# Grundy total domination of rectangular rook graphs via incidence forests

## Finding

For integers \(2\le p\le q\), let \(R_{p,q}=K_p\square K_q\), the rook graph with vertices the \(p q\) cells \((i,j)\) of a rectangular board. Two distinct cells are adjacent when they share a row or a column. A *legal open-neighborhood sequence* is an ordered sequence \((v_1,\ldots,v_t)\) of distinct cells satisfying
\[
N(v_k)\setminus \bigcup_{h<k}N(v_h)\ne\varnothing\qquad(1\le k\le t).
\]
Its maximum length is the Grundy total domination number \(\gamma_{\mathrm{gr}}^t\). Then
\[
\boxed{\gamma_{\mathrm{gr}}^t(R_{p,q})=p+q-2+\mathbf 1_{\{q=p+1\}}.}
\]
Equivalently, using the established general identity \(\gamma_{\mathrm{gr}}^t(H)=|V(H)|-Z_-(H)\), the skew zero-forcing number is
\[
\boxed{Z_-(R_{p,q})=p q-p-q+2-\mathbf 1_{\{q=p+1\}}.}
\]
The structural assertion behind the formula is that **every legal prefix, translated into the corresponding edges of \(K_{p,q}\), forms a forest**. A legal sequence of length \(p+q-1\) exists precisely when the board dimensions differ by one.

## Assumptions and scope

All graphs are finite, simple, and undirected. Rows and columns of \(R_{p,q}\) are distinguished; the relevant bipartite incidence graph is \(K_{p,q}\) on the row vertices and column vertices, with a board cell representing its corresponding edge. The domain is exactly the integer range \(2\le p\le q\); no assertion about the one-row case is included. Open neighborhoods exclude the vertex itself. The skew zero-forcing convention allows a blue *or white* vertex with exactly one white neighbor to force that neighbor.

## Proof

**1. The uncovered-cell identity.** After a prefix \(S\), let \(H_S\) be the bipartite graph on the \(p+q\) row and column vertices whose edges are the cells already chosen. A row or column is *unused* if it has degree zero in \(H_S\). An edge of \(H_S\) is *isolated* if both its endpoints have degree one (so it forms an isolated \(K_2\) component). The uncovered cells of the rook graph are exactly
\[
U_S=\bigl(\text{unused rows}\times\text{unused columns}\bigr)
\;\sqcup\;\bigl\{\text{cells corresponding to isolated edges of }H_S\bigr\}.
\]
Indeed, any unchosen cell is adjacent to some chosen cell if and only if its row or column has previously been used. A chosen cell has a chosen neighbor if and only if its incidence edge is not an isolated component. These two disjoint possibilities exhaust the uncovered cells.

**2. Every legal prefix is a forest.** Induct on the number of chosen cells. If the next incidence edge has a previously unused row or column as an endpoint, adjoining it cannot create a cycle. Otherwise both endpoints were previously used. The new cell cannot share a row or column with any cell in the unused-row by unused-column rectangle. Thus its legality requires adjacency to a cell corresponding to an isolated incidence edge. One endpoint of the new edge consequently belongs to an isolated-edge component of \(H_S\). Since the chosen edge itself is new, its other endpoint cannot be the opposite endpoint of that isolated edge. It therefore joins *different* components, and again cannot create a cycle. This proves the assertion, including for all intermediate prefixes.

**3. A spanning-tree sequence forces consecutive side sizes.** Any incidence forest on \(p+q\) vertices has at most \(p+q-1\) edges. Suppose a legal sequence attains that length. Then its final incidence graph is a spanning tree. Consider the first prefix at which **either** the entire row side or the entire column side is used. Both sides cannot become exhausted simultaneously at that step: immediately beforehand exactly one row and one column would be unused, so the only cell introducing both of them would have no uncovered neighbor by Step 1.

Let \(b\ge1\) denote the number of unused vertices on the other side at this first-exhaustion prefix. Let \(c\) be the number of its incidence-forest components that contain edges, and let \(s\le c\) be the number of isolated-edge components. (There are no isolated vertices among the used support.) At this time there are no uncovered cells from the unused-row by unused-column rectangle. Every subsequent legal edge must therefore be incident to at least one of those \(s\) isolated edges, by Step 1. Such an addition destroys the isolated-edge status permanently; no new isolated-edge component can be created because one side has already been exhausted. Thus at most \(s\) subsequent edges can be legally appended.

On the other hand, completing a spanning tree requires exactly \(b\) edges to introduce the remaining vertices plus \(c-1\) edges to merge the existing nontrivial components. An edge introducing one vertex cannot simultaneously merge two old components, and no edge introduces two new vertices once one side is exhausted. Hence
\[
b+c-1\le s\le c,
\]
so \(b=1\) and \(s=c\): at the exhaustion prefix every component is an isolated edge. Thus that prefix is a matching covering every vertex of one side and all but one vertex of the other. The side sizes must differ by exactly one. Under \(p\le q\), this means \(q=p+1\). Therefore when \(q\ne p+1\), every legal sequence has length at most \(p+q-2\).

**4. Matching constructions.** Number rows \(0,1,\ldots,p-1\) and columns \(0,1,\ldots,q-1\).

For any \(q\ge p\), choose in order the \(p-1\) diagonal cells
\[
(0,0),(1,1),\ldots,(p-2,p-2),
\]
then the \(q-p+1\) cells
\[
(0,p-1),(0,p),\ldots,(0,q-1),
\]
and finally the \(p-2\) cells
\[
(0,1),(0,2),\ldots,(0,p-2).
\]
Each diagonal cell chosen after the first has a previously uncovered neighbor in its row or column, because at least one additional unused row and column remains. Every cell \((0,j)\) with \(j\ge p-1\) has the uncovered neighbor \((p-1,j)\) (its row is still unused), and each final cell \((0,j)\) destroys the isolated incidence edge \((j,j)\). Hence every choice is legal. The length is \((p-1)+(q-p+1)+(p-2)=p+q-2\).

When \(q=p+1\), instead choose all \(p\) diagonal cells \((0,0),\ldots,(p-1,p-1)\) in order, then \((0,p)\), then \((0,1),\ldots,(0,p-1)\). The final diagonal is legal since two columns are still unused immediately before it; each subsequent choice destroys at least one still-isolated diagonal incidence edge. This sequence has \(p+1+(p-1)=p+q-1\) terms. Combined with Step 3 and the forest bound, this proves the formula for all \(2\le p\le q\).

**5. Skew forcing consequence.** The general duality between Grundy total domination and skew zero forcing gives \(Z_-(R_{p,q})=p q-\gamma_{\mathrm{gr}}^t(R_{p,q})\), producing the displayed second formula. This last step uses the previously established duality; it is not claimed as a new duality theorem.

## Verification

The companion `verify.py` constructs open neighborhoods directly from rook adjacency, not from incidence-forest theory. Memoized exhaustive optimization over dominated-cell masks confirms the formula on all \(22\) boards with \(2\le p\le5\) and \(p\le q\le8\). A separate legal-prefix enumeration for six boards examines all reachable chosen-cell subsets and checks both the forest condition and the exact uncovered-cell identity against original neighborhoods. The finite checks are diagnostic, not substitutes for the proof of the unrestricted statement. Run with `python3 verify.py`; `verification-output.txt` records the results.

## Relationship to prior work

Brešar, Bujtás, Gologranc, Klavžar, Košmrlj, Marc, Patkós, Tuza, and Vizer (2017 preprint; 2021 journal publication) establish the general concept and the skew-zero-forcing duality, investigate standard graph products, and in their Cartesian-product section prove bounds for products of paths and cycles. The examined full text does **not** state the present formula for Cartesian products of two complete graphs or their line-graph representation. Abiad, Brimkov, Breen, Cameron, Gupta, and Villagrán (2022), Section 3.2, determine the *positive-semidefinite* zero-forcing number of square rook graphs. For square rook graphs its numerical expression coincides with the present skew value, but the distinct forcing rule supplies no proof of that equality or the rectangular formula. The closed-neighborhood Grundy domination of complete multipartite graphs is also a different parameter on a different graph family. Here the new incidence-forest invariant explains exactly why the upper bound is attained only for consecutive side sizes.

## Limitations

The domain starts at \(p=2\); the theorem does not enumerate all maximum sequences, nor does it directly generalize to higher-dimensional Hamming graphs or arbitrary line graphs. An unindexed pre-existing formula or a stronger line-graph theorem may exist; bibliographic searches do not prove priority. The derivation of the skew zero-forcing corollary relies on a known duality. Finite tests have a stated finite range, and independent mathematical validation is not claimed.

## References

1. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, T. Marc, B. Patkós, Z. Tuza, and M. Vizer, *On Grundy total domination number in product graphs*, arXiv:1712.08780v1, first public 2017-12-23; *Discussiones Mathematicae Graph Theory* 41 (2021), 225–247. https://arxiv.org/pdf/1712.08780 .
2. A. Abiad, B. Brimkov, J. Breen, T. R. Cameron, H. Gupta, and R. R. Villagrán, *Constructions of cospectral graphs with different zero forcing numbers*, *Electronic Journal of Linear Algebra* 38 (2022), 280–294; particularly Section 3.2. https://pure.tue.nl/ws/portalfiles/portal/206533710/vol38_pp280_294.pdf .
