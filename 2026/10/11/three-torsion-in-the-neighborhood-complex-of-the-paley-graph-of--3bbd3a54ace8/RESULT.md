# Three-torsion in the neighborhood complex of the Paley graph of order seventeen

## Finding
Let \(P_{17}\) be the quadratic-residue Paley graph on the additive group \(\mathbb Z/17\mathbb Z\), and let \(\mathcal N(P_{17})\) be its ordinary Lovász open-neighborhood complex. Then
\[
\boxed{\mathcal N(P_{17})\simeq M(\mathbb Z/3,2)\vee\bigvee^{35} S^3,}
\]
where \(M(\mathbb Z/3,2)=S^2\cup_{3}e^3\) is a Moore space whose three-cell is attached by a degree-three map. In particular,
\[
\widetilde H_2(\mathcal N(P_{17});\mathbb Z)\cong\mathbb Z/3,
\qquad
\widetilde H_3(\mathcal N(P_{17});\mathbb Z)\cong\mathbb Z^{35},
\]
and all other reduced integral homology groups vanish. The fundamental group is trivial.

## Assumptions and scope
All complexes are finite and abstract, and all stated homotopy equivalences concern their geometric realizations. Label the vertices of \(P_{17}\) by \(0,1,\ldots,16\). The quadratic-residue set is
\[
Q=\{1,2,4,8,9,13,15,16\}\subset\mathbb Z/17\mathbb Z.
\]
Distinct vertices \(u,v\) are adjacent precisely when \(v-u\pmod{17}\in Q\). The open neighborhood of \(u\) is \(N(u)=u+Q\), with no loop and no addition of the center vertex. A nonempty subset \(\sigma\subseteq\mathbb Z/17\mathbb Z\) is a face of \(\mathcal N(P_{17})\) precisely when \(\sigma\subseteq N(u)\) for some vertex \(u\). Thus the seventeen eight-element neighborhoods are the facets. This is **not** the clique complex, independence complex, closed-neighborhood complex or graph-metric Rips complex.

Represent a face by its integer bit mask, with bit \(i\) indicating vertex \(i\); its dimension is the number of bits minus one. Orient every face by increasing vertex order. All integer matrices below use these fixed conventions.

## Proof
**Finite face reconstruction.** The quadratic residues above yield an eight-regular graph. Every pair of distinct vertices has three common neighbors if adjacent and four if nonadjacent, confirming the strongly regular parameters \((17,8,3,4)\). Taking all nonempty subsets of each of the seventeen open neighborhoods gives exactly \(3468\) faces and the complete face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(17,136,612,1122,952,476,136,17).
\]

**Acyclic matching.** On the nonempty face poset, visit vertices \(v=0,1,\ldots,16\) in that order. At stage \(v\), visit currently unmatched faces in order of increasing cardinality and then increasing bit-mask integer. Whenever both \(\sigma\) and \(\sigma\cup\{v\}\) remain unmatched and \(v\notin\sigma\), match them and remove both from further consideration. This produces exactly \(1711\) pairs. Direct all codimension-one incidences from the larger face to the smaller face, except that the incidence belonging to a matched pair points upward. A complete topological sort on all \(3468\) face nodes and all \(15300\) directed incidences succeeds, so the matching is acyclic. The unmatched faces comprise exactly one vertex, five triangles and forty tetrahedra, with no other critical faces.

**Signed Morse boundary.** The five critical triangles, in increasing mask order, have masks \(70,262,8202,16390,32780\); the forty critical tetrahedra are listed in `morse_boundary.json`. The integral Morse boundary from critical tetrahedra to critical triangles has a \(5\)-by-\(40\) matrix \(B\), reproduced in that artifact. It is computed from the signed ascending-vertex simplicial boundary by the usual gradient-path recurrence. For a triangle \(t\), let \(F(t)\) be its signed projection onto critical triangles: \(F(t)=t\) when \(t\) is critical, \(F(t)=0\) when \(t\) is an upper member of a pair with an edge, and, when \(t\) is paired upward with a tetrahedron \(b\),
\[
F(t)=-[b:t]^{-1}\sum_{u\subset b,\,u\ne t,\,\dim u=2}[b:u]F(u),
\]
where \([b:u]\in\{+1,-1\}\) is the simplicial incidence number. Acyclicity makes the recurrence finite. For each critical tetrahedron \(c\), its Morse boundary is \(\sum_{t\subset c}[c:t]F(t)\). All forty resulting columns have been computed with exact integers; exactly \(99\) matrix entries are nonzero. The compact, row-major JSON encoding of \(B\) has SHA-256 `2947ab3b904e0bdbad58376aa448307433649868212a401978108cedbd4f078a`.

**Integral attaching data.** The \(5\)-by-\(5\) submatrix of \(B\) using zero-indexed columns \((0,1,3,4,8)\) has determinant \(-3\). The \(4\)-by-\(4\) submatrix using rows \((0,1,2,3)\) and columns \((0,1,4,8)\) has determinant \(-1\). Moreover, \(B\) has rank four modulo three and rank five modulo two. Therefore every maximal minor is divisible by three, while one maximal minor is exactly \(-3\); all lower determinantal divisors are one because a four-minor is a unit. The complete nonzero Smith invariant factors are consequently \((1,1,1,1,3)\).

**Homotopy, not just homology.** The acyclic matching produces a CW complex with precisely one zero-cell, five two-cells and forty three-cells. Its two-skeleton is \(\bigvee^5S^2\); in particular it is simply connected and \(\pi_2\cong H_2\cong\mathbb Z^5\) by Hurewicz. Each three-cell attaching map is thus determined by its integer degree vector, so the signed Morse matrix classifies these attachments. Integral changes of basis, which are realized by homotopy self-equivalences of sphere bouquets and elementary cellular handle slides, reduce \(B\) to the Smith diagonal. Four unit-degree cell pairs cancel, one degree-three attachment gives \(M(\mathbb Z/3,2)\), and the remaining thirty-five three-cells are null-attached. This proves the boxed equivalence.

## Verification
Run `python3 verify_morse.py` in a directory containing the packaged file. It reconstructs the graph and every face; tests all strongly regular intersection counts; produces the deterministic matching; verifies every directed face incidence by topological sorting; computes the full signed Morse boundary; and checks the two explicit minor determinants and all stated ranks. `morse_boundary.json` records the complete critical-cell labeling and integral matrix.

Run `python3 verify_modular.py` to obtain an independent face reconstruction from common-neighbor intersections, followed by sparse simplicial boundary elimination over the fields of two, three and five elements. The reduced Betti numbers are concentrated in degree three with rank \(35\) over the fields of two and five elements; over the field of three elements they have rank \(1\) in degree two and rank \(36\) in degree three. These independent field results agree with the integral Moore-space decomposition, but are not substitutes for the integral determinant evidence.

## Relationship to prior work
Matsushita's *Fundamental groups of neighborhood complexes* (first public version 2012) relates fundamental groups of neighborhood complexes to even parts of graph \(r\)-fundamental groups; it does not give the degree-three attachment matrix or this graph's integral homotopy type. Kahle's *The Neighborhood Complex of a Random Graph* concerns random-graph asymptotics and supplies no exact result for this deterministic quadratic-residue graph. Shukla's *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs* provides explicit homotopy classifications for graphs of degrees at most four, whereas \(P_{17}\) is eight-regular. The Paley graph's standard parameters and identity are consistent with the published distance-regular graph reference.

The exact torsion-containing homotopy decomposition is not a formal consequence of the general results cited. Published records and literature searches did not locate a covering computation, but absence from searches is not proof of priority.

## Limitations
The calculation concerns only \(P_{17}\) and its **open** neighborhood complex; it does not establish a result for other Paley graphs or generalized neighborhood complexes. The finite Morse and matrix computations provide an exhaustive proof for this finite complex, not for any infinite family. A mathematically equivalent treatment may exist in unindexed literature; no bibliographic uniqueness is claimed.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (initial submission October 10, 2012), *J. Math. Sci. Univ. Tokyo* **24** (2017), 321–353. https://arxiv.org/abs/1210.2803 ; https://www.ms.u-tokyo.ac.jp/journal/jms240302.pdf .
2. M. Kahle, *The Neighborhood Complex of a Random Graph*, arXiv:math/0512077 (2005). https://arxiv.org/pdf/math/0512077 .
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (2018). https://arxiv.org/pdf/1802.04526 .
4. DistanceRegular.org, *Paley graph P17*, graph parameters and adjacency data. https://www.math.mun.ca/distanceregular/graphs/paley17.html .
5. E. W. Weisstein, *Paley Graph*, Wolfram MathWorld. https://mathworld.wolfram.com/PaleyGraph.html .
