# Integral Second Homology of the Chang and Triangular Graph Independence Complexes

## Finding

Write \(T_8=L(K_8)\) for the triangular graph on the \(28\) unordered pairs from \([8]=\{0,1,\ldots,7\}\). Its three Chang switchings are specified below. For every graph \(G\) in this complete strongly regular parameter class \((28,12,6,4)\), write \(I(G)\) for its ordinary simplicial independence complex, with a simplex for each independent vertex set. The integral second reduced homology groups are

\[
\begin{array}{c|c|c}
G & f_3(I(G)) & \widetilde H_2(I(G);\mathbb Z)\\ \hline
T_8 & 105 & \mathbb Z^{132}\\
\text{Chang, matching switch} & 73 & \mathbb Z^{164}\\
\text{Chang, eight-cycle switch} & 65 & \mathbb Z^{172}\\
\text{Chang, three-plus-five switch} & 65 & \mathbb Z^{172}
\end{array}
\]

For all four complexes, \(\widetilde H_3(I(G);\mathbb Z)=0\) and \(\widetilde H_1(I(G);\mathbb Q)=0\). Thus integral second homology distinguishes the triangular graph and the matching-switched Chang graph from the other two Chang graphs, despite all four graphs having the same strongly regular parameters and adjacency spectrum. The equality of the last two homology groups is not an assertion that those two graphs are isomorphic.

## Assumptions and scope

The vertex set of every graph is \(V=\binom{[8]}2\). For distinct \(a,b\in V\), let \(a\sim_{T_8}b\) mean \(a\cap b\neq\varnothing\). Given a switching set \(S\subseteq V\), define \(G_S\) by toggling exactly those adjacencies for which precisely one of \(a,b\) belongs to \(S\). The four switches are:

\[
\begin{aligned}
S_0&=\varnothing,\\
S_M&=\{01,23,45,67\},\\
S_C&=\{01,12,23,34,45,56,67,07\},\\
S_{3+5}&=\{01,12,02,34,45,56,67,37\},
\end{aligned}
\]

where \(ij\) denotes the unordered pair \(\{i,j\}\). The three nonempty choices are precisely the classical Chang switching constructions: a perfect matching, an eight-cycle, and the disjoint union of a triangle and a five-cycle in \(K_8\). The claimed topological invariant is ordinary integral simplicial homology of these **finite** independence complexes. Neither arbitrary cospectral graphs nor arbitrary strongly regular parameter classes are covered.

## Proof

**1. Parameter and face counts.** Every displayed switching produces a graph with \(28\) vertices, vertex degree \(12\), exactly \(6\) common neighbors of an adjacent pair and \(4\) of a nonadjacent pair. These finite identities are checked directly from the exact adjacency formula by the included standard-library checker. Equivalently, the complementary graph has parameters \((28,15,6,10)\). Consequently the independence complex has \(f_0=28\), \(f_1=\binom{28}{2}-168=210\), and \(f_2=210\cdot6/3=420\). The independent-set enumeration described below checks that there are no independent five-subsets, and that the numbers of independent four-subsets are respectively \(105,73,65,65\). Thus the complexes have dimension three, with the stated four values of \(f_3\).

**2. The second boundary has maximal possible rank over the rationals.** The one-skeleton of each independence complex is the complementary strongly regular graph of positive degree and positive nonneighbor common-neighbor parameter, hence is connected. For the integral simplicial chain complex, \(\operatorname{rank}_{\mathbb Q}(\partial_1)=27\), so \(\operatorname{rank}_{\mathbb Q}(\partial_2)\le210-27=183\). The exact bitset Gaussian elimination in `CHANG_CHECK.py` calculates \(\operatorname{rank}_{\mathbb F_2}(\partial_2)=183\) in all four cases. Any integer matrix has rank over \(\mathbb Q\) at least its rank over \(\mathbb F_2\). Therefore \(\operatorname{rank}_{\mathbb Q}(\partial_2)=183\), with no approximation or inference from a mere numerical sample.

**3. The third boundary is split injective integrally.** For each of the four graphs, exhaustive enumeration verifies that every independent triple lies in at most one independent quadruple. In a given oriented tetrahedral simplex, select one of its triangular facets. That facet is not a face of any other tetrahedron, so its coefficient in the oriented boundary of that tetrahedron is a unit \(+1\) or \(-1\) and its coefficient in every other tetrahedral boundary is zero. These distinct unit rows show that \(\partial_3:C_3\to C_2\) is a split injection of free abelian groups of rank \(f_3\). It follows that \(H_3=0\) and that \(C_2/\operatorname{im}\partial_3\) is torsion-free.

**4. The integral second homology is free.** Because \(\partial_2\partial_3=0\), there is an injective homomorphism
\[
H_2=\ker\partial_2/\operatorname{im}\partial_3\hookrightarrow C_2/\operatorname{im}\partial_3.
\]
The codomain is a free abelian group by Step 3, and every subgroup of a free abelian group is free. The rank is obtained from Steps 1–3:
\[
\operatorname{rank} H_2=420-183-f_3=237-f_3,
\]
which gives \(132,164,172,172\). The rational first homology has dimension \((210-27)-183=0\). No claim about possible torsion in integral first homology is needed.

## Verification

The included `CHANG_CHECK.py` is a deterministic exact enumerator and finite-field linear-algebra verifier using only the Python standard library. Running `python3 CHANG_CHECK.py` reproduces `CHANG_CHECK_OUTPUT.txt`. It constructs each adjacency matrix from the switching sets, checks the complete strongly regular parameters, enumerates every independent face, checks the absence of independent five-subsets and the one-extension-per-independent-triple property, calculates the exact mod-two rank of the triangle boundary, and checks both chain identities. All four resulting face vectors, ranks, and homology ranks are displayed in the output. A separate direct enumeration of all \(\binom{28}{4}\) and \(\binom{28}{5}\) subsets independently reproduced the four tetrahedron counts and the absence of five-element independent sets.

## Relationship to prior work

Classical matching-complex work, including Shareshian and Wachs (2004 preprint), already studies \(I(T_8)=M_8\) and establishes tools for its low-degree homology. The value \(132\) for \(T_8\) is included as a **known comparator**, not claimed as a new calculation. Barmak (2010) studies general independence-complex topology but does not give the three Chang calculations. The classical Chang graph description establishes that precisely three nonisomorphic switched graphs join \(T_8\) in the complete strongly regular parameter class. A related published calculation distinguishes the independence complexes of the Shrikhande and four-by-four rook graphs for different parameters \((16,6,2,2)\); that does not imply the present values for \((28,12,6,4)\). Searches for aliases, switched-triangular-graph terminology, and the exact homology ranks found no covering statement in the checked sources. This is not an exhaustive guarantee of novelty.

## Limitations

The theorem concerns only these four finite graphs, and it determines their integral homology in degree two, not their full homotopy types or integral first-homology torsion. The two cycle-switched Chang graphs have identical second homology, so this invariant does not distinguish all graph isomorphism types. The calculation depends on finite exhaustive enumeration of at most \(28\) vertices and on a transparent exact rank certificate; it does not use finite evidence to assert an infinite generalization. Some older original graph-classification sources were accessible through faithful secondary descriptions rather than original full texts. Independent audit or validation has not been performed.

## References

1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first publicly posted 2004-09-03; Sections 1, 4, and 9. https://arxiv.org/abs/math/0409054
2. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first publicly posted 2010-07-02; introduction and preliminary definitions. https://arxiv.org/abs/1007.0418
3. Eric W. Weisstein, *Chang Graphs*, MathWorld; the complete description of the three switching sets and the strongly regular spectrum. https://mathworld.wolfram.com/ChangGraphs.html
4. L.-C. Chang, *The Uniqueness and Non-Uniqueness of the Triangular Association Scheme*, *Science Record (Peking)* 3 (1959), 604–613. Bibliographic and scope information verified via MathWorld; the original full text was not inspected.
5. *Independence complexes of the Shrikhande and four-by-four rook graphs have different sphere-wedge homotopy types*, published research summary in the published-finding corpus public index, 2026-10-11; different strongly regular parameter class and no direct implication for Chang graphs. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187
