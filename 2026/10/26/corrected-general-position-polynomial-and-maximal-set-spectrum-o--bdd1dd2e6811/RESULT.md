# Corrected general-position polynomial and maximal-set spectrum of crown graphs

## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the graph with two disjoint vertex classes \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and with edges \(a_i b_j\) precisely for \(i\ne j\). Then a set is in general position if and only if it has at most two vertices or is contained in \(A\) or \(B\). Therefore
\[
\psi(\operatorname{Cr}_n;z)=2(1+z)^n-1+n^2z^2.
\]
Its inclusion-maximal general-position sets are exactly the two full classes \(A,B\) and the \(n^2\) cross-class pairs \(\{a_i,b_j\}\); their cardinality spectrum is \(\{2,n\}\). For \(n\ge4\), there are \(n-3\) absent intermediate cardinalities in connected, \((n-1)\)-regular bipartite graphs.

## Assumptions and scope
All graphs are finite, undirected and simple. The deleted perfect matching is \(\{a_i b_i:1\le i\le n\}\). A set \(S\subseteq V(G)\) is a *general-position set* if no three distinct vertices of \(S\) occur on a single shortest path in \(G\). The polynomial counts vertex-distinguished sets by cardinality, including the empty set. *Inclusion-maximal* refers to extending a set by one or more vertices, not merely largest cardinality. The restriction \(n\ge3\) ensures connectedness and existence of a third index for the geodesic argument.

## Proof
**Distances.** Two different vertices of \(A\) have graph distance two, by any common neighbor \(b_\ell\) whose index differs from both; the same holds in \(B\). For \(i\ne j\), \(d(a_i,b_j)=1\). For \(i=j\), \(d(a_i,b_i)=3\): they are nonadjacent vertices in opposite sides of a bipartite graph, and for distinct \(i,j,\ell\), the path \(a_i,b_j,a_\ell,b_i\) has length three. Therefore that distance cannot be smaller.

**All mixed triples fail.** Take distinct \(a_i,a_j\) and any \(b_k\). If \(k\notin\{i,j\}\), the two-edge path \(a_i,b_k,a_j\) is a geodesic. If \(k=i\), choose \(\ell\notin\{i,j\}\); the path \(a_i,b_\ell,a_j,b_i\) has length three, equals \(d(a_i,b_i)\), and contains the selected triple. If \(k=j\), use the symmetrical path \(a_j,b_\ell,a_i,b_j\). Any triple with two vertices of \(B\) and one of \(A\) fails by symmetry. Every vertex subset meeting both sides with at least three vertices includes one such triple, and so is not in general position.

**Pure-side and small sets succeed.** Every set with at most two vertices is trivially in general position. Three vertices in the same side cannot lie on one geodesic: between two distinct same-side vertices the distance is two, and the interior vertex of a two-edge path belongs to the opposite side. Hence every side-contained set is in general position. These two implications give the exact characterization.

**Enumeration.** The union of all side-contained subsets contributes \(2(1+z)^n-1\), where one is subtracted because the empty set was counted twice. The only additional general-position sets are the \(n^2\) cross-side pairs, contributing \(n^2z^2\). Thus the stated polynomial holds. In particular its quadratic coefficient is \(2\binom n2+n^2=\binom{2n}{2}\), as required for every graph on \(2n\) vertices.

**Maximality.** Each full class is inclusion-maximal: adjoining any opposite-side vertex would form a forbidden mixed triple. Any proper subset of one class can be enlarged inside that class. Every mixed pair \(\{a_i,b_j\}\) is inclusion-maximal because adjoining any third vertex yields a mixed triple; no mixed set of size three is feasible. Therefore the complete list of inclusion-maximal sets is exactly \(A,B\) and the \(n^2\) cross pairs. It follows that the maximal-set cardinalities are \(2,n\); for \(n\ge4\), the integers \(3,\ldots,n-1\) do not occur, a gap of \(n-3\). The graph is connected for \(n\ge3\) by the previously described finite paths, and every vertex has degree \(n-1\).

**Concrete discrepancy.** Iršič, Klavžar, Rus and Tuite [3, Sect. 4, Proposition 4.3, displayed expression] explicitly identify \(T^*(r,2)\) with \(K_{r,r}\) minus a perfect matching, then give an expression with additional \(4\binom r2 z^3+\binom r2 z^4\) on top of the pure-side contributions. At \(r=3\), their expression equals \(1+6z+15z^2+14z^3+3z^4\), whereas the theorem gives \(1+6z+15z^2+2z^3\). Indeed \(\operatorname{Cr}_3\) is the six-cycle; it cannot have a four-vertex general-position set. This is a discrepancy in that printed enumeration, **not** a counterexample to the separate assertion that the true polynomial is unimodal.

## Verification
Run `python3 verify.py` with standard Python 3. The program constructs the graphs directly from deleted-matching adjacency, computes all shortest distances by breadth-first search, enumerates every vertex subset for \(3\le n\le8\), and compares each original-definition count with the polynomial coefficients. It separately computes all inclusion-maximal general-position sets directly from the feasible-subset family and compares the full set of them against the characterized list. The program also checks the precise coefficient discrepancies in the printed 2024 expression. The bundled `verify_output.txt` records the execution. These finite cases are corroboration only: the unrestricted theorem follows from the preceding path argument.

## Relationship to prior work
Anand et al. [1] characterize general-position sets in arbitrary graphs using distance-constant, in-transitive clique components; their bipartite diameter-three theorem determines the *maximum cardinality* for crowns, but does not give the explicit whole-polynomial formula or maximal-set census above. The authors of [2] studied the lower general-position setting; the fact that connected bipartite graphs admit maximal two-element sets is not itself claimed as new. Iršič et al. [3] defined and studied general-position polynomials, and explicitly treated the family \(T^*(r,2)\), which they identified with crowns. Unlike an unmentioned instance of their formula, the exact identity here conflicts with their printed expression and is directly proved from geodesics; the discrepancy is quantified at the six-cycle. The actual unimodality conclusion of their Proposition 4.3 is not disputed here. The additional exhaustive maximal-set classification gives an unbounded gap in the spectrum on a natural regular connected bipartite family.

## Limitations
The result applies to \(K_{n,n}\) with a whole perfect matching removed, for integer \(n\ge3\), rather than arbitrary deleted matchings or general multipartite \(T^*(r,a)\). It does not assert that other parts of the 2024 article are incorrect, nor that the paper's unimodality conclusion is false. The conclusion about bibliographic priority is restricted to inspected published and open-access records and available mathematical records; an unindexed correction or equivalent statement may exist. Independent mathematical validation has not been performed.

## References
[1] B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar, and E. J. Thomas, "Characterization of general position sets and its applications to cographs and bipartite graphs," Applied Mathematics and Computation 359 (2019), 84–89. arXiv:1812.08460, first public 20 December 2018. https://arxiv.org/abs/1812.08460

[2] "Lower general position sets in graphs," arXiv:2306.09965, first public 16 June 2023. https://arxiv.org/abs/2306.09965

[3] V. Iršič, S. Klavžar, G. Rus, and J. Tuite, "General Position Polynomials," Results in Mathematics 79 (2024), article 110; DOI:10.1007/s00025-024-02133-3, first publicly available as arXiv:2401.05696 on 11 January 2024. https://arxiv.org/abs/2401.05696 ; https://doi.org/10.1007/s00025-024-02133-3
