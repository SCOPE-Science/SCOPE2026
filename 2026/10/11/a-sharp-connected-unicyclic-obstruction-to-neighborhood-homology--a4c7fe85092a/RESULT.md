# A sharp connected unicyclic obstruction to neighborhood-homology vanishing

## Finding
Let \(G_m\), for every integer \(m\ge1\), be the graph consisting of the cycle \(c_0c_1c_2c_3c_0\) and the pendant path \(c_0t_1t_2\cdots t_{3m}\). Let \(N[U]\) denote the union of the closed neighborhoods of vertices in \(U\), and let \(\operatorname{Ind}(G)\) be the simplicial complex of independent vertex subsets. Then
\[
i(G_m):=\min\{|S|:S\text{ is a maximal independent set of }G_m\}=m+2.
\]
There is no maximal independent set of size \(p=m+1\), but the independent set
\[
U_m=\{t_2,t_5,\dots,t_{3m-1}\},\qquad q=|U_m|=m,
\]
has neighborhood-deletion homology
\[
\widetilde H_{p-q-1}(\operatorname{Ind}(G_m-N[U_m]);\mathbb Z)
=\widetilde H_0(\operatorname{Ind}(C_4);\mathbb Z)
\cong\mathbb Z.
\]
This is an infinite connected unicyclic family violating the vanishing property proved by Berghoff for paths and cycles. Among all connected simple unicyclic graphs, its first counterexample occurs on seven vertices and is unique up to graph isomorphism: \(G_1\).

## Assumptions and scope
All graphs are finite, simple, undirected, and have vertex-set induced subgraphs after deletion. A unicyclic graph means a **connected** graph with exactly one cycle. A maximal independent set means inclusion-maximal, not maximum-cardinality. Homology is reduced simplicial homology with integral coefficients. The tested property \(\mathcal B(G)\) is: for every positive integer \(p\) not realized as the size of a maximal independent set of \(G\), every nonempty independent set \(U\) of size \(q\) has \(\widetilde H_{p-q-1}(\operatorname{Ind}(G-N[U]);\mathbb Z)=0\). Negative homological degree \(-1\) uses the standard augmented-chain convention.

## Proof
**Infinite family.** For each \(j=0,\ldots,m-1\), the vertex \(t_{3j+2}\) can be dominated only by a member of the triple \(B_j=\{t_{3j+1},t_{3j+2},t_{3j+3}\}\). The \(m\) triples are disjoint. Any dominating set, in particular any maximal independent set, consequently contains at least \(m\) tail vertices. The cycle vertex \(c_2\) requires at least one cycle vertex to dominate it, since it has no tail neighbors. Thus a dominating set has at least \(m+1\) elements.

Suppose one had exactly \(m+1\). It would consist of precisely one cycle vertex and precisely \(m\) tail vertices. A single cycle vertex together with tail vertices can dominate all four cycle vertices only if that cycle vertex is \(c_2\) and the selected tail vertices include \(t_1\): choosing \(c_0\) leaves \(c_2\) undominated, and choosing \(c_1\) or \(c_3\) leaves the opposite cycle vertex undominated. Since \(c_2\) dominates no tail vertex, the \(m\) tail vertices would have to dominate all \(3m\) tail vertices. Each tail vertex dominates at most three tail vertices, but \(t_1\) dominates only two tail vertices. This is impossible. Hence any maximal independent set has at least \(m+2\) vertices.

The set \(\{c_0,c_2\}\cup U_m\) is independent and dominates the entire graph: the opposite cycle vertices are nonadjacent, and every pendant block of three consecutive tail vertices is dominated by its middle vertex. Therefore it is maximal independent and has \(m+2\) elements. This proves the exact minimum.

The closed neighborhoods of \(t_{3j+2}\), as \(j\) runs from \(0\) to \(m-1\), are the disjoint triples \(B_j\). Their union is the entire tail and contains no cycle vertex. Consequently \(G_m-N[U_m]\) is the four-cycle. The independence complex of a four-cycle is the disjoint union of the edge on \(\{c_0,c_2\}\) and the edge on \(\{c_1,c_3\}\). It has \(\widetilde H_0\cong\mathbb Z\). Since \(p-q-1=(m+1)-m-1=0\), the proposed vanishing fails.

**Sharp minimum and unique smallest type.** An exhaustive finite enumeration (reproducible by the attached `verify.py`) considers every labeled graph on each of \(3\) through \(7\) vertices with exactly as many edges as vertices, retains precisely the connected ones, and tests all independent sets \(U\), all maximal-independent-set sizes, and all nonzero integral reduced homology groups of each \(\operatorname{Ind}(G-N[U])\). The numbers of connected labeled unicyclic graphs at successive orders are \(1,15,222,3660,68295\); their counterexample counts are \(0,0,0,0,2520\). Independently, the program generates all \(7!\) permutations of the vertices of \(G_1\), obtaining exactly \(2520\) distinct labeled graphs. The set of \(2520\) counterexamples coincides exactly with that orbit. This finite exhaustion establishes minimality and uniqueness up to isomorphism.

## Verification
Run `python3 verify.py` with Python \(3\), no third-party packages. The test constructs signed augmented simplicial boundary matrices of every residual independence complex. Integer row and column operations using unit pivots compute the full ranks and simultaneously establish that all nonzero Smith factors are units for these at-most-five-vertex residual complexes; the code refuses to infer ranks if a nonunit residual block occurs. This proves the integral homology groups, not merely a mod-two approximation. It exhausts the labeled unicyclic graphs at orders \(3\) to \(7\), checks the exact isomorphism orbit of the minimal witness, and also verifies the analytic infinite-family pattern directly for \(1\le m\le4\). The finite computations verify the sharp-order classification; the infinite-family theorem follows from the preceding proof and is not inferred from those finite cases.

## Relationship to prior work
Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, Theorem 5.4 (also Theorem 1.2), proves the vanishing property \(\mathcal B(G)\) for paths and cycles. Question 5.5 asks which larger graph families have the property and notes that a disconnected counterexample exists. The present result gives a connected unicyclic obstruction and determines the smallest one in that class, rather than reproving the path/cycle theorem. Results on the homotopy type of forest or other graph independence complexes do not themselves assert this joint maximal-independent-set and neighborhood-deletion condition.

## Limitations
This does not classify all connected graphs satisfying \(\mathcal B(G)\), all unicyclic graphs satisfying it, or the analogous question for forests; it gives an infinite counterexample family and a sharp smallest unicyclic counterexample. Minimality/uniqueness is a computer-assisted finite classification through seven vertices, not a hand classification. Published literature could contain an equivalent observation under other names.

## References
1. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, first publicly submitted 2020-08-14; *Combinatorial Theory* 2 (2022), DOI:10.5070/C62156880. Theorem 5.4 and Question 5.5. https://arxiv.org/html/2008.06267v2
2. M. Adamaszek and J. Stacho, *Algorithmic complexity of finding cross-cycles in flag complexes*, SoCG 2012, DOI:10.1145/2261250.2261258. Its chordal-graph homology-detection setting is distinct from the nonchordal four-cycle core here.
