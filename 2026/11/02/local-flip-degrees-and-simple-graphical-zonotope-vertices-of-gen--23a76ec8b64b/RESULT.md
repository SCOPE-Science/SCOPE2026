# Local flip degrees and simple graphical-zonotope vertices of generalized theta graphs

## Finding
Let \(k\ge3\), let \(\ell_1,\ldots,\ell_k\ge1\) be integers with **at most one** length equal to one, and let \(G=\Theta_{\ell_1,\ldots,\ell_k}\) be the finite simple graph formed by \(k\) internally vertex-disjoint paths joining two common terminals. Write \(m=\sum_i\ell_i\), so that \(G\) has \(n=m-k+2\) vertices. Its acyclic-orientation flip graph \(\mathcal A(G)\) joins two acyclic orientations precisely when they differ by reversing one edge. Let
\[
 D_{\boldsymbol\ell}(z)=\sum_{\omega\text{ acyclic orientation of }G}z^{\deg_{\mathcal A(G)}(\omega)}.
\]
Define \(q_i=2^{\ell_i}-2\) and \(t_i=2^{\ell_i}-\ell_i-2\). Then the **entire local-degree distribution**, with path lengths individually distinguished, is
\[
\boxed{
D_{\boldsymbol\ell}(z)=z^m\left[\prod_{i=1}^{k}q_i+2\left(\prod_{i=1}^{k}(1+t_i+\ell_i z^{-1})-\prod_{i=1}^{k}(t_i+\ell_i z^{-1})\right)\right].
}
\]
The expression is a polynomial with nonnegative integer coefficients, even when a unique length-one path gives \(t_i=-1\). In particular,
\[
\boxed{\left|V(\mathcal A(G))\right|=2\prod_{i=1}^k(2^{\ell_i}-1)-\prod_{i=1}^k(2^{\ell_i}-2).}
\]
The minimum vertex degree is exactly \(n-1=m-k+1\), attained by exactly
\[
\boxed{s(G)=2\sum_{j=1}^k\prod_{i\ne j}\ell_i=2\tau(G)}
\]
orientations, where \(\tau(G)\) is the number of spanning trees of \(G\). Equivalently, the graphical zonotope of \(G\), a polytope of dimension \(n-1\), has exactly \(2\tau(G)\) *simple* vertices. For instance,
\[
D_{(2,3,4)}(z)=52z^7+154z^8+256z^9,
\qquad D_{(1,2,3,4)}(z)=100z^7+322z^8+208z^9.
\]
The formulas cover arbitrarily many paths, arbitrary unequal lengths, and the family with one direct terminal edge.

## Assumptions and scope
All graphs are finite and undirected before orientation. The path edge sets are disjoint and their internal vertices are distinct. A path of length one directly joins the two terminals; more than one such path would introduce parallel edges, which are excluded. Each edge is oriented independently. A directed cycle is a closed directed simple walk. A flip is legal if and only if the changed orientation remains acyclic. No equivalence under graph automorphisms or global orientation reversal is imposed: all acyclic orientations are counted individually. A vertex of a \(d\)-dimensional convex polytope is simple when it is incident with exactly \(d\) edges.

The assertion concerns the full degree polynomial, not merely total orientation counts, total edges of a zonotope, or one fixed-length subfamily. The special all-length-two family \(\Theta_{2,\ldots,2}\cong K_{2,k}\) is an already-covered specialization and is **not** independently asserted as new.

## Proof
**1. Encode acyclicity by path words.** Fix an order of the terminals \(s,t\) and orient the abstract edge order of each path from \(s\) toward \(t\). Record each edge as a plus sign when its actual orientation agrees with this order and as a minus sign otherwise. A directed cycle necessarily follows one entire \(s\)-to-\(t\) path and a different entire \(t\)-to-\(s\) path: this follows because every internal vertex has degree two. Conversely, any pair of oppositely directed complete paths forms a directed cycle. Hence an orientation is acyclic exactly when **no path is all plus and another is all minus**.

**2. Reversibility is a reachability obstruction.** In any acyclic digraph, reversing an arrow \(u\to v\) creates a directed cycle exactly when an alternative directed path from \(u\) to \(v\) avoids that arrow. For an edge of a theta path of length at least two, such an alternative path must leave its own path toward a terminal, traverse a *different* complete terminal-to-terminal path, and return to the original path from the opposite terminal. In the plus case this is possible if and only if the original path contains **exactly one plus sign** (at the considered edge), all its other signs are minus, and another path is all plus. The minus case is the globally reversed condition: exactly one minus sign on the original path and a different all-minus path. Thus a mixed path contributes at most one blocked, nonreversible edge, and it contributes one precisely in those cases. Edges of any all-plus or all-minus path of length at least two are reversible in every acyclic orientation.

**3. Count paths when all lengths are at least two.** There are \(q_i=2^{\ell_i}-2\) mixed sign words on path \(i\). Among them \(\ell_i\) have exactly one plus, while \(t_i=q_i-\ell_i\) have another mixed pattern. If all paths are mixed, no edge is blocked, giving \(\prod_iq_i\) orientations, each of degree \(m\). Otherwise an acyclic orientation has at least one all-plus path and no all-minus path, or its global reverse. In the first class each all-plus path contributes one word, each mixed exactly-one-plus path contributes \(\ell_i\) possibilities and one blocked edge, and each remaining mixed word contributes \(t_i\) possibilities and no blocked edge. With \(x\) marking the number of blocked edges, the enumerator for this class is
\[
\prod_i(1+t_i+\ell_i x)-\prod_i(t_i+\ell_i x),
\]
subtracting the choices with no all-plus path. Doubling for global reversal and adding the all-mixed class gives
\[
F(x)=\prod_iq_i+2\left[\prod_i(1+t_i+\ell_i x)-\prod_i(t_i+\ell_i x)\right].
\]
Since the number of reversible edges is \(m\) minus the number of blocked edges, \(D_{\boldsymbol\ell}(z)=z^mF(z^{-1})\).

**4. Handle a single direct edge.** Suppose \(\ell_1=1\); orient that edge from \(s\) to \(t\), and multiply the resulting enumerator by two to account for global reversal. No other path may be all minus. As before, every non-direct path that has exactly one plus contributes one blocked edge, with \(\ell_i\) choices for its plus position; all-plus paths contribute one choice, and the other mixed words contribute \(t_i\) choices. Additionally, the direct edge itself is blocked **if and only if another path is all plus**, since then an alternative directed \(s\)-to-\(t\) path exists. Therefore the blocked-edge polynomial is
\[
2\left[\prod_{i=2}^k(t_i+\ell_i x)+x\left(\prod_{i=2}^k(1+t_i+\ell_i x)-\prod_{i=2}^k(t_i+\ell_i x)\right)\right].
\]
Putting formally \(q_1=0\), \(t_1=-1\), \(\ell_1=1\) into \(F(x)\) gives exactly this expression. Thus the displayed master formula holds under all the stated simple-graph assumptions. This separate argument also explains why the negative intermediate \(t_1\) causes no negative coefficients.

**5. Extract the minimum degree and simple-vertex count.** In \(F(x)\) the contributions of degree \(k\) in \(x\) cancel between the two products. Hence at most \(k-1\) edges can be blocked, so every degree in \(\mathcal A(G)\) is at least \(m-k+1=n-1\). The coefficient of \(x^{k-1}\) in the difference of products is
\[
\sum_{j=1}^k[(1+t_j)-t_j]\prod_{i\ne j}\ell_i=\sum_{j=1}^k\prod_{i\ne j}\ell_i.
\]
This is strictly positive, even with a direct path, and gives the claimed exact minimum-degree multiplicity \(2\sum_j\prod_{i\ne j}\ell_i\).

Every spanning tree of \(G\) must keep exactly one entire terminal-to-terminal path; otherwise two intact paths form a cycle, or no intact path connects the terminals. Each of the other \(k-1\) paths must have **exactly one** edge removed: deleting none makes a cycle, deleting two or more strands an internal component. Conversely, choosing the one intact path and one deletion edge independently on each other path yields a spanning tree. Therefore
\[
\tau(G)=\sum_{j=1}^{k}\prod_{i\ne j}\ell_i.
\]
The graphical zonotope has intrinsic dimension \(n-1\); its vertices correspond to acyclic orientations and its edges correspond to legal single-edge reversals, as follows from adjacent regions of the graphic hyperplane arrangement. Thus its simple vertices are precisely the minimum-degree orientations, proving \(s(G)=2\tau(G)\). Finally, evaluate \(F(1)\) to obtain the displayed total number of acyclic orientations. This completes the proof.

## Verification
Two reproducible Python 3 programs are supplied. `verify_direct.py` independently builds each graph, tests acyclicity using topological sorting, tests every individual edge reversal, and compares the complete degree histogram against the product formula in 64 small parameter instances with three to six paths and both simple-graph regimes. It also checks the minimum-degree and spanning-tree count. Its successful terminal marker is `GENERAL_THETA_DIRECT_CHECK_PASS cases= 64`.

The second program, `verify_word_and_trees.py`, independently enumerates sign words, their allowable combinations, and blocked-edge patterns. Separately, it counts spanning trees by selecting graph edges and performing union-find cycle/connectivity checks, rather than using the spanning-tree formula as an enumeration algorithm. It compares both enumerations with the theorem in eleven parameter instances. Its successful terminal marker is `WORD_AND_SPANNING_TREE_PASS cases=11`.

These are **finite checks only**. The proof of the all-parameter theorem is the combinatorial argument above. It does not assume the outputs of either program.

## Relationship to prior work
Brown, Hickman, Sokal and Wagner introduced and analyzed the general \(k\)-path theta family through its chromatic polynomial and chromatic roots (arXiv:math/0012033, first posted December 5, 2000). Their Sections 1–2 define the family and compute its chromatic polynomial. The known evaluation at a negative integer supplies the **total** acyclic-orientation count, but does not classify how many individual edges are legally reversible in each orientation.

Grujić, *Counting faces of graphical zonotopes* (arXiv:1604.06931, first posted April 23, 2016), establishes the general graphical-zonotope face enumerator in terms of graphic-matroid flats and acyclic orientations of contractions. Its Sections 2, 4 and 5 provide the orientation/vertex correspondence, intrinsic dimension, and global face counts for selected graph families; they do not provide the theta-family **local vertex-degree polynomial**. A global \(f\)-vector determines total vertices and total edges but generally cannot reconstruct individual vertex degrees.

Ding, *Geometric bijections between spanning subgraphs and orientations of a graph* (2023), studies zonotopal tilings and spanning-subgraph/orientation bijections. That theory has a different equivalence relation and does not supply the asserted theta flip-degree distribution. The all-length-two case is the complete bipartite graph \(K_{2,k}\), already separately analyzed for its orientation-flip degree distribution, and is treated here solely as a consistency specialization. The statement proved here is about arbitrary mixed path lengths, including one direct terminal edge.

## Limitations
The theorem is limited to connected, loopless, **simple** generalized theta graphs with at least three internally disjoint terminal paths. It does not assert the same formula for parallel edges or arbitrary series-parallel graphs. A finite search of prior research records and inspected primary articles supports the originality assessment but cannot establish absolute historical priority; alternative descriptions under graphic-arrangement chamber walls may exist. One broad dissertation on acyclic graph orientations was not fully accessible and remains an explicit literature-comparison risk. Although the formula yields all degrees, it does not determine the complete adjacency graph or shortest-path metric.

## References
1. J. Brown, C. Hickman, A. D. Sokal and D. G. Wagner, *On the chromatic roots of generalized theta graphs*, arXiv:math/0012033, first public posting December 5, 2000. https://arxiv.org/abs/math/0012033
2. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931, first public posting April 23, 2016. https://arxiv.org/abs/1604.06931
3. C. Ding, *Geometric bijections between spanning subgraphs and orientations of a graph*, Journal of the London Mathematical Society 108 (2023), 1082–1120, DOI 10.1112/jlms.12776. https://doi.org/10.1112/jlms.12776
