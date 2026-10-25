# Integral symmetry lattices of total two-cut complexes over clique–tree products

## Finding

Let \(m\ge 2\) be an integer and let \(T\) be any finite tree with \(t\ge 2\) vertices. Put \(G=K_m\square T\), \(N=mt\), and \(K=\Delta^t_2(G)\), the **total two-cut complex**: a subset of \(V(G)\) is a face precisely when its complement contains two nonadjacent vertices of \(G\). This agrees with the convention that facets are complements of independent pairs.

Let \(\Gamma=S_m\times\operatorname{Aut}(T)\) act on \(K\) by permuting the clique coordinate and the tree coordinate. Define \(U_m=\mathbb Z^{[m]}/\mathbb Z(1,\ldots,1)\), with the coordinate-permutation action. Let \(P_T=\mathbb Z[E(T)]\) be the integral edge-permutation lattice. The connected tree has a bipartition, unique up to swapping its colors; define \(\chi_T(a)=1\) when \(a\) preserves these colors and \(\chi_T(a)=-1\) when it interchanges them. Define the one-dimensional character
\[
\varepsilon(\sigma,a)=\operatorname{sgn}(\sigma)^t\operatorname{sgn}(a)^m,
\]
where \(\operatorname{sgn}(a)\) is the sign of the permutation of \(V(T)\).

**Theorem.** All reduced integral homology of \(K\) vanishes except in degree \(N-4\), and there is a natural \(\Gamma\)-module isomorphism
\[
\widetilde H_{N-4}(K;\mathbb Z)\cong
 (\varepsilon\otimes\chi_T)\otimes U_m\otimes P_T.
\]
In particular, this group is free of rank \((m-1)(t-1)\). For every \((\sigma,a)\in\Gamma\), its rational character is
\[
\operatorname{tr}((\sigma,a)\mid\widetilde H_{N-4}(K;\mathbb Q))
=\operatorname{sgn}(\sigma)^t\operatorname{sgn}(a)^m\chi_T(a)
 (|\operatorname{Fix}_{[m]}(\sigma)|-1)
 |\operatorname{Fix}_{E(T)}(a)|.
\]

The natural equivariant extension
\[
0\longrightarrow (\varepsilon\otimes\chi_T)\otimes P_T
\longrightarrow (\varepsilon\otimes\chi_T)\otimes\mathbb Z^{[m]}\otimes P_T
\longrightarrow\widetilde H_{N-4}(K;\mathbb Z)\longrightarrow0
\]
is **nonsplit as an extension of integral \(\Gamma\)-modules** and has **exact order \(m\)** in the corresponding first extension group. After tensoring with \(\mathbb Q\), it splits. Thus the integral equivariant obstruction is unbounded as the clique size grows, although the ordinary homology groups are torsion-free.

## Assumptions and scope

Graphs are finite and simple, and \(T\) is connected and acyclic. The clique size \(m\) and tree order \(t\) are arbitrary integers at least two. The group action is the specified natural product action, not necessarily the full automorphism group of \(G\). We use simplicial homology with integral coefficients and ordinary cellular cohomology of a finite multigraph. All tensor products of free abelian lattices are over \(\mathbb Z\). When \(N=4\), the relevant reduced homology is in degree zero; this boundary case is included.

The cohomological quotient lattice \(U_m\) is distinct, in general, from the integral root lattice \(\{(z_1,\ldots,z_m):\sum z_i=0\}\): their canonical inclusion has index \(m\). This distinction is essential for the integral extension statement. No global homotopy equivalence or canonical sphere basis for the full class of branching trees is claimed.

## Proof

**1. The dual clique complex.** Let \(L=\operatorname{Cl}(G)\) denote the flag complex of the graph \(G\). By the independent-pair definition, \(K\) is the combinatorial Alexander dual \(L^*\) on the full set of \(N\) vertices. For each \(v\in V(T)\), the \(m\) vertices \((i,v)\) span a simplex. Besides these simplices, \(L\) has precisely the edges \((i,u)(i,v)\) for every \(uv\in E(T)\) and \(i\in[m]\); no higher simplex uses two tree coordinates, because \(T\) is a tree and the Cartesian adjacency constraints preclude a mixed triangle.

Collapse each of the disjoint column simplices to one vertex. This gives a natural equivariant homology identification between \(L\) and the one-dimensional CW multigraph \(Q\) whose vertices are \(V(T)\), with \(m\) parallel, color-labelled edges over each tree edge. More explicitly, the long exact sequence of the pair \((L,\bigsqcup_v\Delta_v)\) gives the same degree-one cohomology group as the relative one-skeleton; the cochain description below is canonical and avoids requiring an equivariant simplicial collapse.

**2. The integral cochain quotient.** Choose the tree bipartition and orient every edge from its first color to its second. Then
\[
C^0(Q;\mathbb Z)=\mathbb Z^{V(T)},\qquad
C^1(Q;\mathbb Z)=\bigoplus_{e\in E(T)}\mathbb Z^{[m]},
\]
and \(\delta(z)\) has over an edge \(u\to v\) the constant-vector component \((z_v-z_u)(1,\ldots,1)\). The incidence map \(\mathbb Z^{V(T)}\to\mathbb Z^{E(T)}\) is surjective **over the integers**, because \(T\) is a tree: assign a root potential and solve each edge difference successively. Consequently,
\[
H^1(L;\mathbb Z)\cong H^1(Q;\mathbb Z)
\cong\bigoplus_{e\in E(T)}
 \bigl(\mathbb Z^{[m]}/\mathbb Z(1,\ldots,1)\bigr)
\cong U_m\otimes P_T.
\]
Every coordinate permutation \(\sigma\) permutes the color basis of each \(\mathbb Z^{[m]}\); each automorphism \(a\) permutes the tree edges and multiplies **every** oriented edge by the common sign \(\chi_T(a)\), since it either preserves or exchanges the bipartition. Thus the displayed identification is \(\Gamma\)-equivariant after twisting by \(\chi_T\). Since \(Q\) is connected and one-dimensional, its other reduced integral cohomology vanishes.

**3. Equivariant Alexander duality.** For a complex \(L\) on an ordered \(N\)-element vertex set, the complement-of-face chain map gives, with its usual orientation signs,
\[
\widetilde H_i(L^*;\mathbb Z)
\cong\operatorname{sgn}_{V(G)}\otimes
\widetilde H^{N-i-3}(L;\mathbb Z).
\]
This is an integral isomorphism compatible with all permutations of the ambient vertices; the sign character occurs because an odd permutation reverses their volume orientation. In the present product action, \(\operatorname{sgn}_{V(G)}(\sigma,a)=\operatorname{sgn}(\sigma)^t\operatorname{sgn}(a)^m=\varepsilon(\sigma,a)\). Taking \(N-i-3=1\), so \(i=N-4\), proves the homology assertion and its stated natural action. Taking traces of the three factors proves the character formula; \(\operatorname{tr}(\sigma\mid U_m)=|\operatorname{Fix}_{[m]}(\sigma)|-1\).

**4. Exact integral extension order.** The coordinate permutation lattice gives a \(S_m\)-equivariant exact sequence
\[
0\to\mathbb Z\xrightarrow{\,1\mapsto(1,\ldots,1)\,}\mathbb Z^{[m]}\to U_m\to0.
\]
Apply \(\operatorname{Hom}_{\mathbb Z[S_m]}(-,\mathbb Z)\) and its right-derived functor. Both \(\operatorname{Hom}_{S_m}(\mathbb Z^{[m]},\mathbb Z)\) and \(\operatorname{Hom}_{S_m}(\mathbb Z,\mathbb Z)\) are \(\mathbb Z\), and restriction from the first to the second is multiplication by \(m\). The connecting morphism therefore sends \(1\) to an extension class of **exact additive order \(m\)**.

A constructive upper-bound certificate, also valid equivariantly after tensoring with \(P_T\) and twisting by \(\varepsilon\chi_T\), is the well-defined \(S_m\)-equivariant map
\[
s:U_m\longrightarrow\mathbb Z^{[m]},\qquad
s([z])=mz-\Bigl(\sum_i z_i\Bigr)(1,\ldots,1).
\]
Its composition with the quotient \(\mathbb Z^{[m]}\to U_m\) is \(m\) times the identity, which shows that multiplying the extension class by \(m\) kills it. To see that no smaller positive multiple kills the full \(\Gamma\)-extension, restrict to the row-permutation subgroup \(S_m\), undo its invertible sign twist, and project onto any fixed tree-edge direct summand. One recovers the single-edge class just shown to have order \(m\). The extension is therefore nonsplit and has exact order \(m\) for every \(m\ge2\). Averaging gives a rational splitting.

## Verification

The accompanying standalone verifier `tree_cut_verify.py` enumerates the complete total two-cut face sets for ten examples, including branching and path trees and clique sizes two, three and four. It computes the signed simplicial Lefschetz number for every element of the prescribed natural symmetry group and checks all \(192\) cases against the character formula. For the cases with at most nine graph vertices, it also computes the exact reduced simplicial Betti numbers over \(\mathbb F_2\) using boundary-matrix elimination. All checks passed.

These finite checks independently test signs, the exceptional degree-zero case, and low-dimensional ranks. They do not establish the assertions for arbitrary \(m\) and \(T\); the preceding integral cochain and extension proofs do that. The verifier needs only Python 3's standard library and is invoked with `python3 tree_cut_verify.py`.

## Relationship to prior work

Chauhan–Shukla–Vinayak (first available 2025-12-04, arXiv:2512.04486), Theorem 1.4, proves the nonequivariant wedge-of-spheres homotopy type of the total two-cut complex for **path** products \(K_m\square P_n\), yielding the same Betti number when \(T=P_n\). That theorem does not specify integral \(S_m\times\operatorname{Aut}(T)\)-modules, a nonsplit lattice extension, or arbitrary branching trees. The present result does not assert a new sphere-wedge theorem for paths.

The 2026 work of Carnero Bravo (arXiv:2602.21427) develops total cuts and Alexander duals, including Cartesian products of paths and of complete graphs, but its described results do not identify the integral symmetry lattice for products with arbitrary trees. The cut-complex homology representation literature, notably Bayer–Denker–Jelić Milutinović–Sundaram–Xue (arXiv:2407.08158), treats other graph families and group actions. The equivariant Alexander-duality method itself is standard; what is singled out here is the explicit integral tree-edge/weight-lattice module and its exact unbounded nonsplitting obstruction.

## Limitations

The result is an integral homology and module statement, not a homotopy classification of every branching example. Its extension is torsion **in a category of equivariant extensions**, not torsion in the underlying homology abelian groups. The natural group \(S_m\times\operatorname{Aut}(T)\) can be smaller than the graph's full automorphism group. The originality comparison covers the inspected primary results and relevant indexed scientific descriptions but cannot exclude equivalent unindexed work; no third-party mathematical audit or independent validation has been performed.

## References

1. P. Chauhan, S. Shukla, K. Vinayak, *Total \(2\)-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486 (first publicly posted 2025-12-04), especially Theorem 1.4 and Section 3.2. https://arxiv.org/abs/2512.04486
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first publicly posted 2026-02-24), Sections 2–5. https://arxiv.org/abs/2602.21427
3. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (first publicly posted 2024-07-11), Section 6. https://arxiv.org/abs/2407.08158
4. M. Bayer et al., *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first publicly posted 2022-09-27), for the original total-cut and Alexander-duality framework. https://arxiv.org/abs/2209.13503
