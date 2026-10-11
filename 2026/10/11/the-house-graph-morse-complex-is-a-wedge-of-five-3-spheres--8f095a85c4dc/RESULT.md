# The house-graph Morse complex is a wedge of five 3-spheres
## Finding
Let \(H\) be the house graph with vertices \(\{0,1,2,3,4\}\) and edges
\[
\{\{0,1\},\{1,2\},\{2,3\},\{3,0\},\{1,4\},\{2,4\}\}.
\]
Its Morse complex of acyclic discrete vector fields satisfies
\[
\mathcal M(H)\simeq \bigvee^{5}S^{3}.
\]

## Assumptions and scope
A primitive discrete vector field on a graph is an incidence pair consisting of a vertex and an incident edge. A discrete vector field is a collection of such pairs in which no graph vertex and no graph edge is used twice. Direct each paired edge away from its paired vertex. For a graph, the field is a gradient vector field exactly when this partial orientation has no directed cycle. The Morse complex \(\mathcal M(H)\) has primitive fields as vertices and gradient fields as simplices. The claim concerns only the stated graph.

## Proof
The six graph edges give \(12\) primitive vector fields. Exhaustive recursion through these primitives, enforcing the matching conditions and rejecting exactly additions that create a directed cycle, yields \(208\) nonempty simplices with face vector
\[
(12,51,90,55).
\]

On the complete nonempty face poset, use the deterministic toggle order
\[
(7,5,4,11,3,9,10,1,6,8,2,0),
\]
with primitive indices reconstructed by `verify.py`. At each stage an unmatched face not containing the current primitive is paired with its union with that primitive whenever the larger face is also present and unmatched. This produces \(101\) matched Hasse covers.

The face poset has \(592\) Hasse covers. Reverse the \(101\) matched covers and orient every other cover downward. Exhaustive topological sorting visits all \(208\) faces, proving that the matching is acyclic. The unmatched faces are exactly one \(0\)-simplex and five \(3\)-simplices. Forman's theorem therefore gives a CW model with one \(0\)-cell, five \(3\)-cells, and no cells in dimensions \(1\) or \(2\). Every \(3\)-cell attaches to the unique \(0\)-cell, so the CW model is \(\bigvee^{5}S^{3}\).

## Verification
The bundled verifier reconstructs all simplices, all Hasse covers, and the complete matching from the graph definition. Independently, exact permutation expansion of the graph Laplacian gives
\[
\det(L+xI)=x^{5}+12x^{4}+51x^{3}+90x^{2}+55x,
\]
whose rooted-forest coefficients reproduce the face vector. Direct simplicial boundary calculations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) all give boundary ranks \((11,40,50)\) and Betti vector \((1,0,0,5)\). These are cross-checks; the wedge conclusion uses the globally verified acyclic matching.

## Relationship to prior work
Scoville and Zaremsky define the same Morse complex, list primary MSC \(55U05\), and state that exact homotopy types are known only for a handful of examples; their general graph results concern connectivity and do not determine the house graph. Capitelli and Minian identify graph Morse complexes with complexes of rooted forests and discuss earlier exact cases for complete graphs, paths, and cycles. Kozlov's closely related directed-tree results concern different graph families. The house graph, which contains both a \(4\)-cycle and a triangle, is not a specialization of those tree/path/cycle families.

Exact searches under “house graph,” “roof graph,” “Morse complex,” “rooted forest complex,” and “complex of directed forests” did not locate a prior statement of the displayed homotopy type. Search failure is not treated as proof of novelty.

## Limitations
This is a finite exact computation for one named graph, not a family theorem. An unindexed computation, thesis, software table, or uncommon alias could contain the same result. Prime-field homology alone would not establish the wedge decomposition; the proof depends on the explicit globally acyclic face-poset matching.

## References
1. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1, first public 2020-04-22; primary MSC \(55U05\).
2. N. A. Capitelli and E. G. Minian, *A Simplicial Complex is Uniquely Determined by Its Set of Discrete Morse Functions*, Discrete Comput. Geom. 58 (2017), 144–157, DOI 10.1007/s00454-017-9865-z.
3. D. N. Kozlov, *Complexes of Directed Trees*, J. Combin. Theory Ser. A 88 (1999), 112–122, DOI 10.1006/JCTA.1999.2984.
