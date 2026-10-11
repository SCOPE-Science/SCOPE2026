# The full octahedral symmetry representation of the matching complex

## Finding
Let \(O=K_{2,2,2}\) be the octahedral graph, equivalently the complete graph on six vertices with the three antipodal edges removed. Let \(M(O)\) be its **ordinary matching complex**: a vertex is an edge of \(O\), and a simplex is a collection of pairwise vertex-disjoint graph edges. Then

\[
M(O)\simeq\bigvee^{11}S^1.
\]

The full graph automorphism group is \(G=\operatorname{Aut}(O)\cong S_4\times C_2\). Under this identification, \(S_4\) is the rotation group acting on the four antipodal pairs of triangular faces, and \(\varepsilon:G\to\{\pm1\}\) is the determinant character, trivial on rotations and nontrivial on central inversion. Write \(S^\lambda\) for the rational irreducible \(S_4\)-representation indexed by a partition \(\lambda\) of four. The **complete rational homology module** is

\[
\widetilde H_1(M(O);\mathbb Q)\cong
(S^{(3,1)}\otimes\varepsilon)\oplus
S^{(2,1,1)}\oplus
(S^{(2,1,1)}\otimes\varepsilon)\oplus
(S^{(2,2)}\otimes\varepsilon).
\]

All other reduced integral and rational homology groups vanish. In particular \(H_1(M(O);\mathbb Z)\cong\mathbb Z^{11}\), and central inversion acts with positive and negative rational eigenspace dimensions \(3\) and \(8\), respectively. There are **no** nonzero \(G\)-invariant classes in positive-degree rational homology.

## Assumptions and scope
The graph has vertices \(0,1,2,3,4,5\), with precisely the unordered pairs \(01\), \(23\), and \(45\) missing. Edges of \(O\) are not distinguished by orientations; orientation signs occur only when they form an oriented simplex in simplicial chains. A matching of size \(q+1\) corresponds to a \(q\)-simplex. The complex is **not** the Morse complex of acyclic discrete vector fields and is **not** the perfect-matching-only subcomplex. This is a complete result for the six-vertex octahedral graph; no assertion is made for higher-dimensional cross-polytope graphs.

For the character table below, write \(\mu\) for the cycle type of the associated permutation of the four antipodal face pairs, and \(\varepsilon(g)\) for the determinant. Every ordered pair \((\mu,\varepsilon(g))\) determines a conjugacy class because \(G\cong S_4\times C_2\).

## Proof
**Cell structure and integral homotopy type.** The complex has \(12\) vertices. Each vertex of \(O\) has degree four, so the number of disjoint unordered pairs of graph edges is
\[
\binom{12}{2}-6\binom42=30.
\]
Its two-simplices are exactly its perfect matchings. There are \(15\) perfect matchings of the complete six-vertex graph; inclusion–exclusion on the three omitted disjoint edges gives \(15-3\cdot3+3\cdot1-1=8\). Thus the complete nonempty face vector is \((12,30,8)\).

Every one-simplex consists of two disjoint edges covering four of the six graph vertices. It lies in a two-simplex only if the remaining two vertices form an edge, and in that case it lies in **exactly one** two-simplex. Each two-simplex therefore possesses three free one-faces, none of which occurs in a different two-simplex. Choose one such free face in each of the eight two-simplices and perform the eight elementary collapses. The resulting one-dimensional graph has \(12\) vertices and \(22\) edges.

The original matching complex is connected: if two graph edges are disjoint, their corresponding complex vertices are adjacent; if they meet, the three remaining graph vertices contain an octahedral edge because the independence number of \(O\) is two, so there is a length-two path between the two complex vertices. Elementary collapses preserve connectedness. The residual graph has first Betti number \(22-12+1=11\), giving the claimed eleven-circle homotopy type and integral torsion-freeness.

**Group identification.** Every graph automorphism permutes the three missing antipodal pairs and can independently exchange the two vertices in each pair, so \(G\cong C_2\wr S_3\) and \(|G|=48\). This is the full signed-coordinate symmetry group of the octahedron. Its orientation-preserving subgroup has order \(24\) and acts faithfully on four antipodal face pairs as \(S_4\); the central inversion is orientation reversing and is central. Consequently \(G\cong S_4\times C_2\), with the stated determinant character.

**Trace computation.** Let \(C_q\) denote rational oriented simplicial chains. Since only \(H_0\) and \(H_1\) are nonzero and \(H_0\) is the trivial module, the equivariant Euler–Poincaré identity gives, for every \(g\in G\),
\[
\operatorname{tr}(g\mid H_1)
=1-\operatorname{tr}(g\mid C_0)
+\operatorname{tr}(g\mid C_1)
-\operatorname{tr}(g\mid C_2).
\]
For each \(q\), the chain trace is the sum over \(g\)-invariant \(q\)-simplices of the sign of the induced permutation of their \(q+1\) edges. Thus the right side involves finite signed fixed-matching counts, not a quotient whose basis must be guessed.

Enumerating the \(48\) signed coordinate permutations gives the complete class table:

| Cycle type \(\mu\) | \(\varepsilon(g)\) | Class size | \(\operatorname{tr}(g\mid H_1)\) |
|---|---:|---:|---:|
| \((1,1,1,1)\) | \(+1\) | 1 | 11 |
| \((1,1,1,1)\) | \(-1\) | 1 | -5 |
| \((2,1,1)\) | \(+1\) | 6 | -1 |
| \((2,1,1)\) | \(-1\) | 6 | -1 |
| \((2,2)\) | \(+1\) | 3 | -1 |
| \((2,2)\) | \(-1\) | 3 | -1 |
| \((3,1)\) | \(+1\) | 8 | -1 |
| \((3,1)\) | \(-1\) | 8 | 1 |
| \((4)\) | \(+1\) | 6 | 1 |
| \((4)\) | \(-1\) | 6 | 1 |

For a useful hand check, central inversion fixes no vertex of the matching complex, reverses the orientation of each of the six antipodal pairs of matching-complex vertices, and fixes no two-simplex. Its chain traces are therefore \((0,-6,0)\) and its first-homology trace is \(1-6=-5\), matching the table.

Taking inner products of this character with the ten irreducible characters \(\chi_\lambda\varepsilon^j\), where \(\lambda\) ranges over the five partitions of four and \(j\in\{0,1\}\), yields multiplicity one precisely for \((\lambda,j)=( (3,1),1 ),((2,1,1),0),((2,1,1),1),((2,2),1)\) and zero otherwise. This establishes the full rational module decomposition. The four summands have dimensions \(3,3,3,2\). The central inversion has trace \(-5\), hence eigenspace dimensions \((11-5)/2=3\) and \((11+5)/2=8\); the trivial irreducible is absent.

## Verification
Run `python3 verify_octahedral_matching.py` with ordinary Python 3. The program generates the graph and all matchings directly from the definitions. It checks \((12,30,8)\), proves all \(24\) one-faces incident to two-simplices are free, constructs the eight elementary collapses, checks connectedness, and explicitly builds a spanning tree and eleven integral fundamental cycles of the residual graph. It enumerates all \(48\) graph automorphisms and obtains their first-homology matrices by transporting these cycles and reducing the eight triangle boundaries over the integers. It checks all \(48^2=2304\) multiplication identities for the resulting exact integer matrices. Independently, it evaluates signed fixed-simplex traces and checks agreement for every group element, the class table, the ten irreducible multiplicities, and the central-inversion eigenspaces. A successful replay ends with `VERIFY_OK`.

The computation is **exhaustive for this six-vertex graph**. The homotopy proof does not infer an infinite-family theorem from a finite experiment.

## Relationship to prior work
Donovan and Scoville's *Star clusters in the Matching, Morse, and Generalized Morse complex* (arXiv:2207.13780v1, first public 2022-07-27; primary MSC 57Q70) gives the definitions and collapse methods for ordinary matching complexes and computes paths, cycles, and Dutch windmill graphs, but its matching-complex section does not contain the octahedral module computed here. Bate, Everitt, Ford, and Ramos (arXiv:2312.13750) treat complete graph/hypergraph matching complexes and symmetric-group representations; the ordinary octahedral graph is the proper subgraph obtained by deleting a perfect matching, and its first Betti number \(11\) differs from the complete six-vertex matching complex's \(16\). Their theorem on complete hypergraphs therefore does not determine the claimed module. Li (arXiv:2202.08828) proves equivariant log-concavity for **permutation representations on matchings**, not the homology representation of their simplicial complex.

A separately published computation titled *The octahedral graph Morse complex is a wedge of 675 four-spheres* concerns the **Morse complex of gradient fields** with \(24\) vertices and nonzero homology in dimension four, whereas the present ordinary matching complex has \(12\) vertices and nonzero reduced homology in dimension one. The names and graphs coincide, but the complexes and statements do not.

## Limitations
The integral assertion is about homotopy type and free homology groups; the irreducible decomposition is **over \(\mathbb Q\)**, not an assertion that the same direct-sum splitting exists as an integral lattice. The calculation is for \(K_{2,2,2}\) alone. A broader result on matching complexes of higher-dimensional cocktail-party graphs is not proved. A differently indexed prior decomposition remains a residual bibliographic risk despite the primary-text and database comparisons.

## References
1. Connor Donovan and Nicholas A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780v1, first public 2022-07-27, Section 5. https://arxiv.org/html/2207.13780v1
2. Michael Bate, Brent Everitt, Sam Ford, and Eric Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750v1, first public 2023-12-21; consulted arXiv full text, https://arxiv.org/html/2312.13750v3
3. Shiyue Li, *Equivariant log-concavity of graph matchings*, arXiv:2202.08828v1, first public 2022-02-17; consulted https://arxiv.org/html/2202.08828v2
4. Xun Dong and Michelle L. Wachs, *Combinatorial Laplacian of the Matching Complex*, Electronic Journal of Combinatorics 9 (2002), R17, DOI:10.37236/1634, concerning the matching complex of complete graphs.
5. *The octahedral graph Morse complex is a wedge of 675 four-spheres*, published mathematical record, full result statement inspected; different complex.
