# A mobility threshold for minimum two-quasiperfect domination on rook graphs

## Finding

**Theorem.** For integers \(3\le m\le n\), let \(R_{m,n}=K_m\square K_n\), with vertices the squares \((i,j)\) of an \(m\)-by-\(n\) board. A two-quasiperfect dominating set \(S\) is a set for which every square outside \(S\) has either one or two neighbors in \(S\). All minimum sets have \(m\) vertices, and the following is their complete classification.

* If \(m<n\), the minimum sets are exactly (a) the \((n)_m=n!/(n-m)!\) placements of one rook in each row and in pairwise distinct columns, and (b) the \(n\) complete columns. There are \((n)_m+n\) minimum sets. Under a legal replacement of exactly one selected square, the state graph is the disjoint union of \(n\) isolated vertices and the arrangement graph \(A(n,m)\) on injective maps \([m]\to[n]\), adjacent when they differ in one coordinate. This component is connected, has degree \(m(n-m)\) at each vertex, radius and diameter \(m+\lfloor m/2\rfloor\), and \((n)_m m(n-m)/2\) edges.
* If \(m=n\), the minimum sets are exactly the \(n!\) permutation placements, the \(n\) complete rows, and the \(n\) complete columns. The number of minimum sets is \(n!+2n\); every such set is isolated under one-square replacement.

The same statements for legal one-square **slides** (new square required to be adjacent to the vacated square in the rook graph) hold: their reconfiguration graph coincides with the unrestricted one-square replacement graph in every case here.

In particular, increasing one board dimension from \(n\) to \(n+1\) changes a completely frozen minimum-configuration space into one with a large connected component. The case of a two-row or two-column board is explicitly excluded because the underlying classification was already observed in the foundational literature.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by board coordinates. Two board squares are adjacent if they share a row or a column and are distinct. No restriction is imposed on the number of selected neighbors of an **inside** square. A token jump replaces one selected square by an unselected square while preserving the exact minimum cardinality and the two-quasiperfect property; a token slide further requires that the removed and added squares are adjacent in \(R_{m,n}\). The arrangement graph \(A(n,m)\) has injective functions from the rows to columns as its vertices. The ranges \(3\le m\le n\) are essential to the stated formulas; switching the factors handles \(3\le n<m\). Graphs with a dimension one or two are not part of the theorem.

## Proof

Let \(r_i=|S\cap (\{i\}\times[n])|\) and \(c_j=|S\cap([m]\times\{j\})|\). An outside square \((i,j)\notin S\) has exactly \(r_i+c_j\) neighbors in \(S\), so feasibility is equivalent to
\[
1\le r_i+c_j\le2\qquad ((i,j)\notin S).
\]

If \(|S|<m\), some row and (because \(n\ge m\)) some column are empty. Their intersection is not dominated. Hence every two-quasiperfect dominating set has at least \(m\) squares. An injection selecting one square in each row and distinct columns attains this bound: every outside square has one or two selected neighbors. Therefore the minimum is \(m\).

Suppose first \(m<n\) and \(|S|=m\). Since \(m<n\), at least one column is empty. If any row were empty, its intersection with that empty column would be undominated. Hence every row contains exactly one selected square. A column containing \(c_j\) selected squares with \(2\le c_j\le m-1\) would have an unselected square in a row with \(r_i=1\); it would have at least three selected neighbors. Thus every column count is \(0\), \(1\), or \(m\). If one column has count \(m\), it is the whole selected set. Otherwise all positive column counts are one, so the configuration is the graph of an injection \([m]\to[n]\). Both types satisfy the condition, proving classification and count.

If \(m=n\) and \(|S|=n\), the existence of both an empty row and an empty column would again leave an undominated square. So either every row or every column is occupied. In the former case each row contains exactly one square, and the preceding column-count argument yields either a permutation placement or a complete column. In the latter case the transposed argument yields a permutation placement or a complete row. These three kinds are disjoint for \(n\ge3\) and all are feasible, proving their count.

In the rectangular case \(m<n\), distinct complete columns have no common selected square. A complete column and an injection placement have exactly one common square, hence differ in \(m-1\ge2\) selected squares. They are all isolated under a single replacement. Two injection placements differ in one square precisely when their corresponding functions differ at one row. Such an exchange is always a slide because the two squares share that row. Each injection has \(m(n-m)\) adjacent injections: choose one of \(m\) rows and one of \(n-m\) unused columns. Since an unused column is always available, one can transform any injection to any other; the exact distances are established below.

For injective maps \(f,g:[m]\to[n]\), write \(t=|\{i:f(i)\ne g(i)\}|\). On the mismatched rows draw an arc from \(i\) to the unique row currently holding \(g(i)\), when such a row exists. The resulting dependency digraph is a disjoint union of paths and directed cycles, with every cycle of length at least two. Let \(c\) be its number of directed cycles. Following a dependency path from the free desired column lets each of its mismatched rows be corrected with one replacement. A directed cycle of length \(\ell\) can be corrected in \(\ell+1\) replacements, using any currently free column as a temporary buffer. These operations yield a path of length \(t+c\). Conversely, every mismatched row must change at least once, and each initially closed dependency cycle requires an additional move: its first changed row cannot be moved directly to its occupied desired column. Different cycles require different extra moves. Thus the exact distance is \(t+c\). As \(c\le\lfloor t/2\rfloor\) and \(t\le m\), the diameter is at most \(m+\lfloor m/2\rfloor\). Equality is attained by permutations of the occupied columns that are products of disjoint transpositions when \(m\) is even, and of disjoint transpositions together with one 3-cycle when \(m\) is odd. The \(S_m\times S_n\) coordinate-action is transitive on injections and preserves adjacency, so radius equals diameter.

For the square case \(m=n\ge3\), two different permutations differ in at least two selected squares. A complete row or column meets any permutation in exactly one square, hence differs from it in \(n-1\ge2\) selected squares. Two distinct complete rows or columns have intersection zero or one and likewise differ in at least two squares. Thus every optimum is frozen. Because every legal one-replacement move between injection placements replaces a square in a fixed row and all other cases have no moves, the slide and unrestricted-exchange graphs coincide.

## Verification

The independently written programs `check_exhaustive.py` and `check_independent.py` use only Python's standard library. Execute from the directory containing the accompanying artifacts:

```sh
python check_exhaustive.py
python check_independent.py
```

The first program enumerates all subsets with fewer than \(m\) squares, all minimum-cardinality subsets, their exact feasibility, both exchange graphs and all distances for the nine boards \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\). The second constructs predicted sets independently with row/column masks for all \(2\le m\le5\), \(m\le n\le7\), checks feasibility and counts, independently checks exchange edges for small cases, and verifies the dependency-cycle distance formula against breadth-first search on five arrangement graphs. Both report `PASS`; their exact recorded outputs are provided as `exhaustive_output.json` and `independent_output.json`. Checks involving a two-row board are regression tests of an already-covered boundary and are not part of the new theorem. These finite checks support but do not replace the all-order proof.

## Relationship to prior work

Chellali, Haynes, Hedetniemi, and McRae (2013) introduced \([1,2]\)-sets and, in their Question 15, explicitly described a family of \([1,2]\)-sets in \(K_p\square K_2\). That two-row boundary is not claimed as new. Cáceres, Hernando, Mora, Pelayo, and Puertas made their general graph results publicly available on November 28, 2014. Their general claw-free-graph theorem (Theorem 1 in the 2017 journal version) gives equality between the minimum two-quasiperfect domination number and the ordinary domination number for rook graphs, since rook graphs are line graphs. Thus the numerical minimum \(m\) is also not claimed as new. Day and Tripathi (1992) introduced arrangement graphs and studied their existing degree, symmetry, and diameter properties; in particular the diameter \(\lfloor 3m/2\rfloor\) is not an independent novelty claim. What is asserted here is the new identification of the full optimum two-quasiperfect configuration space with \(n\) isolated states plus this known graph, and the completely frozen square-board boundary. The explicit distance proof is supplied for self-containment, not as a claim of priority over arrangement-graph theory.

The original full published 2017 paper was examined through its freely accessible journal PDF and its full-text preprint. The 2013 paper's online text and bibliographic record were examined, including its product example. Searches for aliases \([1,2]\)-sets, two-quasiperfect domination, rook graph, line graph of a complete bipartite graph, and optimal-set reconfiguration did not identify a prior complete configuration-space theorem for these ranges. This negative search is not a guarantee of historical priority.

## Limitations

The theorem concerns only minimum-cardinality two-quasiperfect dominating sets, not all feasible sets or higher quasiperfection thresholds. It excludes dimensions one and two from the new claim, and does not assert independent scholarly validation or absolute historical priority. Bibliographic indexing is incomplete; potentially relevant unindexed dissertations or tables may contain stronger results. The smaller-subset enumerations are finite checks and not proofs for arbitrary orders.

## References

1. M. Chellali, T. W. Haynes, S. T. Hedetniemi, A. McRae, “[1,2]-sets in graphs,” *Discrete Applied Mathematics* 161 (2013), 2885–2893. DOI: 10.1016/j.dam.2013.06.012.
2. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, “On Perfect and Quasiperfect Domination in Graphs,” arXiv:1411.7818v1, first posted 2014-11-28; journal version “On Perfect and Quasiperfect Dominations in Graphs,” *Filomat* 31 (2017), 413–423, DOI: 10.2298/FIL1702413C.
3. K. Day and A. Tripathi, “Arrangement graphs: a class of generalized star graphs,” *Information Processing Letters* 42 (1992), 235–241. DOI: 10.1016/0020-0190(92)90030-Y.
4. Standard rook-graph identity \(R_{m,n}=K_m\square K_n=L(K_{m,n})\); used here only as an elementary identification of the objects.
