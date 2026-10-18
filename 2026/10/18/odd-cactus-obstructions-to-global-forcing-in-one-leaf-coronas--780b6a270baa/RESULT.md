# Odd-cactus obstructions to global forcing in one-leaf coronas

## Finding

Let \(G=(V,E)\) be any finite simple graph, with \(n=|V|\) and \(m=|E|\). Attach a distinct pendant vertex \(v'\) to every \(v\in V\), obtaining the one-leaf corona \(W(G)=G\circ K_1\). A *global forcing set for maximal matchings* is an edge set whose intersections with the maximal matchings of \(W(G)\) are all distinct; its minimum size is \(\phi_{\mathrm{gm}}(W(G))\).

For an arbitrary edge set \(S\subseteq E(W(G))\), define its omitted core edges \(R=E\setminus S\), its omitted-pendant vertices \(U=\{v\in V:vv'\notin S\}\), and the spanning graph \(H=(V,R)\). Then **\(S\) is a global forcing set if and only if**

1. \(H\) contains no even cycle; and
2. each connected component of \(H\) contains at most one vertex from \(U\).

For a spanning subgraph \(H=(V,R)\), write \(c(H)\) for the number of components, including isolated vertices, and \(\beta(H)=|R|-n+c(H)\) for its cycle rank. Put
\[
 b_{\mathrm{odd}}(G)=\max_{\substack{R\subseteq E\\(V,R)\text{ has no even cycle}}}\beta((V,R)).
\]
Then
\[
\boxed{\phi_{\mathrm{gm}}(G\circ K_1)=m-b_{\mathrm{odd}}(G).}
\]
Every minimum global forcing set is obtained by selecting an even-cycle-free spanning \(H=(V,R)\) with \(\beta(H)=b_{\mathrm{odd}}(G)\), omitting every edge of \(R\), and omitting exactly one pendant edge per component of \(H\); every minimum set arises uniquely in this way. An even-cycle-free graph is equivalently a cactus whose nontrivial cyclic blocks are odd cycles, so \(b_{\mathrm{odd}}\) is the largest number of cycle blocks in a spanning odd cactus subgraph.

In particular, the standard corona upper bound \(\phi_{\mathrm{gm}}(G\circ K_1)\le m\) is **sharp exactly for bipartite** \(G\). For the path on \(n\ge1\) vertices, the exact number of minimum sets on its fixed labeled corona is the even-index Fibonacci number \(F_{2n}\) (with \(F_0=0,F_1=1\)); their size is \(n-1\). For cycles with \(n\ge3\),
\[
\phi_{\mathrm{gm}}(C_n\circ K_1)=\begin{cases}n-1,&n\text{ odd},\\n,&n\text{ even}.\end{cases}
\]
For complete graphs, \(\phi_{\mathrm{gm}}(K_n\circ K_1)=\binom n2-\lfloor(n-1)/2\rfloor\) for every \(n\ge1\).

## Assumptions and scope

Graphs are finite, undirected, and simple. The original vertex labels and private pendant edges remain distinguished when counting minimum forcing sets. The empty matching of \(G\) is allowed. The corona graph has precisely \(m+n\) edges. An even cycle has positive even length, hence length at least four in a simple graph. The quantity \(b_{\mathrm{odd}}(G)\) is an exact, finite graph invariant defined through spanning subgraphs, not an asserted polynomial-time algorithm.

## Proof

**Matching correspondence.** Every maximal matching \(M\) of \(W(G)\) must saturate each core vertex \(v\): if both \(v\) and its unique leaf \(v'\) were free, the pendant edge could be added. Consequently, the core portion \(A=M\cap E\) is an arbitrary matching in \(G\), and \(M\) contains the pendant edge \(vv'\) precisely when \(v\) is not saturated by \(A\). Conversely, every matching \(A\) of \(G\), extended with precisely those pendant edges, is maximal in \(W(G)\). This is a bijection.

**Necessity of the two conditions.** Suppose \(H\) contains an even cycle. Its two alternating perfect matchings, regarded as core matchings with no other core edge selected, saturate exactly the same core vertices and differ only on omitted core edges. Their corresponding maximal matchings therefore have identical traces on \(S\), contradicting forcing.

If distinct \(u,v\in U\) are joined by a path in \(H\), take such a simple path. Assign alternate path edges to two core matchings, assigning no other core edges. At all internal path vertices the two matchings have identical saturation status, while only the endpoint statuses differ. The corresponding maximal matchings differ only on omitted core edges along the path and on the two omitted pendant edges at \(u,v\). Their \(S\)-traces coincide. Thus no component of \(H\) may contain two vertices of \(U\).

**Sufficiency.** Suppose the two conditions hold, and distinct core matchings \(A,B\) give the same \(S\)-trace after extension. Every edge of their symmetric difference lies in \(R\). The symmetric difference of two matchings is a disjoint union of alternating paths and even cycles. No even-cycle component is possible in \(H\). Each alternating path has two distinct endpoints where the saturation status differs, hence both corresponding pendant edges must be omitted from \(S\); its endpoints therefore lie in \(U\) in the same component of \(H\), contradicting condition 2. Thus \(A=B\), contrary to assumption; \(S\) forces all maximal matchings.

**Optimization and all minimizers.** For a fixed admissible \(R\), the criterion permits at most one omitted pendant edge per component of \(H\), or at most \(c(H)\) omitted pendant edges in total. Omitting one pendant edge from every component achieves this maximum. Thus the largest possible number of omitted edges for this \(R\) is \(|R|+c(H)=n+\beta(H)\), and the smallest forcing set has \((m+n)-(n+\beta(H))=m-\beta(H)\) edges. Maximizing \(\beta(H)\) over even-cycle-free \(R\) gives the formula and the stated unique description of all minimizers. Every even-cycle-free graph is an odd cactus: two distinct cycles with more than one common vertex would contain a theta subgraph; among its three constituent cycles at least one has even length. Thus each cycle forms a distinct odd block and each contributes one to cycle rank.

**Sharpness and examples.** If \(G\) is bipartite, each cyclic spanning subgraph has an even cycle, so every admissible \(H\) is a forest and \(b_{\mathrm{odd}}(G)=0\). Conversely, if \(G\) is not bipartite, it has an odd cycle; taking that cycle and all other vertices isolated gives an admissible \(H\) with \(\beta(H)=1\). Hence equality with \(m\) holds exactly in the bipartite case.

If \(G=P_n\), all subsets \(R\subseteq E(P_n)\) are admissible, and each gives \(\prod_C |V(C)|\) minimum sets by choosing the single omitted pendant in each component. Components are nonempty consecutive intervals. Their ordered length compositions \((k_1,\ldots,k_t)\) of \(n\) contribute \(k_1\cdots k_t\). With \(a_0=1\), the ordinary generating function is
\[
\sum_{n\ge0}a_n z^n=\frac{1}{1-\sum_{k\ge1}kz^k}=\frac{(1-z)^2}{1-3z+z^2}=1+\frac{z}{1-3z+z^2}.
\]
The final summand generates \(F_{2n}\) in degree \(n\ge1\), proving the path count. For \(C_n\), an admissible proper subset of cycle edges is a forest of rank zero. The entire cycle is admissible exactly when \(n\) is odd, then contributes rank one. This gives the claimed parity formula. For \(K_n\), every odd cactus on \(n\) vertices has at most \(\lfloor(n-1)/2\rfloor\) cycle blocks (each introduces at least two vertices), and a collection of \(\lfloor(n-1)/2\rfloor\) triangles sharing exactly one center attains the bound inside \(K_n\). The formula follows.

## Verification

The standalone `verify.py` enumerates all core matchings and computes their observed edge signatures directly. Separately it tests the two structural conditions, and it exhaustively compares the answers for every edge-observation subset. It covers **all labeled graphs on at most four vertices**; paths up to seven vertices; cycles of orders three to seven; \(K_5\), the bowtie graph, the diamond, \(K_{3,3}\), two triangles linked by a bridge, and a chorded six-cycle. It also checks the optimal-size formula and Fibonacci/path and parity/cycle consequences. Run `python3 verify.py` with only the Python standard library; the expected last output is `VERIFY_OK`.

The program is a finite falsification check, not the proof of the universal theorem. The proof above establishes every finite simple graph, including larger graphs not enumerated.

## Relationship to prior work

Klavžar, Tavakoli, and Abrishami (2021 preprint; 2022 journal version) proved general upper and lower bounds for corona products. Their upper bound gives \(\phi_{\mathrm{gm}}(G\circ K_1)\le|E(G)|\); their discussion singles out \(K_2\circ K_1\) as one sharp example and asks for more sharpness examples. The present result identifies **all** bases giving equality, determines the exact deficit for arbitrary bases, and classifies every minimum witnessing edge set. The earlier general upper bound alone does not give these converse statements or the odd-cactus optimization.

The earlier global-forcing literature develops basic bounds, graph-operation inequalities, and a line-graph translation to maximal independent-set identification. Those results do not directly imply the two simultaneous obstructions from omitted pendant endpoints and even alternating core cycles. Global forcing of *perfect* matchings is a different invariant: the present corona has a unique perfect matching (all pendant edges), while its family of maximal matchings encodes **every** core matching.

## Limitations

The parameter \(b_{\mathrm{odd}}(G)\) is a finite graph optimization; the theorem does not establish its computational complexity or a fast algorithm for arbitrary \(G\). The enumerative \(F_{2n}\) formula concerns fixed labeled paths and does not quotient by graph automorphisms. Numerical experiments do not replace the universal combinatorial proof.

## References

1. S. Klavžar, M. Tavakoli, and G. Abrishami, *Global forcing number for maximal matchings in corona products*, arXiv:2107.13786v1 (first public preprint 29 July 2021), later *Aequationes mathematicae* 96 (2022), 997–1005, DOI:10.1007/s00010-022-00869-3.
2. D. Vukičević, S. Zhao, J. Sedlar, S.-J. Xu, and T. Došlić, *Global forcing number for maximal matchings*, *Discrete Mathematics* 341 (2018), 801–809, DOI:10.1016/j.disc.2017.12.002.
3. M. Tavakoli, *Global forcing number for maximal matchings under graph operations*, *Control and Optimization in Applied Mathematics* 4 (2019), 53–63, DOI:10.30473/coam.2020.51754.1138.
4. Y. Zhang and H. Zhang, *Relations between global forcing number and maximum anti-forcing number of a graph*, *Discrete Applied Mathematics* 311 (2022), 85–96, DOI:10.1016/j.dam.2022.01.010 (perfect-matching invariant; distinguished in the comparison above).
