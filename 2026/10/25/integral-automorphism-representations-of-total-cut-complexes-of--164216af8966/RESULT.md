# Integral automorphism representations of total cut complexes of clique unions

## Finding
Let \(G=K_{m_1}\sqcup\cdots\sqcup K_{m_c}\) be the disjoint union of nonempty complete graphs, with \(c\ge k\ge3\) and each \(m_i\ge2\). Put \(N=\sum_{i=1}^c m_i\), and let \(X=\Delta_k^t(G)\) be the simplicial complex whose facets are complements of independent \(k\)-subsets of the graph. The full automorphism group \(\Gamma=\operatorname{Aut}(G)\), including permutations of equal-size components and arbitrary permutations inside them, acts on \(X\).

Write \(U_c=\{(a_1,\ldots,a_c)\in\mathbb Z^c:\sum_i a_i=0\}\), with the natural action through the induced component permutation. Let \(\operatorname{sgn}_{V(G)}\) be the one-dimensional integral character given by the parity of an automorphism on the **entire** vertex set. The complete integral homology module is

\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\operatorname{sgn}_{V(G)}\otimes (\bigwedge^{k-1}U_c)^*,&j=N-k-1,\\
0,&j\ne N-k-1.
\end{cases}
\]

The star denotes the integral dual \(\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)\), with contragredient group action. In particular, all homology is torsion-free, and the sole nonzero reduced Betti number equals \(\binom{c-1}{k-1}\). This classification is valid for **unequal component sizes** without modification to the component factor.

The character of an automorphism \(g\), with induced component permutation \(\pi_g\), is

\[
\chi(g)=\operatorname{sgn}_{V(G)}(g)\,[t^{k-1}]\frac{\prod_{L\in\operatorname{cycles}(\pi_g)}(1-(-t)^L)}{1+t},
\]

where the cycle lengths \(L\) are counted with multiplicity. If every component has the same size \(m\), and \(g\) is written in the natural wreath product \(S_m\wr S_c\) as internal permutations \(\sigma_1,\dots,\sigma_c\) followed by a component permutation \(\pi\), the sign factor is \(\prod_i\operatorname{sgn}(\sigma_i)\operatorname{sgn}(\pi)^m\). Thus the component factor is the dual of the hook lattice \(\bigwedge^{k-1}U_c\), and the internal action is its full vertex-permutation sign twist.

As a consequence, the quotient by the **full automorphism group** has no positive-degree reduced rational homology. An internal transposition in any component acts by negative identity on the displayed homology lattice, so that its full-group invariants vanish. The quotient is connected in the stated range, hence is rationally acyclic in reduced homology.

## Assumptions and scope
The graph is finite, simple and is the disjoint union of \(c\) clique components. The cut parameter satisfies \(3\le k\le c\); every block size \(m_i\ge2\). The degree is the reduced simplicial homology degree. We use the convention that permutations act on oriented simplices with their usual induced orientation signs. The assertion is integral and isomorphism-equivariant for every element of \(\Gamma\). No assertion is made for arbitrary chordal graphs or for the ordinary \(k\)-cut complex (which is generally larger when \(k>2\)).

## Proof
**1. Alexander dual in terms of occupied clique components.** Let \(V=V(G)\). The defining facets of \(X\) are the complements of independent \(k\)-element sets. Consequently its combinatorial Alexander dual on the ambient vertex set \(V\) is

\[
Y=X^\vee=\{F\subseteq V:\alpha(G[F])<k\}.
\]

Because each component of \(G\) is complete, an induced subgraph on \(F\) has independence number exactly the number of clique components meeting \(F\). Therefore \(Y\) consists precisely of those faces meeting **at most \(k-1\) components**.

**2. An explicit equivariant strong deformation retraction.** Let \(K\) be the \((k-2)\)-skeleton of the simplex on \(c\) component labels. A point of \(|Y|\) has barycentric coordinates \((x_v)_{v\in V}\) supported in at most \(k-1\) clique components. Define \(r:|Y|\to|K|\) by \(r(x)_i=\sum_{v\in V_i}x_v\). Conversely, denote by \(b_i\) the uniform barycenter of the full simplex on the vertex set \(V_i\), and define \(s:|K|\to|Y|\) by \(s(w)=\sum_iw_i b_i\). This is well-defined because a point of \(K\) uses at most \(k-1\) component labels. Plainly \(r\circ s=\operatorname{id}\). The straight-line homotopy \(H_u(x)=(1-u)x+u s(r(x))\) is contained in the face of \(Y\) on the union of the components meeting \(x\), and is a strong deformation retraction onto \(s(|K|)\). Every graph automorphism permutes the component sets and their uniform barycenters, so \(r,s,H_u\) are all \(\Gamma\)-equivariant. In particular, **all internal vertex permutations act trivially on the homology of \(Y\)**.

**3. The integral skeleton homology as a lattice.** Put \(E=\mathbb Z^c\) with basis indexed by component labels and \(\varepsilon:E\to\mathbb Z\) the all-ones augmentation. The augmented oriented chain complex of the full simplex identifies in degree \(q\) with \(\bigwedge^{q+1}E\), with differential given by contraction by \(\varepsilon\). The skeleton \(K\) is its truncation in degrees at most \(k-2\). Since \(E\cong\mathbb Z e_1\oplus U_c\) and \(\varepsilon(e_1)=1\), contraction restricts to an isomorphism from \(e_1\wedge\bigwedge^{k-2}U_c\) onto \(\bigwedge^{k-2}U_c\), while it vanishes on \(\bigwedge^{k-1}U_c\). Thus

\[
\widetilde H_{k-2}(K;\mathbb Z)=\bigwedge^{k-1}U_c,
\qquad \widetilde H_q(K;\mathbb Z)=0\ \text{for }q\ne k-2.
\]

The identification is natural for component permutations because the contraction is equivariant and its kernel is canonically \(\bigwedge^{k-1}U_c\); the auxiliary basis choice only proves exactness. This group has rank \(\binom{c-1}{k-1}\). Since it is free, the universal coefficient theorem gives \(\widetilde H^{k-2}(Y;\mathbb Z)=(\bigwedge^{k-1}U_c)^*\) and vanishing cohomology outside this degree.

**4. Equivariant combinatorial Alexander duality and signs.** For a simplicial complex on a specified set of \(N\) vertices, combinatorial Alexander duality identifies its reduced homology in degree \(j\) with reduced cohomology of its Alexander dual in degree \(N-j-3\). At chain level, the canonical orientation of the ambient \((N-1)\)-simplex changes by \(\operatorname{sgn}_V(g)\) under a vertex permutation \(g\). Hence, including this orientation character, duality is equivariant as

\[
\widetilde H_j(X;\mathbb Z)\cong
\operatorname{sgn}_{V(G)}\otimes\widetilde H^{N-j-3}(Y;\mathbb Z).
\]

Substituting the degree \(k-2\) established above yields \(j=N-k-1\) and the asserted complete integral module. The integral dual in the formula is necessary: the cohomology action is contragredient to the homology action, and the two natural integral lattices need not be identified arbitrarily.

**5. Character and quotient.** For a permutation \(\pi\) of the \(c\) blocks with cycle lengths \(L\), \(\det(I+t\pi\mid E)=\prod_L(1-(-t)^L)\). Since \(E=\mathbf1\oplus U_c\) as rational representations, the generating polynomial for exterior-power characters of \(U_c\) is this product divided by \(1+t\). Dual representations have equal rational characters for finite groups, which proves the closed character formula. When all block sizes are \(m\), a transposition of blocks has vertex parity \((-1)^m\), establishing the wreath-product specialization.

Every component has at least two vertices, so an internal transposition is an automorphism that acts trivially on \(U_c\) and by minus one on \(\operatorname{sgn}_V\). It therefore acts by negative identity on \(\widetilde H_{N-k-1}(X;\mathbb Q)\); consequently there are no invariants under the full automorphism group. For a finite simplicial group action the rational homology of the orbit space agrees with the invariant rational homology, as can be seen after equivariant subdivision and rational averaging. The claimed quotient vanishing follows. The first nontrivial homology degree satisfies \(N-k-1\ge2\), so the space and its quotient are connected.

## Verification
The included self-contained standard-library Python program `verify.py` implements two checks independent of the deformation-retraction proof. It enumerates vertex automorphisms of eight small cluster graphs and computes their **signed reduced Lefschetz traces** directly from invariant faces. Across 8,672 group-action instances these agree exactly with the closed hook-character formula, including unequal clique sizes, internal transpositions and block exchanges. The same program builds mod-two simplicial boundary maps from graph faces and independently verifies the predicted sole Betti group for five small examples.

To reproduce: run `python verify.py` in a directory containing the extracted file. The expected lines are `CLUSTER_GRAPH_EQUIVARIANT_CHARACTER_VERIFIED 8672` and `CLUSTER_GRAPH_MOD2_HOMOLOGY_VERIFIED 5`. Finite tests do not establish an integral theorem for arbitrary parameters; the preceding deformation retraction and integral duality provide the proof.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue (arXiv:2209.13503, first public September 27, 2022), Theorem 4.13, prove that the total \(k\)-cut complex of a chordal graph with \(c\) components is a wedge of \(\binom{c-1}{k-1}\) spheres of degree \(N-k-1\). Clique unions are a special case of that **nonequivariant theorem**. The new assertion here is not the wedge count; it is the integral module under the full automorphism group, including internal vertex signs, block-permutation hook lattices, and the quotient consequence.

The companion arXiv:2304.13675 concerns the **ordinary** \(k\)-cut complex, distinct from the total cut complex for \(k>2\). The follow-up arXiv:2407.08158, Section 6.1, computes the rational homology representation of the ordinary cut complex of a **two-clique disjoint union**. It does not imply the classification here, which requires \(k\ge3\) and hence at least three clique components, and takes complements of independent transversals rather than arbitrary disconnected induced sets. The coefficient-field distinction is also substantive: the result here specifies the natural integral lattice.

## Limitations
No classification is claimed for graphs whose components are not complete, for \(k=1,2\), or for the ordinary higher-cut complex. The finite verifier checks only small graphs and mod-two homology; it cannot detect every possible torsion phenomenon by computation. Integral torsion-freeness follows from the exact algebraic proof, not from those checks. The originality comparison is made against identified primary sources and indexed records; it does not rule out uncatalogued equivalent work. The result has not undergone an independent mathematical audit.

## References
Bayer, M.; Denker, M.; Jelić Milutinović, M.; Rowlands, R.; Sundaram, S.; Xue, L. *Total Cut Complexes of Graphs.* arXiv:2209.13503 (first public 2022-09-27), especially Definition 2.3 and Theorem 4.13.

Bayer, M.; Denker, M.; Jelić Milutinović, M.; Rowlands, R.; Sundaram, S.; Xue, L. *Topology of Cut Complexes of Graphs.* arXiv:2304.13675 (2023), especially its distinct ordinary-cut-complex definition and equivariant results.

Bayer, M.; Denker, M.; Jelić Milutinović, M.; Sundaram, S.; Xue, L. *Topology of Cut Complexes II.* arXiv:2407.08158 (first public 2024-07-11), especially Section 6.1 on the ordinary cut complex of a two-clique union.
