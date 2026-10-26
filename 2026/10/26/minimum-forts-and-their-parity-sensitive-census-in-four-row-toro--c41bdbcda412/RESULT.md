# Minimum forts and their parity-sensitive census in four-row toroidal grids

## Finding
Let \(G_n=C_4\square C_n\), with \(n\ge3\). A **fort** is a nonempty set \(F\subseteq V(G_n)\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Write \(f_n\) for the minimum cardinality of a fort, and \(N_n\) for the number of labeled vertex subsets attaining that minimum. Then
\[
f_n=2\lceil n/2\rceil.
\]
For even \(n\),
\[
N_n=4(2^{n/2}+(-1)^{n/2})+8\mathbf1_{4\mid n}.
\]
For odd \(n=2m+1\ge3\),
\[
N_n=\frac n3(8\cdot2^m-2(-1)^m).
\]
The fractional zero forcing number, defined by the linear program assigning nonnegative vertex weights of total minimum weight subject to every fort receiving weight at least one, satisfies
\[
Z^*(G_n)=\frac{4n}{2\lceil n/2\rceil}=\frac{2n}{\lceil n/2\rceil}.
\]
The full minimum-fort census, rather than this easy vertex-transitive fractional corollary, is the principal finding.

## Assumptions and scope
Vertices are pairs \((r,j)\in\mathbb Z/4\mathbb Z\times\mathbb Z/n\mathbb Z\) with adjacency when exactly one coordinate differs by \(\pm1\) in the corresponding cycle. For \(n=3\), the two horizontal neighbors are distinct. A labeled fort is an ordinary subset of this fixed vertex set; rotations and reflections are **not** identified. No assertion is made about general \(C_a\square C_b\) when \(a>4\).

Identify each column with a mask \(b_j\in\{0,\ldots,15\}\), with bit \(r\) indicating whether \((r,j)\in F\). For three consecutive masks \((a,b,c)\), define **admissibility** by requiring, for each bit \(r\) absent from \(b\),
\[
a_r+c_r+b_{r-1}+b_{r+1}\ne1,
\]
where subscripts on bits are modulo four. Here the sum counts neighbors, so admissibility is exactly the fort condition at the middle column.

## Proof
**1. Transfer digraph.** Two consecutive all-zero columns cannot occur in a nonempty fort: for a zero middle column following a zero column, admissibility forces its next column also to be zero, and induction around the cycle forces every column zero. Hence use the \(255\) states \((a,b)\) other than \((0,0)\). Put a directed edge \((a,b)\longrightarrow(b,c)\) precisely when \((a,b,c)\) is admissible. The direct finite construction has \(2671\) edges. Every nonempty fort is bijective with a length-\(n\) closed walk rooted at the first column; it has cardinality \(\sum_{j=0}^{n-1}\operatorname{popcount}(b_j)\). Weight each edge by \(w((a,b),(b,c))=\operatorname{popcount}(b)-1\); then \(\sum w=|F|-n\).

**2. Nonnegative reduced costs.** Assign potential \(p=-1\) to precisely these \(23\) states:

`(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(1,10),(1,11),(2,5),(2,7),(4,10),(4,14),(8,5),(8,13)`.

Assign \(p=0\) elsewhere. Direct checking of all admissible triples proves that the **reduced cost**
\[
\rho(u,v)=w(u,v)+p(u)-p(v)
\]
is a nonnegative integer for every edge. The executable exact check is in `verify.py`: it constructs every state and edge from the displayed adjacency rule, rather than trusting a pretabulated edge list. Potentials telescope on a closed walk, hence \(|F|-n=\sum\rho\ge0\).

**3. Parity obstruction and attainment.** Consider the zero-reduced-cost (tight) directed graph \(T\). Its only recurrent nontrivial strongly connected components have respective sizes \(4,4,10,10\). Each is bipartite as an undirected graph, and there is no tight loop; these properties are verified directly from the fully specified \(255\)-state construction. Thus no tight closed walk has odd length. Consequently \(|F|\ge n+1\) when \(n\) is odd. To attain these bounds, select all four-row masks `0101` in even-indexed columns and the empty mask in odd-indexed columns. At a selected column each outside vertex has two vertical selected neighbors. At an empty column each outside vertex has zero or two selected horizontal neighbors, including at the wraparound when \(n\) is odd. The resulting fort has \(2\lceil n/2\rceil\) vertices. This proves \(f_n\).

**4. The even census.** For even \(n\), a minimum fort corresponds exactly to a closed walk using only tight edges. Two recurrent components are directed four-cycles, with adjacency characteristic polynomial \(t^4-1\). The other two have characteristic polynomial
\[
t^{10}-t^8-2t^6=t^6(t^2-2)(t^2+1).
\]
The attached checker reconstructs each component and calculates these characteristic polynomials over exact integers by the Faddeev--LeVerrier recurrence. A four-cycle component contributes \(4\mathbf1_{4\mid n}\) closed walks; each ten-state component contributes \(2\cdot2^{n/2}+2(-1)^{n/2}\) for positive even \(n\). Summing the four components proves the displayed even formula. Transient vertices cannot appear on any closed walk.

**5. The odd census and finite certificate for all orders.** An odd minimum fort has \(\sum\rho=1\); thus its rooted closed walk contains exactly one cost-one edge, with all other edges tight. Let \(B\) be the \(255\)-square integer adjacency matrix of cost-one edges and \(T\) the tight adjacency matrix. Counting the possible positions of the unique defect gives
\[
N_{2m+1}=(2m+1)h_m,\qquad h_m=\operatorname{tr}(B(T^2)^m),\quad m\ge1.
\]
The exact checker constructs \(T\) and \(B\) from the admissibility and potential definitions and verifies \(h_1=6\), \(h_2=10\), and
\[
h_{m+2}-h_{m+1}-2h_m=0\qquad(1\le m\le255).
\]
This finite identity is an **all-order proof certificate**, not an unproved extrapolation: put \(S=T^2\), a \(255\times255\) matrix. The residual sequence \(r_m=\operatorname{tr}(BS^m(S^2-S-2I))\) obeys the homogeneous linear recurrence determined by the characteristic polynomial of \(S\), by Cayley--Hamilton. The \(255\) verified consecutive zeros \(r_1,\ldots,r_{255}\) force every subsequent residual to vanish. Hence the second-order recurrence is valid for every integer \(m\ge1\). Its unique solution with the displayed initial values is \(h_m=(8\cdot2^m-2(-1)^m)/3\), proving the odd formula.

**6. Fractional corollary.** The graph is vertex-transitive and has \(4n\) vertices. Averaging any feasible fractional fort transversal over its automorphism group produces a uniform feasible weighting of the same total. Since every fort has at least \(f_n\) vertices, assigning weight \(1/f_n\) at every vertex is feasible. Conversely each orbit-average of an optimal weighting assigns equal weights and must give total weight at least \(4n/f_n\) on a minimum fort. Thus \(Z^*(G_n)=4n/f_n\).

## Verification
Run `python3 verify.py` with Python 3.8 or later (only standard library). The script checks all \(2671\) admissible transitions and reduced costs; the four tight recurrent components and their bipartiteness; exact integer characteristic polynomials; \(255\) consecutive Cayley--Hamilton residuals; and, independently of transfer matrices, exhaustive direct fort enumeration for every \(3\le n\le7\). Expected output begins `VERIFY_OK states=255 edges=2671 recurrent_scc=[4,4,10,10]` and ends with the sample counts. Direct enumeration is supportive for small values; the transfer/certificate argument above supplies the unbounded proof.

## Relationship to prior work
Cameron and collaborators (arXiv:2310.17904, initially public 2023-10-27) establish the fort-based zero-forcing framework, Cartesian-product bounds, and corresponding fractional theory, but the inspected discussion does not provide the displayed all-order minimum-fort census. Becker and collaborators (arXiv:2404.05963) enumerate inclusion-minimal forts in other families and investigate products; their inspected examples and constructions do not imply this specific enumeration. Brimkov and collaborators (arXiv:2507.10826) analyze hypercube forts: \(C_4\square C_4\cong Q_4\), so the case \(n=4\), with \(28\) smallest forts, is already covered and is **not** claimed as an individually novel finite result. The contribution is the whole parity-sensitive formula, including every larger \(n\). Related published graph-family enumerations do not logically determine the 255-state transfer census.

## Limitations
The proof relies on a fully specified, independently runnable exact finite-state certificate. No shorter conceptual classification of all extremizers is claimed; uniqueness or priority is not certified. The literary comparison cannot exclude unindexed work on stopping sets, forts or failed zero forcing of toroidal graphs. The result is limited to width four. Independent audit of the certificate has not been performed.

## References
1. T. R. Cameron et al., *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (first public 2023-10-27), https://arxiv.org/abs/2310.17904.
2. P. Becker et al., *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963 (2024), https://arxiv.org/abs/2404.05963.
3. B. Brimkov et al., *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826 (2025), https://arxiv.org/abs/2507.10826.
