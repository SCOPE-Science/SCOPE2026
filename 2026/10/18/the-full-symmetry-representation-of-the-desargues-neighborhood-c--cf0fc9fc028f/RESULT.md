# The full symmetry representation of the Desargues neighborhood complex

## Finding
Let \(D=H(5,2)\) be the Desargues graph, with vertex set the two- and three-element subsets of \([5]\), where inclusion defines adjacency. Let \(X=\mathcal N(D)\) be its **open** Lovász neighborhood complex: a nonempty subset of vertices forms a simplex precisely when its vertices have a common neighbor in \(D\). Its full graph automorphism group is \(G=\operatorname{Aut}(D)\cong S_5\times C_2\), with central complement involution \(\tau\).

Write \(\varepsilon\) for the nontrivial one-dimensional rational representation of the second factor and \(S^{\lambda}\) for the rational Specht representation of \(S_5\) indexed by the partition \(\lambda\). Then

\[
\widetilde H_1(X;\mathbb Q)\cong
\bigl(S^{(3,1,1)}\oplus S^{(2,2,1)}\bigr)
\boxtimes(\mathbf1\oplus\varepsilon),\qquad
\widetilde H_0(X;\mathbb Q)\cong\mathbf1\boxtimes\varepsilon.
\]

All other reduced rational homology groups are zero. Furthermore the **geometric quotient** by the complete graph automorphism group is a closed triangle:

\[
|X|/\operatorname{Aut}(D)\ \cong\ \Delta^2.
\]

Equivalently, for each \(g\in S_5\), the character on degree-one reduced homology is \(\chi_1(g,\tau^e)=(1+(-1)^e)w(g)\), where \(e\in\{0,1\}\). For cycle types \(1^5, 2\,1^3,2^2 1,3\,1^2,3\,2,4\,1,5\), respectively, the values of \(w\) are

\[
(11,-1,-1,-1,-1,1,1).
\]

The reduced degree-zero character is \(\chi_0(g,\tau^e)=(-1)^e\). Each connected component has integral first homology \(\mathbb Z^{11}\), and there are two components; no assertion of an integral Specht-lattice decomposition is made.

## Assumptions and scope
The graph is finite, simple and undirected. Its 20 vertices are precisely \(\binom{[5]}2\sqcup\binom{[5]}3\). The open neighborhood, not the closed neighborhood, is used throughout. The full automorphism group and the identification of its central involution with set complementation follow from Mirafzal's theorem for the bipartite Kneser graph \(H(n,k)\), applied to \((n,k)=(5,2)\). Graph automorphisms act simplicially on \(X\). The module decomposition is asserted over \(\mathbb Q\), while the underlying free abelian homology ranks are proved over \(\mathbb Z\). The quotient statement concerns the ordinary topological orbit space, not a homotopy orbit construction.

## Proof
**1. Components and chains.** Because \(D\) is bipartite and every neighborhood lies in the opposite part, \(X=Y_2\sqcup Y_3\), where \(Y_2\) uses two-element subsets as vertices and \(Y_3\) uses three-element subsets. A maximal simplex of \(Y_2\) is the triple of two-element subsets contained in one given three-element subset. Thus \(Y_2\) has exactly 10 vertices, 30 edges, and 10 triangular faces. Two two-subsets form an edge if and only if they meet in one element; their union is the **unique** three-subset producing that edge. In particular every edge belongs to exactly one triangle, and the one-skeleton, the triangular graph on the ten edges of \(K_5\), is connected. Set complementation gives an \(S_5\)-equivariant simplicial isomorphism \(Y_2\cong Y_3\) and interchanges the components.

The integral augmented chain complex of \(Y_2\) has \(\operatorname{rank}\partial_1=9\). Each of its ten oriented triangle boundaries has an edge coefficient \(\pm1\) in a coordinate where every other triangle boundary is zero. Consequently \(\partial_2\) has a unit 10-by-10 minor, is injective, and has primitive image even as a subgroup of the integral one-cycle lattice. The cycle lattice has rank \(30-9=21\); hence \(H_1(Y_2;\mathbb Z)\cong\mathbb Z^{11}\), \(H_2(Y_2;\mathbb Z)=0\), and the other reduced integral homology vanishes. Equivalently, one can collapse the ten distinct triangle/free-edge pairs and obtain a connected graph of cycle rank eleven.

**2. The full character.** Orient simplices by increasing indices of their two-subset vertices. For \(g\in S_5\), let \(T_i(g)\) be the signed trace on the oriented \(i\)-simplex chains of \(Y_2\), for \(i=0,1,2\). Since \(Y_2\) is connected and only \(H_0,H_1\) are nonzero, the Hopf trace identity gives

\[
w(g)=\operatorname{tr}\bigl(g\mid H_1(Y_2;\mathbb Q)\bigr)=1-T_0(g)+T_1(g)-T_2(g).
\]

A simplex contributes its orientation sign when its vertex set is fixed, otherwise zero. Exhaustive cycle-type computation on the explicitly described ten triangles and their edges gives:

| Cycle type | \(T_0\) | \(T_1\) | \(T_2\) | \(w\) |
|:--|--:|--:|--:|--:|
| \(1^5\) | 10 | 30 | 10 | 11 |
| \(2\,1^3\) | 4 | 0 | -2 | -1 |
| \(2^2 1\) | 2 | -2 | -2 | -1 |
| \(3\,1^2\) | 1 | 0 | 1 | -1 |
| \(3\,2\) | 1 | 0 | 1 | -1 |
| \(4\,1\) | 0 | 0 | 0 | 1 |
| \(5\) | 0 | 0 | 0 | 1 |

The rational Specht characters for partitions \((3,1,1)\) and \((2,2,1)\), in this order of classes, are \((6,0,-2,0,0,0,1)\) and \((5,-1,1,-1,-1,1,0)\). Their sum equals \(w\). Character orthogonality (or the Jacobi–Trudi calculation reproduced by the verifier) shows these are precisely the two irreducible constituents. Because \(\tau\) swaps two equivariantly isomorphic components, degree-one homology is the component module tensored with the regular representation \(\mathbf1\oplus\varepsilon\) of \(C_2\). On degree-zero reduced homology, \(S_5\) fixes both components and \(\tau\) switches them, leaving exactly the sign line \(\varepsilon\).

**3. The orbit space.** Every maximal flag \(v\subset e\subset t\) of faces of \(Y_2\), with dimensions \(0,1,2\), is determined by a three-subset, one of its three edges, and one endpoint of that edge. There are \(10\cdot3\cdot2=60\) such flags. The natural \(S_5\)-action is transitive on them. It follows that it is also transitive on all subflags of each fixed rank-pattern. Complementation \(\tau\) exchanges \(Y_2\) and \(Y_3\), so the full group is transitive on all maximal flags of \(X\). The barycentric subdivision has one vertex for each nonempty face, with simplices given by chains of faces. The group action preserves face dimension, hence acts without inversions on this subdivision. Its quotient has exactly one vertex of each of the three ranks, and exactly one simplex for each nonempty subset of these ranks. This is a single closed \(2\)-simplex. Barycentric subdivision preserves the underlying orbit space, proving the asserted homeomorphism.

## Verification
Two standalone Python standard-library programs accompany this result. `check_characters.py` reconstructs all face sets, evaluates signed chain traces for all 120 permutations of five letters, computes Specht characters by the Jacobi–Trudi permutation-module determinant, checks the two constituents, and verifies that all 60 complete face flags form one orbit. `check_homology.py` independently constructs integral simplicial boundary matrices, verifies ranks 9 and 10 and the boundary identity, selects 21 fundamental graph cycles modulo ten triangle relations, and computes seven representative induced degree-one homology traces **directly from their rational matrices** without using Hopf trace or predefined character tables. Both programs pass. For fixed finite complexes and groups the enumerations are exhaustive; the explicit unit-minor and flag-transitivity arguments explain the integral and quotient claims independently of the enumerations.

Run with a standard Python 3 interpreter from the directory containing the two programs using `python check_characters.py` and `python check_homology.py`. Each raises an assertion if any required check fails. The programs use no network access or third-party dependencies.

## Relationship to prior work
The Lovász neighborhood-complex construction and its chromatic-number role are foundational; Kahle's 2005 preprint supplies an independently dated early public account of the same definition, but treats random graphs rather than this example. Shukla proved that each connected component of the neighborhood complex of a graph of maximum degree at most three (apart from stated exceptions) is contractible or a wedge of circles. Thus the mere presence of circle wedges is **not** new. Mirafzal established the automorphism group of bipartite Kneser graphs, providing the full symmetry group used here. Schultz studied equivariant Hom/box complexes for **stable** Kneser graphs with different object parameters and symmetry group. None of the inspected cited results provides this Desargues-specific complete \(S_5\times C_2\) rational homology character and topological orbit-space identification. This comparison is not a universal novelty guarantee.

## Limitations
This is a theorem for the single explicitly specified finite graph; no arbitrary-parameter bipartite Kneser generalization, integral Specht-lattice decomposition, equivariant homotopy-type classification, or homotopy-orbit computation is claimed. The non-equivariant circle-wedge property and the graph automorphism group are known antecedents. Exact computations corroborate, but do not replace, the argument. A matching equivalent representation calculation in unindexed or historical literature remains a bibliographic risk. Independent scientific verification has not been performed.

## References
1. Matthew Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, version 1 publicly submitted 2005-12-04; https://arxiv.org/abs/math/0512077 .
2. Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, Theorem 2.1 and its proof; https://arxiv.org/abs/1802.04526 .
3. Seyed Morteza Mirafzal, *The automorphism group of the bipartite Kneser graph*, arXiv:1803.02524, Theorem 3.6; https://arxiv.org/abs/1803.02524 .
4. Carsten Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688, for comparison with a distinct graph family; https://arxiv.org/abs/1003.5688 .
