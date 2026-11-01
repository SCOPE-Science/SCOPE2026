# Regular rational automorphism representation in the Heawood graph magnitude homology

## Finding

Let \(H\) be the Heawood graph, the bipartite point–line incidence graph of the Fano projective plane, with its shortest-path metric. Let \(A=\operatorname{Aut}(H)\), of order \(336\), act by permuting graph vertices. This induces an action on the magnitude chain complex by permuting all positions of each ordered tuple. The complete rational representation in magnitude bidegree \((3,4)\) is
\[
\boxed{\operatorname{MH}_{3,4}(H;\mathbb Q)\cong\mathbb Q[A].}
\]
More explicitly, its character is \(336\) at the identity and \(0\) at every nonidentity automorphism. The full-group fixed subspace is one-dimensional; the fixed subspace of the order-\(168\) collineation subgroup is two-dimensional. As an additional integral calculation, \(\operatorname{MH}_{3,4}(H;\mathbb Z)\) is free of rank \(336\). The new conclusion is the **full equivariant representation**, not the already-known numerical homology rank.

## Assumptions and scope

Identify the seven points of the Fano plane with the nonzero vectors \(p\in\mathbb F_2^3\) and its seven lines with the nonzero normals \(a\in\mathbb F_2^3\). Incidence means \(a\cdot p=0\). Thus \(H\) has \(14\) vertices and \(21\) edges, is bipartite of girth \(6\) and diameter \(3\), and every pair of vertices at graph distance \(2\) has a unique intermediate vertex.

For an integer length \(\ell\) and degree \(k\), magnitude chains \(\operatorname{MC}_{k,\ell}(H;\mathbb Z)\) are free on ordered \((k+1)\)-tuples \((v_0,\ldots,v_k)\) of vertices with each consecutive pair distinct and \(\sum_i d(v_{i-1},v_i)=\ell\). An internal vertex is deleted with coefficient \((-1)^i\) only when the deletion preserves the total length. Automorphisms permute tuple entries without simplicial orientation signs. No statement about other bidegrees or other graph families is intended.

## Proof

**Integral chain structure.** Enumerating possible distance compositions gives
\[
\operatorname{rank}C_2=840,\quad\operatorname{rank}C_3=2268,\quad\operatorname{rank}C_4=1134,
\]
where \(C_k=\operatorname{MC}_{k,4}(H;\mathbb Z)\). Chain groups outside degrees \(2\) through \(4\) are zero in total length four. Every nonzero term in the boundary of a four-chain \((v_0,v_1,v_2,v_3,v_4)\) comes from replacing a two-edge geodesic by its distance-two step. Such a step has a **unique** intermediate vertex because \(H\) has girth six. A three-chain of length four contains precisely one distance-two step. Consequently two distinct four-chains never share a basis three-chain in their nonzero boundaries, and every nonzero boundary column contains a coefficient \(+1\) or \(-1\). The boundary of a four-chain vanishes exactly when it reverses direction at each of the three interior positions, namely it is \((u,v,u,v,u)\) for an ordered adjacent pair \((u,v)\). There are exactly \(42\) such chains. It follows that \(\operatorname{rank}\partial_4=1134-42=1092\), and its image is a primitive direct summand of \(C_3\). Its kernel is the integral permutation module on the \(42\) ordered edges.

The map \(\partial_3:C_3\rightarrow C_2\) is surjective **over the integers**, as follows. Write a basis two-chain as \((s,x,t)\). If \(s=t\), then \(d(s,x)=2\); let \(a\) be the unique common neighbor of \(s,x\). The four-tuple \((s,x,a,s)\) has boundary \(\pm(s,x,s)\). If \(s\ne t\), these endpoints belong to the same bipartition class and have distance two. For \(x\) in the opposite class, the distances are \((1,3)\) or \((3,1)\); respectively \((s,x,s,t)\) and \((s,t,x,t)\) provide the desired two-chain as a single nonzero boundary term. For \(x\) in the same class, the distances are \((2,2)\). Let \(a\) be the unique common neighbor of \(s,x\). The chain \((s,a,x,t)\) maps to \(\pm(s,x,t)\), possibly together with \((s,a,t)\), which belongs to the already-generated \((1,3)\) class. These exhaust all basis two-chains and prove integral surjectivity. Hence
\[
\operatorname{MH}_{3,4}(H;\mathbb Z)\cong\mathbb Z^{2268-840-1092}=\mathbb Z^{336}.
\]

**Character computation.** For \(g\in A\), each \(C_k\) is a permutation module on ordered tuples, with character equal to the number of tuples fixed positionwise. The exact chain sequences and the preceding description of \(\ker\partial_4\) give
\[
\chi_{\operatorname{MH}_{3,4}}(g)=\#C_3^g-\#C_2^g-\#C_4^g+\#\mathrm{FixEdge}(g).
\]
Every graph automorphism is either one of the \(168\) collineations \(p\mapsto Mp,\ a\mapsto(M^{-1})^Ta\) for \(M\in\mathrm{GL}(3,\mathbb F_2)\), or a collineation composed with the point–line swap \(p\leftrightarrow a\) (defined using the chosen self-duality). The latter \(168\) automorphisms fix no graph vertex, giving trace zero. The collineations split by order into groups of sizes \(1,21,56,42,48\) for orders \(1,2,3,4,7\), respectively. The identity gives \(2268-840-1134+42=336\). An involution fixes a double-star induced subgraph on six vertices, with fixed counts \((\#C_2^g,\#C_3^g,\#C_4^g,\#\text{ordered edges})=(40,116,86,10)\) and trace zero. An element of order three fixes two nonadjacent vertices, giving no fixed chains; one of order four fixes two adjacent vertices, giving \((0,0,2,2)\) and trace zero. An element of order seven fixes no vertices. These exhaust all \(336\) elements.

The character is therefore precisely the regular character. Because finite-dimensional \(\mathbb Q[A]\)-modules are semisimple and their complex characters determine their rational isomorphism classes, the asserted rational regular-module equivalence follows. Restricting the regular representation to an index-two subgroup produces two regular copies, giving the fixed-space dimensions.

## Verification

The self-contained Python program `verify_fano_magnitude_regular.py` builds the Fano incidence graph by binary dot products and all graph distances, enumerates the exact three relevant chain groups, constructs their signed boundaries, verifies \(\partial_3\partial_4=0\), and verifies that the nonzero four-boundary columns have disjoint supports and that precisely the \(42\) alternating directed-edge walks have zero boundary. An independent mod-two elimination computes \(\operatorname{rank}\partial_3=840\); the integral surjectivity argument above supplies the stronger needed statement. The program enumerates all \(336\) automorphisms (including dualities), calculates each complete fixed-chain trace, and verifies the regular character. Its recorded stdout is in `verify_fano_magnitude_regular.out`, terminating `FANO_MAGNITUDE_REGULAR_CHARACTER_OK`.

## Relationship to prior work

Asao–Hiraoka–Kanazawa establish girth-based vanishing thresholds for off-diagonal magnitude homology. The Heawood graph sits at a nonvanishing girth-six boundary rather than inside their vanishing range. Gu studies graph magnitude homology using algebraic discrete Morse methods. Two directly relevant prior results already calculate the nonequivariant information: the published Heawood case determines the mod-two rank \(336\), and the finite-projective-plane theorem determines all same-type ordered-endpoint ranks over arbitrary fields, implying the same scalar rank in the Fano case. **Neither prior statement determines the action of the complete group of \(336\) graph automorphisms, or the resulting invariant subspace.** Comparisons explicitly distinguish the present representation theorem from the previously known underlying dimension, including formulations via Fano-plane dualities and \(\mathrm{GL}(3,2)\).

## Limitations

The theorem concerns only magnitude bidegree \((3,4)\) on the fourteen-vertex Heawood graph. It is a rational **module** classification; no integral regular-lattice identification is asserted. No higher bidegrees, other plane orders or general representation-stability theorem are covered. The negative literature comparison is limited to the inspected and searchable record; equivalent unindexed work is possible. Independent verification outside the supplied proof and reproducible computation has not been performed.

## References

1. Y. Asao, Y. Hiraoka and S. Kanazawa, *Girth, magnitude homology, and phase transition of diagonality*, arXiv:2101.09044v1 (2021), https://arxiv.org/abs/2101.09044v1.
2. Y. Gu, *Graph magnitude homology via algebraic Morse theory*, arXiv:1809.07240v1 (2018), https://arxiv.org/abs/1809.07240v1.
3. *Endpoint-localized first off-diagonal magnitude homology of finite projective planes*, published research record (2026), https://raw.githubusercontent.com/Resultary/2026/main/2026/10/4/SCOPE-endpoint-localized-first-off-diagonal-magnitude-homology-of-fini--f51b07cd11f1/RESULT.md.
4. *The first off-diagonal magnitude homology of the Heawood graph has mod-2 rank 336*, published research record (2026), https://raw.githubusercontent.com/Resultary/2026/main/2026/10/4/SCOPE-the-first-off-diagonal-magnitude-homology-of-the-heawood-graph-h--6b25a5b68b42/RESULT.md.
