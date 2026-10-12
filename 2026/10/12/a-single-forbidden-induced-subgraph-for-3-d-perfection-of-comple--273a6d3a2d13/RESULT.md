# A single forbidden induced subgraph for \(3,d\)-perfection of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge3\). For every integer \(d\ge2\),
\[
G\text{ is }(3,d)\text{-perfect}\quad\Longleftrightarrow\quad G\text{ has no induced }K_{3,2,1}.
\]
Equivalently, if
\[
M=\max_i n_i,\qquad p=\left|\left\{i:n_i\ge2}\right|,
\]
then \(G\) is \(3,d\)-perfect exactly when \(M\le2\) or \(p\le1\). The graph \(K_{3,2,1}\) is the unique induced-subgraph-minimal non-\(3,d\)-perfect graph within the connected complete multipartite class. The answer is independent of \(d\) for all \(d\ge2\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The notation and definition of \(k,d\)-perfection are those of Cody and Detore: a graph is \(k,d\)-perfect when every induced subgraph \(H\) satisfies
\[
\chi_d^k(H)=\left\lceil\frac{\omega_d^k(H)}{k-1}\right\rceil.
\]
The theorem is stated for connected complete multipartite graphs with at least three nonempty parts. Induced subgraphs occurring in the definition may have fewer parts or may be edgeless. Only the case \(k=3\) is claimed here.

## Proof
A connected complete multipartite graph has diameter at most \(2\). Hence for every \(d\ge2\), the three-vertex sets lying on shortest paths of length at most \(d\) are exactly the triples whose vertices occupy two partite classes with multiplicities \(2+1\). Thus the \((3,d)\)-geodesic hypergraph is independent of \(d\) once \(d\ge2\).

Consider an induced subgraph \(H\). If it lies in one part, or if all of its nonempty parts have size \(1\), then it has no geodesic triple. Consequently \(\chi_d^3(H)=1\), while \(\omega_d^3(H)\le2\), and the perfection equality holds.

Now suppose \(H\) meets at least two parts and has a non-singleton part. Then \(H\) contains a geodesic triple, so \(\chi_d^3(H)\ge2\). If exactly one part of \(H\) is non-singleton, color that part with one color and every remaining singleton part with a second color. If every part of \(H\) has size at most \(2\), color the two vertices of each two-vertex part differently and color singleton parts arbitrarily. If \(H\) has only two nonempty parts, color the two parts with different colors. In every case each color class contains no \(2+1\) triple, so \(\chi_d^3(H)=2\).

For the clique side, when \(H\) has exactly one non-singleton part, a largest \((3,d)\)-clique has size \(3\): take two vertices from that part and one from another part. When \(H\) has at least two non-singleton parts, taking two vertices from each of two such parts gives a \((3,d)\)-clique of size \(4\), and no five vertices can form such a clique: support on at least three parts yields a transversal triple, while support on at most two parts forces three vertices into one part. Thus in every nontrivial case above,
\[
\left\lceil\frac{\omega_d^3(H)}2\right\rceil=2=\chi_d^3(H).
\]

It remains to identify when an induced subgraph can fail the displayed two-color constructions. Failure requires at least three nonempty parts, at least two non-singleton parts, and a part of size at least \(3\). These three conditions are equivalent to containing an induced \(K_{3,2,1}\). Conversely, on \(K_{3,2,1}\), choose two vertices from the three-vertex part and two from the two-vertex part to obtain \(\omega_d^3=4\). A two-coloring is impossible: among the three vertices of the largest part, one color repeats; that color cannot occur outside that part, so the two vertices of the second part and the singleton vertex all receive the other color, producing a monochromatic \(2+1\) geodesic triple. Hence \(\chi_d^3=3\), whereas the clique lower bound is \(2\).

Therefore a complete multipartite graph is \((3,d)\)-perfect exactly when it excludes induced \(K_{3,2,1}\). Deleting any vertex from \(K_{3,2,1}\) produces, up to removal of empty parts, one of \(K_{2,2,1}\), \(K_{3,1,1}\), or \(K_{3,2}\), each of which satisfies one of the two-color conditions above. This proves uniqueness of the minimal obstruction.

## Verification
A standalone checker constructs the graph metric directly, generates all geodesic triples, computes the exact hypergraph chromatic and clique numbers, and tests every induced part profile. It verifies the theorem for every complete multipartite profile of total order at most \(8\) and for \(d\in\{2,3,4\}\). The replay output is included as `verification_output.txt`. These finite checks are corroborative only; the all-orders theorem follows from the analytic proof.

## Relationship to prior work
Cody and Detore introduced the \(k,d\)-invariants and \(k,d\)-perfection and explicitly asked for the invariants and perfection behavior of complete multipartite graphs in Question 6.1 of the current version of their paper. Their first public arXiv version appeared on 2026-01-07, and the current version lists primary MSC 05C12.

Chandran, Di Stefano, Haritha, Thomas, and Tuite determined the general-position chromatic number of complete multipartite graphs. For connected complete multipartite graphs this gives the coloring side of the \((3,2)\) theory, but it neither defines \(k,d\)-perfection nor supplies the clique-side hereditary equality or the forbidden induced-subgraph characterization proved here. The initiating paper was inspected after that coloring result and still lists complete multipartite \(k,d\)-perfection as an open direction.

## Limitations
The theorem is restricted to complete multipartite graphs and to \(k=3\). It does not claim a forbidden-subgraph characterization for arbitrary graphs. Search coverage cannot exclude an unindexed or newly posted equivalent result, and the invariant is recent enough that concurrent work is a residual originality risk. The finite verifier does not prove the infinite theorem.

## References
1. B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351. First public version: 7 January 2026; current version: 27 August 2026.
2. S. V. Ullas Chandran, G. Di Stefano, S. Haritha, E. J. Thomas, and J. Tuite, *Colouring a graph with position sets*, arXiv:2408.13494v2, 10 September 2025.
