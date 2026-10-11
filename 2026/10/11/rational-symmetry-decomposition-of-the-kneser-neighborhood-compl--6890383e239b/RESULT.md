# Rational symmetry decomposition of the Kneser neighborhood complex on six points

## Finding
Let \(G=\mathrm{KG}(6,2)\) be the graph on the fifteen unordered pairs from \(\{1,2,3,4,5,6\}\), with adjacency for disjoint pairs, and let \(K=\mathcal N(G)\) be its ordinary open-neighborhood complex. The natural coordinate permutation action of \(\mathfrak S_6\) on \(K\) induces the following isomorphism of rational representations:
\[
\boxed{\widetilde H_2(K;\mathbb Q)\cong_{\mathbb Q[\mathfrak S_6]} S^{(3,1,1,1)}\oplus S^{(2,2,1,1)}.}
\]
Here \(S^\lambda\) denotes the irreducible rational Specht representation indexed by a partition \(\lambda\) of six. The two dimensions are ten and nine. This representation decomposition, rather than the already-published non-equivariant wedge count, is the finding.

## Assumptions and scope
No conditions beyond the stated finite graph and characteristic-zero coefficients are imposed. Every graph vertex is a two-element subset of the six-point ground set. A nonempty set of graph vertices is a simplex in \(K\) precisely when their union misses at least two of the six ground points. Thus \(K\) is equivalently the simplicial complex whose faces are edge sets of six-vertex simple graphs having at least two isolated vertices. This description is canonical under \(\mathfrak S_6\). The result concerns rational singular or simplicial homology as a \(\mathfrak S_6\)-representation; it is not an equivariant homotopy classification or an integral representation decomposition.

## Proof
**(1) Faces and homology concentration.** Number the fifteen duads lexicographically. The fifteen open neighborhoods each contain the six duads disjoint from a chosen duad. Exhaustively taking all their nonempty subsets yields the complete face vector, by dimensions zero through five,
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(15,105,260,225,90,15).
\]
A staged elementary matching pairs every available simplex \(\sigma\) not containing vertex \(v\) with \(\sigma\cup\{v\}\), processing lexicographic vertices from last to first and removing each pair before the next stage. Its numbers of pairs for the fifteen stages are
\[
(162,60,48,24,20,18,4,4,3,2,0,0,0,0,0).
\]
It leaves one critical zero-simplex and nineteen critical two-simplices. An exhaustive orientation of all 2,430 nonempty face-coface incidences (reverse precisely matched incidences) admits a topological sort visiting all 710 nonempty faces. Hence the matching is acyclic. Ordinary discrete Morse theory provides a CW model with one zero-cell and nineteen two-cells and no other cells, proving \(K\simeq\bigvee^{19}S^2\). This concentration and rank also follow from the previously published family theorem of Nilakantan and Singh; this step only ensures that the trace calculation below isolates degree two. In particular, reduced rational homology vanishes outside degree two, and ordinary \(H_0(K;\mathbb Q)\) is trivial as a representation.

**(2) Lefschetz character without an equivariant collapse.** For each \(g\in\mathfrak S_6\), let \(C_j(K;\mathbb Q)\) carry its canonical action on oriented simplices, with the orientation given by lexicographic vertex order. Define \(c_j(g)\) to be the signed count of \(j\)-faces fixed setwise by \(g\): an invariant face contributes the sign of the induced permutation of its ordered vertices, and any non-invariant face contributes zero. All face lists are exhaustive. The Hopf trace identity, together with the established homology concentration, gives
\[
\chi_2(g):=\operatorname{tr}\bigl(g\mid\widetilde H_2(K;\mathbb Q)\bigr)
=\sum_{j=0}^{5}(-1)^j c_j(g)-1.
\]
The subtraction of one is the ordinary trivial \(H_0\). For the eleven conjugacy classes, listed as the partitions of six in decreasing lexicographic order, the resulting traces are:

| Cycle type | \(\chi_2\) |
|---|---:|
| \((6)\) | \(-1\) |
| \((5,1)\) | \(-1\) |
| \((4,2)\) | \(1\) |
| \((4,1,1)\) | \(1\) |
| \((3,3)\) | \(1\) |
| \((3,2,1)\) | \(1\) |
| \((3,1,1,1)\) | \(1\) |
| \((2,2,2)\) | \(-1\) |
| \((2,2,1,1)\) | \(-1\) |
| \((2,1,1,1,1)\) | \(-5\) |
| \((1,1,1,1,1,1)\) | \(19\) |

**(3) Rational isotypic decomposition.** Generate all eleven irreducible \(\mathfrak S_6\) characters using the Murnaghan–Nakayama rule and verify their pairwise orthogonality against the exact class sizes. If \(\chi^\lambda\) is the irreducible character corresponding to partition \(\lambda\), its multiplicity is
\[
m_\lambda=\frac{1}{720}\sum_{[g]}|[g]|\,\chi_2(g)\chi^\lambda(g).
\]
All inner products are exactly zero except \(m_{(3,1,1,1)}=m_{(2,2,1,1)}=1\). The characters are rational-valued, and the complex irreducibles of symmetric groups admit models over \(\mathbb Q\), so semisimplicity in characteristic zero supplies the asserted rational Specht decomposition. This proves the finding.

## Verification
Run `python3 verify.py` using the Python standard library. It independently checks all face memberships, every matching pair, full acyclicity, each conjugacy-class oriented chain trace, all irreducible characters, and exact multiplicities. Run `python3 check_independent.py` with Python 3 and SymPy to re-enumerate all 32,767 nonempty subsets by endpoint support rather than graph neighborhoods, compute simplicial homology over characteristics two, three, and five, and derive the symmetric-group irreducibles using Young's permutation-module rule and Kostka matrix inversion rather than Murnaghan–Nakayama. Both checks complete without errors. In the first verifier, the identity trace is nineteen; the second yields reduced Betti number nineteen in degree two and zero in all other degrees over each checked field. All finite enumerations cover their exact stated finite domains.

## Relationship to prior work
Nilakantan and Singh's Theorem 1.3 proves the **non-equivariant** formula \(\mathcal N(\mathrm{KG}_{2,k})\simeq\bigvee^{k^2+5k+5}S^k\), giving nineteen two-spheres when \(k=2\). That prior theorem does not specify an \(\mathfrak S_6\)-equivariant homotopy equivalence or the induced nineteen-dimensional homology character. The present decomposition is strictly finer: non-equivariant homotopy data determine the rank but not the \(\mathfrak S_6\)-action. Schultz's equivariant topology results treat stable Kneser graphs and their dihedral symmetry, not this full coordinate-permutation action on the ordinary Kneser graph. Matsushita addresses general neighborhood-complex fundamental groups, not this higher rational character. The bounded-covering-number graph complexes in Jonsson's work are not identical: requiring an independent pair of graph vertices is weaker than requiring two isolated graph vertices. No wider family or general equivariant classification is inferred.

## Limitations
This is one rational representation calculation for a single fifteen-vertex graph. It gives neither an explicit integral Specht lattice decomposition nor full equivariant stable homotopy information. The determination is conditional on the stated exact finite enumerations, which can be reproduced from the two embedded scripts; a separate human audit has not been performed. Equivalence with an unindexed prior calculation cannot be excluded by bibliographic searches alone.

## References
1. N. Nilakantan and A. Singh, *Homotopy Type of Neighborhood Complexes of Kneser Graphs, \(\mathrm{KG}_{2,k}\)*, arXiv:1802.05848v1, 2018-02-16. https://arxiv.org/abs/1802.05848
2. C. Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688v1, 2010-03-29. https://arxiv.org/abs/1003.5688
3. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, 2012-10-10. https://arxiv.org/abs/1210.2803
4. J. Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, SIAM J. Discrete Math. 19 (2005), DOI:10.1137/S0895480104443680.
