# Heawood two-independence homotopy and its sevenfold rotation character

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the point-line incidence graph of the Fano plane. Its **two-independence complex** \(\operatorname{Ind}_2(H)\) consists of vertex sets whose induced connected components contain at most two vertices. There is an integral homotopy equivalence

\[
\operatorname{Ind}_2(H)\simeq\bigvee^{13}S^5.
\]

For the canonical order-seven simultaneous translation \(\rho\) of the point and line labels, the complete rational character on reduced fifth homology is \(13\) at the identity and \(-1\) at every nonidentity element. Equivalently, as a rational \(C_7\)-module,

\[
\widetilde H_5(\operatorname{Ind}_2(H);\mathbb Q)
\cong \mathbb Q\oplus\mathbb Q(\zeta_7)^{\oplus2}.
\]

In particular the rotation-fixed reduced fifth homology is one-dimensional over \(\mathbb Q\).

## Assumptions and scope

Label seven points \(p_i\) and seven lines \(\ell_j\), where \(i,j\in\mathbb Z/7\mathbb Z\). The graph has precisely the edges \(p_i\ell_j\) satisfying \(i-j\in\{0,1,3\}\pmod7\). This is the Fano incidence graph because the differences of the three offsets exhaust all six nonzero residues up to sign. The simplicial complex has vertices \(p_i,\ell_j\), and a subset is a simplex if and only if every connected component in the induced graph has at most two vertices. The order-seven automorphism is \(\rho(p_i)=p_{i+1}\) and \(\rho(\ell_j)=\ell_{j+1}\). No extension to other incidence graphs or higher independence parameters is asserted.

## Proof

**Connected-triple reduction.** In any finite simple graph, an induced subgraph has all components of size at most two exactly when no selected vertex has two selected neighbors. Indeed, a connected component of size at least three contains a vertex of degree at least two. Since the Heawood graph is cubic and triangle-free, the minimal forbidden sets for \(\operatorname{Ind}_2(H)\) are the distinct three-vertex paths, three per possible center. There are therefore \(14\binom32=42\) forbidden triples.

**Exact simplicial enumeration.** Encode a subset as a fourteen-bit integer. Exhaustively retain exactly those nonzero masks containing no forbidden triple. This produces \(2256\) nonempty simplices with face numbers, in dimensions zero through six,

\[
(14,91,322,651,728,392,58).
\]

The \(128\) facets consist of \(70\) six-vertex faces and \(58\) seven-vertex faces; the complex is not pure.

**Discrete-Morse certificate.** Start with all nonempty faces unmatched. In vertex order \(0,1,\ldots,13\), match every remaining face not containing the current vertex to its remaining face obtained by adjoining that vertex, whenever both are available. Faces are inspected in increasing cardinality and then integer-mask order. The resulting matching contains exactly \(1121\) pairs and leaves one critical zero-face and thirteen critical five-faces. It is acyclic: orient all \(10150\) covering incidences upward except matched incidences, which are reversed. A complete topological ordering visits all \(2256\) faces. The supplied `verify_morse.py` regenerates all data and checks every incidence, not just the counts. Discrete Morse theory therefore gives a CW complex having one zero-cell, thirteen five-cells, and no other cells. Every five-cell attaches to a point, proving the integral wedge equivalence. No integral torsion or unverified attaching map is hidden in this inference.

**Equivariant trace.** The complex is invariant under \(\rho\). For any nonidentity rotation \(\rho^t\), invariant nonempty simplices must be unions of the two seven-point orbits. Exactly the entire point class and the entire line class are allowed; their union is not. On either six-simplex the permutation of its seven vertices is a seven-cycle with positive orientation sign. Thus the reduced simplicial Lefschetz number is \(-1+1+1=1\), including the degree-minus-one augmentation term. The only reduced homology occurs in odd degree five, so the homological trace equals \(-1\). At the identity it equals the rank \(13\). The rational irreducibles of \(C_7\) are the trivial module and the six-dimensional cyclotomic module. Writing their multiplicities \(a,b\), the equations \(a+6b=13\) and \(a-b=-1\) give \(a=1\), \(b=2\).

## Verification

The standalone `verify_morse.py` constructs the incidence graph and the \(42\) connected forbidden triples, checks the membership condition using an independent local-neighbor test, enumerates all simplices, forms the complete vertex-toggle matching, and checks the entire reversed-incidence digraph by topological sorting. It also directly sums signed fixed-simplex traces for all seven rotations.

The separate `verify_chains.py` constructs Fano lines by a different enumeration, decides admissibility by connected-component searches, builds all boundary matrices, and independently calculates boundary ranks in characteristics \(2\), \(3\), and \(5\). In each characteristic the ranks of boundaries in dimensions one through six are \((13,78,244,407,321,58)\); the only nonzero reduced Betti number is thirteen in degree five. Logs `morse_output.txt` and `chains_output.txt` were produced by executing those exact standalone scripts. The finite-field calculations corroborate the integral result; the complete acyclic matching proves the claimed integral homotopy equivalence.

## Relationship to prior work

Deshpande and Singh introduced and calculated higher-independence homotopy for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect trees [1]. The Heawood graph belongs to none of those classes. Abdelmalek, Deshpande, Goyal, Roy, and Singh proved shellability and vertex-decomposability statements for trees and caterpillars and studied examples among chordal graphs [2]; their hypotheses do not apply to this nonchordal girth-six graph. Known calculations for the ordinary independence complex of the Heawood graph concern the smaller one-independence complex, and neither they nor calculations for Heawood matching, two-matching, or cut complexes imply the present two-independence classification: those complexes have different vertices or forbidden-face conditions. We found no indexed statement determining this specific two-independence homotopy type or its translation character; an unindexed equivalent computation remains possible.

## Limitations

This is an exact computation for one canonical graph, not an infinite-family formula. The symmetry statement determines the rational representation of the cyclic subgroup, not the integral module or the full automorphism-group representation. The proof relies on an exhaustively checkable finite discrete-Morse certificate, supplied as standard Python source; calculations in finitely many characteristics alone would not establish the integral homotopy type. Novelty is assessed relative to inspected accessible primary works and search records and does not constitute a universal priority guarantee.

## References

[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15, Sections 2–6. https://arxiv.org/abs/2001.05448

[2] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first posted 2021-06-21, Sections 1–4. https://arxiv.org/abs/2106.10863
