# An equivariant sinkless-orientation identity for graph flex complexes

## Finding
Let \(G=(V,E)\) be any finite simple graph with no isolated vertices, and let \(\Gamma\leq\operatorname{Aut}(G)\) be any subgroup. For each orientation \(\theta\) of its edges, a *sink* is a vertex with no outgoing edge. Write \(\mathcal S(G)\) for the finite \(\Gamma\)-set of sinkless orientations. Let \(F(G)=\operatorname{Flex}(G)\) be the cubical complex in which vertices are orientations and a cube simultaneously flips any mutually independent set of sinks or sources, as defined by Kozlov [1].

**Theorem (equivariant sinkless-orientation identity).** In the rational representation ring of \(\Gamma\),
\[
\boxed{\sum_{k\ge0}(-1)^k\,[H_k(F(G);\mathbb Q)]\;=\;[\mathbb Q[\mathcal S(G)]].}
\]
Consequently, for **every** graph automorphism \(g\in\Gamma\), its full unreduced homological Lefschetz number is the nonnegative integer
\[
\boxed{L(g;F(G))=\sum_k(-1)^k\operatorname{tr}(g\mid H_k(F(G);\mathbb Q))
=|\mathcal S(G)^g|.}
\]
For every subgroup \(H\le\Gamma\), the ordinary Euler characteristic of the orbit space obeys
\[
\boxed{\chi(|F(G)|/H)=|\mathcal S(G)/H|.}
\]

There is also an explicit orbit formula for the character. For \(g\in\Gamma\), say that an *edge orbit is reversing* if some positive power of \(g\) preserves an undirected edge but interchanges its endpoints. If such an orbit exists, \(L(g;F(G))=0\). Otherwise, for any \(g\)-invariant independent vertex set \(B\subseteq V\), let \(c_g(B)\) count the \(g\)-orbits of vertices contained in \(B\) and let \(e_g(G[V\setminus B])\) count \(g\)-orbits of edges in the indicated induced subgraph. Then
\[
\boxed{L(g;F(G))=\sum_{\substack{gB=B\\ B\text{ independent}}}
(-1)^{c_g(B)}\,2^{e_g(G[V\setminus B])}.}
\]
At \(g=1\) this specializes to the ordinary sinkless-orientation formula of Kozlov [1, Proposition 4.4 and Corollary 4.5], which is **not** claimed as new.

## Assumptions and scope
Graphs are finite, undirected, loopless and without parallel edges or isolated vertices. All group actions are induced by vertex relabeling, and \(\Gamma\) is finite. Every edge has exactly one direction in an orientation. A sink has every incident edge directed *toward* it; distinct sinks are never adjacent. A legal flex reverses all edges incident to one sink or source. Independent legal flexes span a cube. Homology is **ordinary, unreduced, rational** homology in all degrees; the representation-ring identity is an equality of **virtual representations**, not an isomorphism of individual homology modules or an equivariant deformation retract. The formula concerns the geometric quotient by a finite subgroup and does not posit a quotient cell structure without subdivision.

## Proof
**1. Canonical cells.** A \(d\)-cube can be uniquely encoded by a pair \((\theta,A)\), where \(\theta\) is an orientation of every edge of \(G\) and \(A\subseteq\operatorname{Sink}(\theta)\) has cardinality \(d\). To see this, its \(d\) commuting flexes occur at distinct nonadjacent vertices \(A\), and precisely one of the \(2^d\) cube corners has every vertex of \(A\) as a sink. The no-isolated-vertices hypothesis guarantees that each such flex changes incident edge directions and yields a genuine cube axis. Conversely, any such pair determines a valid \(d\)-cube. This is the equivariant form of the cell indexing used in [1, Sections 2 and 4]. Every automorphism carries \((\theta,A)\) to \((g\theta,gA)\).

**2. Signed fixed-cell contributions.** Fix a total order of \(V\). Orient each cube by ordering its coordinate axes according to the corresponding vertices of \(A\), all directed from *sink* toward *source*. If \(g\) preserves a cell, then its unique all-sink corner is fixed, so \(g\theta=\theta\) and \(gA=A\). It permutes the cube axes according to its permutation of \(A\), without reversing any individual axis because sinks map to sinks. Hence that cube's contribution to the \(d\)-chain trace is exactly \(\operatorname{sgn}(g\mid A)\). The alternating trace on cubical chains is therefore
\[
L(g;F(G))=\sum_{\theta:g\theta=\theta}\;
\sum_{\substack{A\subseteq\operatorname{Sink}(\theta)\\gA=A}}
(-1)^{|A|}\operatorname{sgn}(g\mid A),
\]
by the cellular Lefschetz alternating-trace principle.

**3. Permutation-determinant cancellation.** For any fixed \(\theta\), set \(S=\operatorname{Sink}(\theta)\), a \(g\)-invariant set, and let \(P_{g,S}\) be the permutation matrix of \(g\) on \(\mathbb Q^S\). Expanding \(\det(I-P_{g,S})\) in principal minors gives exactly the inner sum above: a principal minor vanishes unless \(A\) is a union of \(g\)-orbits, in which case it is \(\operatorname{sgn}(g\mid A)\). For \(S=\varnothing\), the empty determinant is \(1\). For nonempty \(S\), the nonzero constant vector is a \(1\)-eigenvector of \(P_{g,S}\), so \(\det(I-P_{g,S})=0\). Thus each fixed orientation contributes one precisely when it is sinkless, and zero otherwise. This proves the character identity. Characters determine rational representations of finite groups after semisimplification, so it also proves the stated equality in \(R_{\mathbb Q}(\Gamma)\).

**4. Quotients.** For every finite subgroup \(H\), barycentric subdivision makes the cellular \(H\)-action simplicial. Rational transfer identifies the cohomology of the quotient with the \(H\)-invariant rational cohomology of the original complex, and hence
\[\chi(|F(G)|/H)=\frac1{|H|}\sum_{h\in H}L(h;F(G))
=\frac1{|H|}\sum_{h\in H}|\mathcal S(G)^h|=|\mathcal S(G)/H|,\]
with the last equality from Burnside's lemma. In particular the quotient Euler characteristic is nonnegative.

**5. Explicit orbit character.** A \(g\)-fixed edge orientation exists if and only if no orbit of an undirected edge returns with the endpoints interchanged. If an edge orbit reverses, there are no invariant orientations at all and the trace is zero. Suppose none reverses. A \(g\)-fixed orientation has a sink set that is a union of vertex orbits. Apply inclusion-exclusion to the \(g\)-orbits of vertices, where the event for a vertex orbit is that all of its vertices are sinks. A selected union \(B\) is feasible only if independent; it then forces every edge incident with \(B\) inward, while each \(g\)-orbit of edges entirely in \(V\setminus B\) admits two independent orientation choices. Hence the number of invariant orientations with every vertex of \(B\) a sink is \(2^{e_g(G[V\setminus B])}\). Its inclusion-exclusion sign is \((-1)^{c_g(B)}\), establishing the displayed finite orbit formula. Taking \(g=1\) recovers [1, Proposition 4.4].

## Verification
The standalone standard-library Python file `verify.py` independently enumerates graph automorphisms, all edge orientations, canonical cubical cells, signed fixed-cell traces, and sinkless fixed orientations on eleven graphs: a single edge, three- and four-vertex paths, a triangle, a square, a four-clique, a four-leaf star, a pentagon, a triangle with a leaf, two disjoint edges, and a square with a diagonal. Each group element was checked. As a **separate** computation, the code implements the explicit edge-orbit reversal test and the vertex-orbit inclusion-exclusion formula. It also counts sinkless-orientation orbits directly and independently checks the quotient Euler average. All tests passed with final line `VERIFY_OK graph_families=11`; the exact stdout is supplied as `verification_output.txt`. Execute `python3 verify.py` from the extracted package directory. These finite checks do not establish the theorem for arbitrary graphs; the determinant and inclusion-exclusion arguments do.

## Relationship to prior work
Kozlov [1] defines the flex cubical complex, establishes its cell indexing, and proves the **nonequivariant** Euler identity \(\chi(F(G))=|\mathcal S(G)|\) in Corollary 4.5. That formula is an essential established input and follows again when \(g=1\). The present result supplies the formerly absent **signed character at each automorphism**, its full virtual rational representation, an explicit vertex- and edge-orbit character formula, and quotient Euler invariants for arbitrary graph automorphism subgroups. Published work [2] calculates more detailed graded homology representations and actual quotients for **complete graphs alone**, not arbitrary graphs. Work [3] classifies connected components and flex distances for general graphs, not automorphism traces. Work [4] treats equivariant matrices for the **different ordinary discrete Morse matching complex**, not this cubical flex construction. Thus none of these statements provides the universal character formula by implication. The possibility of an unindexed equivalent or a general equivariant chain cancellation theorem is retained as an originality risk.

## Limitations
Only a virtual character identity is asserted; individual homology representations or a genuine equivariant homotopy equivalence with a discrete orientation set are **not** implied. Graphs with isolated vertices are excluded to avoid degenerate flex-coordinate conventions. The quotient assertion is about ordinary rational Euler characteristic, not a claim that every fixed-point space is discrete or that an arbitrary-group fixed-point Euler invariant equals the cardinality of fixed sinkless orientations. Primary-source review and indexed searches do not establish global uniqueness, and there has been no independent scientific audit.

## References
1. D. N. Kozlov, *Flex complexes of graphs*, *Journal of Applied and Computational Topology* **10**, article 10 (first published online 2026-05-23), DOI: 10.1007/s41468-026-00235-1. Full manuscript: https://link.springer.com/content/pdf/10.1007/s41468-026-00235-1.pdf. In particular Sections 2 and 4 and Proposition 4.4–Corollary 4.5.
2. *Equivariant homology and symmetry quotients of complete-graph flex complexes*, publicly indexed mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-equivariant-homology-and-symmetry-quotients-of-complete-graph-fl--d33423646847.
3. *A complete cycle-anchor invariant and geodesic formula for graph flexes*, publicly indexed mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-complete-cycle-anchor-invariant-and-geodesic-formula-for-graph--adc90e8a9935.
4. *Equivariant matrix–forest character formula for graph Morse complexes*, publicly indexed mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-equivariant-matrix-forest-character-formula-for-graph-morse-comp--0f531889a464.
