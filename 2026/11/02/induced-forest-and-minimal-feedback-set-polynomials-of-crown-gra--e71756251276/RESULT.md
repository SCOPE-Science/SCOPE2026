# Induced-forest and minimal-feedback-set polynomials of crown graphs

## Finding

For every integer \(n\ge3\), let \(C_n\) be the crown graph \(K_{n,n}\) with the edges of one perfect matching deleted. Write \(\mathcal F_n(z)\) for the polynomial whose coefficient of \(z^k\) counts \(k\)-vertex subsets inducing forests. Write \(\mathcal M_n(z)\) for the corresponding polynomial counting **inclusion-maximal** induced-forest vertex subsets. Then

\[
\begin{aligned}
\mathcal F_n(z)={}&2(1+z)^n-1+2nz((1+z)^n-1)-n^2z^2\\
&+\binom n2(2n-3)z^4+n(n-1)(n-2)z^5.
\end{aligned}
\]

The inclusion-maximal polynomial is

\[
\mathcal M_3(z)=6z^5,
\qquad
\mathcal M_n(z)=n(n-1)(n-2)z^5+2nz^{n+1}
\quad(n\ge4).
\]

For \(n\ge4\), all inclusion-maximal forests are exactly those of one of the following two disjoint types: (i) two vertices on one shore and three on the other, with the index set of the first shore contained in the second; (ii) one vertex on one shore and every vertex on the other shore. In the boundary case \(n=3\), only type (i) is maximal.

In particular, for every \(n\ge6\) the maximal induced-forest cardinality spectrum is precisely \(\{5,n+1\}\), so the consecutive cardinalities \(6,7,\ldots,n\) do not occur. The graph \(C_n\) is connected, regular, bipartite, and vertex-transitive. Complementing selected sets gives the complete cardinality polynomial of inclusion-minimal feedback vertex sets:

\[
\mathcal P_3(z)=6z,
\qquad
\mathcal P_n(z)=n(n-1)(n-2)z^{2n-5}+2nz^{n-1}\quad(n\ge4).
\]

Equal exponents, including those at \(n=4\), are combined.

## Assumptions and scope

All graphs are finite and simple. Label the two shores \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i b_j\) an edge if and only if \(i\ne j\). A forest means an acyclic graph, not necessarily connected; the empty graph is a forest. A vertex subset is inclusion-maximal forest-inducing if adding any currently omitted vertex creates a cycle. A feedback vertex set is inclusion-minimal if deleting any of its vertices from that set would cease to meet all cycles. All polynomials enumerate labeled vertex subsets, with no quotient by automorphisms.

## Proof

**1. Classification of all acyclic selections.** For any vertex subset \(S\), let \(X=\{i:a_i\in S\}\) and \(Y=\{j:b_j\in S\}\). Put \(a=|X|\), \(b=|Y|\), and \(c=|X\cap Y|\). The induced graph has \(a+b\) vertices and exactly \(ab-c\) edges. If \(a=0\) or \(b=0\), it is edgeless. If \(a=1\) or \(b=1\), it is a star with at most one additional isolated vertex, hence a forest.

For \(a,b\ge3\), the edge count satisfies \(ab-c\ge ab-\min(a,b)>a+b-1\), so it cannot be a forest. For \(a=2\), \(b\ge4\), the same argument gives \(ab-c\ge2b-2>b+1\); the opposite orientation is symmetric. For \(a=2,b=3\), the edge count is \(6-c\); acyclicity requires \(c=2\), in which case the graph is a path with five vertices. For \(a=b=2\), the case \(c=0\) is a four-cycle, while \(c=1\) is a four-vertex path and \(c=2\) is a two-edge matching. This list exhausts all induced forests.

**2. Enumeration.** Sets on at most one shore contribute \(2(1+z)^n-1\). Sets using both shores, one of which has exactly one selected vertex, contribute \(2nz((1+z)^n-1)-n^2z^2\); the subtraction corrects double counting of pairs with one selected vertex on each shore. For \(a=b=2\), fix the two-index set \(X\). The allowable \(Y\) are \(X\) and the \(2(n-2)\) two-index sets meeting \(X\) in one element. This gives \(\binom n2(2n-3)z^4\). For \((a,b)=(2,3)\) or \((3,2)\), choose the two-index set, one extra index in the other shore, and an orientation, giving \(2\binom n2(n-2)z^5=n(n-1)(n-2)z^5\). This proves \(\mathcal F_n\).

**3. Maximality.** A selected set on one shore alone can be extended by a vertex of the opposite shore. Any forest with exactly one selected vertex on one shore can be enlarged, if necessary, until the entire opposite shore is selected. A selection with two vertices on both shores and nonempty index intersection is also extendible: if \(|X\cap Y|=1\), add to \(Y\) the unique element of \(X\setminus Y\); if \(X=Y\), add any element outside \(X\) to \(Y\). Since \(n\ge3\), this yields an acyclic \((2,3)\) configuration.

Every acyclic \((2,3)\) selection is maximal: any new vertex would give shore counts \((3,3)\) or \((2,4)\), both cyclic by step 1. For \(n\ge4\), any \((1,n)\) selection is maximal, because adding another vertex from the singleton shore gives a cyclic \((2,n)\) selection. When \(n=3\), a \((1,3)\) selection remains extendible to an acyclic \((2,3)\) selection. These are all the cases by step 1, proving the formula for \(\mathcal M_n\).

**4. Feedback vertex sets and gaps.** Complementation \(S\mapsto V(C_n)\setminus S\) is a bijection from inclusion-maximal forest-inducing sets to inclusion-minimal feedback vertex sets, changing cardinality \(k\) to \(2n-k\). Thus \(\mathcal P_n(z)=z^{2n}\mathcal M_n(z^{-1})\) as a polynomial identity. The displayed formulas, exact two-point support for \(n\ge6\), and gap of \(n-5\) consecutive integers follow immediately.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and is executed by `python verify.py`. It builds adjacency lists directly from the deleted-matching definition, exhaustively considers every vertex subset for \(3\le n\le9\), detects cycles by graph traversal, and tests inclusion-maximality by checking each one-vertex extension. It compares both resulting cardinality distributions to the two closed formulas, including boundary cases and coincident exponents. The recorded outcome is:

`VERIFY_OK graph_orders 7 all_candidate_subsets 349504 maximal_and_all_forest_polynomials True`

The finite test counts \(349504\) candidate vertex subsets. It is a corroborating finite check, not a proof for unbounded \(n\); the proof above is combinatorial and unrestricted.

## Relationship to prior work

Melo and Ribeiro [1] formulate and computationally study the maximum weighted induced-forest problem and its feedback-vertex-set complement. Hertz [2] studies decycling in bipartite graphs and related bounds and examples. Lampis, Melissinos, and Vasilakis [3] study the parameterized complexity of the **maximum size of an inclusion-minimal feedback vertex set**, thereby directly motivating the minimal-set perspective. Ghalavand and Li [4] establish general forest-number results for dense balanced bipartite graphs; in particular their minimum-degree theorem yields the scalar maximal forest size \(n+1\) for the crown graphs when \(n\ge4\). That known scalar extremum is **not** presented as new here. The contribution assessed here is the complete all-forests and inclusion-maximal cardinality distributions, their explicit structural classification, and the resulting gaps. The reviewed primary texts do not give those crown-graph distributions.

## Limitations

The results are restricted to the crown family \(K_{n,n}\) minus a perfect matching and to unweighted, labeled vertex subsets. This is a mathematical proof supported by finite computational tests, not an independent audit or a global novelty guarantee. Although several closely related primary texts and alternative names were examined, it remains possible that an equivalent enumerator was published elsewhere or indexed under a different graph name.

## References

[1] R. A. Melo and C. C. Ribeiro, *Maximum weighted induced forests and trees: New formulations and a computational comparative review*, arXiv:2102.09194 (first posted 2021-02-18), https://arxiv.org/abs/2102.09194.

[2] A. Hertz, *Decycling Bipartite Graphs*, Journal of Graph Algorithms and Applications 25 (2021), 461–480, doi:10.7155/jgaa.00567, https://doi.org/10.7155/jgaa.00567.

[3] M. Lampis, N. Melissinos, and M. Vasilakis, *Parameterized Max Min Feedback Vertex Set*, arXiv:2302.09604 (first posted 2023-02-19), https://arxiv.org/abs/2302.09604.

[4] A. Ghalavand and X. Li, *On Maximum Induced Forests of the Balanced Bipartite Graphs*, arXiv:2501.05145 (first posted 2025-01-09), https://arxiv.org/abs/2501.05145.
