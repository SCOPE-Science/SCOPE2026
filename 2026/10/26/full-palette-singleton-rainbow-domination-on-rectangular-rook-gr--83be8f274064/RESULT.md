# Full-palette singleton rainbow domination on rectangular rook graphs

## Finding
For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\), with vertices the \(m\times n\) board cells and edges joining cells in a common row or column. Its degree is \(r=m+n-2\). A *singleton rainbow \(r\)-dominating function* assigns to each cell either no color or one label from \(\{1,\ldots,r\}\); every uncolored cell must see all \(r\) distinct labels among its neighbors. A *support* here means the set of **uncolored** cells, not the selected/colored set.

Set \(\varepsilon_{m,n}=1\) if \(m\) is odd and \(n\in\{m,m+1\}\), and \(\varepsilon_{m,n}=0\) otherwise. A cell set is a feasible uncolored support if and only if it is a placement of nonattacking rooks (at most one cell per row and per column) and either has fewer than \(m\) cells or \(\varepsilon_{m,n}=0\). Consequently, the polynomial enumerating *distinct feasible uncolored supports*, with no multiplicity for assignments of colors, is
\[
F_{m,n}(z)=\sum_{j=0}^{m}\binom{m}{j}\binom{n}{j}\,j!z^j-\varepsilon_{m,n}\frac{n!}{(n-m)!}z^m.
\]
This coincides with the classical nonattacking-rook (independence) polynomial when the exception indicator is zero; for an odd nearly-square board it deletes exactly the top matching coefficient. The minimum number of colored vertices is
\[
\widetilde\gamma_{r}(R_{m,n})=mn-m+\varepsilon_{m,n}.
\]
The number of distinct optimal uncolored supports is \(n!/(n-m)!\) when \(\varepsilon_{m,n}=0\), and \(m\binom n{m-1}(m-1)!\) when \(\varepsilon_{m,n}=1\). The result concerns the singleton-label model, not standard multicolored-vertex rainbow domination.

## Assumptions and scope
All graphs are finite, simple, undirected and labeled by their row and column coordinates. Integers satisfy \(2\le m\le n\). The palette has exactly \(r=m+n-2\) labels, one per colored cell, and an uncolored cell sees all palette labels if and only if its \(r\) neighbors receive pairwise distinct labels. Feasibility is existential over assignments to the colored cells; \(F_{m,n}\) counts uncolored supports, not the number of different assignments or their color permutations. We use \(\chi'(H)\) for the smallest number of colors in a proper edge-coloring of a multigraph \(H\), in which parallel edges must receive distinct colors.

## Proof
**Step 1: The support is a matching.** Every uncolored cell has precisely \(r\) neighbors and needs to see \(r\) different singleton colors. None of its neighbors can be uncolored. Therefore two uncolored cells never share a row or column, and their set corresponds to a size-\(j\) matching in the complete bipartite graph \(K_{m,n}\), for some \(0\le j\le m\).

**Step 2: The doubled-clique obstruction is necessary.** Permute rows and columns so that the uncolored cells are \((i,i)\), for \(0\le i<j\). For every distinct \(i,h<j\), the two board cells \((i,h)\) and \((h,i)\) are colored cells adjacent to *both* uncolored cells \((i,i)\) and \((h,h)\). No other colored cell has two uncolored neighbors: an intersection of an uncolored row and another uncolored column is one of the displayed two cells. Hence these \(j(j-1)\) colored cells form the edge set of the doubled complete multigraph \(2K_j\), with an edge incident to each uncolored vertex it touches. The singleton labels on these cells must be distinct at each uncolored vertex, so they give a proper edge-coloring of \(2K_j\) using no more than \(r\) labels. For \(j\in\{0,1\}\) this condition is vacuous.

**Step 3: The edge-coloring obstruction is sufficient.** Conversely suppose \(2K_j\) has a proper edge-coloring with at most \(r\) labels. Assign these labels to the corresponding \((i,h)\) and \((h,i)\) cells. At each uncolored cell, all already colored adjacent cells have different labels. Its other adjacent cells are neighbors of no other uncolored cell (by Step 2). Assign to these other cells the remaining unused labels in any order, one per cell. There are exactly as many such remaining adjacent cells as remaining labels, since the uncolored cell has degree \(r\). Finally assign an arbitrary palette label to every still unassigned cell. Every uncolored cell now sees all \(r\) labels, with no conflict between their requirements. Thus a nonattacking \(j\)-rook placement is feasible exactly when \(\chi'(2K_j)\le r\).

**Step 4: Exact doubled-clique edge-chromatic index.** For even \(j\ge2\), a 1-factorization of \(K_j\) into \(j-1\) perfect matchings, duplicated with disjoint labels, gives a proper coloring of \(2K_j\) with \(2(j-1)\) colors; this equals its maximum degree, so
\[\chi'(2K_j)=2(j-1)\quad(j\ge2\text{ even}).\]
For odd \(j\ge3\), every matching has at most \((j-1)/2\) edges and \(2K_j\) has \(j(j-1)\) edges, forcing at least \(2j\) colors. This is attained by two disjoint color palettes, each of size \(j\), on the two copies of \(K_j\). For example, with vertices \(0,\ldots,j-1\), assign color \((i+h)/2\pmod j\) to the first edge \(\{i,h\}\) (division by two means multiplication by its inverse modulo odd \(j\)); each color class is a near-perfect matching. Duplicate these \(j\) colors for the second copy. Thus
\[\chi'(2K_j)=2j\quad(j\ge3\text{ odd}),\]
and the empty and one-vertex cases require no colors.

**Step 5: Determine the feasible support sizes.** For even \(j\le m\), \(2(j-1)\le2m-2\le m+n-2=r\). For odd \(j<m\), \(2j\le2m-2\le r\). For odd \(j=m\), the condition becomes \(2m\le m+n-2\), equivalently \(n\ge m+2\). Hence all nonattacking placements are feasible except the maximum-size placements when \(m\) is odd and \(n\in\{m,m+1\}\).

**Step 6: Count supports and optimize.** Choosing \(j\) of the \(m\) rows, \(j\) of the \(n\) columns, and a bijection between them gives \(\binom{m}{j}\binom{n}{j}\,j!\) nonattacking placements. Remove the forbidden top coefficient when appropriate. The maximum feasible uncolored size is \(m-\varepsilon_{m,n}\); since weight equals \(mn-j\), the optimum and its multiplicity follow. This proves all assertions for every \(2\le m\le n\).

## Verification
A standalone dependency-free program `verify_rook.py` supplies explicit constructions using round-robin one-factorizations for even support size and modular near-one-factorizations for odd support size. It independently checks the complete rainbow condition on \(917\) constructed board assignments across \(2\le m\le15\) and \(m\le n\le m+6\). A separate backtracking constraint solver checked feasibility versus the theorem on \(51\) small parameter triples. Its recorded output ends in `VERIFY_OK`. The program and its output accompany this result. These tests are finite checks only; the proof above establishes the unrestricted statement.

## Relationship to prior work
Piotr Lange's October 2026 preprint defines and studies the same singleton rainbow parameter on regular graphs, proves the general independence-number bound \(\widetilde\gamma_r(G)\ge |V(G)|-\alpha(G)\), and determines values for cycles, Möbius ladders, prisms and selected generalized Petersen graphs. For the rook graph the bound alone yields \(mn-m\); it does not supply the odd nearly-square obstruction, the sufficiency characterization of all uncolored supports, or their generating polynomial. The full preprint, including its appendices, was checked for this claimed distinction.

Stephan Mertens's 2024 rook-graph domination polynomial counts *ordinary dominating sets*, not feasible uncolored supports of full-palette singleton rainbow assignments. Its rook-board methods motivate comparison but its formula cannot replace the two-neighbor color-consistency obstruction. Earlier singleton-rainbow work on cylindrical graphs concerns products of paths and cycles with a fixed smaller palette, not arbitrary complete-graph products. Classical complete-graph one-factorization and edge-coloring facts are used as standard ingredients, not claimed as new.

## Limitations
The theorem counts support sets only, not all colored-label assignments. Its formula need not apply when multiple labels may be placed at a vertex, when fewer colors than the degree are required, or to rook graphs with deleted edges. This is a mathematical proof with finite code checks, not an independently certified result. Relevant earlier articles may contain an equivalent conclusion under different terminology; bibliographic priority is not definitively established.

## References
1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1 (first posted 2026-10-01), https://arxiv.org/html/2610.06906v1 .
2. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences **27** (2024), Article 24.3.7, https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.html .
3. J. Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, Mathematics **14** (2026), 2917, https://doi.org/10.3390/math14162917 .
