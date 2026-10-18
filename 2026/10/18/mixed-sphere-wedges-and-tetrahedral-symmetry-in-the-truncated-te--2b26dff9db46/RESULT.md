# Mixed sphere wedges and tetrahedral symmetry in the truncated-tetrahedron two-independence complex

## Finding

Let \(T\) be the graph obtained by truncating all four vertices of a tetrahedron. Its vertices are the ordered pairs \((u,v)\) with \(u,v\in\{0,1,2,3\}\), \(u\ne v\); distinct pairs \((u,v)\) and \((w,z)\) are adjacent when \(u=w\), or when \((w,z)=(v,u)\). For the simplicial complex \(X=\operatorname{Ind}_2(T)\) of vertex subsets whose induced connected components each have at most two vertices,

\[
X\simeq\bigvee^3 S^3\ \vee\ \bigvee^3 S^4.
\]

The homotopy equivalence is integral, not merely a rational or mod-two homology calculation. Moreover, every graph automorphism is induced by a permutation of the four original tetrahedron vertices, so \(\operatorname{Aut}(T)\cong S_4\). With \(S^\lambda\) denoting the rational irreducible Specht representation of partition \(\lambda\),

\[
\widetilde H_3(X;\mathbb Q)\cong \operatorname{sgn}\oplus S^{(2,2)},
\qquad
\widetilde H_4(X;\mathbb Q)\cong S^{(2,1,1)}.
\]

In particular, all reduced integral homology outside degrees three and four vanishes, the two nonzero ranks are each three, and all integral homology is torsion-free. One degree-three rational class is invariant under the rotational subgroup \(A_4\), whereas no nonzero reduced rational class is invariant under all of \(S_4\).

## Assumptions and scope

The graph \(T\) is finite, simple, cubic, connected, and has exactly twelve vertices and eighteen edges. This is the ordinary graph-theoretic skeleton of the Archimedean truncated tetrahedron, not the tetrahedron itself or its face triangulation. The complex contains the empty face as usual; the finite face-poset matching omits it, retaining an explicit critical vertex. The condition defining \(\operatorname{Ind}_2(T)\) is equivalent to requiring maximum degree at most one in every induced subgraph on a selected vertex set. This equivalence holds because any connected graph on at least three vertices contains a path of two incident edges.

The full simplicial complex has maximal face size six, hence dimension five. All chain orientations below use increasing order in the fixed lexicographic vertex list \((0,1),(0,2),(0,3),(1,0),(1,2),(1,3),(2,0),(2,1),(2,3),(3,0),(3,1),(3,2)\). A hexadecimal mask encodes a subset with bit \(i\) standing for vertex \(i\). The result is only for this explicitly specified graph and complex; it asserts no extension to arbitrary truncated polyhedra or arbitrary higher-independence parameters.

## Proof

**Step 1: exhaustive finite face set.** A vertex subset is a face if and only if each selected vertex has at most one selected neighbor. Testing every one of the \(2^{12}\) bitmasks gives exactly \(863\) nonempty simplices, with face counts by dimension zero through five equal to \((12,66,192,303,228,62)\). These numbers and the graph definition are regenerated independently from the declared edge rule by the enclosed verifier.

**Step 2: acyclic face-poset matching.** Process the vertices in the fixed index order \((1,7,10,0,6,11,4,5,2,8,9,3)\). For each chosen vertex \(v\), pair each currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) when both are currently unmatched faces. This gives \(428\) disjoint pairs. The verifier constructs every Hasse covering relation \(\tau\lessdot\sigma\), directing unmatched covers from the lower face to the upper, but reversing matched covers. There are exactly \(3432\) such covers, and a topological sort visits all \(863\) nodes, proving acyclicity, without a sample-based inference. The seven critical cells are one vertex with mask `002`, three three-simplices with masks `254`, `8e0`, `909`, and three four-simplices with masks `368`, `925`, `a51`. These are all the critical cells.

**Step 3: exact integral Morse differentials.** Orient each nonempty simplex by its increasing vertex indices, so that removal of its \(j\)-th vertex contributes coefficient \((-1)^j\). For a simplex \(\alpha\), recursively define its algebraic-Morse projection \(P(\alpha)\): a critical cell projects to itself, a matched upper cell to zero, and a matched lower cell \(\alpha\) with matched upper cell \(\beta\) projects to

\[
P(\alpha)=-\epsilon(\beta,\alpha)
\sum_{\substack{\delta\lessdot\beta\\\delta\ne\alpha}}
\epsilon(\beta,\delta)P(\delta),
\]

where \(\epsilon(\beta,\delta)\in\{+1,-1\}\) is the ordinary signed incidence coefficient. The recursion terminates by acyclicity. The integral Morse boundary of every critical simplex \(\kappa\) is \(P(\partial\kappa)\). Direct integer evaluation gives the zero matrix \(\partial_4:\mathbb Z^3\to\mathbb Z^3\); all other potentially nonzero Morse boundaries vanish for dimensional reasons. The included executable computes all the relevant signed coefficients exactly rather than relying on floating-point approximations.

**Step 4: promotion from homology to homotopy.** Discrete Morse theory supplies a CW homotopy model with exactly one zero-cell, three three-cells and three four-cells. There are no one- or two-cells, hence the three-skeleton is \(\bigvee^3S^3\). Its third Hurewicz map \(\pi_3\to H_3\) is an isomorphism, so the attaching homotopy class of each four-cell is determined by its degree vector in \(\mathbb Z^3\). Step 3 shows all three degree vectors are zero. Each attaching map is therefore nullhomotopic, and the CW model is precisely homotopy equivalent to \(\bigvee^3 S^3\vee\bigvee^3 S^4\).

**Step 5: symmetry representation.** The four triangles \(\{(u,v):v\ne u\}\) are exactly the three-cycles of \(T\), so any automorphism permutes them. The vertex \((u,v)\) is characterized inside triangle \(u\) by having its unique exterior neighbor in triangle \(v\). Thus every automorphism is induced by exactly one element of \(S_4\), and every permutation indeed defines an automorphism. To evaluate the homology action, the verifier constructs for each critical cell \(\kappa\) an integral simplicial cycle \(z_\kappa=\kappa-H(\partial\kappa)\) using the explicit gradient lifting operator \(H\). It checks \(\partial z_\kappa=0\) and \(P(z_\kappa)=\kappa\). For each of the twenty-four vertex permutations \(g\), the exact integer matrix in this cycle basis is obtained by applying the signed simplicial action to \(z_\kappa\) and then \(P\). These matrices satisfy all \(24^2\) group-composition laws separately in degrees three and four. Their traces on permutation cycle types, ordered as \((1^4),(2,1^2),(2^2),(3,1),(4)\), are

\[
\chi_3=(3,-1,3,0,-1),\qquad
\chi_4=(3,-1,-1,0,1).
\]

Comparison with the standard rational character table of \(S_4\) gives \(\chi_3=\chi_{\rm sgn}+\chi_{(2,2)}\) and \(\chi_4=\chi_{(2,1,1)}\), proving the displayed representation decompositions.

## Verification

Run `python3 verify.py` using the Python standard library. It independently enumerates every possible vertex subset, generates the full directed Hasse graph, performs the topological sort, evaluates signed integral Morse projection and cycle lifts, and computes the action of each of the twenty-four graph symmetries. It checks the group law on all \(1152\) degree-specific ordered pairs of group elements and the signed simplicial Lefschetz identity for all twenty-four elements. As a separate mod-two check, it row-reduces all ordinary simplicial boundary operators; their nonzero ranks in degrees one through five are \((11,55,137,163,62)\), giving Betti numbers \((1,0,0,3,3,0)\). The exact reference output is included as `verify_output.json`. The finite exhaustive calculation is a proof for the specified finite graph; no infinite-family conclusion is inferred from it.

## Relationship to prior work

Sawant's May 24, 2026 manuscript identifies three-vertex-path-free complexes with two-independence complexes and proves vertex decomposability for trees, not for this cubic graph with triangles [1]. Deshpande and Singh classify higher-independence homotopy for complete multipartite graphs, whiskered families, paths, cycles and perfect-ary trees [2]; their theorem hypotheses do not cover the truncated-tetrahedral graph. The graph itself and its tetrahedral symmetry are classical [3]. Public mathematical findings on the **same graph** treating the ordinary edge matching complex, cut complexes, graph-metric Rips complexes, and intrinsic Čech complexes are about different simplicial constructions, with no established implication giving this vertex-based two-independence homotopy or the two degree-separated representations [4]. The terms *dissociation complex*, *three-path-free complex*, and *induced maximum-degree-one complex* were also compared. This is a best-knowledge novelty assessment, not a guarantee that no unindexed equivalent result exists.

## Limitations

This is a standalone exact finite classification, not a general theorem about all Archimedean graphs or all graph truncations. The rational symmetry decomposition does not assert a particular integral Specht-lattice splitting. The self-review are exhaustive for the specified finite complex and the explicitly given \(S_4\)-action, but no independent audit is claimed. Unindexed earlier work and inaccessible full texts remain bibliographic risks.

## References

1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted May 24, 2026. https://arxiv.org/abs/2605.25150
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448. https://arxiv.org/abs/2001.05448
3. E. W. Weisstein, *Truncated Tetrahedral Graph*, MathWorld. https://mathworld.wolfram.com/TruncatedTetrahedralGraph.html
4. Public mathematical finding record: *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83 (search summary inspected; full text was inaccessible during comparison).
