# Strong odd chromatic number of complete multipartite graphs
## Finding
For every connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\), a proper coloring is a strong odd coloring if and only if every color class has odd cardinality. Consequently, if \(e=|\{i:n_i\text{ is even}\}|\), then \(\chi_{\mathrm{so}}(G)=r+e\).

Equivalently, every odd partite class needs one private color and every even partite class needs two. In particular, for a complete bipartite graph \(K_{m,n}\),
\[
\chi_{\mathrm{so}}(K_{m,n})=
\begin{cases}
2,&m,n\text{ odd},\\
3,&\text{exactly one of }m,n\text{ is even},\\
4,&m,n\text{ even}.
\end{cases}
\]

## Assumptions and scope
All graphs are finite and simple. A strong odd coloring is a proper vertex coloring such that, for every vertex \(v\) and every color that occurs in the open neighborhood \(N(v)\), that color occurs there an odd number of times. The graph \(K_{n_1,\ldots,n_r}\) has \(r\ge2\) nonempty partite classes \(V_1,\ldots,V_r\), with \(|V_i|=n_i\). Thus the graph is connected.

## Proof
In any proper coloring of a complete multipartite graph, a color cannot occur in two different partite classes, because every two vertices in distinct classes are adjacent. Hence every color class is contained in a unique \(V_i\).

Fix a color class \(C\subseteq V_i\). Since \(r\ge2\), choose a vertex \(v\) in a different part. Every vertex of \(C\) is adjacent to \(v\), and no vertex outside \(V_i\) has the color of \(C\). Therefore that color occurs exactly \(|C|\) times in \(N(v)\). The strong odd condition forces \(|C|\) to be odd. This proves that every color class of a strong odd coloring has odd cardinality.

Conversely, suppose a proper coloring has only odd-sized color classes. For a vertex \(v\in V_i\), its neighborhood consists of all vertices outside \(V_i\). Every color occurring in \(N(v)\) belongs to one part \(V_j\) with \(j\ne i\), and all vertices of that color class lie in \(N(v)\). Its multiplicity in \(N(v)\) is therefore the odd size of that color class. Hence the coloring is strong odd. This establishes the characterization.

It remains to minimize the number of colors. Because colors cannot be shared between parts, the optimization separates over the \(r\) partite classes. An odd integer \(n_i\) is itself one positive odd summand, so one color is both necessary and sufficient on an odd part. An even integer cannot be one odd summand, so it needs at least two colors; two suffice by splitting it as \(1+(n_i-1)\), whose two summands are odd. Summing these independent minima gives
\[
\chi_{\mathrm{so}}(G)=\sum_{i=1}^r\bigl(1+\mathbf{1}_{2\mid n_i}\bigr)=r+e.
\]

## Verification
The proof is analytic and covers arbitrary positive part sizes. The attached `artifacts/verify.py` is only a finite stress test. It enumerates, up to relabeling of colors, every vertex coloring of every nontrivial complete multipartite part-size profile of total order from \(2\) through \(8\). It checks properness and the strong odd neighborhood condition directly, finds the minimum number of colors, and compares it with \(r+e\). The replay output is stored in `artifacts/verification_output.txt`.

The finite computation is not used to justify the universal quantifiers.

## Relationship to prior work
Kwon and Park introduced strong odd coloring and used complete bipartite graphs to show that the gap from square coloring can be arbitrarily large; for \(K_{m,n}\) they record the upper bound \(\chi_{\mathrm{so}}(K_{m,n})\le4\), without an exact parity classification. Their examples \(K_{1,2}\) and \(K_{1,3}\) already exhibit the even/odd transition captured by the formula here.

Manattu, Vinay, and Lakshmanan subsequently studied exact strong odd chromatic numbers for joins. Their 2026 paper notes that exact values are known for very few graph classes and observes that, in a join with an empty graph, a color class seen across the join must have odd size. A complete multipartite graph is an iterated join of empty graphs, and the theorem above turns that local parity mechanism into an exact all-parameter characterization for the entire class. The inspected paper treats joins of cycles with empty graphs and one-point unions, not arbitrary complete multipartite graphs.

Targeted literature and published-finding corpus searches under “strong odd,” “complete multipartite,” “complete bipartite,” the notation \(\chi_{\mathrm{so}}\), and the parity formula found no statement implying this classification. The closest published-finding corpus record concerns ordinary odd coloring of complete multipartite graphs, a different invariant with a different neighborhood requirement.

## Limitations
The theorem is restricted to complete multipartite graphs. It does not provide bounds for arbitrary joins whose factors contain edges, nor does it address list, online, or other variants of strong odd coloring. The originality assessment is necessarily limited by discoverability: the proof is short, so an equivalent observation may exist under terminology not surfaced by the targeted searches. No claim of bibliographic uniqueness is made.

## References
1. A. J. Manattu, A. Vinay, and A. Lakshmanan S., “On a conjecture about the strong odd chromatic number of planar graphs,” arXiv:2602.03259v1, first submitted 2026-02-03. Primary MSC 05C15, 05C10.
2. H. Kwon and B. Park, “Strong odd coloring of sparse graphs,” arXiv:2401.11653.
3. Public research record `2026/9/30/SCOPE-exact-odd-chromatic-number-and-optimal-coloring-count-for-comple--2f4a2e65a3d2`, concerning ordinary odd coloring of complete multipartite graphs.
