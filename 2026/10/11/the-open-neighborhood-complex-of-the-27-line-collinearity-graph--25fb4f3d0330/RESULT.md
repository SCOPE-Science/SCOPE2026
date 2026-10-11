# The open-neighborhood complex of the 27-line collinearity graph is a wedge of 71 four-spheres

## Finding

Let \(H\) be the intersection graph of the 27 lines on any smooth complex cubic surface, equivalently the point-collinearity graph of the unique generalized quadrangle \(\mathrm{GQ}(2,4)\). The ordinary Lovász open-neighborhood complex has the integral homotopy type

\[
\mathcal N(H)\simeq \bigvee^{71}S^4.
\]

Thus its only nonzero reduced integral homology group is \(\widetilde H_4(\mathcal N(H);\mathbb Z)\cong\mathbb Z^{71}\). The statement determines homotopy type and not merely homology. In particular, it implies the standard neighborhood-complex chromatic lower bound \(\chi(H)\ge6\).

## Assumptions and scope

Use the exceptional-divisor intersection model on the blow-up of the projective plane at six points in general position. The 27 labels are six exceptional classes \(E_i\), fifteen classes \(L-E_i-E_j\) for \(i<j\), and six classes \(2L-\sum_{j\ne i}E_j\), where \(0\le i,j<6\). Represent a divisor by \((a,b_0,\ldots,b_5)\), meaning \(aL+\sum_i b_i E_i\), and evaluate intersection using

\[
(a,b)\cdot(c,d)=ac-\sum_{i=0}^5 b_i d_i.
\]

Distinct graph vertices are adjacent precisely when their divisor classes have intersection number one, i.e. the corresponding lines meet. All other pairs have intersection zero. This is the **complement** of the usual Schläfli skew-line graph. Direct enumeration gives 27 vertices, 135 edges, valency 10, one common neighbor for adjacent pairs, and five for nonadjacent pairs: the strongly regular parameters \((27,10,1,5)\).

The simplicial complex \(\mathcal N(H)\) consists of the empty face and those nonempty vertex subsets \(\sigma\subseteq V(H)\) for which there is a vertex \(v\) with \(\sigma\subseteq N_H(v)\). The neighborhood is **open**, so the common-neighbor vertex need not itself belong to the face and in fact cannot if the graph is loopless. All homotopy claims concern this specific undirected graph and complex, not a matching complex, a skew-line clique complex, or a metric Vietoris–Rips complex.

## Proof

**Graph and face enumeration.** Build all 27 divisor vectors in the stated order, form the symmetric adjacency masks by intersection, and insert every nonempty submask of each of the 27 ten-element open neighborhoods. Removing duplicates yields 23,778 nonempty simplices and the face counts in dimensions zero through nine:

\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9)
=(27,351,1800,4590,6588,5670,3240,1215,270,27).
\]

Thus \(\chi(\mathcal N(H))=72\), consistent with a wedge of 71 even-dimensional spheres but not by itself proving one.

**Explicit complete matching.** Encode each nonempty face by its 27-bit vertex mask. Initially mark all 23,778 faces as remaining. For each pivot \(p=0,1,\ldots,26\) in that order, examine a snapshot of remaining faces in increasing order of their cardinality and then integer mask. When \(p\notin\sigma\) and both \(\sigma\) and \(\sigma\cup\{p\}\) remain, match them and remove both. This yields exactly 11,853 disjoint pairs. The unmatched faces are exactly one vertex and 71 faces with five vertices (critical four-cells).

**Global acyclicity.** Construct the complete Hasse diagram of proper nonempty faces, one edge for each codimension-one incidence. Direct unmatched incidence edges upward from smaller to larger faces and reverse the 11,853 matched incidences downward. There are exactly 126,522 directed incidences. A topological sort visits all 23,778 faces. Accordingly, the directed graph has no directed cycle, so the matching is acyclic in Forman's discrete-Morse sense. These complete finite checks are implemented, asserted and replayable in `verify_neighborhood_gq.py`; they are not inferred from a partial sample or a timeout.

**Homotopy conclusion.** Forman's discrete-Morse theorem yields a CW complex homotopy equivalent to \(\mathcal N(H)\), with exactly one zero-cell and 71 four-cells, and no cells in dimensions one, two or three. Each four-cell's attaching map has source \(S^3\) and target the one-point three-skeleton, so every attaching map is constant. The CW complex is therefore \(\bigvee^{71}S^4\), as asserted. No computation of attaching degrees is required in the absence of lower-dimensional critical cells.

## Verification

The standalone standard-library-only program `verify_neighborhood_gq.py` builds the cubic-surface graph, exhaustively enumerates its faces, deterministically constructs all Morse pairs, and checks acyclicity over the complete 126,522-incidence Hasse graph. An independent program `verify_polar_model.py` constructs the 27-point elliptic-quadric model over the two-element field, tests a given explicit graph isomorphism to the divisor model, and independently enumerates the entire neighborhood-complex face vector by combinations rather than subset masks. Each program exits with an error if an asserted numerical or structural certificate fails. Their successful replay verifies the stated finite proof premises; the homotopy implication then follows from the cited discrete-Morse theorem.

## Relationship to prior work

The 27-line and exceptional-divisor configurations, including their connection with the Gosset polytope, are standard and described by Lee. The usual Schläfli graph joins *skew* lines; it must not be mistaken for \(H\), which joins *intersecting* lines. Lee's incidence and polytopal face data do not supply the present open-neighborhood homotopy computation.

Matsushita identifies fundamental groups of neighborhood complexes in broad graph families, without computing this complex's higher-dimensional homotopy type. Matsushita and Wakatsuki show how an open-neighborhood complex is Alexander dual to the dominance complex of a complementary graph; in this terminology the present complex is the Alexander dual of the dominance complex of the Schläfli graph. That equivalence is a useful alternate description but does not yield the specific 71-sphere conclusion from the inspected results. This result should be considered subject to independent priority review; negative database and literature searches are not proof that equivalent work does not exist.

## Limitations

Only the finite graph defined here is classified; no comparable classification for all generalized quadrangles, Schläfli-related graph constructions, or larger finite polar graphs is claimed. The verification programs supply complete finite discrete-Morse and graph certificates but do not constitute an independently performed scientific audit. An equivalent result could be present in literature not retrieved or indexed in the searches described in the review documents.

## References

1. J.-H. Lee, *Gosset Polytopes in Picard Groups of del Pezzo Surfaces*, arXiv:0905.3025, first public 2009-05-19.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first public 2012-10-10.
3. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639 (supporting duality reference).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse matching theorem).
