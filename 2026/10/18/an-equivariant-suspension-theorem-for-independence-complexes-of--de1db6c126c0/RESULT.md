# An equivariant suspension theorem for independence complexes of Mycielski graphs

## Finding
For every finite nonempty simple graph \(G\) and every subgroup \(\Gamma\leq\operatorname{Aut}(G)\), there is a \(\Gamma\)-homotopy equivalence
\[
\operatorname{Ind}(\mu(G))\simeq_{\Gamma}\Sigma\operatorname{Ind}(G),
\]
where \(\mu(G)\) is the **ordinary** Mycielski graph and \(\Gamma\) fixes both suspension poles. In particular, for every \(H\leq\Gamma\), including the trivial subgroup,
\[
\operatorname{Ind}(\mu(G))^H\simeq\Sigma\bigl(\operatorname{Ind}(G)^H\bigr).
\]
The suspension of the empty fixed-point space is understood to be two discrete points. The equivalence yields, in every degree and with integral coefficients, \(\Gamma\)-module isomorphisms
\[
\widetilde H_{i+1}(\operatorname{Ind}(\mu(G));\mathbb Z)
\cong\widetilde H_i(\operatorname{Ind}(G);\mathbb Z).
\]
The equivalences respect graph isomorphisms. For every positive integer \(r\), they may be iterated to obtain \(\operatorname{Ind}(\mu^r(G))\simeq_{\Gamma}\Sigma^r\operatorname{Ind}(G)\) under the inherited action.

## Assumptions and scope
Graphs are finite, undirected, simple, and have at least one vertex; isolated vertices are allowed. Write \(V=V(G)\). The ordinary Mycielski graph \(\mu(G)\) has old vertices \(v\), shadow vertices \(v'\) for every \(v\in V\), and one apex \(w\). Its edges are the old edges \(uv\) for \(uv\in E(G)\), the old-to-shadow edges \(uv'\) and \(u'v\) for \(uv\in E(G)\), and all \(wv'\). No shadows are mutually adjacent, and no old vertex is adjacent to its own shadow. The canonical action of any \(\Gamma\leq\operatorname{Aut}(G)\) permutes old vertices and corresponding shadows simultaneously and fixes \(w\). The notation \(\operatorname{Ind}(F)\) means the geometric realization of the finite independence complex of a graph \(F\). Unreduced suspension \(\Sigma X\) carries the induced \(\Gamma\)-action on \(X\) and the trivial action on its suspension parameter. Geometric fixed points, not merely sets of invariant vertices, are meant by \(X^H\).

## Proof
**1. An invariant contractible subcomplex.** Put \(K=\operatorname{Ind}(\mu(G))\), \(A=\operatorname{Ind}(\mu(G)-w)\), and let \(S\subseteq A\) be the full simplex on all shadow vertices. Define a simplicial map \(p:A\to S\) by sending both \(v\) and \(v'\) to \(v'\). It is a retraction, and it commutes with every automorphism in \(\Gamma\).

For each face \(\sigma\) of \(A\), the union of its vertex set with the vertex set of \(p(\sigma)\) is again independent in \(\mu(G)-w\). Indeed, there are no edges between shadows; if an old \(u\in\sigma\) and a shadow \(v'\in p(\sigma)\) were adjacent, then \(uv\in E(G)\). When \(v'\) was already in \(\sigma\), this contradicts independence of \(\sigma\); when \(v'\) comes from old \(v\in\sigma\), it contradicts the presence of both old \(u\) and old \(v\) in the same independent face. This also covers \(u=v\), since old-to-own-shadow edges are absent. Therefore the inclusion \(j:S\hookrightarrow A\) and \(j\circ p:A\to A\) satisfy that \(\operatorname{id}_A\) and \(j\circ p\) are **contiguous** simplicial maps. Their straight-line geometric contiguity homotopy is \(\Gamma\)-equivariant and is pointwise constant on \(S\). Hence \(A\) \(\Gamma\)-equivariantly strongly deformation retracts onto \(S\).

Because \(V\ne\varnothing\), the full shadow simplex is nonempty. Its barycenter \(b=|V|^{-1}\sum_{v\in V}v'\) is fixed by every element of \(\Gamma\), and straight-line contraction of \(S\) to \(b\) is equivariant. Therefore \(A\) is \(\Gamma\)-equivariantly contractible **to a fixed point**. In particular \(A^H\) is nonempty and contractible for every subgroup \(H\leq\Gamma\).

**2. Apex decomposition and the quotient.** Let \(L\subseteq A\) be the independence complex on the old vertices; it is exactly \(\operatorname{Ind}(G)\). The link of the apex \(w\) in \(K\) is \(L\), because \(w\) is adjacent to every shadow and to no old vertex. Thus there is an equality of \(\Gamma\)-simplicial subcomplex unions
\[
K=A\cup (w*L),\qquad A\cap(w*L)=L.
\]
The quotient \(K/A\), which collapses the entire \(\Gamma\)-invariant \(A\) to one fixed point, is canonically \(\Gamma\)-homeomorphic to \((w*L)/L\). The latter is precisely the unreduced suspension \(\Sigma |L|\): its two poles are the image of \(A\) and the vertex \(w\), both fixed by \(\Gamma\).

**3. Equivariant homotopy equivalence.** The inclusion \(A\hookrightarrow K\) is a cofibration of finite \(\Gamma\)-CW complexes (one may use equivariant barycentric subdivisions to check fixed-point cofibrations). For each subgroup \(H\leq\Gamma\), the inclusion \(A^H\hookrightarrow K^H\) is a cofibration with contractible, nonempty source. The quotient map \(K^H\to K^H/A^H\) is therefore a homotopy equivalence, by the cofibration homotopy sequence (or homotopy extension and the homotopy-pushout lemma). For a finite group acting on a finite complex, the natural map \(K^H/A^H\to(K/A)^H\) is a homeomorphism: a point outside \(A\) cannot become fixed merely by collapsing \(A\). Hence the quotient \(K\to K/A\) is a weak equivalence on \(H\)-fixed spaces for every subgroup \(H\), and is a \(\Gamma\)-homotopy equivalence by the equivariant Whitehead theorem. Combining with step 2 proves the theorem including its fixed-point conclusion.

**4. Modules, iterates, and a distinguishing example.** Suspension with fixed poles gives the standard natural suspension isomorphism on reduced singular or simplicial homology. The maps above commute with \(\Gamma\), so the isomorphism is one of integral \(\Gamma\)-modules, not just of underlying abelian groups. Repeating the same argument for the iterated Mycielski graphs, on which the original \(\Gamma\)-action extends by permuting each new shadow family and fixing each new apex, yields the stated \(r\)-fold result.

For a concrete genuine-equivariant consequence, take \(G=C_5\) with its standard cyclic rotation group \(C_5\). The action of \(C_5\) on \(\operatorname{Ind}(C_5)\) has no fixed point: an invariant nonempty face would contain the entire five-vertex orbit, which is not independent. Nonetheless \(\operatorname{Ind}(\mu(C_5))^{C_5}\simeq S^0\), with representatives the fixed apex and the barycenter of the five-shadow simplex. A nonequivariant sphere classification alone does not specify this fixed-point space. Under the dihedral group \(D_5\), the action on \(\widetilde H_2(\operatorname{Ind}(\mu(C_5));\mathbb Z)\cong\mathbb Z\) has rotations acting as \(+1\) and reflections as \(-1\), inherited from the orientation action on \(\operatorname{Ind}(C_5)\cong S^1\).

## Verification
The supplied self-contained Python 3 program `verify.py` enumerates all faces of the old-and-shadow deletion and the complete Mycielski complex for every labeled four-vertex graph (all \(64\) edge sets), together with the dihedral actions for five- and seven-cycles. It independently tests the face-union condition for contiguity, the simplicial retraction, all graph automorphisms for the four-vertex cases, equivariance on faces, the exact apex face decomposition, and the reduced signed Lefschetz identity \(\widetilde L(\mu(G),g)=-\widetilde L(G,g)\). The successful deterministic output is `C_5: A_faces=92, Mycielski_faces=103, symmetries=10`, `C_7: A_faces=576, Mycielski_faces=605, symmetries=14`, and `VERIFY_OK four_vertex_graphs=64 cycle_examples=2`. These finite computations test definitions and signs; **the proof for arbitrary graphs and subgroups is the preceding equivariant homotopy argument**, not an extrapolation from those tests.

## Relationship to prior work
Goyal, Shukla and Singh (2019), Theorem 4.1, established the nonequivariant formula \(\operatorname{Ind}(\mu(G))\simeq\Sigma\operatorname{Ind}(G)\) for any graph. Carnero Bravo (first publicly posted January 19, 2026), Theorem 5 and Corollary 6, developed the nonequivariant generalized and iterated Mycielskian formulas. A separately published result, *The symmetric-group homology modules of generalized Mycielskians of complete graphs* (2026), computes full rational \(S_n\)-homology representations for the special input \(G=K_n\) and exploits equivariant simplicial folds. These are important predecessors. The new assertion is **not** the known ordinary suspension equivalence or a new wedge count: it promotes the suspension to a **genuine \(\Gamma\)-homotopy equivalence simultaneously for every finite nonempty graph and every subgroup of its automorphism group**, giving all geometric fixed-point spaces and integral module isomorphisms. None of the inspected predecessor statements implies the claimed fixed-point equivalences merely from its ordinary homotopy type or from rational character data. General equivariant models outside the inspected corpus could still imply this result.

## Limitations
Only the ordinary Mycielski construction (and its direct iteration) is classified equivariantly, not arbitrary higher-level generalized Mycielskians. The action considered is the inherited action of a subgroup of \(\operatorname{Aut}(G)\), not every potentially larger automorphism of the Mycielski graph. The proof does not construct a \(\Gamma\)-equivariant elementary-collapse sequence or classify independent-point-set persistence. Its fixed-point equivalence is an equivalence of geometric realizations, not an assertion that fixed-vertex subcomplexes suffice. Searches cannot rule out every unindexed equivalent theorem.

## References
1. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1, first public 2019-05-16, Theorem 4.1 and proof. https://arxiv.org/pdf/1905.06926
2. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1, first public 2026-01-19, Theorem 5 and Corollaries 6 and 9. https://arxiv.org/html/2601.13432
3. *The symmetric-group homology modules of generalized Mycielskians of complete graphs*, published research result, October 11, 2026; especially §§1–5 of its proof and its stated limitations. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-symmetric-group-homology-modules-of-generalized-mycielskians--a69c919d2b95
