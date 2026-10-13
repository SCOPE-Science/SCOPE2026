# A parity-component formula for the paired-domination polynomial of rook graphs

## Finding
For all positive integers \(m,n\), let \(R_{m,n}=K_m\square K_n\). A paired-dominating set is a dominating vertex set whose induced graph has a perfect matching. The paired-domination polynomial records *sets*, not matchings:
\[P_{m,n}(z)=\sum_{\substack{S\subseteq V(R_{m,n})\\S\text{ paired-dominating}}}z^{|S|}.\]
Put
\[A(u,v;z)=\sum_{a,b\ge0}\frac{u^a v^b}{a!b!}(1+z)^{ab}.\]
**Theorem.** In the formal ring \(\mathbb Q[z][[u,v]]\), with the square root chosen to have constant coefficient \(1\),
\[\boxed{P_{m,n}(z)=m!n!\,[u^m v^n](e^{-u}+e^{-v}-e^{-u-v})\sqrt{A(u,v;z)A(u,v;-z)}}.\]
In particular, for \(mn\ge2\),
\[\gamma_{\mathrm{pr}}(R_{m,n})=2\left\lceil\frac{\min\{m,n\}}2\right\rceil.\]
The one-vertex graph \(R_{1,1}\) has no paired-dominating set. Example:
\[P_{3,3}(z)=81z^4+84z^6+9z^8.\]

## Assumptions and scope
The graphs are finite and simple; rows and columns are distinguished labeled vertex classes. Two distinct rook cells are adjacent exactly when they share a row or column. Domination includes vertices belonging to the dominating set; the perfect matching is on the *induced graph* and a chosen set is counted only once even when it has several perfect matchings. All identities hold for every \(m,n\ge1\), without connectedness hypotheses on auxiliary bipartite subgraphs. The series are formal; no analytic convergence is invoked.

## Proof
**1. Translate to bipartite edges.** Identify the cells of the rectangular board with the edges of \(K_{m,n}\). For a selected cell set \(S\), let \(H_S\) be the spanning bipartite graph consisting of the selected edges. The induced rook graph on \(S\) is exactly the line graph \(L(H_S)\). An unselected cell \((i,j)\) is undominated exactly when its row \(i\) and column \(j\) both have no selected edges. Thus \(S\) dominates the whole board if and only if *either* all row vertices of \(H_S\) are nonisolated *or* all column vertices are nonisolated. The necessity follows by pairing any isolated row with any isolated column; the converse is immediate.

**2. Pair edges by parity, componentwise.** For any finite connected loopless graph \(H\) with at least one edge, the line graph \(L(H)\) has a perfect matching if and only if \(|E(H)|\) is even. Necessity is parity of the vertex count. For sufficiency, choose a rooted spanning tree of \(H\); assign each nontree edge arbitrarily to one endpoint. Traverse the tree in postorder. At each nonroot vertex, collect its as-yet-unpaired child-tree edges and nontree edges assigned to it. If their number is even, pair them arbitrarily at that vertex, leaving the parent-tree edge unpaired. If their number is odd, include the parent-tree edge and pair the resulting even pool. Each paired pair shares the current vertex and hence is an edge of \(L(H)\). Every edge enters exactly one pool. At the root, the number of remaining edges has the parity of \(|E(H)|\), so is even and can be paired. Applying this to each edge-containing component shows that \(L(H_S)\) has a perfect matching precisely when every edge-containing component of \(H_S\) has an even number of edges. Isolated vertices impose no parity restriction.

**3. Enumerate even-edge components.** The coefficient of \(u^a v^b/(a!b!)\) in \(A(u,v;z)\) is \((1+z)^{ab}\), the edge-number generating polynomial of all labeled bipartite graphs on two fixed labeled parts. Let \(C(u,v;z)=\log A(u,v;z)\). The labeled exponential formula says that \(C\) enumerates *connected* components, with an isolated row or column vertex contributing respectively \(u\) or \(v\). The even-edge part of this connected-component series is
\[C_{\mathrm{even}}(u,v;z)=\tfrac12\big(C(u,v;z)+C(u,v;-z)\big).\]
Thus every graph whose edge-containing components have even sizes, and whose isolated vertices are unrestricted, is enumerated by
\[F(u,v;z)=\exp C_{\mathrm{even}}(u,v;z)=\sqrt{A(u,v;z)A(u,v;-z)}.\]
Both logarithms and the square root are legitimate formal series because their arguments have constant coefficient \(1\).

**4. Remove the domination obstruction.** Isolated row vertices contribute a factor \(e^u\) to \(F\), independently of other components. Therefore graphs in \(F\) with no isolated rows are counted by \(e^{-u}F\), and those with no isolated columns by \(e^{-v}F\). The graphs meeting both restrictions are counted by \(e^{-u-v}F\). Inclusion-exclusion for their union gives \((e^{-u}+e^{-v}-e^{-u-v})F\). Extracting the labeled \((m,n)\) coefficient and using steps 1–2 proves the boxed identity.

**5. Minimum degree.** Suppose \(mn\ge2\). Any dominating set must meet all \(m\) rows or all \(n\) columns, so it contains at least \(\min\{m,n\}\) cells; the perfect-matching condition forces even cardinality. Assume \(m\le n\). If \(m\) is even, choose all cells of one column. If \(m\) is odd, choose them together with one further cell in any of its rows but another column (possible because \(m\le n\) and \(mn\ge2\)). In either case the selected-edge bipartite graph is connected and has an even number of edges, and meets every row. Steps 1–2 give a paired-dominating set of the asserted minimum cardinality. Transpose the board for \(n<m\). Finally, a singleton graph cannot contain a nonempty even-sized induced set, so \(P_{1,1}=0\).

## Verification
The supplied `verify_rook_pair.py` uses only Python 3's standard library and makes two independent calculations. It enumerates all labeled cell subsets for every board of dimensions at most \(4\) by \(4\), using exact bitset domination tests and induced-perfect-matching dynamic programming. Separately, it computes the stated formal bivariate coefficient identity using rational polynomial arithmetic, truncated to the requested dimensions. The outputs coincide for all sixteen boards, including the \(1\)-by-\(1\) exceptional case and the \(4\)-by-\(4\) board with \(2^{16}\) possible subsets. The successful last line reads `VERIFY_OK 16 boards 2^16-largest exhaustive subset search; 30118 paired dominating sets checked against formal coefficient identity`. The independent proof in the preceding section, not this finite enumeration, covers all dimensions.

## Relationship to prior work
Brešar, Henning and Rall study *paired-domination numbers and inequalities* of Cartesian products of arbitrary graphs. Their full accessible manuscript establishes product bounds, not this all-cardinality polynomial for complete-graph factors. Dettlaff, Gözüpek and Raczek investigate paired domination versus ordinary domination and packings, including complexity results and trees, rather than rook-graph enumeration. Existing ordinary domination polynomials for rook and lattice graphs omit the perfect-matching requirement. The graph-product identification \(R_{m,n}=L(K_{m,n})\), edge-component parity reduction, and bivariate exponential formula together distinguish the present exact enumerator from those scalar or different-invariant results.

## Limitations
This formula counts paired-dominating *sets*, not the number of their possible perfect matchings. It is an exact formal coefficient formula rather than a single-term elementary expression for arbitrary polynomial coefficients. Finite checks cover only dimensions at most four, while the general result relies on the written proof. Literature overlap under alternative names for edge-partitions into incident pairs or line-graph paired domination is a residual possibility; independent external verification has not been performed.

## References
1. B. Brešar, M. A. Henning, D. F. Rall, “Paired-domination of Cartesian products of graphs”, *Electronic Notes in Discrete Mathematics* 22 (2005), 233–237, doi:10.1016/j.endm.2005.06.059; expanded treatment in *Utilitas Mathematica* 73 (2007), 255–265.
2. M. Dettlaff, D. Gözüpek, J. Raczek, “Paired Domination versus Domination and Packing Number in Graphs”, arXiv:1911.04098v1, first public 2019-11-11; doi:10.1007/s10878-022-00873-y.
3. S. Mertens, “Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph”, arXiv:2408.08053, 2024. Its ordinary domination counting does not require matched selected vertices.
