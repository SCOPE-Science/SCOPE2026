# Directed Hamiltonian cycles form an integral basis for top multipath homology

## Finding

Let \(D=(V,A)\) be any finite loopless simple directed graph with \(n=|V|\ge3\). A multipath is a collection of pairwise vertex-disjoint directed simple paths, including isolated vertices. Let \(X(D)\) be the abstract simplicial complex on the arc set \(A\), whose simplices are arc sets constituting multipaths. Write \(\mathcal H(D)\) for the directed spanning Hamiltonian cycles, identified up to cyclic rotation but **not** identified with their oppositely oriented cycles.

For each \(C\in\mathcal H(D)\), orient its arc set using any ordering and let \(z_C\) be the simplicial boundary of the formal simplex on all its \(n\) arcs. Every proper subset of a directed simple cycle forms a multipath; hence \(z_C\in\widetilde C_{n-2}(X(D);\mathbb Z)\), even though that formal \((n-1)\)-simplex does not belong to \(X(D)\). Then

\[
\widetilde H_{n-2}(X(D);\mathbb Z)
 =\bigoplus_{C\in\mathcal H(D)}\mathbb Z[z_C]
 \cong\mathbb Z^{|\mathcal H(D)|}.
\]

In particular, the top reduced homology is nonzero precisely when the digraph has a directed Hamiltonian cycle. For any automorphism subgroup \(G\le\mathrm{Aut}(D)\), the integral top-homology module is the signed permutation module on directed Hamiltonian cycles:

\[
\widetilde H_{n-2}(X(D);\mathbb Z)
\cong_{\mathbb Z[G]}
\bigoplus_{\mathcal O\in\mathcal H(D)/G}
\operatorname{Ind}_{G_C}^G\epsilon_C,
\]

where \(C\) represents orbit \(\mathcal O\), \(G_C\) fixes \(C\) as an unoriented set of **directed arcs**, and \(\epsilon_C(g)\) is the sign of its permutation of the \(n\) arcs. If \(g\) rotates the directed arc positions by \(r\), then \(\epsilon_C(g)=(-1)^{r(n-1)}\).

As a concrete noncomplete example, let \(W_m=C_m*K_1\) be the undirected wheel with \(m\ge4\) rim vertices and one hub, and let \(\overleftrightarrow{W_m}\) replace every edge by both arcs. There are exactly \(2m\) directed Hamiltonian cycles. Their natural dihedral \(D_m\)-action is free and transitive, giving

\[
\widetilde H_{m-1}(X(\overleftrightarrow{W_m});\mathbb Z)
\cong_{\mathbb Z[D_m]}\mathbb Z[D_m].
\]

## Assumptions and scope

A directed simple path uses pairwise distinct vertices, and a single arc is a path of length one. The input digraph has neither loops nor parallel arcs, but it may contain both opposite arcs on an edge, directed cycles, disconnected components and isolated vertices. The top degree \(n-2\) is the *possible* maximal dimension: a multipath has at most \(n-1\) arcs. If no such simplices exist, both sides of the theorem are zero. Reduced integral simplicial chains use the standard alternating-sign boundary. The notation \(\mathcal H(D)\) counts directed cycles, so the two orientations of an undirected Hamiltonian cycle contribute separately when present.

## Proof

**1. Top faces and ridge completions.** An arc set of cardinality \(n-1\) which is a multipath must consist of one directed Hamiltonian path: for a spanning collection of \(c\) disjoint directed paths, the number of arcs is \(n-c\). Any \(n-2\)-arc multipath similarly comprises precisely two vertex-disjoint directed paths, of which one may be a singleton. Call such an \((n-3)\)-simplex a *ridge*. It can be completed to a Hamiltonian path by joining the terminal vertex of the first path to the initial vertex of the second, or by joining in the reverse order. There are at most two such extensions, and no others.

**2. A ridge with two extensions belongs to exactly one Hamiltonian cycle.** Write the two directed components as \(P\) and \(Q\). The two possible joins are \(t(P)\to s(Q)\) and \(t(Q)\to s(P)\). If both arcs exist, their union with \(P\cup Q\) is a directed Hamiltonian cycle \(C\). Conversely, removing either one of those two joins from \(C\) produces exactly the two Hamiltonian-path extensions of that ridge. This proves that every ridge has exactly one incident top face or two incident top faces belonging to the **same** unique directed Hamiltonian cycle.

**3. The integral top-boundary kernel.** Each Hamiltonian path \(P\) has a unique possible closing arc, from its terminal vertex to its initial vertex. If the arc exists, \(P\) belongs to the unique directed Hamiltonian cycle \(C=P\cup\{t(P)\to s(P)\}\); otherwise \(P\) belongs to none. For the latter case, every ridge of \(P\) has just one top-face extension: a second extension would produce the missing closing arc by Step 2. Thus a top chain with zero boundary has coefficient zero on every path with no closing arc.

The remaining top faces split into disjoint blocks indexed by \(C\in\mathcal H(D)\). Each block consists of the \(n\) facets obtained by deleting one arc from \(C\), and by Step 2 no ridge joins two different blocks. Within one block, the boundary equations at the ridges are the simplicial boundary equations for the entire boundary sphere of the formal \((n-1)\)-simplex with vertex set \(A(C)\): every \((n-2)\)-subset of \(A(C)\) occurs in precisely two of its \((n-1)\)-subsets. Its kernel over \(\mathbb Z\) is exactly the rank-one lattice spanned by the alternating boundary \(z_C\). One can see the rank-one assertion directly by fixing one top-facet coefficient; the equations force every other coefficient with alternating sign, and the resulting coefficient vector is \(z_C\). The top boundary kernel is therefore the direct sum of these rank-one lattices, integrally and without divisibility issues.

**4. Passing to homology.** No multipath contains \(n\) arcs, so \(\widetilde C_{n-1}(X(D);\mathbb Z)=0\). The top boundary kernel is therefore already \(\widetilde H_{n-2}\), giving the asserted basis and Hamiltonicity criterion. This reasoning does not infer a universal theorem from sampled computations.

**5. Symmetry.** An automorphism of \(D\) takes \(z_C\) to the alternating boundary of the corresponding arc permutation of \(C\); thus \(g z_C=\operatorname{sgn}(g|_{A(C)})z_{gC}\) with orientations chosen consistently. The stabilizer of a directed Hamiltonian cycle acts on its arcs by rotations, with sign \((-1)^{r(n-1)}\). Orbit-by-orbit this is the indicated induced sign character over \(\mathbb Z\).

**6. Wheels.** A Hamiltonian cycle in \(\overleftrightarrow{W_m}\) enters and leaves the hub once. Deleting the hub gives a spanning path of the rim \(C_m\), obtained by omitting exactly one of its \(m\) rim edges. The omitted edge and one of the two traversal orientations determine the cycle, giving \(2m\) possibilities. The dihedral symmetries of the rim act freely and transitively on these choices: a symmetry preserving an oriented Hamiltonian cycle would fix the hub and be a cyclic rotation of the directed Hamiltonian cycle, but the unique hub among its vertices must then be fixed, forcing the identity. Hence the stabilizer is trivial and the integral signed permutation module is the regular module \(\mathbb Z[D_m]\).

## Verification

The supplied dependency-free Python program `verify_hamiltonian_top.py` reconstructs the integer signed cycle boundaries, all relevant Hamiltonian-path ridges, the full top boundary matrix over \(\mathbb F_2\), and the wheel dihedral action. It checks all loopless simple digraphs on three and four labeled vertices (64 and 4,096 cases), deterministic random examples on five and six vertices (100 each), four bidirected wheels, the bidirected \(K_{3,3}\), and integral cycle-sign behavior for the complete bidirected four-vertex graph. The finite checks support the theorem but are not a substitute for the all-graph argument in the Proof section. Execution output is recorded in `verification_output.txt`.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith introduced the graph-theoretic multipath-complex homotopy framework and computed selected graph families in their publicly posted 2022 work [1]. Vrećica and Živaljević studied the cycle-free chessboard complexes of complete digraphs and more general cycle-free directed structures, proving connectivity results [2]. A later bidirected-polygon study computes complete homology for that special graph family [3]. The present result determines only the **possible highest** integral homology, but does so simultaneously for *all* finite simple digraphs and with their automorphism actions; it does not claim the earlier full homology computations as new. The complete bidirected-graph case is a specialization, not the claimed advance. A bibliographic search found no explicit general Hamiltonian-cycle top-basis theorem, but this is not proof of novelty or an independent literature certification.

## Limitations

The theorem gives no lower-dimensional integral homology, general homotopy type, or efficient algorithm to evaluate the top rank. The equivalence between Hamiltonicity and top-homology nonvanishing is structural; directly forming the full simplicial chain complex can be exponentially costly. The wheel application is limited to \(m\ge4\) so that the rim is a chordless cycle with a distinguished hub. Unindexed or implicitly equivalent literature may exist. All finite computations are corroborative, not a proof of the all-digraph statement. No independent audit has been performed.

## References

[1] L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first public preprint 2022-08-09), https://arxiv.org/abs/2208.04656.

[2] S. T. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252 (2007), https://arxiv.org/abs/0710.5252.

[3] L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (2026), https://arxiv.org/abs/2601.05670.
