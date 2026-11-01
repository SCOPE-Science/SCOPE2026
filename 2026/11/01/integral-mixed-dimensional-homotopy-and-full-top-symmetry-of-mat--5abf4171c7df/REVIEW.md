# Review of the integral homotopy and equivariant calculation

## Correctness
PASS. The complete combinatorial definition is exhausted using all 21 open neighborhoods, producing 18,494 nonempty simplices. A full directed Hasse-graph topological sort certifies acyclicity of 9,120 Morse pairs across 98,805 incidences. The seven critical 4-cells have a fully zero 246-by-7 **integer** Morse differential, and the executable constructs seven explicit integral simplicial 4-cycles. Since the resulting CW complex has only cells in dimensions 0, 3 and 4 and its three-skeleton is a three-sphere wedge, the vanishing differential forces its four-cell attaching maps to be nullhomotopic. Signed chain projections produce a unimodular 7-cycle basis and check all six adjacent \(S_7\)-transpositions, establishing the full integral module rather than a character guess. Main risk: the full acyclicity/integer algebra and equivariant basis depend on reproducibly executing `verify.py`, which accompanies the proof.

## Originality
PASS with residual bibliographic risk. The closest exact published same-object work computed only mod-two ranks 246 and 7 and explicitly did not claim integral homology, homotopy type or attaching maps. Earlier same-family equivariant work covers the six-label triangular graph, not the seven-label case. General graph-Hom equivalence, first fundamental-group results, the degree-bounded neighborhood classifications and other neighborhood complex tables do not logically imply the integral wedge or the top integral symmetry module. Semantic record searches across graph aliases and character descriptions did not identify a dominating claim. Unindexed or subsequently published equivalent analysis remains possible; search noncoverage is not novelty proof.

## Value
PASS. The seven-label triangular graph is the first member of this standard family previously observed to have nonzero reduced neighborhood homology in two dimensions. Showing its two homology groups are integrally free, that all attaching maps vanish, and that its entire top lattice is a natural signed permutation module resolves meaningful structural questions left open by the earlier field calculation. This is a natural finite boundary case rather than a cosmetic parameter change; the symmetry computation distinguishes the full and alternating quotients at top rational degree.

## Scope and limitations
The result is limited to the open-neighborhood complex of this 21-vertex graph and to its fourth-homology integral symmetry lattice. It does not classify the integral third-homology symmetry lattice, homotopy-equivalent actions, or integral homology of quotient spaces. A remaining publication-priority risk is unindexed equivalent literature.

Self-review: passed. Independent audit: not yet performed.
