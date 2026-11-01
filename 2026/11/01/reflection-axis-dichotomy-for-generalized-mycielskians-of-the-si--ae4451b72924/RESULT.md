# Reflection-axis dichotomy for generalized Mycielskians of the six-cycle

## Finding
Let \(C_6\) have labels \(\mathbb Z/6\mathbb Z\), with consecutive labels adjacent, and let \(\mu_\ell(C_6)\) be the generalized \(\ell\)-Mycielskian in the convention of Carnero Bravo (\(\ell\ge1\)). Its vertices are an apex \(w\) and \((j,i)\) for \(1\le j\le\ell+1\) and \(i\in\mathbb Z/6\mathbb Z\). The apex is adjacent to all first-level vertices; successive levels are joined according to adjacency in \(C_6\); the top level contains the cycle edges. Put \(X_\ell=\operatorname{Ind}(\mu_\ell(C_6))\). The two reflection classes of the base hexagon induce simplicial involutions on \(X_\ell\): \(\nu(j,i)=(j,-i)\) (vertex-axis) and \(\epsilon(j,i)=(j,1-i)\) (edge-axis), both fixing \(w\).

**Theorem.** For every integer \(\ell\ge1\), the geometric fixed spaces have the integral homotopy types
\[
|X_\ell|^{\langle\nu\rangle}\simeq *,\qquad
|X_\ell|^{\langle\epsilon\rangle}\simeq
\begin{cases}
*, & \ell=3k+1,\quad k\ge0,\\
\displaystyle\bigvee^{2^{k+1}}S^{2k+1},&\ell=3k+2,\quad k\ge0,\\
\displaystyle\bigvee^{2^k}S^{2k},&\ell=3k,\quad k\ge1.
\end{cases}
\]
In particular the edge-axis fixed space has unbounded, exponentially growing free integral Betti numbers in a single degree, while the vertex-axis fixed space is always contractible. The two spaces are fixed sets in the *geometric realization*, not complexes on individually fixed vertices.

## Assumptions and scope
The graph is the simple undirected six-cycle, with its specified dihedral action on labels on every level, and with the generalized Mycielskian indexing above. The two reflections represent the two conjugacy classes of reflections of \(C_6\). Homotopy equivalences are nonequivariant equivalences of their *individual fixed spaces*. A wedge of zero spheres is not needed in the stated ranges. All homology consequences hold with integral coefficients, including torsion-freeness. This result does not claim equivariant homotopy equivalences of the ambient spaces.

## Proof
**1. Geometric orbit-complex lemma.** Let an involution act simplicially on an independence complex \(\operatorname{Ind}(H)\) of a finite simple graph. An invariant independent set is precisely a union of vertex-orbits which are each internally independent and pairwise have no cross-edge in \(H\). Make a conflict graph with one vertex for every internally independent orbit, and an edge when the original graph has any edge between the two orbits. On each invariant simplex, fixed barycentric coordinates are constant along each orbit. Replacing each constant coordinate by its orbit-sum gives a linear homeomorphism onto the corresponding simplex of the conflict graph's independence complex, with inverse dividing by the orbit size. These maps agree on faces. Hence the entire geometric fixed space is PL homeomorphic to the independence complex of the orbit-conflict graph. This argument includes orbits of size two: keeping only pointwise-fixed vertices would give the wrong space.

**2. The vertex-axis quotient.** The four label-orbits under \(i\mapsto-i\) are \(\{0\},\{1,5\},\{2,4\},\{3\}\), in this order. Every orbit is internally independent, including in the top layer; their conflict graph on the labels is the ordinary path \(P_4\). Cross-level conflicts reproduce the categorical-product edges of \(P_4\), and top-level conflicts reproduce \(P_4\). Consequently the orbit-complex lemma gives a PL homeomorphism
\[
|X_\ell|^{\langle\nu\rangle}\cong_{\mathrm{PL}}|\operatorname{Ind}(\mu_\ell(P_4))|.
\]
The independence complex of \(P_4\) is a contractible three-edge path. Its Kronecker double cover is the disjoint union of two copies of \(P_4\); its independence complex is a join of two contractible complexes and is contractible. Carnero Bravo's Theorem 5 (for simple graphs) then implies \(\operatorname{Ind}(\mu_\ell(P_4))\simeq*\) for all \(\ell\ge1\). The same conclusion follows from the folding decomposition in that theorem. Thus the vertex-axis part is proved.

**3. The edge-axis quotient and its exceptional top layer.** The label-orbits under \(i\mapsto1-i\) are \(b_0=\{0,1\}\), \(b_1=\{2,5\}\), \(b_2=\{3,4\}\). The two endpoint orbits \(b_0,b_2\) contain edges of \(C_6\); the middle orbit does not. At each non-top level all three orbit vertices are allowed, while at the top only \(b_1\) is allowed. The off-diagonal conflicts between adjacent levels are given by the symmetric relation
\[
\mathcal R=\{(0,0),(0,1),(1,0),(1,2),(2,1),(2,2)\}.
\]
It is useful to regard \(\mathcal R\) as the adjacency relation of a three-vertex path with a loop at each endpoint. This *auxiliary* looped relation is only notation: all actual finite graphs used in the proof are simple, since the relation joins vertices in **different** levels. The apex is adjacent to all three vertices of the first level. The top level is the single middle vertex. Denote this simple orbit-conflict graph by \(Y_\ell\), and write \(A_\ell=Y_\ell-w\). Also put \(A_0\) equal to a single vertex, to describe the terminal remainder of the folding. The orbit-complex lemma yields
\[
|X_\ell|^{\langle\epsilon\rangle}\cong_{\mathrm{PL}}|\operatorname{Ind}(Y_\ell)|.
\]
This model is *not* the generalized Mycielskian of an ordinary simple three-vertex path: the two endpoint self-relations would be lost, and the top layer is restricted. The simple-graph hypothesis of the published generalized-Mycielskian theorem therefore does not directly handle this fixed set.

**4. A three-level fold valid at all widths.** Let \(D\) denote the induced simple graph on two consecutive complete non-top layers of \(Y_\ell\), with edges specified by \(\mathcal R\). Number its vertices \((a,j)\), \(a\in\{0,1,2\}\), \(j\in\{0,1\}\). Its edges form exactly one six-cycle, for example
\[
(0,0)-(0,1)-(1,0)-(2,1)-(2,0)-(1,1)-(0,0).
\]
Hence \(D\cong C_6\). For \(\ell\ge3\), the open neighborhood of each \((1,a)\) in \(A_\ell\) consists only of \((2,b)\) with \((a,b)\in\mathcal R\). The neighborhood of \((3,a)\) contains all these vertices and possibly additional fourth-level vertices. Therefore
\[
N_{A_\ell}((1,a))\subseteq N_{A_\ell}((3,a))\qquad(a=0,1,2).
\]
The standard independence-complex fold lemma permits deletion of the three third-level vertices, successively, without changing the homotopy type. Those deletions separate levels \(1,2\), which form \(D\), from levels \(4,\ldots,\ell+1\), which form \(A_{\ell-3}\) after reindexing. Since independence complexes of disjoint unions are joins,
\[
\operatorname{Ind}(A_\ell)\simeq\operatorname{Ind}(D)*\operatorname{Ind}(A_{\ell-3})\qquad(\ell\ge3).
\]
The base graphs are explicit: \(A_0\) is one isolated vertex; \(A_1\) has an isolated middle vertex in the bottom level, hence its independence complex is a cone; and \(A_2\) contains a top middle vertex whose open neighborhood equals that of the bottom middle vertex. Deleting that top vertex folds \(\operatorname{Ind}(A_2)\) onto \(\operatorname{Ind}(D)\). Thus, writing \(T=\operatorname{Ind}(D)\), for all \(k\ge0\),
\[
\operatorname{Ind}(A_{3k})\simeq *,\qquad
\operatorname{Ind}(A_{3k+1})\simeq *,\qquad
\operatorname{Ind}(A_{3k+2})\simeq T^{*(k+1)}.
\]
(The first display at \(k=0\) means the contractible \(\operatorname{Ind}(A_0)\).)

**5. Apex cofiber and integral wedge decomposition.** For each \(\ell\ge1\), deleting the apex and its closed neighborhood yields precisely \(A_{\ell-1}\), up to level relabeling (also for \(\ell=1\) by the definition of \(A_0\)). Consequently
\[
\operatorname{Ind}(Y_\ell)=\operatorname{Ind}(A_\ell)\cup\bigl(w*\operatorname{Ind}(A_{\ell-1})\bigr),
\]
with intersection \(\operatorname{Ind}(A_{\ell-1})\). This union is the homotopy cofiber of the inclusion of the intersection. If its target is contractible, the cofiber is the suspension of the source; if its source is nonempty and contractible, the cofiber has the homotopy type of the target. The three residue classes from Step 4 therefore give
\[
\operatorname{Ind}(Y_{3k+1})\simeq*,\quad
\operatorname{Ind}(Y_{3k+2})\simeq T^{*(k+1)},\quad
\operatorname{Ind}(Y_{3k})\simeq\Sigma T^{*k}\quad(k\ge1).
\]
Finally \(D\cong C_6\), and \(\operatorname{Ind}(C_6)\simeq S^1\vee S^1\): its two disjoint independent-set triangles are contractible and are connected by three independent bridge edges, so collapsing the triangles produces two vertices joined by three edges. Standard join-smash suspension gives \(T^{*h}\simeq\bigvee^{2^h}S^{2h-1}\) for all \(h\ge1\). Substitution proves every claimed homotopy equivalence and all integral homology statements. No finite enumeration is used as an infinite proof.

## Verification
The self-contained standard-library program `verify.py` reconstructs the original Mycielskian graph and both reflections without using the quotient model. For all \(1\le\ell\le11\), it calculates every allowed involution-orbit and every pairwise conflict and checks equality with the two independently defined quotient graphs. It checks the required open-neighborhood containments behind the fold for \(2\le\ell\le11\). For the edge-axis case \(1\le\ell\le7\), it enumerates every independent simplex of the quotient, constructs exact mod-two boundary columns, and computes homology ranks, recovering respectively contractible, two circles, two two-spheres, contractible, four three-spheres, four four-spheres, and contractible. It additionally checks the vertex-axis mod-two homology for \(1\le\ell\le3\). Successful execution prints `VERIFY_OK`. Finite checks corroborate, but do not replace, the all-\(\ell\) fold-and-cofiber proof.

## Relationship to prior work
Carnero Bravo (arXiv:2601.13432, first posted January 19, 2026) proves a general nonequivariant homotopy formula for generalized Mycielskians of **simple graphs**, including paths and cycles. The present argument uses that theorem only for the ordinary path \(P_4\) and uses its standard fold lemma. The edge-axis fixed quotient has two endpoint self-relations and a restricted top layer, and therefore is not one of the simple-graph Mycielskians to which that published theorem directly applies. Here the quotient and the complete all-parameter fold/cofiber classification are proved explicitly. The earlier Goyal–Shukla–Singh paper treats nonequivariant Mycielskians of complete graphs, not these geometric reflection fixed spaces. Related published rational representation results for generalized Mycielskians of complete graphs concern a different base graph and do not determine this cycle's fixed-set homotopy types. A failure to find an indexed equivalent is not proof of absolute novelty.

## Limitations
Only the two reflection conjugacy classes of the standard dihedral action on generalized Mycielskians of \(C_6\) are classified. This does not determine arbitrary subgroup fixed points, ambient equivariant homotopy type, or integral action on ambient homology. The first-source publication date refers to the motivating 2026 paper, not to the date of the new proof. An unindexed equivalent result or a stronger result outside the inspected literature cannot be excluded. Independent mathematical validation has not been performed.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432 (first public 2026-01-19), Sections 2--3, especially Lemma 2, Theorem 5, Corollaries 9 and 11. https://arxiv.org/html/2601.13432.
2. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, Contributions to Discrete Mathematics 16(3) (2021), 74--92, https://doi.org/10.55016/ojs/cdm.v16i3.71284.
