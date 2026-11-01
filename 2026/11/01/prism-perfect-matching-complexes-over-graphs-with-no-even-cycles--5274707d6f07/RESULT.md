# Prism perfect-matching complexes over graphs with no even cycles

## Finding

Let \(H\) be any finite nonempty simple graph containing **no even simple cycle**, let \(n=|V(H)|\), and form its two-layer Cartesian prism \(P=H\square K_2\). Define \(\mathcal P(P)\) to be the simplicial complex consisting of edge sets of \(P\) extendable to perfect matchings. Then

\[
\mathcal P(H\square K_2)\simeq
\begin{cases}
\mathrm{pt},&H\text{ has no perfect matching},\\
S^{n/2-1},&H\text{ has a perfect matching}.
\end{cases}
\]

The homotopy equivalence follows from an explicit acyclic matching on the augmented face poset with, respectively, zero or one unmatched face. In the second case its sole unmatched face has dimension \(n/2-1\), and the empty face is matched. The class of base graphs includes arbitrary forests and graphs built by joining odd cycles along bridges or articulation vertices; connectivity is not required. For \(n\ge2\) when \(H\) has a perfect matching, the prism complex is pure of dimension \(n-1\) but has reduced integral homology in degree \(n/2-1\), hence is not shellable.

## Assumptions and scope

Graphs are finite, simple, undirected and loopless. The base graph \(H\) has at least one vertex and no even *simple* cycle; distinct components and isolated vertices are permitted. The Cartesian prism has a top copy and a bottom copy of each base vertex, a top and bottom horizontal edge corresponding to each \(e\in E(H)\), and a vertical rung \(r_v\) above each \(v\in V(H)\). Denote the horizontal lifts by \(u_e\) and \(\ell_e\). The empty face is included in the augmented face poset, while homotopy types refer to the usual geometric realization. A perfect matching covers every graph vertex exactly once. A matching is a set of pairwise vertex-disjoint edges.

For a face \(\sigma\) define its *horizontal projection* \(J(\sigma)=\{e\in E(H):u_e\in\sigma\text{ or }\ell_e\in\sigma\}\). Fix an arbitrary total order on the base vertices and edges to specify pivots.

## Proof

**1. Unique matching on every induced subgraph.** Any two distinct perfect matchings on a graph differ in a disjoint union of even alternating simple cycles, obtained by taking their symmetric difference. Since \(H\) has no even simple cycle, every induced subgraph of \(H\) has at most one perfect matching.

**2. Classification of prism facets.** In any perfect matching \(Q\) of \(P\), let \(R\subseteq V(H)\) be the set of vertices whose vertical rungs belong to \(Q\). Both horizontal layers on the complement \(V(H)\setminus R\) must be perfectly matched. By Step 1, their projected perfect matchings coincide; write that common matching as \(M\). Conversely any matching \(M\) of \(H\) determines a prism perfect matching

\[
Q(M)=\{u_e,\ell_e:e\in M\}\cup\{r_v:v\in V(H)\setminus V(M)\}.
\]

Thus \(Q\mapsto M\) is a bijection between perfect matchings of \(P\) and arbitrary matchings of \(H\). In particular \(P\) always has a perfect matching, even if \(H\) does not. A subset \(\sigma\) is a face of \(\mathcal P(P)\) if and only if \(J(\sigma)\) is a matching in \(H\) and every rung appearing in \(\sigma\) lies over a vertex outside \(V(J(\sigma))\). Necessity follows from the facet description; sufficiency follows by extending \(\sigma\) to \(Q(J(\sigma))\).

**3. A complete involutive face pairing.** Process each face \(\sigma\), including the empty face, according to its projection \(J=J(\sigma)\).

If \(V(J)\neq V(H)\), choose the least vertex \(v\notin V(J)\). Pair \(\sigma\) with \(\sigma\triangle\{r_v\}\). Both faces have the same projection; either choice of the rung is allowed by Step 2, so this is a well-defined one-element face matching.

If \(V(J)=V(H)\), then \(J\) is a perfect matching of \(H\), and such a matching is unique by Step 1. There are no rungs in \(\sigma\). If \(\sigma\) contains at least one bottom lift, choose the least edge \(e\in J\) whose bottom lift \(\ell_e\) is present, and pair \(\sigma\) with \(\sigma\triangle\{u_e\}\). Again both are faces, the projection and the selected pivot are unchanged, and the pair differs by one vertex. If \(\sigma\) contains no bottom lift, then full projection forces \(\sigma=\{u_e:e\in J\}\). Leave this one face unmatched.

If \(H\) has no perfect matching, the second case never occurs, and **every augmented face is paired**. If \(H\) has a perfect matching on \(n=2m\) vertices, precisely \(\{u_e:e\in J\}\), of size \(m\), remains unmatched.

**4. Acyclicity.** Orient each cover relation of the augmented face poset upward when it is a matched pair and downward otherwise. Along each oriented arrow, the horizontal projection can only lose edges, never gain them: an upward arrow toggles a rung or an upper lift whose lower counterpart is already selected, and a downward arrow removes a vertex of the simplicial face. Thus the projection \(J\) must remain constant on a directed cycle.

Within a fixed nonperfect projection, each horizontal lift present can only be removed along a downward arrow; it cannot be added by any matching arrow. On a hypothetical cycle those horizontal lift sets must therefore also remain fixed. All remaining arrows concern rungs. The pivot \(r_v\) associated to that projection is added only by its matched upward arrows, and its removal is precisely the reversed matched incidence, hence cannot be a downward arrow. Every other rung can only be removed. No nontrivial directed cycle exists in this stratum.

Within the (unique) perfect projection, the set of bottom lifts can only decrease along directed arrows, because matched upward arrows toggle upper lifts only. Thus a cycle would have fixed bottom lifts and hence a fixed least bottom-lift pivot \(\ell_e\). The associated upper lift \(u_e\) can only be added along its matched upward arrow, and it cannot be removed along a downward arrow because that incidence is matched and reversed. Every other upper lift can only be removed. Again no directed cycle exists. This proves global acyclicity, for any size of \(H\).

**5. Homotopy consequence.** By discrete Morse theory on the augmented face poset, a complete matching of all faces—including the empty face—gives a contractible complex. When there is a single unmatched face of dimension \(m-1\) and the empty face is paired with a vertex, the resulting CW model has one basepoint and one \((m-1)\)-cell. For \(m=1\), this is two isolated points, \(S^0\); for \(m\ge2\), the attaching map of the only positive-dimensional cell lands at the basepoint, giving \(S^{m-1}\). The facets of the original complex each contain \(n\) prism edges, so the complex is pure of dimension \(n-1\). A pure shellable complex has reduced homology only in its top dimension (if nonzero); hence the sphere case is nonshellable.

## Verification

Run `python3 checker.py` using only the Python standard library. The program enumerates every labeled base graph on at most five vertices with no even cycle (613 graphs), independently constructs prism perfect matchings and the predicted facet set, enumerates all faces, checks the proposed involutive matching, exhaustively verifies acyclicity of the directed face-poset Hasse diagram, and checks reduced mod-two homology. It also tests seven larger named bases, including a branched tree, a glued pair of triangles, and disconnected edges. In total the exhaustive small cases contain 92,400 augmented faces and 260,989 directed incidences. The code verifies that the even-cycle boundary base \(H=C_4\) instead has reduced mod-two first Betti number four, demonstrating that dropping the hypothesis invalidates the stated dichotomy. This is a boundary example, not a classification of all bases containing even cycles.

The computations corroborate and mechanically stress-test the proof. The infinite-family conclusion rests on Steps 1–5 and not on finite enumeration. `CHECKS.txt` records the output reproduced from the standalone checker.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega introduced and investigated perfect-matching complexes for honeycomb families, with homotopy results for specified tilings [1]. Chandrakar and Singh classified two-row rectangular grid perfect-matching complexes—equivalently prisms over path graphs—and polygonal line tilings [2, Theorem 3.3 and Sections 4–5]. The path-graph cases of the present formula are therefore **already covered** by [2] and are not claimed as new. Agarwal and Basak classified the perfect-matching complexes of circular and Möbius ladders [3, Theorem 25]; the contractible prism-over-odd-cycle cases here are **already covered** by [3].

The new scope is arbitrary even-cycle-free base graphs, notably branching trees, forests, odd-cycle cacti and disconnected unions, together with a uniform explicit acyclic matching that works without path or cyclic symmetry. The pertinent theorem statements, definitions and proofs in [1] and [2], and the revised arXiv HTML text of [3], were compared against this scope; none contains a theorem for every such base or the stated general prism pairing. Index searches found no directly covering record. This does not establish global priority against work not indexed or otherwise unseen.

## Limitations

The no-even-cycle hypothesis is essential to the uniqueness argument. The asserted two-way homotopy classification fails for \(H=C_4\), whose prism perfect-matching complex has reduced first homology of rank four over \(\mathbb F_2\), rather than one. The result does not classify arbitrary prisms, general even-cycle-containing bases, equivariant homotopy types, or the simple-homotopy type of the complexes. The statement about nonshellability uses the standard pure shellability convention. No independent audit has been performed.

## References

1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first posted 2022-09-06), https://arxiv.org/abs/2209.02803.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tiling*, arXiv:2407.05809v1 (first posted 2024-07-08), https://arxiv.org/abs/2407.05809.
3. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (revised 2026-09-14), https://arxiv.org/html/2608.30601v2.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. The use of acyclic matchings is standard discrete Morse theory.
