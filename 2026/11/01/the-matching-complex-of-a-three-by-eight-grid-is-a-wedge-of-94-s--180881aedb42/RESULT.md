# The matching complex of a three-by-eight grid is a wedge of 94 seven-spheres

## Finding
Let \(G=P_3\square P_8\) be the finite Cartesian grid graph with three rows and eight columns. Its ordinary matching complex \(\mathcal M(G)\) has one vertex for each edge of \(G\), and a nonempty edge set is a simplex exactly when its graph edges have pairwise disjoint endpoints. Then the geometric realization has integral homotopy type
\[
|\mathcal M(P_3\square P_8)|\simeq\bigvee^{94}S^7.
\]
Equivalently, \(\widetilde H_7(\mathcal M(G);\mathbb Z)\cong\mathbb Z^{94}\) and \(\widetilde H_i(\mathcal M(G);\mathbb Z)=0\) for every \(i\ne7\). The assertion is about the **full ordinary matching complex**, not the perfect-matching subcomplex or the discrete-Morse complex.

## Assumptions and scope
Use row indices \(r\in\{0,1,2\}\) and column indices \(c\in\{0,\ldots,7\}\). Vertex \((r,c)\) is assigned integer label \(8r+c\). Edges are precisely horizontal pairs \((r,c)(r,c+1)\) for \(c<7\) and vertical pairs \((r,c)(r+1,c)\) for \(r<2\). There are 24 vertices and 37 undirected edges. Number the 37 edges in the following explicit deterministic order: visit \((r,c)\) with row increasing first and column increasing second; append its vertical downward edge if present, then append its rightward edge if present. The matching complex uses these edges as ordered simplicial vertices. Chain groups, incidence numbers, and Morse boundaries are over \(\mathbb Z\); orientations follow increasing vertex indices.

## Proof
**1. Complete face enumeration.** Every matching is encoded by a 37-bit mask. Traverse all graph edges recursively: either skip an edge or include it when neither endpoint is already used. Discard the empty set. This produces exactly \(1{,}222{,}549\) nonempty faces, with dimension-indexed face vector
\[
(37,584,5161,28191,99183,227262,335396,308330,165871,46801,5580,153).
\]
Independently, a three-state-column monomer–dimer transfer dynamic program records the incoming occupied subset of each three-vertex column and the accumulated number of selected edges. Its resulting matching-count polynomial, including its constant term one, has exactly the same coefficients as this face vector. The attached `verify.py` implements both enumerations from the definitions.

**2. A complete acyclic discrete-Morse matching.** Start with every nonempty simplex unmatched. Visit the 37 ordered graph edges successively. At pivot edge \(e\), pair each remaining face \(F\) not containing \(e\) with \(F\cup\{e\}\) whenever the latter is also among the remaining faces; remove both. These pairs form a matching on the nonempty face poset. Exactly \(611{,}209\) pairs are made, leaving 131 critical faces: one of dimension zero, 112 of dimension seven, and 18 of dimension eight. Exhaustively construct every nonempty codimension-one incidence and direct it from upper face to lower face except that paired incidences are reversed. There are exactly \(8{,}827{,}379\) such incidences. A topological sort visits all \(1{,}222{,}549\) faces, so the directed Hasse graph is acyclic. This supplies a finite, complete acyclic discrete-Morse matching rather than a heuristic face count.

**3. Integral Morse boundary.** The resulting Morse CW model has one zero-cell, 112 seven-cells, 18 eight-cells, and no other cells. Its only possibly nonzero differential is \(\partial_8:\mathbb Z^{18}\to\mathbb Z^{112}\). Determine this differential using signed gradient paths. If \(f\) is a noncritical seven-face paired with an eight-face \(u\), and the incidence coefficient \([u:f]\) is \(\pm1\), then the contribution of \(f\) to critical seven-faces is
\[
R(f)=-[u:f]\sum_{g\subset u,\;|g|=|f|,\;g\ne f}[u:g]R(g).
\]
For a critical seven-face \(f\), set \(R(f)=f\); for other seven-faces not involved in those pairs, set \(R(f)=0\). Acyclicity makes this recursion well founded. For each critical eight-face \(u\), the Morse boundary is \(\sum_{f\subset u}[u:f]R(f)\). Exhaustive calculation gives a 112-by-18 integer matrix with exactly 182 nonzero entries, all \(\pm1\). Integer row and column operations, using only unit pivots and no division, reduce it to 18 diagonal ones and otherwise zeros; the checker supplies every operation deterministically by finding the first available unit pivot. In particular, its Smith invariant factors are eighteen ones, so its cokernel is free of rank 94 and its kernel is zero.

**4. Homotopy classification.** As there are no cells in dimensions one through six, the seven-skeleton of the Morse CW model is \(\bigvee^{112}S^7\). For a wedge of seven-spheres the Hurewicz map \(\pi_7\to H_7\) is an isomorphism, so each eight-cell attaching map is completely determined by its integer degree vector, i.e. its Morse boundary column. Unimodular basis changes of \(\mathbb Z^{112}\) are realized by self-homotopy equivalences of the seven-sphere wedge, while elementary column changes correspond to homotopy changes of the eight-cell attachments. The 18 unit diagonal attachments therefore cancel 18 corresponding seven-spheres up to homotopy. The remaining complex is \(\bigvee^{112-18}S^7\), proving the claim. No inference of homotopy type is made from field-valued homology alone.

## Verification
Run `python verify.py` with Python 3.9 or later, using only the standard library. The checker regenerates every matching mask and an independent column-transfer count; reconstructs the complete 611,209-pair discrete-Morse matching; builds and topologically sorts all 8,827,379 oriented Hasse incidences; calculates the signed 112-by-18 Morse differential; and verifies eighteen integral unit pivots and the predicted reduced Euler characteristic. Its complete successful output is:

```text
VERIFY_OK edges=37 faces=1222549 f_vector=(37, 584, 5161, 28191, 99183, 227262, 335396, 308330, 165871, 46801, 5580, 153)
VERIFY_OK transfer_counts=agreement pairs=611209 critical=(1_0,112_7,18_8)
VERIFY_OK hasse_incidences=8827379 dag_vertices=1222549
VERIFY_OK integer_morse_differential=112x18 nonzero=182 unit_pivots=18
VERIFY_OK homotopy=vee_94_S7 reduced_euler=-94
```

## Relationship to prior work
Chauhan, Sharma, and Shukla's September 2026 preprint [1] proves connectivity and homological vanishing statements for the entire family of three-row rectangular-grid matching complexes. Its publicly accessible abstract states that for \(n\ge2\) the reduced homology vanishes in dimensions at most \(n-2\) and in the top dimension, with nonzero homology in degree \(n-1\), and it establishes simple connectivity for \(n\ge3\). The present result supplies an **explicit integral homotopy classification at width eight**, which does not follow from those abstract statements. However, this preprint's full text was unavailable in the access attempts, so its possible additional width-eight computations cannot be ruled out. A previously published general sphere-wedge classification [2] was explicitly retracted; the authors' corrigendum identifies an error in certain purported nullhomotopy arguments. Consequently that withdrawn classification cannot be used to imply the result. Other known finite-grid matching-complex calculations, including those for a four-by-four square grid, concern distinct graph parameters and do not imply the exact width-eight homotopy statement.

## Limitations
Only the ordinary matching complex of this particular three-by-eight grid is classified. This does not prove a wedge-of-spheres theorem for every rectangular width or a general three-row family. The 94-dimensional homology rank may be deducible from earlier enumerative work; the distinctive conclusion is the verified integral homotopy type, with an explicit acyclic matching and primitive boundary. Primary-paper full-text access was limited, so undiscovered equivalent formulations remain an originality risk. The computation is reproducible but has not been independently mathematically audited.

## References
1. P. Chauhan, A. Sharma, and S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, first submitted 2026-09-23, https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, and A. Singh, *Matching complexes of \(3\times n\) grid graphs*, Electronic Journal of Combinatorics 28 (2021), P4.16, DOI:10.37236/10496, explicitly retracted by authors' corrigendum.
3. Standalone `verify.py` included with this result, providing exhaustive face, acyclicity, and integral-boundary calculations.
