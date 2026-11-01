# Mixed-dimensional integral homotopy of the Pappus two-independence complex

## Finding
Let \(P\) be the standard eighteen-vertex Pappus graph, the cubic bipartite Levi graph of the Pappus \((9_3)\) incidence configuration. Let \(\operatorname{Ind}_2(P)\) be the simplicial complex of subsets whose induced graph has every connected component of at most two vertices (equivalently, induced maximum degree at most one). Its exact integral homotopy type is
\[
\boxed{\operatorname{Ind}_2(P)\simeq\bigvee^{9}S^5\vee S^6.}
\]
The underlying complex is nine-dimensional, yet its homotopy is concentrated in dimensions five and six, with free integral homology of ranks nine and one respectively and no torsion. A full acyclic discrete-Morse certificate and exact **zero integral attaching boundary** determine the homotopy, not just mod-two Betti numbers.

## Assumptions and scope
Use vertices \(0,\dots,17\), the Hamiltonian cycle \(0-1-\dots-17-0\), and nine additional undirected chords. Equivalently, use the standard LCF notation \([5,7,-7,7,-7,-5]^3\): from vertex \(i\) add an edge to \(i+d_i\pmod{18}\), where \(d_i\) is the indicated repeated displacement. The chord list and the cycle together produce the precise 27-edge graph in `verify_pappus_ind2.py`, which verifies independently that its hardcoded edge set agrees with this LCF construction. For every finite graph, a subset induces components of at most two vertices if and only if every selected vertex has at most one selected neighbor. All homology is reduced unless stated otherwise; integral simplicial orientations use ascending vertex labels.

## Proof
**Complete face construction.** The checker incrementally enumerates every two-independent subset using the induced-degree rule, obtaining exactly 20,652 augmented faces, including the empty face. Its independent exhaustive pass over all \(2^{18}=262144\) possible vertex subsets checks membership using the same local graph condition but without the incremental enumeration. Face numbers by dimensions \(-1,0,1,\ldots,9\) are
\[
(1,18,153,762,2394,4806,6027,4428,1728,308,27).
\]
In particular, all 27 top-dimensional nine-simplices are included.

**Exact Morse reduction.** Start with all augmented faces unmatched. For vertices \(v=0,\dots,17\) in order, inspect remaining faces by increasing cardinality and increasing integer bit mask and pair any remaining face \(A\) with its remaining coface \(A\cup\{v\}\), when both exist. This specifies all \(10{,}321\) matched face/coface pairs without discretionary choices. Exactly nine critical five-faces and one critical six-face survive; there are no other critical faces in the augmented complex. Reverse each of the matched covering relations in the downward-oriented Hasse graph. There are exactly \(120{,}240\) incidences, and topological sorting of the complete reversed graph visits every face, proving the matching is acyclic.

**Integral attaching map.** For each oriented five-face \(A\) in the signed boundary of the unique critical six-face, recursively eliminate matched lower five-faces using their oriented upper six-faces, with incidence coefficients \(\pm1\). The deterministic gradient-path recursion is given explicitly in the checker. It produces the exact integral Morse boundary column
\[
\partial_6=(0,0,0,0,0,0,0,0,0)^{\mathsf T}.
\]
No field reduction or numerical approximation is used here. The empty face is matched with one vertex, so deleting that pair yields an ordinary acyclic Morse matching with one critical vertex, nine five-cells and one six-cell. Its five-skeleton is a wedge of nine five-spheres. The six-cell attaching map lies in \(\pi_5(\bigvee^9S^5)\cong\mathbb Z^9\) by the Hurewicz theorem. The displayed integral boundary gives its Hurewicz coordinates, all zero; therefore the map is nullhomotopic and the CW space is \(\bigvee^9S^5\vee S^6\).

**Independent chain verification.** Using *all original simplices* rather than Morse cells, the checker computes mod-two simplicial boundary ranks in dimensions one through nine:
\[
(17,136,626,1768,3038,2980,1447,281,27).
\]
These imply the independently reconstructed reduced mod-two Betti numbers \((0,0,0,0,0,9,1,0,0,0)\). The reduced Euler characteristic obtained directly from the complete face vector is \(-8\). These calculations corroborate the Morse proof; alone they would not imply the integral homotopy type.

## Verification
Run `python verify_pappus_ind2.py` with Python 3.10 or later. The script uses only Python's standard library and includes all edge data. It verifies LCF graph reconstruction, all 262,144 subset membership decisions, every matching pair and Hasse incidence, exact signed Morse differential, full unreduced mod-two ranks and Euler characteristic. It exits successfully with `PAPPUS_TWO_INDEPENDENCE_MIXED_WEDGE_OK`, and its complete actual output is in `VERIFICATION_OUTPUT.txt`.

## Relationship to prior work
Abdelmalek, Deshpande, Goyal, Roy and Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first publicly posted 2021-06-21), defines higher independence and establishes sphere-wedge and shellability results for chordal graphs, trees and caterpillars. The Pappus graph has induced six-cycles, so the cited hypotheses do not cover it. Published Pappus *ordinary* independence and matching-complex calculations concern distinct simplicial constructions; the exact Pappus \(\operatorname{Ind}_2\) homotopy type is not implied by these. Indexed searches also retrieved two-independence calculations for the Petersen, Heawood, Möbius–Kantor, Clebsch and crown graphs, all different objects. Neither searches under the Pappus, Levi graph, \(\operatorname{Ind}_2\), dissociation and induced-degree-one aliases nor targeted web literature searches identified a published covering result. Absolute novelty remains subject to discovery of unindexed equivalents.

## Limitations
The theorem concerns this one natural graph and cutoff two only; it does not classify other Pappus-related complexes, higher cutoffs, automorphism-group actions, shellability or infinite graph families. The mathematical proof is finite and computer-assisted, with an explicit independently checkable certificate. No independent external audit has been performed.

## References
Abdelmalek, F. M.; Deshpande, P.; Goyal, S.; Roy, A.; Singh, A. *Chordal graphs, higher independence and vertex decomposable complexes*. arXiv:2106.10863, first public 2021-06-21; International Journal of Algebra and Computation 33 (2023), 481–498. https://arxiv.org/abs/2106.10863; https://arxiv.org/pdf/2106.10863.
