# Three five-spheres and irreducible octahedral symmetry for the cube two-matching complex

## Finding
Let \(Q_3\) have vertex set \(\{0,1\}^3\), with edges joining Hamming-distance-one vertices. Let \(M_2(Q_3)\) be its two-matching simplicial complex: vertices are the twelve edges of \(Q_3\), and a face is a set of edges for which each cube vertex has selected degree at most two. Then
\[
|M_2(Q_3)|\simeq S^5\vee S^5\vee S^5.
\]
Its only nonzero reduced integral homology group is \(\widetilde H_5(M_2(Q_3);\mathbb Z)\cong\mathbb Z^3\).

The full cube automorphism group is naturally \(\operatorname{Aut}(Q_3)\cong S_4\times C_2\). Here, identify the cube with the crown graph \(K_{4,4}\) minus the four diagonal edges, with even-parity cube vertices labeled as rows, antipodal odd-parity vertices as corresponding columns; the first factor permutes rows and columns simultaneously, and the second interchanges them. If \((\pi,t)\in S_4\times C_2\), with \(t\in\{0,1\}\), then the rational fifth-homology character is
\[
\chi_5(\pi,t)=(-1)^t\operatorname{sgn}(\pi)(\#\operatorname{Fix}(\pi)-1).
\]
Consequently, as a rational representation,
\[
\widetilde H_5(M_2(Q_3);\mathbb Q)\cong S^{(2,1,1)}\boxtimes\varepsilon,
\]
where \(S^{(2,1,1)}\) is the sign-twisted standard irreducible representation of \(S_4\), and \(\varepsilon\) is the nontrivial character of the row-column interchange factor. In particular, the three-dimensional homology representation is irreducible, interchange acts as minus the identity, and there is no nonzero invariant rational homology class.

## Assumptions and scope
All complexes are finite abstract simplicial complexes, and all homotopy assertions concern their ordinary geometric realizations. The two-matching complex is a bounded-degree complex with capacity two, not the ordinary matching complex with capacity one. Reduced homology is over the indicated coefficients. The cube graph is not filled in by square faces. The same complex is \(\mathrm{CF}_3(L(Q_3))\), the triangle-free vertex-set complex of the cuboctahedral line graph, because \(Q_3\) is triangle-free and its line graph's triangles are exactly the eight three-edge stars.

## Proof
**Finite simplicial model.** Number the cube vertices by binary integers from zero through seven, and order its twelve edges lexicographically as the pairs \((u,v)\), \(u<v\), with binary Hamming distance one. Encode each nonempty edge subset by a twelve-bit mask. It is a face precisely when all eight selected vertex degrees are at most two. The reproducible verifier enumerates all masks, checking this definition independently against avoidance of the eight three-edge stars. Both descriptions yield exactly 1698 nonempty faces, with face vector
\[
(f_0,\ldots,f_7)=(12,66,212,423,516,352,108,9).
\]
There are 49 inclusion-maximal faces, of dimensions five (four facets), six (36 facets), and seven (nine facets).

**Acyclic matching and integral homotopy.** Visit the twelve edge indices in decreasing order. At each index, among all currently unmatched nonempty faces, pair a face not containing the index with its one-index extension whenever both remain unmatched. This gives exactly 847 disjoint pairs, leaving one critical vertex and three critical five-simplices. Independently construct every codimension-one incidence among the 1698 nonempty faces: there are 7980. Orient every unmatched incidence from the larger to the smaller face, and reverse precisely the 847 matched incidences. A complete topological sort visits all 1698 vertices, so the resulting Hasse digraph is acyclic. The matching is therefore an acyclic discrete-Morse matching. Its Morse CW model has exactly one zero-cell, three five-cells, and no other cells. Every attaching map \(S^4\to\{*\}\) is nullhomotopic, proving the integral homotopy equivalence displayed above. This is a finite certificate, not an inference from numerical Betti numbers.

**Full automorphism representation.** The eight cube vertices split into four even and four odd vertices. Each even vertex is adjacent to all odd vertices except its antipode. These four omitted pairs provide the crown-graph row-column labeling. Thus every automorphism is either simultaneous row/column permutation \(\pi\in S_4\) or its composition with row-column interchange; there are 48 such automorphisms. The induced action permutes the twelve simplex vertices (cube edges). For each of the 48 automorphisms \(g\), the verifier directly evaluates the signed reduced simplicial Lefschetz number
\[
\widetilde L(g)=\sum_{\substack{\emptyset\ne F\in M_2(Q_3)\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(g|_F)-1.
\]
Because the only nonzero reduced rational homology is in degree five, \(\chi_5(g)=-\widetilde L(g)\). Exact evaluation for all 48 group elements gives the stated formula. As a separate consistency check, an independent signed-coordinate description \(g(v)=\sigma(v)\oplus b\), with \(\sigma\in S_3\) and \(b\in\{0,1\}^3\), yields
\[
\chi_5(g)=\operatorname{sgn}(\sigma)
\sum_{i:\sigma(i)=i}(-1)^{b_i}.
\]
These two complete character evaluations agree element by element. The standard \(S_4\)-module has character \(\#\operatorname{Fix}(\pi)-1\); tensoring by \(\operatorname{sgn}\) gives \(S^{(2,1,1)}\), and the interchange sign gives \(\varepsilon\). The standard representation is irreducible over \(\mathbb Q\), and character twisting preserves irreducibility. The full character's average is zero, so the invariant subspace is zero.

## Verification
The standalone file `verify.py` requires Python 3.10 or later and no external packages. Run `python verify.py` from the directory containing that file. It independently reconstructs the face set and the forbidden-star model, checks the exact face vector, all matching pairs, every Hasse incidence and global acyclicity, and directly sums signed traces for both descriptions of all 48 automorphisms. Successful execution prints five `VERIFY_OK` lines. The certificate specifies the complete finite algorithms and their deterministic edge order; no auxiliary data files are needed.

## Relationship to prior work
Vega introduced the two-matching-complex framework and proved homotopy results for clawed graphs, wheels and caterpillars; those theorems do not give this cubic cube/crown graph result. Singh's higher-matching results treat complete graphs and complete bipartite graphs; the crown graph omits a perfect matching and is neither. Ghosh and Selvaraja's recent study establishes shellability conditions for clique-free complexes of suitable chordal graphs; the cuboctahedral line graph contains induced square cycles and those conditions do not determine its homotopy or symmetry representation. The same objects can be described as capacity-two rook placements on the four-by-four board with its diagonal excluded, an equivalence included in the comparison rather than used to evade prior results. A published computation for the full \(K_{4,4}\) two-matching complex gives a different object and does not imply the result after diagonal deletion.

## Limitations
This theorem is specific to the three-dimensional cube (equivalently, the four-by-four crown graph). It neither proves a classification for all hypercubes or crown graphs nor identifies a canonical integral lattice model of the group action. The rational character determines a rational representation, not its integral module structure. Non-shellability is not asserted. The result is supported by exhaustive finite computation and standard discrete Morse and Lefschetz theory, and has not received independent external mathematical verification.

## References
1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, first posted 2019-09-23, v2 2021-01-28; especially the introduction and Sections 3–6.
2. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 2020-06-24; Theorems 1.1–1.2.
3. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first posted 2026-02-10; especially Theorem 3.3 and its scope.
