# Geometric layer-fixed topology of prism perfect-matching complexes

## Finding

Let \(H\) be **any finite simple graph** with \(n\geq1\) vertices, and write \(P=H\mathbin{\square}K_2\) for its two-layer Cartesian prism. The involution \(\tau\) interchanges the two layers. Denote by \(\mathcal P(P)\) the simplicial complex of partial matchings of \(P\) that extend to perfect matchings, and let \(Y_H=|\mathcal P(P)|^{\langle\tau\rangle}\) be the *geometric* fixed-point subspace (not the complex of vertexwise-fixed simplices). Let \(b(H)\) be the number of perfect matchings of \(H\), including \(b(H)=0\) when no such matching exists.

**Theorem.** The fixed space is PL homeomorphic to the ordinary matching complex of the fully whiskered graph \(W(H)\), obtained by adjoining one distinct pendant leaf to every vertex of \(H\). More precisely, for every finite simple \(H\),

\[
Y_H\simeq\begin{cases}
\ast,&n\text{ odd},\\
\bigvee^{b(H)}S^{m-1},&n=2m\text{ even}.
\end{cases}
\]

A wedge with zero summands means a point. In particular, for even \(n=2m\), the reduced integral homology is free, is supported only in degree \(m-1\), and has rank \(b(H)\).

**Integral naturality.** Every group \(\Gamma\leq\operatorname{Aut}(H)\) acts naturally on \(Y_H\). There is an isomorphism of integral \(\Gamma\)-modules

\[
\widetilde H_{m-1}(Y_H;\mathbb Z)\cong
\bigoplus_{M\in\operatorname{PM}(H)}\mathbb Z\,[M],
\]

where a group element sends an oriented generator \([M]\) to \(\operatorname{sgn}(g|_M)[gM]\). Here \(\operatorname{sgn}(g|_M)\) means the sign of the induced permutation of the ordered *edges* of the perfect matching, relative to independently selected edge orderings for \(M\) and \(gM\). This states the complete integral representation, without requiring a rationalization or an integral splitting.

For \(H=C_{2m}\), \(m\ge2\), the fixed space is a wedge of two \((m-1)\)-spheres. For \(H=C_{2m+1}\), it is contractible. For \(H=K_{m,m}\), it is a wedge of \(m!\) spheres of dimension \(m-1\), including nonouterplanar examples for \(m\ge3\).

## Assumptions and scope

Graphs are finite, undirected, and simple. Every matching complex includes the empty face. The prism has vertex set \(V(H)\times\{0,1\}\), horizontal edges from \(H\) in either layer, and a rung between the two copies of each base vertex. The geometric fixed-point set is taken in the standard affine realization of the simplicial complex, with the layer swap permuting its vertices (which represent prism edges). In the wedge formula \(n=2m\), the integer \(m\) is at least one; the case \(m=1\) uses the usual based zero-sphere convention. The group \(\Gamma\) acts diagonally on both prism layers and commutes with the layer swap.

## Proof

**1. Fixed simplices correspond to whiskered matchings.** Write \(a_v\) for the rung at a vertex \(v\) of \(H\). Each horizontal edge \(uv\in E(H)\) gives a two-element orbit \(e_{uv}\) consisting of its copy in each layer. The rung orbits have one element each. A \(\tau\)-invariant subset of prism edges is a matching exactly when its selected horizontal orbits correspond to pairwise disjoint edges of \(H\) and no selected rung meets an endpoint of those edges. In that case, adjoining every missing rung gives a perfect matching of the prism, so every such invariant partial matching is a face of \(\mathcal P(P)\). Conversely every fixed point in its affine realization has barycentric support a union of full \(\tau\)-orbits, with equal coefficients within each horizontal pair. Replacing a horizontal orbit by its barycenter identifies the geometric fixed space simplicially (and PL homeomorphically) with the complex on vertices \(\{a_v:v\in V(H)\}\cup\{e_{uv}:uv\in E(H)\}\) whose faces obey those matching conditions. This is precisely \(\mathcal M(W(H))\), the matching complex of the fully whiskered base graph.

**2. A contractible rung-star core.** In this orbit complex \(K\), let \(A=\bigcup_{v\in V(H)}\operatorname{st}_K(a_v)\) be the union of the closed simplicial stars of the rung vertices. These are subcomplexes. For every nonempty \(J\subseteq V(H)\),

\[
\bigcap_{v\in J}\operatorname{st}_K(a_v)
=\operatorname{st}_K(\{a_v:v\in J\}),
\]

because all rungs are mutually compatible and their compatibility with a horizontal orbit depends only on whether it meets a vertex in \(J\). The right side is nonempty and contractible (a star with a cone point). The nerve of this finite star cover is the full simplex on \(V(H)\), so the simplicial nerve theorem gives \(A\simeq\ast\). Alternatively, the same conclusion follows from the homotopy colimit of the contractible intersections.

**3. Exactly the perfect-matchings survive outside the core.** Every face containing a rung lies in \(A\). A face using only horizontal orbits lies in \(A\) whenever it leaves some vertex of \(H\) uncovered, since then the corresponding rung can be adjoined. Thus the *only* faces outside \(A\) are the sets of horizontal edges constituting perfect matchings of \(H\). If \(n\) is odd there are none, and \(K=A\) is contractible. If \(n=2m\), every such exceptional face has dimension \(m-1\), its proper faces lie in \(A\), and different exceptional faces intersect only inside \(A\). Consequently

\[
K/A\cong\bigvee_{M\in\operatorname{PM}(H)}S^{m-1}.
\]

Since \(A\) is a nonempty contractible subcomplex of the finite simplicial complex \(K\), the quotient map \(K\to K/A\) is a nonequivariant homotopy equivalence. This proves the homotopy classification also in degree zero.

**4. The integral symmetry action.** The action of \(\Gamma\) permutes rung vertices and preserves \(A\). The relative chain groups \(C_j(K,A;\mathbb Z)\) vanish except in degree \(j=m-1\), where the free basis consists of oriented exceptional simplices, one per perfect matching of \(H\). Hence there are no relative differentials, and the reduced long exact sequence for the contractible nonempty \(A\) yields a natural isomorphism \(\widetilde H_{m-1}(K;\mathbb Z)\cong H_{m-1}(K,A;\mathbb Z)\). Permuting the vertices of an oriented exceptional simplex is exactly the sign of the induced permutation of its ordered matching edges. This supplies the stated natural integral representation.

**5. Named families.** A cycle of odd order has no perfect matching; an even cycle has exactly its two alternating perfect matchings. A complete bipartite graph \(K_{m,m}\) has \(m!\) perfect matchings. Substituting these independent elementary counts proves the examples.

## Verification

The standalone script `verify_fixed_prism.py` constructs the prism and all its perfect matchings for finite named graphs, independently enumerates invariant edge-orbit faces, checks that they coincide with invariant matchings, computes complete mod-two boundary ranks of the fixed complex, and compares signed top-homology character predictions with the simplicial Lefschetz trace of each tested automorphism. Run with `python3 verify_fixed_prism.py`; successful execution ends with `ALL_CHECKS_PASSED`. The checked examples are cycles of lengths three through eight, paths of lengths two through six, complete graphs of orders three through five, and \(K_{3,3}\). These checks are finite corroboration; the proof above is uniform and independent of computation.

## Relationship to prior work

Agarwal and Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs* (arXiv:2608.30601v2, posted September 14, 2026), classify the **nonequivariant** homotopy types of the perfect-matching complexes of circular ladders. Their result is about the entire complex, rather than the geometric layer-swap fixed-point subspace, and does not determine the signed integral representation of base-graph automorphisms. Neither a nonequivariant homotopy classification nor an ordinary Betti-number formula determines geometric fixed points of an involution.

Bayer, Jelić Milutinović, and Vega, *Matching Complexes of Outerplanar Graphs* (arXiv:2411.04601v2; originally publicly posted November 7, 2024), show that the matching complex of any outerplanar graph is contractible or a wedge of spheres. In particular, this is compatible with the whiskered-cycle cases but does **not** provide their exact sphere counts, generalize to arbitrary nonouterplanar base graphs, or state the integral symmetry module. The whiskered-graph identification is explicitly included here because any theorem for matching complexes of fully whiskered graphs could imply part or all of this finding.

The result is not a statement about the fixed-vertex subcomplex alone: it uses the full geometric fixed set, including barycenters of two-edge orbits. Additional relevant literature on matching and perfect-matching complexes was examined by subject and terminology. No claim of exhaustive novelty certification is made.

## Limitations

The theorem concerns a **layer-swap fixed-point space** of the perfect-matching complex of a Cartesian prism, not the homotopy type of the full prism perfect-matching complex. It assumes a simple finite base graph and the canonical two-layer exchange. It determines the nonequivariant fixed-space homotopy type and the induced integral homology representations under automorphisms of the base; it does not determine an equivariant homotopy splitting or interactions with other graph symmetries of the full prism. An equivalent general whiskering formula may exist in unindexed or unexamined literature. Independent mathematical validation has not been performed.

## References

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (September 14, 2026), https://arxiv.org/html/2608.30601v2. Especially Section 5.2.
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2 (September 23, 2026; initial version November 7, 2024), https://arxiv.org/html/2411.04601v2. Especially Theorem 2.
3. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (September 6, 2022), https://arxiv.org/abs/2209.02803 (background).
