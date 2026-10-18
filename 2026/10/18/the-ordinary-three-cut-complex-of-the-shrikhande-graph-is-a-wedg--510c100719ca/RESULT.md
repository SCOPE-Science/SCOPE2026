# The ordinary three-cut complex of the Shrikhande graph is a wedge of eleven eleven-spheres

## Finding
Let \(S\) be the Shrikhande graph on \((\mathbb Z/4\mathbb Z)^2\), with edges of differences \(\pm(1,0)\), \(\pm(0,1)\), and \(\pm(1,1)\). Its **ordinary three-cut complex** \(\Delta_3(S)\) has as facets precisely the complements of three-vertex subsets whose induced graph is disconnected. Then
\[
\boxed{\Delta_3(S)\simeq\bigvee^{11} S^{11}.}
\]
In particular, its only nonzero reduced integral homology is \(\widetilde H_{11}(\Delta_3(S);\mathbb Z)\cong\mathbb Z^{11}\). The complex is pure of dimension twelve and is not shellable. This differs from the known rank twenty-seven in the same homological degree for the ordinary three-cut complex of the \(4\times4\) rook graph. These two graphs have the same strongly regular parameters \((16,6,2,2)\).

## Assumptions and scope
A disconnected triple means that the graph induced on its three vertices has at most one edge. This is the **ordinary** three-cut construction, not the total three-cut complex in which the excluded triple must be independent. The sixteen Shrikhande vertices are labeled by the integer \(4a+b\) for \((a,b)\in(\mathbb Z/4\mathbb Z)^2\), using representatives \(0,1,2,3\). Reduced homology is taken over \(\mathbb Z\), and homotopy equivalences are non-equivariant. No conclusion for other cut sizes or a general class of strongly regular graphs is asserted.

For a simplicial complex \(X\) on the full vertex set \(V\), write its combinatorial Alexander dual as \(X^\vee=\{U\subseteq V:V\setminus U\notin X\}\). Put \(L=\Delta_3(S)^\vee\). Thus \(U\in L\) if and only if **every** three-element subset of \(U\) induces a connected graph. This converts the topological calculation to an explicit small-dimensional complex.

## Proof
**1. Determine the dual faces.** A connected triple has two or three graph edges. Directly from the six Cayley differences, the graph has sixteen vertices, forty-eight edges, degree six at each vertex, and two common neighbors for every pair of distinct vertices. The number of connected triples is
\[
\sum_v\binom{\deg(v)}2-2t(S)=16\binom62-2(32)=176,
\]
where \(t(S)=32\) counts graph triangles. Exhaustive enumeration of the \(\binom{16}{4}\) four-subsets finds exactly sixty subsets all of whose three-subsets are connected: forty-eight induce a diamond (five graph edges) and twelve induce a four-cycle (four graph edges). None of the \(\binom{16}{5}\) five-subsets has this property. Since the property is hereditary, the full augmented face counts of \(L\), indexed by cardinality, are
\[
(f_{-1},f_0,f_1,f_2,f_3)=(1,16,120,176,60),
\]
with no higher-dimensional faces.

**2. Collapse the sixty tetrahedra integrally.** Among the 176 two-faces of \(L\), 144 are contained in precisely one tetrahedron and 32 in precisely three. Every tetrahedron has at least two triangular faces of the first kind. Select the lexicographically first such private triangle for each tetrahedron and remove the pair. Because these private triangles have no other tetrahedral cofaces, these are sixty legitimate elementary simplicial collapses; no two pairs share a face. The resulting two-dimensional complex \(Y\) retains the complete one-skeleton on sixteen vertices and has exactly 116 two-faces. Thus \(L\simeq Y\).

**3. Compute the exact integral two-boundary.** Choose the spanning tree of the complete one-skeleton consisting of the fifteen edges from vertex zero. The integral cycle group of this one-skeleton is free of rank \(120-16+1=105\), with coordinates the 105 edges avoiding vertex zero. The signed boundary of every surviving oriented triangle gives a column in the integer matrix \(B\) of shape \(105\times116\), where rows are these non-tree edges. Projection to non-tree edge coordinates is an isomorphism from the integral cycle group, not merely a rational projection.

The supplied executable `verify.py` builds \(B\) from the graph definition and the stated lexicographic collapse choices, then performs **105 integral unit pivots** using only row swaps, column swaps, row negations and addition of integer multiples of one row or column to another. It ends with an identity block of size 105 and eleven zero columns. Every transformation is unimodular, so \(B:\mathbb Z^{116}\to\mathbb Z^{105}\) is surjective, its kernel is free of rank eleven, and its cokernel is zero. Therefore
\[
\widetilde H_i(L;\mathbb Z)\cong
\begin{cases}\mathbb Z^{11},&i=2,\\0,&i\ne2.\end{cases}
\]
This integral calculation establishes the absence of torsion, which would not follow from finitely many modular rank computations.

**4. Alexander duality and the homotopy upgrade.** Integral combinatorial Alexander duality on sixteen vertices identifies \(\widetilde H_i(\Delta_3(S);\mathbb Z)\) with \(\widetilde H^{13-i}(L;\mathbb Z)\). The universal coefficient theorem and Step 3 show that \(\Delta_3(S)\) has exactly \(\mathbb Z^{11}\) in reduced degree eleven. Because \(L\) has no face of cardinality five, the cut complex includes **every** subset of the sixteen vertices of size at most eleven: it contains the full ten-skeleton of the fifteen-simplex. It is therefore nine-connected. Vanishing of its degree-ten integral homology and the Hurewicz theorem make it ten-connected. Representing an integral basis of degree-eleven homology by eleven sphere maps gives a homology equivalence \(\bigvee^{11}S^{11}\to\Delta_3(S)\), which is a homotopy equivalence by the homological Whitehead theorem for simply connected CW complexes.

Every facet of \(\Delta_3(S)\) has thirteen vertices, so it is pure twelve-dimensional. Its nonzero eleventh homology obstructs shellability, since a pure shellable twelve-complex has reduced homology only in dimension twelve. This completes the proof.

## Verification
Run `python3 verify.py` in a directory containing the accompanying source file. It requires only the Python standard library, checks all graph pairs, all possible triples, four-sets and five-sets, validates the sixty private-face collapses, constructs the complete signed integer boundary matrix after those collapses, and performs the 105 unimodular pivots. The final line is exactly `VERIFY_OK`; a complete reference output appears in `verification_output.txt`. The computations are finite and exhaustive **for this fixed sixteen-vertex graph**. The Alexander-duality, connectivity, Hurewicz and Whitehead deductions in Step 4 are mathematical arguments, not consequences of finite experiments alone.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary cut complexes in *Topology of Cut Complexes of Graphs* (arXiv:2304.13675). Their Theorem 6.1 does **not** settle this example: its complete codimension-one skeleton hypothesis fails, because sixty four-subsets of Shrikhande vertices correspond to absent twelve-vertex faces of the cut complex. Their named graph families and sequel (arXiv:2407.08158) do not include the Shrikhande graph.

A previously published calculation for the rook graphs \(K_m\square K_n\) gives reduced integral three-cut homology rank \(\binom m2\binom n2-(m-1)(n-1)\) in degree \(mn-5\), hence rank twenty-seven for \(m=n=4\). That result concerns a different graph: the rook graph has eight four-cliques, whereas the Shrikhande graph has none. Its rook-rectangle decomposition consequently does not compute \(L\) above. Previously published results for graphs with no four-cycles or with sufficiently high girth cannot be applied to the Shrikhande graph, which has twelve induced four-cycles and many additional non-induced four-cycles.

The new point is a complete **integral homotopy** classification for the Shrikhande ordinary three-cut complex, exhibiting a topological distinction between two strongly regular graphs with identical numerical parameters. Searches of the relevant literature and research index found no result implying this classification, but cannot exclude unindexed equivalent work.

## Limitations
The result does not determine the integral action of the automorphism group on homology, other cut sizes, the ordinary three-cut homotopy types of arbitrary strongly regular graphs, or a shelling obstruction stronger than the degree-of-homology argument. The unit-pivot computation is reproducible but remains a computational certificate rather than a symbolic all-graphs theorem. No independent mathematical audit has been performed; literature completeness and research priority remain subject to specialist verification.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly submitted 2023-04-26; especially Sections 1, 5–7.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly submitted 2024-07-11; especially Sections 2 and 5.
3. *Integral and equivariant homology of three-cut complexes of rook graphs*, published published-finding corpus research record, 2026-10-11; its rook-graph statement and proof were inspected for implication comparison.
4. A. Hatcher, *Algebraic Topology*, 2002, for cellular connectivity, Hurewicz and Whitehead theorems; standard combinatorial Alexander duality as used in Reference 1.
