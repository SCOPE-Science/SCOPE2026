# Signed-cactus GLMY homology: persistent ranks and exact automorphism characters

## Finding

Let \(G=(V,E)\) be any finite simple **cactus graph** (possibly disconnected, with isolated vertices): each edge belongs to at most one simple undirected cycle. Give each edge a sign \(\sigma_e\in\{+1,-1\}\), the same in both orientations. All homology is over \(\mathbb R\) in the signed GLMY theory of Bai–Li–Yau [1] for the canonical bidirected completion. A connected signed graph is **balanced** when every simple cycle has positive sign product; an isolated vertex is balanced. Write \(b_\sigma(G)\) for the number of balanced connected components and \(k_\sigma(G)\) for the number of balanced simple cycles with length three or four.

**Theorem (cactus signed GLMY classification and persistence).** For every such signed cactus,
\[
\dim H_0^\sigma(G)=b_\sigma(G),\qquad
\dim H_1^\sigma(G)=|E|-|V|+b_\sigma(G)-k_\sigma(G).
\]
For any finite nested filtration \(G_0\subseteq G_1\subseteq\cdots\subseteq G_T\subseteq G\) with the **same vertex set** and inherited edge signs, every map \(H_1^\sigma(G_s)\to H_1^\sigma(G_t)\), \(s\le t\), is injective. Thus the degree-one persistence barcode has exactly \(\beta_1(G_t)-\beta_1(G_{t-1})\) intervals born at stage \(t\) (using the appropriate initial dimension at stage zero); all live through the final stage. If the filtration is extended constantly, these intervals have infinite death time. In degree zero, the induced maps are surjective, with rank \(b_\sigma(G_t)\).

**Exact symmetry trace.** Let \(g\) be a vertex automorphism preserving both adjacency and every edge sign. Let \(a(g)\) count edges whose endpoints are each individually fixed; let \(r(g)=\sum_{\{u,v\}\in E\,,\,g(u)=v\,,\,g(v)=u}\sigma_{uv}\); and let \(f(g)\) be the number of fixed vertices. For each balanced component \(K\) stabilized by \(g\), choose a potential \(t_K:V(K)\to\{\pm1\}\) with \(\sigma_{uv}=t_K(u)t_K(v)\), and define \(\kappa_K(g)=t_K(v)t_K(gv)\) for any \(v\in K\). For each balanced triangle or quadrilateral \(C\) stabilized by \(g\), similarly choose a potential \(t_C\) and set \(\lambda_C(g)=\varepsilon_C(g)t_C(v)t_C(gv)\), where \(\varepsilon_C(g)\) is \(+1\) when the chosen cyclic orientation is preserved and \(-1\) when reversed. These signs are well defined independently of the potential and chosen vertex. Then
\[
\operatorname{tr}\bigl(g\mid H_1^\sigma(G)\bigr)
=a(g)-r(g)-f(g)
+\sum_{\substack{K\text{ balanced}\\gK=K}}\kappa_K(g)
-\sum_{\substack{C\text{ balanced},\,|C|\in\{3,4\}\\gC=C}}\lambda_C(g).
\]
The formula determines the complete real character of every finite group of sign-preserving cactus automorphisms.

**Example (friendship graph).** Join \(m\ge2\) triangles at a single common vertex, and give every edge sign \(-1\). Each triangle is unbalanced, so \(b_\sigma=k_\sigma=0\), \(|V|=2m+1\) and \(|E|=3m\); hence \(\dim H_1^\sigma=m-1\). The group \(S_m\), permuting triangles while retaining their within-triangle ordering, acts with character \(\#\operatorname{Fix}(g)-1\) on this homology. Consequently it is isomorphic to the standard (augmentation) real \(S_m\)-representation, not merely an abstract vector space of the same dimension.

## Assumptions and scope

For each undirected edge \(\{u,v\}\), choose one orientation \(u\to v\). Let \(C_1=\mathbb R^E\), \(C_0=\mathbb R^V\), and define the signed incidence operator by \(B_\sigma e_{uv}=\sigma_{uv}e_v-e_u\). Reversing an oriented edge changes its chain generator by \(e_{vu}=-\sigma_{uv}e_{uv}\). Define \(Z_\sigma=\ker B_\sigma\). For a balanced cycle \(C\), its **signed circulation line** \(L_C\subseteq Z_\sigma\) is the unique one-dimensional space of signed flows supported entirely on \(C\). Let \(R_\sigma=\sum_{C\text{ balanced},\,|C|\in\{3,4\}}L_C\). The graph is finite and simple; path chains use regular paths and the signed-double-cover convention in [1]. We make no statement about degree-two or higher signed GLMY groups.

## Proof

**Step 1: a natural short-cycle presentation.** In the bidirected signed complex, an allowed directed one-step lift \((u,v)\) has boundary \(\sigma_{uv}e_v-e_u\). Its reverse-lift backtrack \((u,v,u)\) is an allowed signed two-path with boundary \(e_{uv}+\sigma_{uv}e_{vu}\). Quotienting the one-path group by all such backtrack boundaries identifies reversed arcs with the signed oriented-edge group \(C_1\) and induces precisely \(B_\sigma\).

Every other directed two-path \((u,v,w)\), with \(u\ne w\), has a missing-middle shortcut from \(u\) to \(w\) in the cover with sign transport \(\delta=\sigma_{uv}\sigma_{vw}\). If the signed shortcut edge exists and has sign \(\delta\), the two-path boundary closes a balanced triangle. Otherwise its forbidden shortcut lies in a basis component identified by its ordered endpoints and transported sheet \((u,w,\delta)\). A linear combination of two-paths has allowed boundary exactly when the sum of coefficients in every such forbidden component is zero. That kernel is spanned by pairwise differences of two-paths with the same forbidden component. Their allowed boundaries are signed circulations around balanced four-cycles (or zero). Conversely every balanced quadrilateral circulation is obtained directly by such a difference, or as a linear combination of two balanced triangle boundaries when its diagonal shortcut is allowed with matching transport. This proves a natural edge-inclusion- and sign-preserving-automorphism-equivariant identification
\[
H_1^\sigma(G)\cong Z_\sigma/R_\sigma
\]
for **any** finite simple signed graph. This lemma is a low-degree reformulation of the signed-double-cover chain construction [1] together with the unsigned triangle-and-square cycle-space presentation [2]; no general independent novelty is attributed to those existing foundations.

**Step 2: dimensions for a cactus.** The signed incidence matrix has rank \(|V|-b_\sigma(G)\). To verify this, a left null vector \(x\) satisfies \(x_u=\sigma_{uv}x_v\) on every edge, giving precisely one free scalar on a balanced connected component and zero on an unbalanced component. Thus \(\dim Z_\sigma=|E|-|V|+b_\sigma(G)\). Distinct simple cycles of a cactus are edge-disjoint. Their balanced short circulations therefore have disjoint supports and are linearly independent, giving \(\dim R_\sigma=k_\sigma(G)\). The two displayed Betti-number formulas now follow, using \(H_0^\sigma=C_0/\operatorname{im}B_\sigma\).

**Step 3: persistence.** For a signed subgraph \(G_t\) on the fixed vertices, \(Z_\sigma(G_t)\) embeds in \(Z_\sigma(G_s)\) whenever \(t\le s\). Since each edge belongs to at most one cycle of the final cactus, the balanced-short-cycle supports are pairwise disjoint. A linear combination of distinct such cycles can be supported on \(E(G_t)\) only when every contributing cycle is wholly contained in \(E(G_t)\). Hence
\[
R_\sigma(G_s)\cap C_1(E(G_t))=R_\sigma(G_t)
\]
for \(t\le s\), and consequently the induced \(H_1\) map is injective. Homology-zero maps are always surjective because the vertex chain group stays unchanged while incidence images increase. These claims hold for arbitrary nonuniform additions of edges and do not require every stage to be connected.

**Step 4: trace.** The oriented-edge chain representation has trace \(a(g)-r(g)\): fixed-pointwise edges contribute \(+1\), and setwise-fixed edges with exchanged endpoints contribute \(-\sigma_e\). The vertex chain representation has trace \(f(g)\). The exact sequences
\[
0\to Z_\sigma\to C_1\xrightarrow{B_\sigma}\operatorname{im}B_\sigma\to0,
\quad
0\to\operatorname{im}B_\sigma\to C_0\to H_0^\sigma\to0,
\quad
0\to R_\sigma\to Z_\sigma\to H_1^\sigma\to0
\]
give trace additivity. The signed component-potential argument identifies \(\operatorname{tr}(g|H_0^\sigma)=\sum_{K:gK=K}\kappa_K(g)\), summing balanced components only. Each balanced short-cycle circulation line is stabilized with eigenvalue \(\varepsilon_C(g)t_C(v)t_C(gv)\), and all other such lines are permuted. Thus \(\operatorname{tr}(g|R_\sigma)=\sum_{C:gC=C}\lambda_C(g)\). Substitution gives the asserted formula.

**Step 5: friendship symmetry.** For the all-negative \(m\)-triangle friendship graph there are no balanced components or balanced short cycles. An arm permutation fixing \(j\) arms fixes \(2j+1\) vertices and exactly \(3j\) edges pointwise, and it exchanges no endpoints of an edge. The trace formula therefore gives \(3j-(2j+1)=j-1\), the standard permutation-augmentation character of \(S_m\). Character semisimplicity over \(\mathbb R\) identifies the representation, including the cases \(m=2\) and all larger \(m\).

## Verification

The standalone `verify.py` constructs the actual signed two-sheet one- and two-path boundaries, solves the condition that a two-chain has allowed boundary, computes exact ranks modulo the prime \(1009\), and compares them with the proposed short-cycle presentation. It also checks signed-cactus edge-filtration ranks and natural graph automorphism characters. Run `python3 verify.py` from a directory containing this file. The observed result is `VERIFY_OK`, `SYMMETRY_OK`, `ALL_GRAPH_SHORT_CYCLE_OK`, `CACTUS_FILTRATION_OK`, and `FRIENDSHIP_SYMMETRY_OK`. These are finite computational checks only; the unrestricted theorem follows from Steps 1–5. Every claimed rank in the full theorem is over \(\mathbb R\), not deduced from finite-field rank equality.

## Relationship to prior work

Bai, Li and Yau [1] introduced signed GLMY homology through anti-invariant chains on double covers, proved switching invariance and the balanced-component degree-zero formula, and computed sign-sensitive examples including a two-triangle graph. The signed complex and its basic properties are theirs, not new here. Kempton, Münch and Yau [2] established the **unsigned** cycle-space presentation modulo short triangle and square cycles. Chen [3] independently develops signed incidence homology and frame-matroid flows, but not signed GLMY persistence. The present result combines these foundations to classify all signed cacti with persistent inclusion maps and exact symmetry characters; the arbitrary-cactus theorem and its representation refinement are the stated contributions.

## Limitations

The theorem is restricted to finite simple **cactus** underlying graphs, bidirected edges with the same sign in both directions, and real coefficients; its persistence maps use a fixed vertex set and inherited signs. It does not classify higher-degree homology, arbitrary digraph orientations, signed filtrations changing the signs of existing edges, or integral module splittings. The short-cycle presentation is closely connected to [1–2], so the originality of any corollary is limited to the cactus-wide persistence and equivariant classification actually stated. A logically equivalent treatment in unindexed literature remains possible; the conclusions have not been independently audited.

## References

1. Shuliang Bai, Jingyan Li, Shing-Tung Yau, *Signed GLMY Homology of Signed Graphs via Double Covers*, arXiv:2609.25557 (first posted 2026-09-22), https://arxiv.org/abs/2609.25557.
2. Mark Kempton, Florentin Münch, Shing-Tung Yau, *Relationships between cycle spaces, gain graphs, graph coverings, fundamental groups, path homology, and graph curvature*, arXiv:1710.01264 (first posted 2017-10-03), https://arxiv.org/abs/1710.01264.
3. Beifang Chen, *On the foundations of signed graphs I: chain groups, frame matroid, and bivariate flow polynomial*, arXiv:2508.11288 (first posted 2025-08-15), https://arxiv.org/abs/2508.11288.
