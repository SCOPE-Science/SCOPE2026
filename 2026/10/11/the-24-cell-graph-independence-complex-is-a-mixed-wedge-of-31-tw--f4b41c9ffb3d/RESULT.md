# The 24-cell graph independence complex is a mixed wedge of 31 two-spheres and 21 three-spheres

## Finding
Let \(G\) be the edge graph of the regular four-dimensional 24-cell, with vertex set
\[
V=\{(x_1,x_2,x_3,x_4)\in\{0,\pm1\}^4:\text{exactly two coordinates are nonzero}\}
\]
and with an edge between distinct \(v,w\) exactly when their Euclidean dot product is \(1\). Let \(\operatorname{Ind}(G)\) be the abstract simplicial complex consisting of all vertex subsets containing no edge of \(G\). Then
\[
\boxed{\operatorname{Ind}(G)\simeq\bigvee^{31}S^2\vee\bigvee^{21}S^3.}
\]
In particular, its reduced integral homology is \(\mathbb Z^{31}\) in degree \(2\), \(\mathbb Z^{21}\) in degree \(3\), and zero in all other degrees. This is an integral homotopy classification, not just a homology calculation.

## Assumptions and scope
All graphs are finite, undirected, and simple; all simplicial complexes are realized geometrically. Here the 24 vectors have squared norm \(2\). Distinct vertices at Euclidean distance \(\sqrt 2\) have dot product \(1\), so the adjacency rule reproduces the ordinary edge graph of the regular 24-cell. It has 24 vertices, 96 edges and degree eight at every vertex. A simplex is any nonempty independent subset, together with the conventional empty face. The statement is for this exact graph, not for arbitrary four-polytopes or every root-system graph.

For reproducibility, label the vectors by increasing ordered support \((i,j)\), with \(0\le i<j<4\), and then by signed coordinates \((-1,-1),(-1,1),(1,-1),(1,1)\). Encode a face as an integer whose set bits are its vertex labels. In each dimension, the critical cells used below are ordered by increasing bit mask.

## Proof
**Step 1: exhaustive face poset.** Recursively generate an independent set by adding only a higher-index vertex nonadjacent to all previously selected vertices. Every independent set has a unique increasing vertex list, so this procedure is exhaustive without multiplicities. Its face vector in dimensions \(0\) through \(7\) is
\[
(24,180,488,474,216,84,24,3),
\]
representing 1,493 nonempty faces; there are no higher-dimensional faces. The graph and every face are reconstructed from the integer vectors by the standalone verifier.

**Step 2: explicit acyclic matching.** Start with all nonempty faces unmatched. For each vertex label \(i=0,1,\ldots,23\), in that order, pair every still-unmatched face \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\), whenever both faces remain unmatched. Remove each pair before moving to the next label. This prescribes exactly 717 incident face pairs and leaves one critical vertex, 34 critical two-simplices and 24 critical three-simplices. Orient every Hasse incidence from the larger face to the smaller, reversing the matched incidences. Direct inspection of **all 5,496 directed incidences**, by a complete topological sort visiting all 1,493 faces, proves acyclicity. Forman's discrete Morse theorem yields a CW complex with exactly those critical cells and no others.

**Step 3: signed integral Morse differential.** Orient each simplex by the increasing order of its vertex labels. If \(\tau=\{i_0<\cdots<i_d\}\), use
\[
\partial\tau=\sum_{j=0}^{d}(-1)^j\bigl(\tau\setminus\{i_j\}\bigr).
\]
Compute the differential from the 24 critical three-cells to the 34 critical two-cells by signed gradient-path elimination: the projection of a critical two-cell to itself is one, the projection of a two-cell matched with a one-cell is zero, and a two-cell \(f\) matched upward with three-cell \(g\) is replaced by the negative, sign-adjusted sum of the remaining faces of \(\partial g\). Acyclicity guarantees that this recurrence terminates. The exact resulting \(34\times24\) integer matrix \(B\) has the following complete sparse description, with row and column indices beginning at zero.

Let \(e_j\) denote the \(j\)-th standard basis row vector of \(\mathbb Z^{24}\), and set
\[
\begin{aligned}
a&=-e_0+e_1+e_2+e_4+e_6-e_{15}-e_{19},\\
b&=e_0+e_{15}+e_{19},\\
c&=-e_0+e_9+e_{11}.
\end{aligned}
\]
Rows \(0,1,2\) of \(B\) are \(a,a,-a\), rows \(3,4,5\) are \(b,b,-b\), rows \(6,7,8\) are \(c,c,-c\), and rows \(9\) through \(33\) vanish. Thus \(\operatorname{rank}_{\mathbb Q}B\le3\). The submatrix in rows \(0,3,6\) and columns \(0,1,9\) is
\[
\begin{pmatrix}-1&1&0\\1&0&0\\-1&0&1\end{pmatrix},
\]
with determinant \(-1\). Hence \(B\) has rank exactly three and has three unit Smith invariant factors, with all remaining entries zero after unimodular row/column operations. This verifies the *integral* attaching degrees, not merely a finite-field rank.

**Step 4: passage to homotopy type.** The Morse CW complex has a single zero-cell, no one-cells, and 34 two-cells. Its two-skeleton is therefore \(\bigvee^{34}S^2\). By the Hurewicz isomorphism \(\pi_2(\bigvee^{34}S^2)\cong\mathbb Z^{34}\), each attaching map of a three-cell is completely determined by its integer degree vector. Unimodular basis changes of the two-spheres and three-cell slides realize the Smith reduction of \(B\) up to homotopy equivalence. The three unit attachments cancel three two/three-cell pairs, while 21 remaining three-cells have null attaching maps. The result is exactly \(\bigvee^{31}S^2\vee\bigvee^{21}S^3\). There are no cells in dimension four or above in the Morse model, so no higher attaching maps remain.

## Verification
Run `python3 verify_24cell.py` and `python3 verify_24cell_independent.py` using Python 3.10 or later; both scripts require only the standard library. The first enumerates the complete face poset, constructs and independently checks each proposed incidence matching, topologically sorts the entire directed Hasse diagram, computes the signed Morse differential, verifies its exact sparse formula, its rational rank three, and its displayed determinant \(-1\). The second uses a differently ordered root construction and a separate increasing-tuple enumeration, then computes all raw simplicial boundary ranks over the fields of two, three and five elements. In each field its boundary-rank vector is
\[
(23,157,300,153,63,21,3),
\]
which gives reduced Betti ranks \((0,0,31,21,0,0,0,0)\). The finite-field checks are independent corroboration; the proof of the integral homotopy type relies on the integral Morse differential and its unimodular minor.

## Relationship to prior work
Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418v1, publicly submitted July 2, 2010) develops general techniques and evaluates special graph classes, including cases with triangle-free and claw-free hypotheses. Its results do not compute the independence complex of the 24-cell graph. In particular, each vertex of this graph belongs to twelve triangles, so the triangle-free-vertex suspension criterion cannot be applied directly. Deshpande and Singh's *Higher independence complexes of graphs and their homotopy types* (arXiv:2001.05448v2) computes complete multipartite, fully whiskered, path, cycle and perfect-tree families; its graph classes do not include this regular degree-eight 24-cell graph. Its staged element-matching method is related to the method used for this calculation, but does not supply the matrix or the asserted answer.

The 24-cell's standard vertex coordinates and the facts that it has 24 vertices and 96 edges are documented in MathWorld's entry *24-Cell*. The new content here is the exact integral homotopy type of the ordinary independence complex of its edge graph. These comparisons are not a claim that an equivalent statement is absent from all unindexed or unpublished literature.

## Limitations
The classification concerns only the specifically defined 24-cell edge graph. Exhaustive enumeration and exact Morse-path algebra are feasible because the complex has 1,493 nonempty faces; no asymptotic family theorem, stronger equivalence of graph invariants, or conclusion about other root polytopes is claimed. The verification routines constitute a reproducible finite certificate, not an external independent mathematical assessment.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, July 2, 2010; https://arxiv.org/html/1007.0418v1 .
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v2; https://arxiv.org/html/2001.05448v2 .
3. Wolfram MathWorld, *24-Cell*, https://mathworld.wolfram.com/24-Cell.html .
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
