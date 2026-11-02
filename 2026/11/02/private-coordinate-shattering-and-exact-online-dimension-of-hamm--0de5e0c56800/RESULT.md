# Private-coordinate shattering and exact online dimension of Hamming-box convexity

## Finding
Let \(d\ge1\) and let \(X_i\) be a finite alphabet of size \(n_i\ge1\). The **Hamming graph** \(G=K_{n_1}\square\cdots\square K_{n_d}\) has vertex set \(X=\prod_i X_i\), with two tuples adjacent precisely when they differ in exactly one coordinate. Let \(\mathcal C(G)\) contain every geodesically convex vertex set, including the empty set, and query membership at individual vertices. Set
\[
k=\sum_{i=1}^{d}(n_i-1),\qquad r=|\{i:n_i\ge2\}|.
\]

**Exact classification.** Every convex set is a Cartesian product of coordinate subsets (a *box*), with the empty set admitted, and
\[
|\mathcal C(G)|=1+\prod_{i=1}^{d}(2^{n_i}-1).
\]
A finite support \(S\subseteq X\) is VC-shattered precisely when, for every point \(x\in S\), there is a coordinate \(i\) such that the value \(x_i\) appears in that coordinate in no other point of \(S\). This includes the vacuous empty support. Moreover,
\[
\operatorname{Ldim}(\mathcal C(G))=k+1,\qquad
\operatorname{VCdim}(\mathcal C(G))=
\begin{cases}k+1,&r\le1,\\k,&r\ge2.\end{cases}
\]
When at least two coordinates have more than one possible value, the adaptive-minus-static gap is exactly one for **every** tuple of finite alphabet sizes.

For two nontrivial factors \(K_m\square K_n\), identify a grid vertex \((i,j)\) with the edge \(ij\) of the abstract complete bipartite graph \(K_{m,n}\). A support is shattered exactly when this bipartite edge set is a disjoint union of stars. Its largest size is \(m+n-2\). The number of largest shattered supports is
\[
\begin{cases}
mn,&m,n\ge3,\\
2^{\max(m,n)},&\min(m,n)=2<\max(m,n),\\
6,&m=n=2.
\end{cases}
\]
Here a star includes a single edge, and isolated graph vertices do not count as components.

## Assumptions and scope
The graph is finite and simple with the **all-shortest-path** version of geodesic convexity: a set contains every vertex of every shortest path between any of its own vertices. All queries are vertex-membership queries; the online dimension refers to complete binary adversarial mistake trees, not a self-directed or probabilistic protocol. Factors \(K_1\) are allowed. In particular, the graph with one vertex has two distinct concepts and both dimensions equal one. A factor \(K_n\) by itself has every subset convex and both dimensions equal \(n\).

## Proof
**1. Rectangularization.** In the Cartesian product of complete graphs, the graph distance between \(x,y\) is the number of coordinates where they differ. The graph interval between \(x,y\) contains exactly those tuples whose \(i\)-th coordinate belongs to \(\{x_i,y_i\}\). For any nonempty convex set \(C\) and any tuple of values each drawn from one of its coordinate projections, repeated coordinate mixing along such shortest-path intervals constructs that tuple within \(C\). Hence \(C\) is the Cartesian product of its projections. Conversely, all products of coordinate subsets contain those intervals. Every nonempty box has unique coordinate projections; there are \(\prod_i(2^{n_i}-1)\) nonempty boxes, plus the empty set.

**2. Exact criterion for shattered supports.** For \(T\subseteq S\), the smallest box containing \(T\) is the Cartesian product of the coordinate projections of \(T\); define the smallest box containing the empty set to be empty. To realize the trace \(S\setminus\{x\}\) while excluding \(x\), some coordinate of \(x\) must be absent among the corresponding coordinate values of \(S\setminus\{x\}\). Thus each \(x\in S\) needs a private coordinate value. Conversely, if all points have that property, the smallest box containing any specified \(T\subseteq S\) excludes each \(x\in S\setminus T\) by one of its private values. So every trace is realized. This proves the if-and-only-if statement, including singletons and the empty support.

**3. Exact VC dimension.** If \(r\le1\), all boxes are arbitrary subsets of a set of cardinality \(k+1\), so VC dimension is \(k+1\). Suppose \(r\ge2\). Select a base tuple \(b\). For each coordinate \(i\) and each value \(v\ne b_i\), take the point equal to \(b\) except at coordinate \(i\), where it equals \(v\). These \(k\) points all have private coordinate values and thus form a shattered support.

For the upper bound, let \(S\) have \(s\) points. Since at least two factors are nontrivial, \(k\ge\max_i n_i\). If \(s\le\max_i n_i\), then \(s\le k\). Otherwise \(s>n_i\) for every \(i\). In each coordinate some value is used at least twice, so among the \(n_i\) coordinate values at most \(n_i-1\) are private singleton values. As every point of a shattered support requires a private value, and one private value belongs to at most one point, \(s\le\sum_i(n_i-1)=k\).

**4. Upper bound for online shattering.** Fix any first query \(x\). The positive version space consists of precisely \(2^k\) boxes, since every coordinate side must contain \(x_i\) and each of the other \(k\) coordinate values can independently be included or omitted. No complete online tree of depth \(k+1\) can exist inside a class with only \(2^k\) hypotheses (each root-to-leaf trace requires a distinct hypothesis). Hence no full tree has depth \(k+2\), and \(\operatorname{Ldim}\le k+1\).

**5. Constructive online lower bound.** We prove \(\operatorname{Ldim}\ge k+1\) by induction on \(k\), allowing singleton factors. For \(k=0\), the domain is one point and the two concepts shatter a one-query tree. If only one factor is nontrivial, the class contains every subset of its \(k+1\) vertices, and querying each vertex once gives depth \(k+1\).

Now assume at least two factors are nontrivial. Choose distinct coordinates \(i,j\) with \(n_i,n_j\ge2\), and a base tuple \(x\). On the **yes** child of the query \(x\), the \(k\) independent optional coordinate symbols can be read by querying points that differ from \(x\) in one coordinate only. Thus that child admits a complete depth-\(k\) tree.

On the **no** child of \(x\), query a point \(y\) differing from \(x\) only at coordinate \(j\). If the answer at \(y\) is **yes**, membership of \(y\) fixes the chosen symbol in every coordinate as included, while the earlier **no** forces the old value \(x_j\) to be excluded. Precisely \(k-1\) coordinate-inclusion bits remain free, distinguishable by one-coordinate changes from \(y\); this child therefore has online depth at least \(k-1\). If the answer at \(y\) is **no**, restrict to the subfamily of boxes omitting the value \(x_i\) from coordinate \(i\). Both queries are then automatically negative. This subfamily, after ignoring points with \(i\)-th coordinate \(x_i\), is exactly the full box family on the reduced product with \(n_i\) replaced by \(n_i-1\). The reduced parameter is \(k-1\), so the induction hypothesis gives online depth \(k\) for that subfamily. In particular, this branch has depth at least \(k-1\). Both children of the query \(y\) can therefore support depth \(k-1\), making the original **no** child of \(x\) support depth \(k\). Both children of \(x\) support depth \(k\), completing a depth-\(k+1\) tree. This matches the upper bound.

**6. Two-factor maximum-support count.** In two factors, the private-coordinate condition says exactly that each selected bipartite edge has at least one endpoint of degree one in the support graph; equivalently every nontrivial component is a star. A star forest with at least two nontrivial components has at most \(m+n-2\) edges. A single star has at most \(\max(m,n)\) edges, no larger than \(m+n-2\) when \(m,n\ge2\). This bound is attained by the two disjoint stars centered at one chosen vertex of each bipartition class.

If \(m,n\ge3\), a maximum star forest must span all vertices with exactly two stars, one center in each bipartition class, yielding precisely \(mn\) supports. If \(m=2<n\), maximum supports have exactly one edge incident to each of the \(n\) right vertices, freely choosing one of the two left endpoints for each: \(2^n\) choices, all star forests. Symmetry handles \(n=2<m\). If \(m=n=2\), every two-edge subset of the four-edge graph is a star forest, giving \(\binom42=6\).

## Verification
The companion Python script `check_hamming_boxes.py` constructs the concept family directly, and independently reconstructs geodesic convexity by testing graph distances and all points on shortest paths. For manageable products, it enumerates every candidate query support and compares actual traces against the private-coordinate criterion. It separately evaluates the complete Littlestone version-space recursion without assuming the formulas. The script checks small degenerate factors, two-dimensional grids, binary cubes, and three-dimensional mixed alphabets; it also verifies the two-factor extremal-support counts. See `VERIFICATION.md` for exact tested ranges and limitations. Run using `python3 check_hamming_boxes.py`.

## Relationship to prior work
Cartesian-product behavior of graph geodesic convexity is established in prior graph-convexity research, including Jiang, Pelayo and Pritikin (2004); the rectangularization of convex sets is not asserted as new in isolation. Dourado and collaborators (first public version 2022) survey graph-convexity structures, notably Ptolemaic and convex-geometry characterizations. Thiessen and Gärtner (2022) develop general online mistake bounds for convex sets on graphs, including a generic upper bound through VC dimension. The present exact private-symbol criterion, static dimension, and matching constructive adversarial online dimension are specialized theorems for complete-graph Cartesian products, not consequences of the general asymptotic bounds in those inspected sources.

Chepoi, Labourel and Ratel (2017) use a different notion of VC dimension assigned to *subgraphs* of Cartesian products to bound edge densities; that is not the VC dimension of the family of all convex subsets. The binary specialization can also be described by conjunctions of signed literals, and arbitrary alphabets by unrestricted Cartesian rectangles; prior results under that learning-theory terminology remain a possible priority risk.

## Limitations
The theorem is exact for finite Hamming graphs only, with geodesic convexity including **all** shortest paths, and with vertex-membership queries. It says nothing about arbitrary graph products, halfspace-only concepts, label-noise models, or online algorithms with computational restrictions. The program is finite corroboration, not an infinite proof. The literature comparison is based on accessible primary text, abstracts, and research-record searches and is not an exhaustive historical-priority certification. One older Cartesian-product paper's complete text was not available at its original draft address, so only the accessible abstract and bibliographic description were used for that comparison. Independent mathematical audit has not been performed.

## References
1. M. C. Dourado, M. Gutierrez, F. Protti, R. Sampaio, S. Tondato, *Characterizations of graph classes via convex geometries: a survey*, arXiv:2203.15878, first submitted 2022-03-29, https://arxiv.org/abs/2203.15878.
2. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML-PKDD 2022, pp. 349–364, DOI: 10.1007/978-3-031-26412-2_22, available preprint https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2022/lncs13716/lncs13716354.pdf.
3. T. Jiang, I. Pelayo and D. Pritikin, *Geodesic Convexity and Cartesian Products in Graphs*, 2004 preprint; product-convexity theorem stated in publicly accessible abstract.
4. V. Chepoi, A. Labourel and S. Ratel, *On density of subgraphs of Cartesian products*, arXiv:1711.11485 (2017), https://arxiv.org/abs/1711.11485.
