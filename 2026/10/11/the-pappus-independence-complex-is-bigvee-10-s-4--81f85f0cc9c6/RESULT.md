# The Pappus independence complex is \(\bigvee^{10}S^4\)
## Finding
Let \(P\) be the standard Pappus graph, equivalently the cubic graph with LCF notation \([5,7,-7,7,-7,-5]^3\). Its independence complex satisfies
\[
\operatorname{Ind}(P)\simeq \bigvee^{10}S^4.
\]
Equivalently, the complex of independent vertex sets of \(P\) has the homotopy type of a wedge of ten four-spheres.

## Assumptions and scope
The graph is the simple graph on vertices \(0,1,\ldots,17\) consisting of the Hamiltonian cycle \(0-1-\cdots-17-0\) together with the chords encoded by the LCF word \([5,7,-7,7,-7,-5]^3\). This is the standard Pappus graph. The independence complex \(\operatorname{Ind}(P)\) contains a face exactly when its vertices are pairwise nonadjacent.

The claim concerns this one finite graph. It does not assert a formula for all Levi graphs, all cubic symmetric graphs, or all incidence graphs.

## Proof
The complete list of nonempty independent sets has \(2597\) faces and face vector
\[
(18,126,438,801,756,348,90,18,2).
\]
Use the vertex order
\[
2,1,16,14,3,10,4,13,15,11,8,9,17,0,7,5,12,6.
\]
Starting with all faces unmatched, at the stage for a vertex \(v\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unmatched. Each pair is a codimension-one cover in the face poset.

The resulting matching has \(1293\) pairs. Exhaustive orientation of all \(11430\) Hasse covers, with matched covers reversed and all other covers directed upward, is acyclic: a complete topological sort visits all \(2597\) faces. Thus this is an acyclic discrete-Morse matching.

Exactly eleven faces are critical: one critical \(0\)-simplex and ten critical \(4\)-simplices. There are no other critical cells. Discrete Morse theory therefore gives a CW complex homotopy equivalent to \(\operatorname{Ind}(P)\) with one \(0\)-cell, ten \(4\)-cells, and no cells in positive dimensions below \(4\). Every attaching map of a \(4\)-cell has target the \(0\)-skeleton, so all attaching maps are constant. Hence the CW complex is \(\bigvee^{10}S^4\), proving the claim.

## Verification
The bundled `verify.py` reconstructs the graph from its explicit edge list, enumerates every independent set, reproduces the fixed sequential matching, checks every matched cover, constructs the full directed Hasse graph, and verifies acyclicity by topological sorting.

As an independent chain-level check, it computes all simplicial boundary ranks over \(\mathbf F_2\):
\[
(17,109,329,472,274,74,16,2)
\]
for boundary maps in dimensions \(1\) through \(8\). The reduced Betti vector is
\[
(0,0,0,0,10,0,0,0,0),
\]
and the Euler characteristic is \(11\), both agreeing with the Morse model. Running `verify.py` produces the bundled `verification_output.txt` ending in `VERIFY_OK`.

## Relationship to prior work
Matsushita and Wakatsuki study exact homotopy types of independence complexes and emphasize that even easily described graphs can have difficult independence-complex homotopy types. Their 2022 paper treats square-grid graphs and has primary MSC 55P10; the inspected full text contains no Pappus or incidence-graph instance.

Tsukuda proves a general theorem identifying the independence complex of a finite incidence graph, up to suspension, with the Alexander dual of a hypergraph independence complex. This applies structurally because the Pappus graph is a Levi graph, but the inspected paper does not compute the Pappus instance and contains no occurrence of “Pappus.” Thus that theorem explains why the example is natural but does not imply the numerical homotopy type above without an additional computation or argument.

Exact-claim and alias searches for the Pappus graph, its Levi-graph description, its incidence-graph description, and the wedge \(\bigvee^{10}S^4\) did not locate a published statement of this homotopy type. This negative search is evidence of a gap, not a proof of global novelty.

## Limitations
This is a finite exact result, not a family theorem. The proof relies on a fully enumerated finite discrete-Morse certificate, although the certificate is independently replayable from the graph definition. A residual originality risk remains from older or differently indexed literature on independence complexes, Levi graphs, Alexander duality, or the Pappus configuration that was not surfaced by the searches.


## References
1. T. Matsushita and S. Wakatsuki, “Independence complexes of \( (n\times 6) \)-grid graphs,” arXiv:2207.10363, first public 2022-07-21. The paper lists 2020 MSC 55P10 and 05C69.
2. S. Tsukuda, “Independence complexes and incidence graphs,” Contributions to Discrete Mathematics 12 (2017), 28–46, doi:10.55016/ojs/cdm.v12i1.62277.
3. R. Forman, “Morse theory for cell complexes,” Advances in Mathematics 134 (1998), 90–145.
4. E. W. Weisstein, “Pappus Graph,” MathWorld, for the standard graph description and LCF notation.
