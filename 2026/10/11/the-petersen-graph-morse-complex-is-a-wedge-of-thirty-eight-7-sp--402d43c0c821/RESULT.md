# The Petersen graph Morse complex is a wedge of thirty-eight 7-spheres and 294 8-spheres

## Finding
Let \(P\) be the Petersen graph, and let \(\mathcal M(P)\) be its **ordinary discrete Morse complex**: a vertex is an incident vertex–edge pair in \(P\), and a simplex is a simultaneously compatible set of such pairs with no closed gradient path. Then
\[
\mathcal M(P)\simeq \bigvee^{38}S^{7}\vee\bigvee^{294}S^{8}.
\]
In particular the only nonzero reduced integral homology groups are \(\widetilde H_7\cong\mathbb Z^{38}\) and \(\widetilde H_8\cong\mathbb Z^{294}\), with no torsion. This assertion concerns the ordinary Morse complex, not the edge-matching, pure-Morse, or strong-Morse subcomplexes.

## Assumptions and scope
Take the graph vertices to be \(\{0,1,\ldots,9\}\). For each \(i\in\{0,\ldots,4\}\), include edges \(\{i,(i+1)\bmod5\}\), \(\{i,5+i\}\), and \(\{5+i,5+((i+2)\bmod5)\}\). There are fifteen undirected edges and thirty possible oriented incidences \(v\to w\), one for each choice of endpoint \(v\) of an edge \(\{v,w\}\).

Represent a set of incidences by a 30-bit mask, with incidences ordered lexicographically by undirected edge then its oriented endpoint as in the attached verifier. It is a face if every graph vertex occurs at most once as a tail, every undirected edge appears at most once, and the chosen arrows form no directed cycle. These are exactly the acyclic partial matchings of the graph's vertex–edge Hasse diagram. The topological claim is for the entire resulting simplicial complex, including all nonmaximal faces, over the integers.

## Proof
**1. Complete finite model.** Each face is a rooted spanning forest with each component oriented toward its unique root: outdegree is at most one, and an undirected cycle would necessarily be directed because its number of selected arrows equals its number of vertices. Conversely an oriented rooted forest supplies an allowed set of incidences. Exhausting the four outgoing choices (none or one of three neighbors) at each of ten vertices and rejecting cycles gives the face counts, indexed by incidence-set size \(k=0,\ldots,9\):
\[
(1,30,390,2880,13305,39882,77640,94800,66000,20000).
\]
The total is \(314{,}928\) including the empty face. Independently the matrix–forest theorem and the Petersen Laplacian give the generating polynomial
\[
\det(I+tL)=(1+2t)^5(1+5t)^4,
\]
whose coefficients agree with this entire vector. The second checker proves the polynomial identity by evaluating the determinant with exact fraction-free arithmetic at ten integers and invokes polynomial uniqueness, not a floating-point spectral estimate.

**2. Acyclic Morse reduction.** Sort the thirty incidence symbols by the same graph representation, and process them in the deterministic order recorded in `artifacts/verify_petersen.py`. At each stage, pair every as-yet-unmatched face \(\sigma\) lacking the chosen incidence with \(\sigma\cup\{a\}\) whenever both remain. The verifier checks that each face participates in at most one pair and then explicitly constructs the complete directed face-incidence graph, reversing exactly the matched arrows. An exhaustive topological sort visits all \(314{,}928\) faces over all \(2{,}099{,}520\) cover incidences, certifying acyclicity. In the augmented matching the empty face is paired with one vertex. Removing that one pair and restricting to nonempty faces leaves an acyclic matching, because deleting a vertex and its incident arrows from an acyclic directed graph cannot create a cycle. The ordinary Morse CW model therefore has exactly one critical 0-cell, 77 critical 7-cells, and 333 critical 8-cells, with no other critical cells.

**3. Integral attaching matrix.** Give each oriented simplex its increasing-incidence orientation. For a face \(\tau\) obtained by deleting one symbol from \(\sigma\), the simplicial incidence number is \((-1)^r\), where \(r\) is the zero-based position of that symbol. For every matched pair \(\ell\subset u\) with \(\dim\ell=7\), the elementary elimination relation is
\[
[\ell]\longmapsto -[u:\ell]^{-1}\sum_{\tau\subset u,\;\tau\ne\ell}[u:\tau]\,[\tau].
\]
Here all incidence coefficients \([u:\ell]\) equal \(\pm1\). Acyclicity makes the recursive expansion terminate. Applying these substitutions to the boundary of every critical 8-simplex gives the exact integral degree matrix \(B\) of size \(77\times333\), with 235 nonzero entries, all in \(\{-1,1\}\). The verifier performs integral row and column operations and finds precisely 39 unit pivots, each \(\pm1\), followed by a **zero** remaining submatrix. Thus \(B\) is integrally equivalent to \(\operatorname{diag}(I_{39},0)\). This is a direct unimodular certificate, not a rank computation only over a field.

**4. From integral degrees to homotopy.** The 7-skeleton of the Morse CW complex is a wedge of 77 seven-spheres, since all cells of dimensions 1 through 6 are absent. Because this wedge is 6-connected, the Hurewicz isomorphism identifies its \(\pi_7\) with its seventh integral homology, so every 8-cell attaching map is classified by its integer degree vector. Basis changes of the free 7-cells and slides of 8-cells realize the unimodular equivalence above on attaching maps. Cancelling 39 unit-degree cell pairs leaves 38 seven-spheres and 294 eight-spheres. This proves the claimed homotopy equivalence, not merely the homology ranks.

## Verification
Execute `python3 artifacts/verify_petersen.py` using standard Python 3. The program reconstructs every face, outputs `FACES_OK 314928`, constructs 157,259 augmented matched pairs, verifies all cover incidences and acyclicity, computes the signed 77-by-333 Morse boundary and all 39 unit cancellations, and terminates with `PETERSEN_HOMOTOPY_PASS S7_x_38 S8_x_294`. Execute `python3 artifacts/verify_petersen_counts.py` for an independent determinant-based face enumeration check; it terminates with `INDEPENDENT_ROOTED_FOREST_COUNT_OK` and the ten coefficients above. Both programs were executed from these source contents prior to release. Only exact integer arithmetic is used.

## Relationship to prior work
Chari and Joswig identify graph discrete Morse faces with rooted forests and relate their enumerators to graph Laplacians; they do not establish the present Petersen homotopy type. Kozlov studies simple-homotopy comparison methods for graph-derived complexes, providing the archive-era topological context but no Petersen-specific Morse classification. Donovan, Lin, and Scoville prove graph-family and strong-collapse results; the Petersen graph does not satisfy the leaf assumptions used in their family calculations. Scoville and Zaremsky establish connectivity bounds but not these integral attaching maps.

The publicly available *Mod-2 homology of the Petersen graph Morse complex* gives exactly the same mod-two Betti ranks \(38\) and \(294\). That numerical result alone cannot imply either torsion-freeness or this wedge decomposition. Here the new information is the integer attaching-degree cancellation certificate and resulting full homotopy type. The earlier numerical ranks are expressly not claimed as new.

## Limitations
This is an exact finite classification of a single canonical graph. It does not establish a graph-family theorem or any uniqueness of the result across all publications; an unindexed or unpublished integral computation might overlap. The reproducibility checks are computational proofs conditional on standard integer arithmetic and the independently described finite graph-to-face correspondence. Independent external validation has not been performed.

## References
1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1 (first public 2005-03-28; primary MSC 57Q10), https://arxiv.org/abs/math/0503613.
2. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (2000), https://arxiv.org/abs/math/0011234.
3. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1 (2019), https://arxiv.org/abs/1909.11440.
4. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1 (2020), https://arxiv.org/abs/2004.10481.
5. *Mod-2 homology of the Petersen graph Morse complex*, public online result: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-petersen-graph-morse-complex--445405e72d9e.
