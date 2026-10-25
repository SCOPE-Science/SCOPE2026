# Six tetrahedral spheres and joint symmetry in the four-vertex multipath complex

## Finding

Let \(D=K_4^{\leftrightarrow}\) be the loopless directed complete graph on \(\{0,1,2,3\}\): it has each arrow \(i\to j\) for \(i\ne j\). Let \(X=X(D)\) have one simplicial vertex for each of the 12 arrows, and let a set of arrows be a face precisely when its components are vertex-disjoint directed simple paths (isolated graph vertices are allowed). This is the cycle-free chessboard complex \(\Omega_4\).

For \(G=S_4\times C_2\), the \(S_4\) factor relabels the four underlying vertices. The nontrivial element \(\rho\) of \(C_2\) reverses every arrow: \(\rho(i\to j)=j\to i\). Although \(\rho\) is not a digraph automorphism fixing orientations, it is a simplicial automorphism of \(X\) because it reverses each directed path. It commutes with vertex relabeling.

The integral homotopy type is
\[
 X\simeq\left(\bigvee^7 S^1\right)\vee\left(\bigvee^6 S^2\right).
\]
Thus \(\widetilde H_1(X;\mathbb Z)=\mathbb Z^7\), \(\widetilde H_2(X;\mathbb Z)=\mathbb Z^6\), and all other reduced integral homology vanishes. The **complete joint rational symmetry representation** is
\[
\begin{aligned}
\widetilde H_1(X;\mathbb Q)&\cong S^{(1,1,1,1)}_+\oplus S^{(2,1,1)}_+\oplus S^{(3,1)}_-,\\
\widetilde H_2(X;\mathbb Q)&\cong S^{(3,1)}_+\oplus S^{(1,1,1,1)}_-\oplus S^{(2,2)}_-.
\end{aligned}
\]
Here \(S^\lambda\) is the rational irreducible Specht module of \(S_4\), and subscripts \(+/-\) indicate the eigenvalue of the commuting arrow-reversal involution.

For explicit reproducibility, the character values are below. Columns are the five \(S_4\) cycle types \((1,1,1,1)\), \((2,1,1)\), \((2,2)\), \((3,1)\), \((4)\), in that order. Within each row, \(r=0\) is no arrow reversal and \(r=1\) is arrow reversal.

| Group element coset | Degree-one trace vector | Degree-two trace vector |
|---|---|---|
| \(r=0\) | \((7,-1,-1,1,-1)\) | \((6,0,2,0,-2)\) |
| \(r=1\) | \((1,-3,1,1,1)\) | \((0,2,-4,0,0)\) |

## Assumptions and scope

The directed graph has **exactly four** labeled vertices and all 12 nonloop arrows. Its multipath complex is the ordinary abstract simplicial complex on arrows; not a directed flag complex, a graph independence complex, or a standard \(4\times3\) chessboard complex. Homology uses integer coefficients for the homotopy statement and rational coefficients for the group decomposition. The theorem asserts no uniform extension to larger vertex sets and no integral group-ring splitting.

## Proof

**1. Six tetrahedral boundaries.** A multipath has at most three arrows: the permitted connected components are simple directed paths on at most four vertices. A three-arrow multipath is a directed Hamiltonian path, and the missing closing arrow is uniquely determined. Hence every maximal triangle is a face of the boundary \(\partial\Delta(c)\) of the tetrahedron on the four arrows of a unique directed Hamiltonian four-cycle \(c\). There are \(4!/4=6\) such oriented cycles, each with four triangles.

Every valid two-arrow face also lies in a **unique** directed Hamiltonian four-cycle. For adjacent arrows \(a\to b\to c\), append the remaining vertex \(d\) to form the cycle \(a\to b\to c\to d\to a\). For disjoint arrows \(a\to b\) and \(c\to d\), the unique completion is \(a\to b\to c\to d\to a\). Consequently, different tetrahedral boundaries have no common edge or triangle. Conversely, every face belongs to at least one such boundary (each individual arrow extends in two ways). Thus \(X\) is precisely their union, pairwise intersecting in sets of vertices. Its face counts are \((f_0,f_1,f_2)=(12,36,24)\).

**2. Integral homotopy type.** Let \(\mathcal C\) be the six oriented Hamiltonian four-cycles, \(\mathcal A\) the twelve arrows, and \(\mathcal I=\{(c,a):c\in\mathcal C,\ a\in c\}\). The bipartite incidence graph \(B\) has \(6+12=18\) vertices and \(|\mathcal I|=6\cdot4=24\) edges. It is connected: each cycle contains four distinct arrows, each arrow occurs in precisely two cycles, and any two distinct cycles share at most one arrow, so the graph on cycle nodes is the connected six-vertex graph with degree four (the octahedral graph). Hence \(\beta_1(B)=24-18+1=7\).

Form the homotopy-colimit graph of spaces consisting of six copies of \(S^2=|\partial\Delta^3|\) and twelve point spaces joined by the 24 incidence intervals. Contracting each incidence interval recovers \(X\); the contraction is a homotopy equivalence because it contracts mapping-cylinder intervals arising from inclusions of subcomplexes at vertices. Since each sphere is simply connected, shrinking a maximal tree of \(B\) yields \(X\simeq(\bigvee^6 S^2)\vee(\bigvee^{\beta_1(B)}S^1)\). This proves the displayed integral homotopy type, with no torsion.

**3. Equivariant homology.** Both factors of \(G\) permute the six sphere subcomplexes and the 12 arrow vertices, and therefore preserve \(B\). The natural graph-of-spaces construction yields integral \(G\)-isomorphisms
\[
 \widetilde H_1(X;\mathbb Z)\cong H_1(B;\mathbb Z),\qquad
 \widetilde H_2(X;\mathbb Z)\cong \bigoplus_{c\in\mathcal C}\widetilde H_2(\partial\Delta(c);\mathbb Z).
\]
In degree two, a symmetry that fixes \(c\) acts on its oriented fundamental class with the sign of the permutation it induces on the four arrows of \(c\). In degree one, \(H_1(B;\mathbb Q)\) is the kernel of the incidence-graph boundary, and since \(B\) is connected, the augmented exact sequence implies, for each \(g\in G\),
\[
 \chi_1(g)=\#\mathcal I^g-\#\mathcal C^g-\#\mathcal A^g+1,
 \qquad \chi_2(g)=\sum_{c\in\mathcal C^g}\operatorname{sgn}(g|_c).
\]
No orientation correction occurs on incidence-graph edges because every group element preserves the two vertex parts.

Enumerating only the six directed Hamiltonian cycles and the twelve arcs gives the two trace vectors in the table, constant on the ten conjugacy classes of \(G\). Their scalar products with the five irreducible \(S_4\) characters, after projecting onto the \(\pm1\) reversal eigenspaces, yield exactly the stated Specht decompositions. This establishes the **entire** rational character, not just its dimension.

## Verification

The standalone file `check_omega4.py` enumerates all 12 arcs, all admissible one-, two- and three-arrow faces, the six oriented Hamiltonian cycles and their 24 incidences. It independently checks unique cycle containment of every edge and triangle, incidence-graph connectivity, and traces of all 48 group actions. The same program verifies the ten class-character values and the rational irreducible multiplicities using exact integers; it requires only Python 3 and runs via `python3 check_omega4.py`. No finite sample extrapolation is used: the domain has exactly four underlying vertices and the enumeration covers every simplex and symmetry.

## Relationship to prior work

Vrećica and Živaljević introduced/studied the same cycle-free chessboard complexes \(\Omega_n\) and proved connectivity bounds. In particular, their 2007 preprint proves that \(\Omega_4\) is connected, but the relevant statements do not specify the six-sphere/seven-circle decomposition or a \(S_4\times C_2\) homology character. Caputi, Collari and Di Trani (2021 preprint) define the multipath complex and link it to multipath cohomology; Caputi, Collari, Di Trani and Smith (2022 preprint) study homotopy types of other directed-graph families and explicitly acknowledge the earlier complete-digraph work. A 2026 paper on *bidirected polygons* concerns different digraphs and supplies no four-vertex complete-digraph character. A 2020 review of generalized chessboard complexes treats ordinary rook complexes, which are not the cycle-free complex in this theorem. None of those general statements implies the specific two-degree integral homotopy decomposition and joint character without the incidence calculation here.

## Limitations

This is a finite, intrinsically motivated first-connected-case classification. It neither settles the homology of \(\Omega_n\) for \(n\ge5\) nor supplies integral irreducible module decompositions (which require more than rational characters). No independent audit has been performed. Although inspected publications and semantic record searches revealed no dominating equivalent result, a differently indexed computation of \(\Omega_4\) remains possible.

## References

1. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206, first public version 21 October 2021, especially Section 6.
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656, first public version 9 August 2022, especially introduction and Sections 4–5.
3. S. T. Vrećica, R. T. Živaljević, *Cycle-free Chessboard Complexes and Symmetric Homology of Algebras*, arXiv:0710.5252, 2007, especially Definition 1 and Theorem 10.
4. D. Jojić, G. Panina, S. T. Vrećica, R. T. Živaljević, *Generalized Chessboard Complexes and Discrete Morse Theory*, arXiv:2003.04018, 2020.
5. L. Caputi, C. Collari, J. P. Smith, *Multipath Complexes of Bidirectional Polygonal Digraphs*, arXiv:2601.05670, 2026, introduction and Section 1.1 (different digraph family).
