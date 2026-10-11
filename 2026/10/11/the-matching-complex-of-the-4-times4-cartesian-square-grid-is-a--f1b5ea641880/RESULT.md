# The matching complex of the \(4\times4\) Cartesian square grid is a mixed-dimensional sphere wedge

## Finding
Let \(G=P_4\mathbin{\square}P_4\) be the Cartesian square grid on sixteen vertices, and let \(\mathcal M(G)\) be its ordinary matching complex, whose vertices are the twenty-four edges of \(G\) and whose simplices are collections of pairwise vertex-disjoint graph edges. There is an integral homotopy equivalence
\[
\boxed{|\mathcal M(G)|\simeq\bigvee^{6}S^{4}\vee\bigvee^{2}S^{5}.}
\]
In particular its reduced integral homology is \(\mathbb Z^6\) in degree four, \(\mathbb Z^2\) in degree five, and zero in all other degrees. The claim is an exact statement for this one natural finite grid, not a claimed formula for all rectangular grids.

## Assumptions and scope
The vertices of \(G\) are pairs \((r,c)\) with \(0\le r,c<4\), numbered \(4r+c\); two vertices are joined precisely when one coordinate agrees and the other differs by one. The twenty-four graph edges are numbered from \(0\) to \(23\): loop through vertices in increasing row-major order, recording the edge to the vertex immediately below when it exists, then the edge to the right when it exists. A simplex of \(\mathcal M(G)\) is represented by a twenty-four-bit mask. The empty mask is used only for augmented chain and matching computations.

## Proof
**Complete face enumeration.** Begin with the empty edge set. Scan the twenty-four graph edges in the order just defined. At each edge, append a copy of each previously generated matching to which the new edge may be added without sharing an endpoint, preserving the order of the existing list. This produces every matching exactly once. An exhaustive run produces \(10{,}012\) masks including the empty mask, with the complete face-count vector by dimensions \(-1,0,\ldots,7\):
\[
(1,24,224,1044,2593,3388,2150,552,36).
\]
This is exhaustive because every matching has a unique largest numbered edge and arises exactly once from the matching formed by deleting it.

**Explicit acyclic partial matching.** Scan potential toggle edges in the fixed order
```
23,17,21,10,5,11,14,20,9,7,6,12,22,19,3,0,1,2,13,16,4,8,18,15
```
At each step, traverse the original generated list of faces. If both the currently unmatched mask \(F\), with the toggle bit absent, and \(F\cup\{e\}\) remain unmatched, pair them and remove them from further consideration. Every pair is a genuine codimension-one simplex incidence. The supplied `verify.py` constructs all \(5002\) augmented pairs and checks that precisely eight masks are unmatched: six of dimension four and two of dimension five. The pair involving the empty face and a vertex can be dropped, leaving an ordinary partial matching with \(5001\) pairs and one additional critical vertex.

Orient each cover relation \(\sigma\gtrdot\tau\) from higher to lower dimension unless it is a matched relation, in which case reverse it. On the augmented face poset this gives exactly \(47{,}968\) oriented cover relations. An exhaustive topological sort removes all \(10{,}012\) vertices: there is no directed cycle. Deleting the empty-face vertex and its incident edges gives a subgraph of this acyclic directed graph, and therefore establishes acyclicity of the ordinary matching. Forman's discrete-Morse theorem now gives a CW model with one zero-cell, six four-cells and two five-cells, with no cells in any other positive dimension.

**Integral attaching maps, not merely homology ranks.** Orient simplices by increasing edge label. For a simplex \(\sigma=\{e_0<\cdots<e_k\}\), use the integral boundary \(\partial\sigma=\sum_{i=0}^{k}(-1)^i(\sigma\setminus\{e_i\})\). The verifier calculates the *integer* discrete-Morse differential by recursively eliminating paired simplices with their unit \(\pm1\) incidences. Both critical five-dimensional cells have zero differential to every critical four-dimensional cell, giving the complete matrix
\[
\partial^{\mathrm{Morse}}_5=
\begin{pmatrix}
0&0\\0&0\\0&0\\0&0\\0&0\\0&0
\end{pmatrix}.
\]
(The verifier prints the transpose, two rows of six zeros.) Acyclicity makes the signed gradient recursion terminating, and unit incidences make the reduction integral. The four-skeleton of the Morse CW model is \(\bigvee^6 S^4\); its fourth homotopy group maps isomorphically to fourth homology by the Hurewicz theorem. Therefore the zero cellular incidence vector means that each five-cell attaches by a null-homotopic map, and both five-cells split off as \(S^5\) summands. This proves the claimed **homotopy type**, not just the Betti vector.

## Verification
The accompanying standalone standard-library Python programs may be run as follows:
```
python3 verify.py
python3 crosscheck.py
```
`verify.py` independently builds the graph and all faces, constructs the entire discrete-Morse matching, explicitly checks the complete directed Hasse graph for cycles, and evaluates the full signed integral Morse differential. Its expected summary includes `faces 10012`, `augmented_matching_pairs 5002`, `ordinary_matching_pairs 5001`, `critical_dimensions {5: 2, 4: 6}`, `hasse_arcs 47968`, `acyclic_processed 10012`, and an all-zero two-by-six integer boundary.

`crosscheck.py` enumerates matchings using a distinct recursive graph-edge order and calculates all boundary ranks by exact bitwise Gaussian elimination over \(\mathbb F_2\). It obtains ranks \((0,1,23,201,843,1750,1632,516,36,0)\) (using cardinality-graded chain groups), hence reduced Betti ranks six and two in dimensions four and five, respectively. This modular cross-check corroborates but does not replace the integral Morse certificate.

## Relationship to prior work
Matsushita's 2019 *Matching Complexes of Small Grids* proves a sphere-wedge classification for two-row grids and associated generalized line graphs; it does not give the ordinary four-row Cartesian grid considered here. Chauhan, Sharma, and Shukla's 2026 paper on three-row grids establishes connectivity and homological restrictions there, and notes the general rectangular-grid problem remains largely unresolved. Gupta, Sarkar, Sawant, and Shukla study *categorical* products of paths, which have a different edge relation from the Cartesian product. Bayer, Jelić Milutinović, and Vega prove a wedge-of-spheres result for **outerplanar** graphs and conjecture it for arbitrary planar graphs; the square \(4\times4\) grid is planar but nonouterplanar. The present result gives an exact nonouterplanar planar example in two adjacent homotopy dimensions, consistent with that conjecture. A published homology computation for the \(10\)-cut complex of the same \(4\times4\) graph involves a different simplicial construction, and does not imply this matching-complex theorem.

## Limitations
This exact computation proves no recurrence or stability theorem for \(4\times n\) grids beyond the square \(4\times4\) case, and makes no prediction about larger rectangular grids or arbitrary planar graphs. The finite certificate proves the specified finite statement completely; it is not an inference from a sample of grids. Comparison with indexed literature does not exclude unindexed tables, independent unpublished computations, or a more general theorem not located in the inspected sources.

## References
1. P. Chauhan, A. Sharma, and S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1 (first public 2026-09-23), in particular the introduction, Theorems 1.2 and 1.3, and Section 4.
2. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics **26** (2019), P3.1, DOI:10.37236/8480, Theorems 1.1 and 1.2.
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2, Theorem 2 and Conjecture 11.
4. R. K. Gupta, S. Sarkar, S. S. Sawant, and S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298v2.
