# The missing degree seven in the octahedral graphical zonotope

## Finding
Let \(O=K_{2,2,2}\) have labeled parts \(\{0,1\},\{2,3\},\{4,5\}\). Orient each of its twelve edges, and call the orientation acyclic when it has no directed cycle. Form the one-edge reversal graph \(\mathcal A(O)\) on the acyclic orientations, connecting precisely those differing by one arc reversal that remains acyclic. Then
\[
\sum_{D\in V(\mathcal A(O))}t^{\deg(D)}=288t^5+120t^6+18t^8.
\]
Thus the 426-state graph has exactly 1152 edges and no vertex of degree seven. The associated graphical zonotope is five-dimensional and has 288 simple vertices. Under planar duality, the same polynomial counts reversible-arc degrees of strong (strongly connected) orientations of the cube graph \(Q_3\). Under the 48 automorphisms of \(O\), the 426 states split into exactly 15 orbits.

## Assumptions and scope
All graphs are finite, labeled and simple. In \(K_{2,2,2}\), edges join vertices in different specified parts. In \(Q_3\), vertices are three-bit vectors and edges differ in one bit. Orientations are distinguished by all edge directions, not identified under symmetry. A directed graph is strong if every ordered pair of vertices is connected by a directed path. A reversible arc is one that can be flipped without destroying acyclicity (in the octahedral interpretation) or strong connectivity (in the cube interpretation). The graphical zonotope is \(Z_O=\sum_{\{u,v\}\in E(O)}[e_u,e_v]\) in the affine hyperplane where coordinate sum equals twelve. It has dimension five since \(O\) is connected. Its one-skeleton is canonically the acyclic-orientation reversal graph; simple means degree five.

## Proof
An acyclic orientation has a topological ordering, and orienting all graph edges from earlier to later in any linear order produces an acyclic orientation. Thus the orientations are *exactly* the distinct twelve-bit strings obtained from the \(6!=720\) permutations of the six labeled vertices. Number the edges lexicographically as
\[
(02,03,04,05,12,13,14,15,24,25,34,35).
\]
The bit at position \(i\) is one when the first endpoint precedes the second in the order. Taking the set of all such strings removes duplicates without omitting any acyclic orientation. For a string \(a\), its reversal degree is exactly the number of indices \(i\in\{0,\ldots,11\}\) for which \(a\mathbin{\mathrm{xor}}2^i\) also belongs to this set. This test is equivalent to the direct acyclicity criterion because the set includes all and only acyclic orientations.

The computation can also be compressed to a human-checkable 15-row orbit certificate. The full graph automorphism group is \((S_2)^3\rtimes S_3\), of order 48, obtained by permuting the three two-vertex parts and swapping their members. The following rows give for each orientation orbit one representative twelve-bit *integer* \(a\), its size and its reversal degree, using the edge order above. Every orbit is the set of images under these 48 explicit vertex permutations.

| Representative | Orbit size | Degree |
|---:|---:|---:|
| 0 | 6 | 8 |
| 1 | 24 | 5 |
| 3 | 12 | 6 |
| 7 | 24 | 6 |
| 15 | 12 | 8 |
| 23 | 48 | 5 |
| 31 | 24 | 6 |
| 55 | 24 | 5 |
| 63 | 12 | 6 |
| 262 | 48 | 5 |
| 263 | 48 | 5 |
| 271 | 48 | 5 |
| 303 | 48 | 5 |
| 358 | 24 | 6 |
| 783 | 24 | 6 |

Direct substitution into the specified bit test verifies that the listed orbits are pairwise disjoint, cover all 426 topological-order orientations and have constant degree. Grouping their sizes by degree yields \(288,120,18\) in degrees \(5,6,8\). Their degree sum is \(2304\), so the reversal graph has \(1152\) edges.

For the dual interpretation, embed the cube in the plane and take its octahedral planar dual. Consistent clockwise rotation of primal arcs gives a bijection between totally cyclic orientations of the cube and acyclic orientations of its dual; a connected orientation is strong precisely when each edge belongs to a directed cycle. The bijection respects reversal of a single dual edge. Therefore the same degree enumerator applies to the cube's strong-orientation flip graph. In particular the 288 vertices of degree five in the five-dimensional zonotope are simple.

## Verification
The included `verify_octahedron.py` independently generates 720 linear orders, deduplicates to 426 acyclic orientations, determines each reversal degree, and exhaustively constructs the 15 symmetry orbits. The included `verify_cube.py` uses a different graph and *directed cut characterization*, examining all \(2^{12}=4096\) orientations of the cube against every nonempty proper vertex cut. It independently obtains 426 strong orientations, 1152 reversible arcs up to undirected exchange edges and the same degree polynomial. Both programs ran successfully from the extracted final artifact files. The second also checks that all shortest-path distances in the cube reversal graph equal Hamming distances, consistent with the general partial-cube property; that is an auxiliary confirmation, not the novelty claim. Neither program uses a published numerical table as input.

## Relationship to prior work
Stanley's 1973 chromatic-polynomial evaluation counts acyclic orientations. The known 426 for the octahedral graph appears explicitly as the first term of OEIS A338154, so 426 itself is *not claimed as original*. General results on orientation flips and graphical zonotopes explain the ambient constructions and the existence of flip paths, but do not, in the inspected material, supply the local degree stratification. Aksoy and Horn study general asymptotic abundance of strong orientations, not this cube or its arc-reversal degree spectrum. The new exact object is the entire \(288t^5+120t^6+18t^8\) polynomial, including the missing degree seven and fifteen-orbit refinement.

## Limitations
The theorem concerns the fixed canonical octahedral graph and its dual cube, not a general complete-tripartite or hypercube family. The full 426-state enumeration is finite and exhaustive; no claim of a new general flip-connectivity theorem is made. Historical specialized tables of zonotope vertex degrees might exist outside the searched sources, and full inspection of Fukuda–Prodon–Sakuma was not available. Independent scholarly auditing has not been performed.

## References
[1] S. Aksoy and P. Horn, "Graphs with many strong orientations", arXiv:1505.00767, first posted 2015-05-04; SIAM J. Discrete Math. 30 (2016), 1269–1282. https://arxiv.org/abs/1505.00767.
[2] R. Stanley, "Acyclic orientations of graphs", Discrete Math. 5 (1973), 171–178, doi:10.1016/0012-365X(73)90108-8.
[3] K. Fukuda, A. Prodon and T. Sakuma, "Notes on acyclic orientations and the shelling lemma", Theor. Comput. Sci. 263 (2001), 9–16, doi:10.1016/S0304-3975(00)00226-7.
[4] OEIS A338154, the number of acyclic orientations of antiprism graphs, including 426 for the octahedron; https://oeis.org/A338154 (a pre-existing count, not the degree spectrum).
