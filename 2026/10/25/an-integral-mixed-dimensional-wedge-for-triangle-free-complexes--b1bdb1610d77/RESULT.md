# An integral mixed-dimensional wedge for triangle-free complexes of edge-glued cliques

## Finding
For every pair of integers \(a,b\ge2\), let \(G_{a,b}\) be the graph obtained by identifying one edge of \(K_{a+2}\) with one edge of \(K_{b+2}\), retaining the common edge and identifying no further vertices or edges. Let \(\mathsf{CF}_3(G_{a,b})\) be its simplicial complex of vertex subsets containing no graph-theoretic triangle. Then there is an integral homotopy equivalence
\[
\mathsf{CF}_3(G_{a,b})\simeq
S^1\vee\bigvee^{2(a-1)(b-1)}S^2\vee
\bigvee^{\binom{a-1}{2}\binom{b-1}{2}}S^3.
\]
A wedge with zero summands is omitted. In particular, the complex has one persistent integral first-homology generator and simultaneous nonzero second- and third-homology groups when \(a,b\ge3\).

## Assumptions and scope
Write the common vertices as \(u,v\), and the private vertices of the two cliques as disjoint sets \(A,B\), with \(|A|=a\) and \(|B|=b\). Every pair within \(A\cup\{u,v\}\) is an edge, every pair within \(B\cup\{u,v\}\) is an edge, and there are no edges between \(A\) and \(B\). A face of \(\mathsf{CF}_3\) is a subset of vertices that contains no three pairwise adjacent vertices. This is a *clique-free complex*, not the ordinary clique or independence complex. Homotopy and homology are integral; \(\simeq\) denotes homotopy equivalence of geometric realizations. All formulas hold for every finite integer pair in the stated range, with no limiting or generic-position assumption.

## Proof
**Step 1: Exact face decomposition.** Put \(F_A=\operatorname{skel}_1(\Delta^A)\) and \(F_B=\operatorname{skel}_1(\Delta^B)\), the full one-skeleta of the respective simplices; define \(X=F_A*F_B\). A face not using \(u,v\) chooses at most two private vertices from each clique, so belongs exactly to \(X\). Define \(L=\operatorname{skel}_0(\Delta^A)*\operatorname{skel}_0(\Delta^B)\). A face using exactly one of \(u,v\) may select at most one member of each private set, and therefore lies in the corresponding cone over \(L\). No face using both \(u,v\) can contain any private vertex, since that would give a forbidden triangle. Consequently, *as abstract simplicial complexes*,
\[
\mathsf{CF}_3(G_{a,b}) = X\cup(u*L)\cup(v*L)\cup\{u,v\},
\]
where \(\{u,v\}\) in the final union means the closed one-simplex with its faces. The intersection of each cone with \(X\) is exactly \(L\); the two cones intersect precisely in \(L\), and the last edge meets their union only at its endpoints.

**Step 2: Both cone attachments split.** For \(a,b\ge2\), both \(F_A\) and \(F_B\) are nonempty connected graphs, hence their join \(X\) is simply connected (indeed, at least two-connected by the join-connectivity inequality). Meanwhile \(L\) is the connected one-dimensional complete bipartite graph \(K_{a,b}\). Every map from a connected one-dimensional CW complex to a simply connected CW complex is nullhomotopic: choose a spanning tree and contract it, then use nullhomotopy of each remaining loop. Therefore the simplicial inclusion \(L\hookrightarrow X\) is nullhomotopic. As the inclusion is a cofibration, its mapping cone \(X\cup_L(u*L)\) is homotopy equivalent to \(X\vee\Sigma L\). The attaching map for the second cone \(v*L\) factors through \(L\hookrightarrow X\) and is still nullhomotopic in the first mapping cone. A second application gives
\[
Y:=X\cup(u*L)\cup(v*L)\simeq X\vee\Sigma L\vee\Sigma L.
\]
All these spaces are connected. Attaching the final one-cell with distinct endpoints \(u,v\) in the connected space \(Y\) contributes one free circle: equivalently, contract a chosen path between the endpoints in the homotopy pushout of the boundary of an interval. Thus \(\mathsf{CF}_3(G_{a,b})\simeq X\vee\Sigma L\vee\Sigma L\vee S^1\).

**Step 3: Compute the constituent homotopy types.** The complete graph regarded as a one-dimensional CW complex has cycle rank \(\binom{a-1}{2}\), so \(F_A\simeq\bigvee^{\binom{a-1}{2}}S^1\), and likewise for \(F_B\). The join identity \(P*Q\simeq\Sigma(P\wedge Q)\) for connected based CW complexes yields
\[
X\simeq\bigvee^{\binom{a-1}{2}\binom{b-1}{2}}S^3.
\]
The connected graph \(L=K_{a,b}\) has \(ab\) edges and \(a+b\) vertices, hence first Betti rank \((a-1)(b-1)\), giving
\[
\Sigma L\simeq\bigvee^{(a-1)(b-1)}S^2.
\]
Combining the last two displays with Step 2 establishes the asserted equivalence integrally, including cases with zero third-sphere multiplicity. No finite-computation assumption enters this proof.

## Verification
A standalone program `verify_clique_glue.py` independently builds all edges of each glued graph, enumerates the triangles from its adjacency relation, enumerates every face avoiding them, and computes the full augmented mod-two boundary ranks. It separately derives the exact face-count polynomial by the decomposition in Step 1, namely
\[
\bigl(1+az+\tbinom a2z^2\bigr)\bigl(1+bz+\tbinom b2z^2\bigr)
+2z(1+az)(1+bz)+z^2.
\]
For every \(2\le a,b\le6\) (25 parameter pairs), the program found the predicted face counts and complete reduced Betti vectors, enumerating 4,875 faces including the empty face in each complex; its recorded output ends in `VERIFY_OK`. These finite tests corroborate the theorem but cannot prove the universal integral homotopy statement; the proof above supplies that argument. Reproduce with `python3 verify_clique_glue.py 6` using the included script and standard Python 3 only.

## Relationship to prior work
Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623v1, publicly posted 2026-02-10), define the same \(t\)-clique-free complexes. Their Theorem 3.3 addresses shellability for \(t\)-diamond-free chordal graphs, while Theorem 4.2 treats attachment of a clique at *one* vertex, and Example 3.6 supplies a different graph. Here the two maximal cliques meet in a full *edge*: selecting one private vertex from each clique together with the shared edge produces a diamond, so their diamond-free hypothesis fails, and the attachment operation is not the same. Moreover none of those assertions specifies this integral mixed-dimensional homotopy type. This claim is an explicit calculation for the natural first non-block intersection size, not a claim about all chordal graphs or arbitrary clique-sums.

## Limitations
Only \(t=3\) and exactly two cliques meeting in one retained edge are covered. The theorem does not classify more cliques, arbitrary intersection sizes, general shellability, or equivariant group actions. It makes no claim that the general splitting method for joins and cones is itself novel. An equivalent result could occur in an unindexed paper on independence complexes of 3-uniform clique hypergraphs; known-result checks reduce but cannot eliminate this bibliographic risk. Independent scientific audit has not been performed.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, 2026-02-10, especially Theorems 3.3 and 4.2 and Example 3.6, https://arxiv.org/pdf/2602.09623.
2. Standard CW-complex mapping-cone splitting and join/smash-product identities are used in their classical form; no priority is claimed for these topological tools.
