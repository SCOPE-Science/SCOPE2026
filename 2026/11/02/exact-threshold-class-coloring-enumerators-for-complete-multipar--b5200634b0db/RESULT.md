# Exact threshold-class coloring enumerators for complete multipartite graphs

## Finding
Let \(r\ge1\) and \(n_1,\ldots,n_r\ge1\) be integers. Give the vertices of the labelled complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) distinct identities, with the prescribed \(r\) partite sets. A *threshold-class coloring* with a palette of \(k\) named colors is a function from \(V(G)\) to \(\{1,\ldots,k\}\) such that every color class induces a threshold graph; unused colors are allowed. A threshold graph is obtained from a one-vertex graph by successively adjoining isolated or universal vertices, with the empty graph allowed as well.

For every integer \(k\ge0\), define the formal multivariate exponential series
\[
F_r(\mathbf{x})=\prod_{i=1}^r(1+x_i)+\sum_{i=1}^r\bigl(e^{x_i}-1-x_i\bigr)\prod_{j\ne i}(1+x_j).
\]
Here \(F_r\) has constant term \(1\), and \(F_r^0=1\). **The number of threshold-class colorings using a palette of \(k\) named colors, including unused colors, is exactly**
\[
T_G(k)=\Bigl(\prod_{i=1}^r n_i!\Bigr)[x_1^{n_1}\cdots x_r^{n_r}]F_r(\mathbf{x})^k.
\]
The number using every named color is
\[
T_G^{\mathrm{onto}}(k)=\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}T_G(j),
\]
and the number of unordered partitions into exactly \(k\) nonempty induced threshold graphs equals \(T_G^{\mathrm{onto}}(k)/k!\).

In particular, the least possible number of nonempty threshold classes is the explicit *part-size threshold*
\[
\boxed{\tau(G)=\min\bigl\{k\ge1:\ |\{i:n_i>k\}|\le k\bigr\}.}
\]
The same theorem gives the alternating chromatic number of the complete two-edge-colored graph in which pairs from distinct original parts receive one edge color and pairs within parts receive the other: the correspondence with threshold-induced parts is established in the referenced literature. The underlying graph \(G\) itself is fixed throughout this statement.

## Assumptions and scope
The graph is a finite simple complete multipartite graph, with all part sizes positive. Vertices within each part are individually labelled; colors in \(T_G(k)\) are named and may be unused. The base \(k=0\) contributes zero for nonempty \(G\). The formal series is interpreted coefficientwise, so no analytic convergence assumption is involved. If the color classes must be nonempty, use the displayed inclusion-exclusion formula. The ordinary threshold property, not distance-threshold labeling or weighted-threshold representation, is used.

## Proof
**Step 1 (exact induced-class criterion).** For a subset \(S\subseteq V(G)\), put \(b_i=|S\cap V_i|\). Then \(G[S]\) is threshold if and only if at most one \(b_i\) is at least \(2\). Indeed, two distinct indices with \(b_i,b_j\ge2\) produce an induced four-cycle \(K_{2,2}\), which cannot be threshold: neither an isolated nor a universal vertex occurs in that induced four-cycle. Conversely, if at most one \(b_i\ge2\), the vertices taken singly from the other parts form a clique and are all universal in \(G[S]\); removing those universal vertices leaves an edgeless graph. Reversing the removals gives a threshold construction. This includes the empty class and singleton classes.

**Step 2 (count one named color class).** There are two disjoint possibilities for a single class: every original part contributes zero or one vertex; or exactly one original part \(i\) contributes at least two, while every other part contributes zero or one. In exponential generating functions for labelled vertices, the first option contributes \(\prod_i(1+x_i)\). For a fixed heavy part \(i\), the contribution is \((e^{x_i}-1-x_i)\prod_{j\ne i}(1+x_j)\). Their sum is exactly \(F_r\). An ordered assignment to \(k\) named colors is a tuple of these independent color classes with a partition of the original labelled vertex sets. The exponential formula therefore gives \(T_G(k)\) after extraction of the designated monomial and multiplication by \(\prod_i n_i!\). There is no overcounting because every class has either no heavy part or a unique heavy part. Inclusion-exclusion over omitted named colors proves \(T_G^{\mathrm{onto}}(k)\). A partition into nonempty unordered classes has exactly \(k!\) labellings, proving the final counting statement.

**Step 3 (sharp minimum).** Suppose a threshold-class coloring uses \(k\ge1\) named colors. For every part with \(n_i>k\), the pigeonhole principle gives some color present on at least two of that part's vertices. By Step 1, different such original parts require different heavy colors. Therefore \(|\{i:n_i>k\}|\le k\). Conversely, suppose this inequality holds, and assign a distinct color to each of these large parts, giving all its vertices that color. For every remaining original part, \(n_i\le k\), assign its vertices injectively into the palette (independently of the injections for other parts). Thus each color is repeated in at most one original part. Step 1 verifies every resulting color class. The minimum is exactly the displayed integer. Empty named classes at the smallest feasible palette would otherwise contradict minimality, hence the minimum agrees with the minimum number of nonempty classes.

**Step 4 (graph-theoretic equivalence).** On any complete multipartite graph, an induced subgraph is split if and only if it is threshold. If two parts contribute at least two vertices there is an induced \(C_4\), violating the split property. If not, the graph is a complete split graph and threshold by Step 1. Therefore the minimum is also the classical minimum split-coloring number on this graph family. The equivalence between threshold-induced partitions and alternating-cycle-free color classes of two-edge-colored complete graphs is a prior result, not a new assertion of general equivalence.

## Verification
The accompanying self-contained `verify.py` uses exact rational arithmetic to compute the coefficient formula and independently enumerates named-color assignments. For every integer partition of total order \(1\) through \(7\) and every palette size up to \(4\), it checks the original threshold graph condition by recursively deleting an isolated or universal vertex, rather than assuming the heavy-part criterion. All \(166\) graph-profile/palette tests agree, covering \(345279\) literal color assignments. Seven additional larger parameter tuples verify the part-size threshold inequalities. Running `python3 verify.py` prints `VERIFY_OK`. These finite tests support but do not replace the infinite proofs in Steps 1–4.

For illustration, \(G=K_{3,2,2}\) has \(\tau(G)=2\) and exactly \(64\) two-named-color assignments; \(K_{4,4,4}\) has \(\tau=3\) and exactly \(55566\) three-named-color assignments (equivalently \(9261\) unordered partitions into three classes). The outputs can be obtained by coefficient extraction as well as by direct counting on smaller instances.

## Relationship to prior work
Bang-Jensen, Bessy and Reinald (2026, arXiv:2610.32954v1, first public 2026-10-23) introduce the alternating chromatic number for two-edge-colored graphs and prove NP-completeness for the two-class decision problem on complete edge-colored graphs; their Corollary 4.2 identifies its equivalence with partitioning a graph into two induced threshold graphs. The present theorem addresses a restricted but arbitrary-order multipartite family and gives an all-palette enumerator, not merely a decision procedure.

Demange, Ekim and de Werra (2006) define minimum split-coloring and study approximations, and their earlier 2005 work gives polynomial algorithms for deciding clique/stable partitions of cographs, a superclass of complete multipartite graphs. Consequently, polynomial-time *computability of the minimum* on this family is not claimed as new. The contribution here is the explicit part-size law together with the exact all-palette multivariate enumerator and the onto/unordered refinements. The 2005 full text was not completely accessible during this assessment; a possible more explicit earlier specialization is an unresolved historical-priority limitation.

## Limitations
The formulas count threshold-induced partitions only for complete multipartite graphs with labelled vertices and specified positive part sizes. They do not extend to arbitrary graphs, and they do not assert a general tractability result for counting threshold-class partitions on cographs. General algorithms for split-coloring on cographs predate this result. Historical priority of the exact symbolic formulas remains provisional, and no independent mathematical audit has been performed.

## References
1. J. Bang-Jensen, S. Bessy, A. Reinald, *Acyclic 2-edge-coloured graphs: polynomial-time linkages and colouring hardness*, arXiv:2610.32954v1 (2026-10-23), https://arxiv.org/abs/2610.32954, particularly Introduction and Corollary 4.2.
2. M. Demange, T. Ekim, D. de Werra, *On the approximation of Min Split-coloring and Min Cocoloring*, Journal of Graph Algorithms and Applications 10(2) (2006), 297–315, https://doi.org/10.7155/jgaa.00129.
3. M. Demange, T. Ekim, D. de Werra, *Partitioning cographs into cliques and stable sets*, Discrete Optimization 2(2) (2005), 145–153, https://doi.org/10.1016/j.disopt.2005.03.003.
