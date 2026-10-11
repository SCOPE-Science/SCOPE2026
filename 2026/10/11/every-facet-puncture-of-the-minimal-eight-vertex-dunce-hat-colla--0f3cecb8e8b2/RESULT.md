# Every facet puncture of the minimal eight-vertex dunce hat collapses to a circle
## Finding
Let \(K\) be the simplicial complex on vertices \(1,\ldots,8\) with facets
\[
124,127,128,134,135,136,156,178,235,237,238,245,348,367,456,468,678.
\]
For every facet \(\tau\in K_2\), write \(K-\tau\) for the subcomplex obtained by deleting only the two-simplex \(\tau\), retaining all its proper faces. Then
\[
K-\tau\searrow C
\]
for a simple cycle \(C\), for every one of the \(17\) choices of \(\tau\). Hence every one-facet puncture has simple-homotopy type \(S^1\).

The unpunctured complex behaves sharply differently at the first move: among its \(24\) edges, \(21\) lie in exactly two triangles and \(3\) lie in exactly three triangles. Thus \(K\) has no free edge and no elementary collapse can start.

## Assumptions and scope
The claim concerns the specified labelled eight-vertex triangulation, not every minimal triangulation of the dunce hat. A facet puncture removes the two-simplex itself but keeps its three boundary edges and vertices. An elementary \(2\)-to-\(1\) collapse removes a triangle together with an edge contained in no other remaining triangle; after all triangles have been removed, an elementary \(1\)-to-\(0\) collapse removes a leaf vertex together with its incident edge.

The conclusion is a direct simplicial-collapse statement. It is stronger than merely computing the homology or homotopy type of a puncture, but it does not assert that different collapse choices have the same terminal cycle.

## Proof
The face set reconstructed from the displayed facets has \(8\) vertices, \(24\) edges and \(17\) triangles. Direct incidence counting gives triangle-degree \(2\) for \(21\) edges and triangle-degree \(3\) for the remaining \(3\), proving the no-free-edge assertion for \(K\).

For each facet \(\tau\), the accompanying `collapse_certificate.json` starts from \(K-\tau\). Each recorded two-dimensional step gives an edge contained in exactly one current triangle and deletes that edge together with that triangle. Once no triangles remain, each recorded one-dimensional step gives a degree-one vertex and deletes it together with its unique incident edge. Every step is therefore an elementary simplicial collapse.

The certificate contains one such sequence for every facet, with no repeated or omitted facet. In every case the terminal subcomplex is connected and two-regular, with the same number of vertices and edges; hence it is a simple cycle. Therefore every \(K-\tau\) collapses to a circle.

For reproducibility only, the deterministic lexicographic rule used to construct the supplied certificate reaches a three-cycle for \(12\) punctures and a four-cycle for \(5\) punctures. This split is a property of that chosen certificate and is not asserted to be an invariant of the punctures.

## Verification
`verify.py` independently reconstructs the face set, checks the full-complex incidence profile and absence of free edges, then replays every step of `collapse_certificate.json`. At every two-dimensional step it recomputes the current edge-to-triangle incidence and requires the recorded edge to be free. At every graph step it recomputes vertex degrees and requires the recorded vertex to be a leaf. It finally checks that each terminal graph is connected and two-regular.

A successful replay prints exactly:

`VERIFY_OK f=8,24,17 full_free_edges=0 punctures=17 all_collapse_to_cycle=yes certificate_core_lengths=3:12,4:5`

All checks use exact finite set operations. No experiment on a proper subset of facets is extrapolated to the universal statement.

## Relationship to prior work
Benedetti and Lutz exhibit a minimal eight-vertex triangulation of the dunce hat and emphasize that the dunce hat is contractible but no triangulation of it is collapsible because there is no free edge. Paixão and Spreer later classify the seven minimal triangulations of the dunce hat among the contractible non-collapsible complexes with \(17\) triangles. These results establish the object class and its global noncollapsibility, but the inspected statements do not give a facet-by-facet puncture-collapse classification.

A later simple-homotopy study shows that a particular eight-vertex dunce hat can be made collapsible after one pure three-dimensional expansion and discusses a specific alternative collapse after that expansion. That is a different operation from directly deleting each of the \(17\) original two-dimensional facets.

A published exact discrete-Morse census for this same labelled complex counts all optimal fields with Morse vector \((1,1,1)\) and proves that each accepted triangle-edge layer has a residual unicyclic graph. Its statement is aggregate: it does not assert that every individual facet can serve as the sole critical triangle, nor does it supply a direct elementary-collapse sequence for every puncture. The present universal per-facet collapse certificates therefore are not a statement-level corollary of that census.

## Limitations
The claim is restricted to this labelled minimal triangulation. It does not classify the other six minimal dunce-hat triangulations, nor does it classify all possible collapse sequences or all possible terminal cycles for any puncture. The originality assessment is literature-based; an unindexed historical computation could in principle contain the same seventeen puncture sequences.

## References
1. B. Benedetti and F. H. Lutz, *The dunce hat in a minimal non-extendably collapsible 3-ball*, arXiv:0912.3723v1, submitted 2009-12-18.
2. J. Paixão and J. Spreer, *Random collapsibility and 3-sphere recognition*, arXiv:1509.07607v1, submitted 2015-09-25.
3. M. Hachimori, Simplicial Complex Library, datum `dunce_hat.dat`.
4. B. Benedetti, C. Lai, D. Lofano and F. H. Lutz, *Random simple-homotopy theory*, DOI `10.1007/s41468-023-00139-4`.
