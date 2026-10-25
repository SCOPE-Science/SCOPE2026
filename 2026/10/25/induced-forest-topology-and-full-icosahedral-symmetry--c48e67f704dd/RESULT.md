# Induced-forest topology and full icosahedral symmetry

## Finding

Let \(I\) be the twelve-vertex icosahedral graph and let
\[
K=\mathcal F(I)=\{A\subseteq V(I):I[A]\text{ is a forest}\}
\]
be the simplicial complex of cycle-free **induced vertex subsets**. There is an integral homotopy equivalence
\[
K\simeq\bigvee^{40}S^4.
\]
The full graph automorphism group is \(G\cong A_5\times C_2\). If \(V_4\), \(V_5\), and \(V_6\) denote the rational irreducible \(A_5\)-representations of respective dimensions four, five, and six, and \(\varepsilon\) is the nontrivial character of the central antipodal \(C_2\), then
\[
\widetilde H_4(K;\mathbb Q)\cong
(V_4\oplus V_5\oplus V_6)\boxtimes\mathbf1
\;\oplus\;
(2V_4\oplus V_5\oplus 2V_6)\boxtimes\varepsilon.
\]
Here \(V_6\) is the six-dimensional **rational** irreducible whose complexification is the sum of the two Galois-conjugate three-dimensional complex irreducibles. The antipodal eigenspaces have dimensions fifteen and twenty-five, and the antipodal trace is \(-10\). No nonzero rational fourth-homology class is fixed by all icosahedral rotations (hence none by all graph automorphisms).

## Assumptions and scope

The graph is the one-skeleton of the regular icosahedron, a connected five-regular simple graph on twelve vertices with thirty edges and twenty triangular faces. The `EDGES` constant in the standalone `verify.py` gives a complete labeled graph model; the claim is invariant under graph isomorphism. A face is a subset of **graph vertices**, not a collection of graph edges. A subset is admitted exactly when the induced subgraph has no undirected cycle, not merely when some chosen spanning subgraph is acyclic. The empty subset is included as the augmented face of dimension minus one.

The asserted homotopy equivalence is nonequivariant and integral. The representation decomposition is over \(\mathbb Q\), not an integral decomposition of the homology lattice. The group action is induced by permuting graph vertices and orienting simplices by ascending vertex labels.

## Proof

**1. Exhaustive and independently checked face description.** For each of the \(2^{12}=4096\) vertex subsets, `verify.py` tests the induced subgraph for cycles in two ways: union–find on its induced edges and a parent-sensitive depth-first search. Both predicates agree for all subsets. Exactly 984 faces, including the empty face, remain. The nonempty face vector, in dimensions zero through five, is
\[
(12,66,200,345,300,60).
\]
There are exactly sixty maximal faces of cardinality five and sixty of cardinality six. Thus the complex is nonpure, even though its eventual homotopy dimension is four.

**2. Integral homotopy certificate.** Process vertices in increasing order \(0,1,\ldots,11\). At stage \(i\), traverse unmatched masks in increasing numeric order and match \((\sigma,\sigma\cup\{i\})\) whenever both are still unmatched and \(i\notin\sigma\). Each face occurs in at most one pair. The algorithm gives 472 matched pairs and forty unmatched simplices, all of dimension four. In particular, the empty face is paired with vertex zero. Reverse the matched edges of the augmented face-poset Hasse diagram and orient every other covering relation downward. A complete topological sort of all 984 faces and 3,984 covering relations visits every face: there is no directed cycle. Deleting the matched empty-face/vertex pair from the matching preserves acyclicity and makes vertex zero critical. The resulting ordinary discrete-Morse matching has one critical zero-cell and forty critical four-cells, with no other critical cells. Forman's theorem gives a CW model consisting of one point with forty four-cells attached; all attaching maps are constant because there are no positive-dimensional cells below dimension four. This proves \(K\simeq\bigvee^{40}S^4\) over the integers. In particular, the integral homology is torsion-free, concentrated in reduced degree four with rank forty.

**3. Full symmetry and its character.** The generators `ROT5`, `ROT3`, `ANTIPODE` in `verify.py` preserve the edge set. The first two have orders five and three, their product has order two, and they generate sixty permutations; adjoining the central antipode gives 120 distinct permutations. The graph has exactly twenty triangles, every edge belongs to two of them, and the dual triangular adjacency graph is connected. A graph automorphism fixing an oriented triangular flag fixes each triangle by propagation, so the full automorphism group has at most \(12\cdot5\cdot2=120\) elements. Thus the exhibited 120 are all graph automorphisms, with their usual \(A_5\times C_2\) structure.

For every such graph automorphism \(g\), calculate the signed trace on the augmented simplicial chains by enumerating every invariant face. On an invariant nonempty face, the trace contribution is its alternating-dimensional sign multiplied by the sign of the permutation induced on its ordered vertices; the empty face contributes \(-1\). The equivariant Euler–Poincaré identity and the homotopy result identify this alternating trace with the character \(\chi(g)\) on \(\widetilde H_4(K;\mathbb Q)\). For rotations \(r\in A_5\), with classes grouped by element order \(1,2,3,5\), the class sizes are \(1,15,20,24\) and the computed traces are
\[
\chi(r)=(40,-4,1,0),\qquad
\chi(ar)=(-10,2,-1,0),
\]
where \(a\) denotes the central antipode. Both order-five conjugacy classes give the same value. Therefore the antipodally even and odd rational characters on \(A_5\) are respectively
\[
\chi_+=(15,-1,0,0),\qquad \chi_-=(25,-3,1,0).
\]
Compare with the four rational irreducible characters, indexed in the same order:
\[
\begin{array}{c|rrrr}
&1&2&3&5\\
\mathbf1&1&1&1&1\\
V_4&4&0&1&-1\\
V_5&5&1&-1&0\\
V_6&6&-2&0&1
\end{array}
\]
(the complex-character norm of \(V_6\) is two). Exact character inner products yield \(\chi_+=V_4+V_5+V_6\) and \(\chi_-=2V_4+V_5+2V_6\), establishing the displayed decomposition and the absence of an \(A_5\)-invariant line.

## Verification

Run `python3 verify.py` from the directory containing this file. It requires only Python 3 standard-library modules. `verification_output.txt` is the recorded output and ends in `VERIFY_OK`. The verifier reconstructs all 4,096 induced-subgraph decisions, independently compares two cycle tests, checks the complete face vector and maximal-facet distribution, reproduces all matching pairs, topologically sorts every Hasse arrow, and independently computes ordinary boundary-matrix ranks over \(\mathbb F_2\) and \(\mathbb F_3\). In degrees one through five those ranks are \((11,55,145,200,60)\) over each field, giving ordinary Betti numbers \((1,0,0,0,40,0)\). These modular checks are corroboration; the torsion-free integral homotopy conclusion follows from the acyclic discrete-Morse certificate, not from modular ranks.

The same verifier checks the triangular flag bound, generates the 120 graph automorphisms, enumerates every signed Lefschetz trace, and reconstructs the two rational character decompositions.

## Relationship to prior work

Taylan's 2015 preprint introduced the general forbidden-induced-subgraph (“devoid”) complex formalism and matching-tree reductions. Its inspected full text proves specific classifications for paths, cycles, and forests with path-pattern avoidance; these are not a classification of induced acyclic vertex sets in the icosahedral graph. Carnero Bravo's *The Forest Filtration of a Graph* (first submitted in 2023) defines precisely the last-stage induced-forest complex and calculates homotopy for paths, cycles, double stars, cactus graphs, and selected graph products. Its inspected full text does not supply this icosahedral calculation. The present statement is a complete icosahedral homotopy and equivariant refinement, not a relabeling of a graph-edge forest (graphic-matroid) complex. Other icosahedral independence, neighborhood, Rips, matching, and cut complexes do not imply it: their faces obey different conditions.

## Limitations

This is one exact, finite, twelve-vertex graph classification and not a theorem for all polyhedral or vertex-transitive graphs. No equivariant *homotopy* splitting or integral \(A_5\times C_2\)-lattice decomposition is claimed; the representation statement is rational. The proof uses an exhaustive but replayable certificate rather than a compact conceptual classification of all induced-forest complexes. An equivalent result in unindexed or uninspected literature remains possible.

## References

1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1, first submitted 2015-01-27, https://arxiv.org/abs/1501.06754.
2. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first submitted 2023-07-25, https://arxiv.org/abs/2307.13271.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
