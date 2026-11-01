# An integral Moore space in the icosahedral three-clique-free complex

## Finding
Let \(I\) be the twelve-vertex icosahedral graph, and let \(\mathrm{CF}_3(I)\) be the simplicial complex of vertex subsets containing no triangle of \(I\). Then its geometric realization has the **integral homotopy type**
\[
|\mathrm{CF}_3(I)|\simeq M(\mathbb Z/2,4)=S^4\cup_{\,2}e^5.
\]
Here the attaching map of the five-cell has degree two. In particular, \(\widetilde H_4(\mathrm{CF}_3(I);\mathbb Z)\cong\mathbb Z/2\), all other reduced integral homology groups vanish, and the complex is simply connected. Its pure five-dimensional simplicial structure is **not shellable**, since a pure shellable complex has torsion-free reduced homology concentrated in its top dimension. This is a calculation of a specific complex, not a classification of all polyhedral graphs.

## Assumptions and scope
There are no additional graph hypotheses. A concrete labeling fixes the twelve vertices \(0,1,\ldots,11\). Put \(U_i=1+i\) and \(L_i=6+i\) for \(i\in\mathbb Z/5\mathbb Z\), with north pole \(0\) and south pole \(11\). The graph has edges \(0U_i\), \(11L_i\), \(U_iU_{i+1}\), \(L_iL_{i+1}\), \(U_iL_i\), and \(U_iL_{i-1}\), for every index modulo five. These are thirty distinct edges; all twelve vertices have degree five, and this is the standard icosahedral graph. The twenty triangles are, for each \(i\),
\[
\{0,U_i,U_{i+1}\},\quad
\{11,L_i,L_{i+1}\},\quad
\{U_i,U_{i+1},L_i\},\quad
\{U_{i+1},L_i,L_{i+1}\}.
\]
The face condition is exactly that none of these twenty triples is contained in a chosen vertex subset. The empty face is included by convention, but face counts below count only nonempty faces.

## Proof
Represent a nonempty vertex subset by its twelve-bit integer mask \(m\), with vertex \(v\) represented by the bit \(2^v\). Exhaustively checking the twenty forbidden triples gives exactly \(1{,}047\) nonempty faces and face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,200,345,312,112).
\]
All \(112\) facets have six vertices. The executable verifier reconstructs the facets from first principles, rather than loading a face table.

Apply the following deterministic acyclic-matching algorithm to the nonempty face poset. Start with every face unmatched. Process the vertex labels in the order
\[
(6,0,4,3,2,5,9,8,10,11,1,7).
\]
At vertex \(v\), pair every still-unmatched pair \((\sigma,\sigma\cup\{v\})\) of faces, examining the smaller masks in increasing integer order. Remove both faces from further consideration. The result consists of \(522\) pairs and three unmatched faces, with masks \(64\) (a vertex), \(3124\) (a four-simplex), and \(1926\) (a five-simplex). The complete directed Hasse graph has \(1{,}047\) vertices and \(4{,}344\) codimension-one incidences. Orient unmatched incidences downward and matched incidences upward. An exhaustive topological sort visits every vertex, proving that the matching is acyclic, not merely locally compatible.

For the integer Morse differential, orient each simplex by increasing vertex labels and use the usual alternating simplicial boundary. Write \(a\prec b\) when \(a\) is a codimension-one face of \(b\), and set \([b:a]=(-1)^j\) when the removed vertex has position \(j\), counted from zero. For a four-face \(a\), define its projection coefficient \(c(a)\) onto the critical four-cell as follows: the critical four-face has coefficient one; a four-face matched downward to a three-face has coefficient zero; and if \(a\) is paired upward with a five-face \(b\), use the integral cancellation relation
\[
c(a)=-[b:a]\sum_{a'\prec b,\ a'\ne a}[b:a']c(a').
\]
Acyclicity makes these recurrences well-founded. Summing \([b:a]c(a)\) over the six codimension-one faces of the critical five-simplex gives **\(-2\)**. Specifically, the six contributions, ordered by removed vertices \(1,2,7,8,9,10\), are \((0,0,-1,0,0,-1)\). The verifier also computes the same integer by a different method: a triangular system cancelling all \(111\) four-to-five matched pairs on the column side.

Thus Forman's discrete-Morse theorem gives a CW model with one zero-cell, one four-cell, and one five-cell, whose only nonzero cellular differential is multiplication by \(-2\) from degree five to four. The four-skeleton is \(S^4\); the attaching map represents \(\pm2\) in \(\pi_4(S^4)\cong\mathbb Z\). Therefore the CW model is the Moore space \(M(\mathbb Z/2,4)\), proving the claim.

## Verification
Run `python3 verify.py` with Python 3. The self-contained checker constructs the thirty graph edges, independently enumerates triangles from edges and from the explicit twenty-triangle formula, constructs all admissible faces, and recomputes facets. It checks the \(522\) pairs, all \(4{,}344\) incidences, directed acyclicity, the two matching-based calculations of the integer Morse coefficient, and simplicial boundary ranks modulo \(2,3,5,7\). The latter provide a separate diagnostic: mod-two reduced Betti numbers are one in degrees four and five, while the corresponding ranks vanish over the three odd-prime fields. The integral Morse differential, not the modular checks, establishes the exact order-two torsion and homotopy type.

## Relationship to prior work
Ghosh and Selvaraja's *Shellability in Clique-Free Complexes of Graphs* (first posted February 10, 2026, arXiv:2602.09623v1) studies \(t\)-clique-free complexes, establishes shellability for certain chordal graph classes, and gives clique-attachment constructions. The icosahedral graph is neither chordal nor one of the covered special graph constructions; that paper does not give this complex's integral homotopy type or torsion. Moradi's *\(t\)-clique ideal and \(t\)-independence ideal of a graph* (arXiv:1712.00583v1, December 2, 2017) develops the ideal-language formulation and treats complements of paths and cycles and other classes, but not this icosahedral example. The statement is also different from results on **the ordinary matching complex**, **three-cut complex**, or **neighborhood complex** of the icosahedral graph: those complexes have different vertices or face conditions, and their homotopy types do not imply the present claim. Searches using the phrases "icosahedral clique-free", "icosahedron triangular-face hypergraph independence", "triangle-free vertex subsets of the icosahedral graph", "icosahedral \(\mathrm{CF}_3\)", and exact torsion/face-count aliases did not identify a covering statement. This is a best-knowledge literature comparison, not a proof that no unindexed equivalent exists.

## Limitations
The classification is for the **three-clique-free complex** of the specific twelve-vertex graph; it does not establish a general formula for all triangulated spheres or other Platonic graphs. The example is non-shellable, but makes no assertion that all nonchordal graphs have non-shellable clique-free complexes. Exact equivalence in literature not indexed by the searches remains a residual originality risk. The supplied program is a finite exhaustive certificate, not a formally verified proof assistant development or independent audit.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (2026-02-10), https://arxiv.org/abs/2602.09623.
2. S. Moradi, *\(t\)-clique ideal and \(t\)-independence ideal of a graph*, arXiv:1712.00583v1 (2017-12-02), https://arxiv.org/abs/1712.00583.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; standard discrete-Morse CW reconstruction.
4. A. Hatcher, *Algebraic Topology* (2002), Chapter 2, Example 2.40, for integral homology and Moore spaces.
