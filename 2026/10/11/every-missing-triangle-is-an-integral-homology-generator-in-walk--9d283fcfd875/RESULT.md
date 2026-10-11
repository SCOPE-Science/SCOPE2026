# Every missing triangle is an integral homology generator in Walkup's nine-vertex 3-dimensional Klein bottle
## Finding
Let \(K=K^3_9\) be Walkup's nine-vertex triangulation of the twisted \(S^2\)-bundle over \(S^1\), on \(\mathbb Z/9\mathbb Z\), equivalently the union of difference cycles \((1:1:2:5)\), \((1:1:5:2)\), and \((1:2:1:5)\). Then \(K\) has exactly \(30\) missing triangles. Every missing triangle, with either orientation, represents a primitive generator up to sign of \(H_1(K;\mathbb Z)\cong\mathbb Z\). Under cyclic translation the missing triangles split into four orbits, with cyclic gap types \((1:4:4)\), \((2:3:4)\), \((2:4:3)\), and \((3:3:3)\), of sizes \(9,9,9,3\), respectively. Consequently the simplicial integral-homology systole among simple edge cycles is \(3\), and the \(30\) missing triangles are exactly the three-edge cycles realizing it. Translation by one vertex acts as \(+1\) on \(H_1(K;\mathbb Z)\).

## Assumptions and scope
Vertices are the residue classes in \(\mathbb Z/9\mathbb Z\). The complex is the canonical cyclic triangulation \(K^3_9\): equivalently, its facets are obtained from each five-vertex path in the nine-cycle by deleting one of the three interior vertices, or as the union of the three difference cycles \((1:1:2:5)\), \((1:1:5:2)\), and \((1:2:1:5)\). A missing triangle is a three-vertex set whose three edges are present but whose two-simplex is absent. The simplicial integral-homology systole here means the least number of edges in a simple simplicial cycle representing a nonzero class in \(H_1(-;\mathbb Z)\).

## Proof
The face vector is \((9,36,54,27)\), so the one-skeleton is complete and there are \(\binom{9}{3}-54=30\) missing triangles.

For a directed edge from \(a\) to \(b\), let \(\delta(a,b)\) be the unique integer in \(\{-4,-3,-2,-1,1,2,3,4\}\) congruent to \(b-a\pmod 9\). For any oriented edge cycle \(C\), define
\[
W(C)=\frac19\sum_{(a,b)\in C}\delta(a,b).
\]
The numerator is divisible by \(9\), because the ordinary differences telescope modulo \(9\).

The face triangles have exactly the following cyclic gap types, with cyclic rotation understood:
\[
(1,1,7),\ (1,2,6),\ (1,3,5),\ (1,5,3),\ (1,6,2),\ (2,2,5).
\]
In each case one gap is at least \(5\). Orienting around the ambient nine-cycle, that long gap contributes its value minus \(9\), while the other two contribute their positive values, so the sum of the three \(\delta\)-values is \(0\). Hence \(W\) vanishes on every triangular two-boundary and descends to a homomorphism
\[
W:H_1(K;\mathbb Z)\longrightarrow\mathbb Z.
\]

The missing triangles are exactly those triples whose three cyclic gaps are at most \(4\). Their cyclic gap types are
\[
(1,4,4),\ (2,3,4),\ (2,4,3),\ (3,3,3),
\]
with orbit sizes \(9,9,9,3\). For the cyclic orientation of any one of them, all three gap increments are already in \(\{1,2,3,4\}\), sum to \(9\), and therefore \(W=1\).

It remains to show that this value is the primitive integral class rather than a nontrivial multiple. Collapse the spanning tree consisting of the eight edges from vertex \(0\). The cycle lattice of the complete one-skeleton then has rank \(36-9+1=28\), with one basis coordinate for each edge not incident to \(0\). Expressing the \(54\) face-triangle boundaries in this basis gives a \(54\times28\) integer relation matrix. Its Smith normal form has exactly \(27\) nonzero diagonal entries, all equal to \(1\). Thus
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]
Since \(W\) takes the value \(1\) on a missing triangle, the induced homomorphism from this infinite cyclic group onto \(\mathbb Z\) is an isomorphism. Every missing triangle is therefore a primitive generator up to orientation.

Cyclic translation preserves \(\delta\), so it preserves \(W\) and acts by \(+1\) on \(H_1(K;\mathbb Z)\). Finally, every simple simplicial cycle has at least three edges; face triangles are null-homologous and every missing triangle is nonzero. Hence the systole is \(3\), realized by exactly the \(30\) missing triangles.

## Verification
The accompanying `verify.py` reconstructs the complex independently from both the path-deletion description and the three published difference cycles, checks equality of the two facet sets and the face vector, computes the Smith normal form of the integral first-homology presentation, exhausts all \(84\) vertex triples, verifies the four missing-triangle orbit types, and checks the winding functional on every face and missing triangle. Its replay output is:

`VERIFY_OK f=9,36,54,27 H1=Z empty3=30 gap_orbits=1:4:4x9,2:3:4x9,2:4:3x9,3:3:3x3 winding=1_all_missing shift_action=+1`

## Relationship to prior work
Walkup introduced the nine-vertex example; Bagchi and Datta give a computer-free uniqueness theorem and the path-deletion description of \(K^3_9\), identifying it as the twisted \(S^2\)-bundle over \(S^1\). Spreer records the same complex as the smallest cyclic triangulation of this manifold, gives the three difference cycles above, and calls it minimal and tight. Those sources establish the object, topology, symmetry, and tightness, but the inspected text does not state the integral primitive class of every missing triangle, the four missing-triangle orbit types, the exact count of \(30\) systolic loops, or the explicit winding isomorphism. Tightness supplies a broader induced-homology framework; it does not by itself record the integral primitive multiplier computed here.

## Limitations
This result concerns this specific canonical nine-vertex triangulation and simple edge cycles. It does not classify longer representatives, geodesic lengths for a geometric realization, or analogous spectra for all triangulations of the same manifold. The originality search cannot exclude an unindexed older hand computation of these exact missing-triangle classes.

## References
1. D. W. Walkup, *The lower bound conjecture for 3- and 4-manifolds*, Acta Mathematica 125 (1970), 75--107, DOI `10.1007/BF02392331`.
2. B. Bagchi and B. Datta, *Uniqueness of Walkup's 9-vertex 3-dimensional Klein bottle*, arXiv:`math/0610825v1` (2006); MSC 57Q15, 57R05.
3. J. Spreer, *Combinatorial 3-manifolds with cyclic automorphism group*, Stuttgart preprint 2011/028; MSC 57Q15, 57N10, 57M05.
