# Five three-spheres in the full strong Morse complex of the eight-cycle

## Finding
Let \(C_8\) be the unfilled one-dimensional cycle with vertices \(\mathbb Z/8\mathbb Z\) and edges between cyclic neighbors. Let \(\mathcal{SM}(C_8)\) denote its **full**, rather than pure or ordinary, complex of strong discrete-Morse matchings. Then
\[
\boxed{\mathcal{SM}(C_8)\simeq\bigvee^5 S^3.}
\]
This is an integral homotopy classification: reduced homology is \(\mathbb Z^5\) in degree three and zero in every other degree. The complex has exactly 16 vertices, 1,060 nonempty simplices, and 60 maximal facets: 56 five-dimensional facets and four three-dimensional facets. Removing those four additional three-dimensional facets leaves the pure subcomplex, with 1,056 nonempty faces. The distinction between full and pure first occurs at cycle length eight (among cycles with at least three vertices).

## Assumptions and scope
Each edge is a one-dimensional cell, even when the cycle is a triangle; no triangular face is filled. A matching-complex vertex is an incident vertex–edge pair \((v,e)\), with \(v\) an endpoint of \(e\). A strict total ordering \(v_1,\ldots,v_8\) of the original graph vertices yields the strong matching containing \((v_j,\{v_j,u\})\) exactly when \(v_j\) has a unique neighbor \(u\) among the earlier vertices. The full complex consists of all subsets of such matching sets for all \(8!\) total orders. In the **pure** strong subcomplex only facets having the global maximum matching cardinality are retained, together with their faces. These conventions agree with the vertex-filtration description of strong Morse matchings used by Knudson and Owens–White.

Fix cycle edges \(e_i=\{i,(i+1)\bmod 8\}\), ordered by \(i=0,\ldots,7\). Number the sixteen incidence vertices by listing the two endpoints of each \(e_i\) in increasing numeric order; represent any simplex by the bitmask of its selected incidences. All certificate loops use this fixed convention and count the empty face separately.

## Proof
**Complete complex reconstruction.** Enumerating each of the \(8!=40,320\) strict vertex orders, applying the unique-earlier-neighbor rule and taking downward closures gives 253 distinct order-generated matchings and exactly 1,061 simplices including the empty face. The nonempty face vector in dimensions zero through five is
\[
(16,96,272,380,240,56).
\]
Exhaustive maximality checks give exactly 56 five-simplices and four tetrahedra as the 60 maximal faces. The pure complex is the downward closure of the maximum-sized order-generated matchings; it contains 1,057 faces including the empty face. Its exact difference from the full complex is the four maximal tetrahedra, encoded by masks \(2313,9252,20624,33346\) under the preceding convention. Analogous exhaustive comparison for each of the cycles of lengths three through seven finds no difference between full and pure.

**Explicit matching.** On the **nonempty** face poset, process the incidence-bit positions \(i=0,\ldots,15\) in order. At stage \(i\), visit all still-unmatched faces in increasing order of (number of vertices, integer mask). Whenever a face lacks \(i\) and both it and its union with \(\{i\}\) are still present, pair them and remove both from further stages. This algorithm produces precisely 527 distinct covering pairs. Its critical cells consist of one vertex, represented by mask \(1\), and exactly five three-simplices, represented by masks \(4420,8836,10308,20624,33346\). There are no other critical cells.

**Acyclicity certificate.** The complete nonempty face poset has 4,064 codimension-one incidences. Orient every unmatched incidence from the larger simplex to the smaller one, and reverse each of the 527 matched incidences. The accompanying executable certificate independently reconstructs all 4,064 incidences, checks each matched pair is a genuine codimension-one inclusion, and verifies that a topological sort visits all 1,060 vertices of this directed Hasse graph. Hence the matching is acyclic, not merely a proposed cancellation sequence. Every enumeration is finite, exhaustive and integer-exact.

**Homotopy conclusion.** Forman's discrete Morse theorem gives a CW complex homotopy equivalent to the original, with exactly one zero-cell, five three-cells and no other cells. Its two-skeleton is therefore a point. Every attaching map of a three-cell, whose domain is a two-sphere, is nullhomotopic; accordingly the resulting CW complex is exactly a wedge of five three-spheres. No inference from finite experiments to an unbounded parameter range is made: the complete finite complex is verified.

## Verification
Run the standalone Python standard-library file `verify.py`. It independently builds all vertex-filtration matchings, enumerates downward-closed simplices, checks a separate three-symbol cyclic face criterion against every one of the \(2^{16}\) incidence subsets, verifies facet counts and the pure/full comparison, constructs the complete directed Hasse diagram, and checks acyclicity of every matching pair by topological sorting. Independent mod-prime boundary reductions over characteristics two, three and five recover Betti numbers \((1,0,0,5,0,0)\) including unreduced degree zero. The exact combinatorial Morse proof, not field experiments, establishes integral homotopy and torsion-freeness. Terminal output begins `VERIFY_OK`.

## Relationship to prior work
Knudson and Owens–White (first public September 6, 2026) introduce the full and pure strong matching complexes and provide homotopy classifications for the **pure** cycle complex; for the **full** cycle complex their stated contribution is homology through cycle length 21. In particular, the pure eight-cycle is not the complex classified here. Prior work on the ordinary (non-strong) Morse complex does not imply this result. Published equivariant Euler-characteristic computations for full strong cycle complexes determine alternating traces, not the integral homotopy type or a perfect Morse matching for this particular full complex. The new information is the complete simple-homotopy reduction and the sharp four-facet divergence from the pure complex at length eight.

## Limitations
The claim concerns this one-dimensional eight-cycle, not every cycle length, and does not determine the integral dihedral action on the five-dimensional top-homology lattice. The source preprint's accessible abstract and related full-text mathematical comparisons were examined, but the preprint's primary full text was inaccessible in this examination. A logically equivalent result in an unexamined section of that text or in unindexed literature remains a residual originality risk. The finite checker is a complete certificate for this specific finite object, not evidence for unspecified larger cycles.

## References
- Kevin Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first posted September 6, 2026), https://arxiv.org/abs/2609.06844.
- Manoj K. Chari and Michael Joswig, *Discrete Morse Complexes*, arXiv:math/0011234, *Discrete Mathematics* **302** (2005), 39–51.
- *Dihedral Euler characters of full strong Morse complexes of cycles*, public mathematical research record, October 2026; examines equivariant alternating characters without a full homotopy classification.
- *The threefold rotation character of pure strong Morse matching complexes of cycles*, public mathematical research record, October 2026; treats the distinct pure cycle subcomplex.
