# The total three-cut complex of the thirteen-vertex Paley graph is \(S^5\)

## Finding

Let \(P_{13}\) be the Paley graph on \(\mathbb F_{13}\), with \(x\sim y\) exactly when \(y-x\) is a nonzero square. Let \(K=\Delta^t_3(P_{13})\) be the **total** three-cut complex: a vertex subset is a simplex of \(K\) precisely when its complement contains three pairwise nonadjacent vertices. Then

\[
K\simeq S^5,\qquad \widetilde H_j(K;\mathbb Z)=
\begin{cases}\mathbb Z,&j=5,\\0,&j\ne5.\end{cases}
\]

The natural affine subgroup \(A=\{x\mapsto ax+b: a\in\{1,3,4,9,10,12\},\ b\in\mathbb F_{13}\}\), of order \(78\), acts on \(\widetilde H_5(K;\mathbb Z)\cong\mathbb Z\) by the character

\[
\chi(a,b)=\begin{cases}+1,&a\in\{1,3,9\},\\-1,&a\in\{4,10,12\}.\end{cases}
\]

Equivalently, \(\chi(a,b)\) is the integer sign represented by \(a^3\pmod{13}\). Translation acts trivially. The complex has twenty-six facets of dimension nine, so the nonzero fifth homology also proves that this pure complex is **not shellable**.

## Assumptions and scope

All graphs are finite and simple. The ground vertices are labeled \(0,1,\ldots,12\); the nonzero squares modulo thirteen are \(Q=\{1,3,4,9,10,12\}\). The simplices here are *not* complements of all disconnected induced triples: that latter definition gives the larger ordinary three-cut complex. No claim is made about other Paley graph orders, arbitrary cut parameters, or an equivariant homotopy equivalence.

## Proof

**Facet characterization.** A triple \(\{u,v,w\}\) is independent if every pair difference avoids \(Q\). There are exactly twenty-six such triples. Their complements are all the facets of \(K\), each of size ten. Enumerating their downward-closed subsets gives \(6,553\) faces including the empty face, with augmented face counts by dimension \(-1\) through nine:

\[
(1,13,78,286,715,1287,1677,1469,780,221,26).
\]

**Complete acyclic matching.** Represent a face by its thirteen-bit indicator. Start with the set of all faces (including the empty one). Successively use the seven vertices

\[
(0,2,4,12,6,3,7).
\]

At stage \(v\), match every *currently unmatched* pair \((\sigma,\sigma\cup\{v\})\) for which \(v\notin\sigma\) and both faces remain, and remove both from further stages. The respective pairing counts are

\[
(3012,153,71,21,9,5,5).
\]

Only the six-vertex face \(\{2,3,4,6,7,12\}\) remains after the seven stages. Discard the pair consisting of the empty face and \(\{0\}\); the matching on nonempty faces then has exactly two critical cells, the vertex \(\{0\}\) and the five-simplex \(\{2,3,4,6,7,12\}\). The supplied exact program verifies that every pair differs by one vertex, that no face is paired twice, and that the full directed face-poset graph—formed by orienting unmatched covers down and matched covers up—is acyclic. This checks all \(39,156\) incidences and all \(6,553\) augmented-face vertices. Removing the empty-face pair does not change this conclusion.

The acyclic-matching theorem of discrete Morse theory therefore supplies a CW model with one zero-cell and one five-cell and no other cells. Its attaching map lands in a point, so the CW model is \(S^5\). This is an **integral homotopy** statement, not a deduction merely from ranks over fields.

**Affine integral character.** For each \(a\in Q\) and \(b\in\mathbb F_{13}\), the affine permutation \(g(x)=ax+b\) preserves adjacency, and hence acts simplicially on \(K\). For every one of these seventy-eight maps, compute its reduced simplicial Lefschetz number by summing \((-1)^{|\sigma|-1}\) times the sign of the permutation of the ordered vertices of each setwise-fixed simplex, including the empty-face term \(-1\). As reduced homology is concentrated in degree five, the induced trace on \(\widetilde H_5\) is the negative of this number. Exhaustive integer evaluation gives trace \(+1\) for multipliers \(1,3,9\) and \(-1\) for \(4,10,12\), independently of translation. Since the integral homology has rank one, these traces completely determine its integral action.

## Verification

Run `python3 verify.py` in the directory containing the files. The program enumerates faces from the adjacency definition, reproduces all seven specified matching stages, validates a full topological sort of the oriented Hasse diagram, computes independent mod-two simplicial boundary ranks, and computes exact signed reduced Lefschetz numbers for all seventy-eight affine maps. The expected output is saved in `verification_output.txt`. The mod-two checks corroborate, but do not replace, the integral discrete-Morse homotopy proof.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced total cut complexes and proved classifications for several families, including chordal graphs, cycles, and complete multipartite examples. The present graph is a nonchordal six-regular Paley graph, not one of those classified graph families. Their companion paper studies the **ordinary** cut complex, which admits more facets for parameter three. The exact sphere type and the signed affine action above do not follow from the cited classifications. The literature comparison does not establish an absolute priority claim against every unindexed source.

## Limitations

This is an exact computation for the natural thirteen-vertex Paley graph, not an all-order Paley theorem. The subgroup \(A\) is specified explicitly; no full graph-automorphism classification is asserted. The action is identified on integral homology, not as an equivariant homotopy decomposition. Independent mathematical audit has not been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first publicly posted 2022-09-27, especially Definitions 2.3, Theorem 7.2, and Sections 4–5. https://arxiv.org/abs/2209.13503
2. The same authors, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted 2023-04-26, for the distinct ordinary cut-complex definition and graph-family results. https://arxiv.org/abs/2304.13675
