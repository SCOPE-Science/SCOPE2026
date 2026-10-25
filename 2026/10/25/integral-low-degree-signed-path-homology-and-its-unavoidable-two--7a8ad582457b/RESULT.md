# Integral low-degree signed path homology and its unavoidable two-torsion

## Finding

For a finite connected simple undirected graph \(G\) with at least one edge and a signing \(\sigma:E(G)\to\{+1,-1\}\), form the *integral signed GLMY complex* \(\Omega_*^{\sigma}(G;\mathbb Z)\) of its bidirected completion: start with integral allowed regular paths in the signed double cover, impose the deck relation \([\tau p]=-[p]\), and retain precisely those allowed chains whose regular boundary remains allowed. This integral complex is defined directly, rather than by taking anti-invariants in cover homology. Write \(\mathcal H_i^{\sigma}(G;\mathbb Z)\) for its homology, and \(b=|E(G)|-|V(G)|+1\).

**Theorem.** Without any girth assumption,
\[
\mathcal H_0^{\sigma}(G;\mathbb Z)\cong
\begin{cases}\mathbb Z,&\text{every cycle has positive sign product},\\
\mathbb Z/2\mathbb Z,&\text{some cycle has negative sign product}.
\end{cases}
\]
If \(G\) has girth at least five (trees have infinite girth), then
\[
\mathcal H_1^{\sigma}(G;\mathbb Z)\cong
\begin{cases}\mathbb Z^{b},&\text{the signing is balanced},\\
\mathbb Z^{b-1},&\text{the signing is unbalanced}.
\end{cases}
\]
Both descriptions follow from an exact, natural two-term chain identification after quotienting the integral degree-one chains by integral two-boundaries:
\[
\Omega_1^{\sigma}(G;\mathbb Z)/\operatorname{im}\partial_2
\xrightarrow{\ \partial_1\ }\Omega_0^{\sigma}(G;\mathbb Z)
\quad\cong\quad
\bigl(\mathbb Z^{E(G)}\xrightarrow{B_\sigma}\mathbb Z^{V(G)}\bigr),
\]
where the column for a chosen orientation \(u\to v\) of edge \(e\) is \(B_\sigma(e)=\sigma(e)v-u\). In particular the first group is torsion-free, but integral degree-zero signed homology detects unbalanced signings by genuine order-two torsion. For any connected unbalanced signed graph, the integral double cover is connected, and hence
\[
\mathcal H_0^{\sigma}(G;\mathbb Z)\cong\mathbb Z/2\mathbb Z
\quad\text{while}\quad H_0(\widetilde G;\mathbb Z)^-=0.
\]
Thus the real-coefficient identification of signed homology with the anti-invariant part of cover homology cannot be extended to integer homology by simply taking deck anti-invariants after homology.

## Assumptions and scope

The graph is finite, connected, simple and loopless, with at least one edge. Every undirected edge is replaced by two oppositely directed arrows with the same sign. The signed double cover has vertices \(u^+\) and \(u^-\) and a lifted arrow \(u^\epsilon\to v^{\epsilon\sigma(uv)}\) over either base arrow \(u\to v\). Its deck map \(\tau\) negates the sheet label. Regular path boundaries omit nonregular deleted faces. The degree-\(p\) signed *allowed* module is the quotient of the free abelian group on signed-cover allowed regular \(p\)-paths by \(\tau p=-p\). The signed GLMY chain group \(\Omega_p^{\sigma}\) comprises the allowed chains whose boundary, computed in the free module on all regular signed-cover paths modulo deck relations, belongs to the allowed module. We use the unaugmented degree-zero boundary \(\partial_0=0\).

A signing is **balanced** if the product of its edge signs around every simple cycle is \(+1\), including the vacuous case of a tree. Its girth is the length of a shortest simple cycle, with trees assigned infinite girth. No assertion about degree-two or higher integral signed homology is made.

## Proof

**1. Integral lift and incidence boundary.** A deck orbit of any regular path has exactly two members: a signed-cover path and its sheet-reversed path are distinct, even when their projected base path agrees. Thus imposing \([\tau p]=-[p]\) gives a free abelian group with one generator for each projected base path and a chosen initial sheet. Its boundary is well defined over integers because the deck action commutes with the regular boundary and \(\partial^2=0\) before quotienting. For each vertex choose generator \(v=[v^+]\). For a directed edge \(u\to v\), choose its lift beginning on the positive sheet, giving a generator \(e_{uv}\); the lift ends on sheet \(\sigma(uv)\). Therefore
\[
\partial_1e_{uv}=\sigma(uv)v-u.
\]
This agrees with the twisted incidence differential already established over real coefficients in Bai–Li–Yau, Proposition 3.8; the point here is the integral degree-zero cokernel and degree-one quotient.

**2. All degree-two boundaries when girth is at least five.** Every base allowed two-path has the form \((u,v,w)\) with both adjacent pairs edges. If \(u=w\), then the length-two sign product is \(+1\), so deleting its middle vertex produces a repeated identical lifted vertex, a nonregular term interpreted as zero. Taking initial positive sheet, the surviving endpoint deletions give
\[
\partial_2 e_{uvu}=e_{uv}+\sigma(uv)e_{vu}.
\]
For \(u\ne w\), deleting \(v\) produces a regular \(u\)-to-\(w\) lifted path of length one which is **not allowed**, since absence of triangles forces \(uw\notin E(G)\). In a graph without four-cycles, each ordered distinct pair \((u,w)\) has at most one common neighbor \(v\). Hence no nontrivial integer linear combination of these nonbacktracking two-paths can cancel its forbidden shortcut, even after imposing deck antisymmetry. Consequently \(\Omega_2^{\sigma}\) is freely generated by the backtracking paths \(e_{uvu}\), and \(\operatorname{im}\partial_2\) is generated by the relations \(e_{uv}+\sigma(uv)e_{vu}\), one for each underlying edge \(uv\). These relations are primitive and independent: each involves just the two directed generators of its edge with one coefficient a unit. Quotienting identifies \(e_{vu}=-\sigma(uv)e_{uv}\) and yields a free abelian group canonically equivalent, after choosing one orientation per edge, to \(\mathbb Z^{E(G)}\). The displayed \(B_\sigma\) is the induced boundary. No other degree-two boundaries exist under the girth condition.

**3. Smith-form calculation, including the no-girth degree-zero case.** The degree-zero group and the degree-one boundary formula in step 1 hold for **every** connected simple signed graph; possible additional higher boundaries do not affect degree zero. Choose a spanning tree \(T\) and perform integral unit row sign changes corresponding to vertex switching so that every tree edge has positive sign. In \(\operatorname{coker}B_\sigma\), the \(|V|-1\) tree columns identify every vertex generator with one root generator \(x\). Every non-tree edge then yields either the zero relation or \(2x=0\), with the latter occurring exactly when the associated fundamental cycle has negative sign product. All fundamental cycles are positive exactly when the signing is balanced. Therefore the cokernel is \(\mathbb Z\) when balanced and \(\mathbb Z/2\mathbb Z\) otherwise. Integral Smith reductions also show \(\operatorname{rank}_{\mathbb Q}B_\sigma=|V|-1\) when balanced and \(|V|\) otherwise. The kernel of a homomorphism between free abelian groups is free, and with \(m=|E|\), its rank is \(m-|V|+1=b\) or \(m-|V|=b-1\), respectively. Step 2 identifies this kernel with degree-one signed homology under girth at least five.

**4. Failure of integer homology/anti-invariants interchange.** If one cycle has negative sign product, traversing it exchanges the two sheets. As \(G\) is connected, the signed double cover is connected. Therefore ordinary degree-zero GLMY homology of that cover over \(\mathbb Z\) is \(\mathbb Z\), and deck interchange acts trivially on its connected-component generator. Its anti-invariant subgroup vanishes. Step 3 gives \(\mathcal H_0^{\sigma}(G;\mathbb Z)=\mathbb Z/2\mathbb Z\). This disproves the naive integral extension of the real-coefficient isomorphism \(H_i^{\sigma}(G;\mathbb R)\cong H_i(\widetilde G;\mathbb R)^-\). It does **not** dispute the integral chain-level identification with the deck anti-invariant subcomplex: formation of anti-invariant *homology* fails to commute with taking homology when \(2\) is not invertible.

## Verification

The bundled reproducible Python checker constructs the signed-cover allowed two-path boundary and twisted integer incidence matrix independently for cycles, an attached two-cycle cactus, the Petersen graph and the Heawood graph. In all, 362 signings were tested, including every signing of each cycle of lengths five through seven, all signings on the two five-cycle cactus, and sample signings on the Petersen and Heawood graphs. The checker verified 16,644 two-path generator instances and 6,764 backtrack relations, full Smith invariant factors of the signed incidence map, its kernel ranks, the signed balance test, and connectedness of the signed cover. It ended with `VERIFY_OK`; see `verify.py` and `verification.log`. These finite checks do not establish the universal theorem, which follows from the proof above.

## Relationship to prior work

Bai, Li and Yau (arXiv:2609.25557, first publicly submitted September 22, 2026) introduce signed GLMY homology over **real** coefficients. Their Proposition 3.8 already gives twisted incidence, Proposition 3.10 identifies real signed homology with the anti-invariant part of real cover homology, and their Example 4.4 analyzes backtrack relations in a signed bowtie. None of those statements yields an integral \(\mathbb Z/2\mathbb Z\) degree-zero group, an integral high-girth first-homology classification, or the counterexample to commuting integer homology with deck anti-invariants. The integral local-coefficient cellular graph incidence and its Smith reduction are classical; novelty is claimed only for their precise relationship with the *integral refinement* of the signed GLMY construction and its integral comparison failure. Asao (arXiv:2201.08047) supplies a different ordinary (unsigned) path-homological large-girth result; it does not treat this signed integral comparison.

## Limitations

The integer-coefficient theory here is the explicitly defined deck-quotient/anti-invariant-chain refinement of the real signed GLMY complex; this choice must not be conflated with taking integral anti-invariants after homology. The first-homology formula assumes no triangle and no square; H0 requires no girth restriction. The proof makes no claim about integral higher-degree groups or how square/triangle fillings change signed H1. The twisted graph incidence calculation itself is standard; the mathematical observation is the exact relationship and the integral two-torsion obstruction for the recent GLMY construction. Bibliographic priority remains subject to independent specialist review, particularly local-coefficient treatments not explicitly indexed under signed GLMY terminology.

## References

1. S. Bai, J. Li and S.-T. Yau, *Signed GLMY Homology of Signed Graphs via Double Covers*, arXiv:2609.25557v1, submitted September 22, 2026, especially §§3–4, Proposition 3.8, Proposition 3.10 and Example 4.4. https://arxiv.org/html/2609.25557v1
2. Y. Asao, *Magnitude homology and path homology*, arXiv:2201.08047, especially Proposition 8.14 on ordinary path homology in the large-girth setting. https://arxiv.org/abs/2201.08047
3. F. Harary, classical switching/balance criterion for signed graphs (as cited and formulated in [1], Theorem 2.3).
