# Same-carrier reconstruction and sharp agent ambiguity for anonymous \(\mathsf{S5}\) knowledge

## Finding

Write \(\Phi_{E,G}(S)=\{w\in W:[w]_E\subseteq S\text{ or }[w]_G\subseteq S}\) for the anonymous two-agent knowledge operator of a pair of \(\mathsf{S5}\) equivalence relations. In the nonredundant two-generator case, \(\Phi_{E,G}\) determines its ordered fixed-carrier representations up to independent exchanges of agents on connected components of a recoverable incidence graph.

Precisely, the operator is realizable by such a pair **if and only if** the minimal supports persist at every world they contain and their incidence graph is bipartite. For \(c\) components, it admits exactly \(2^c\) ordered representations and \(2^{c-1}\) up to a single global agent exchange. On \(n\ge4\) labelled worlds the maximum is \(2^{\lfloor n/4\rfloor}\) ordered representations, and eight worlds are necessary and sufficient for two genuinely different representations modulo the global exchange.

## Assumptions and scope

Fix a finite nonempty set \(W\), \(n=|W|\), and a monotone \(F:\mathcal P(W)\to\mathcal P(W)\). Define its **minimal knowledge supports** at \(w\) by
\[
\mathcal A_w=\min_{\subseteq}\{S\subseteq W:w\in F(S)}.
\]
Assume \(|\mathcal A_w|=2\) and \(w\in B\) for every \(B\in\mathcal A_w\) and every \(w\in W\). The two supports are incomparable because they are distinct minimal elements. Let \(\mathcal B=\bigcup_{w\in W}\mathcal A_w\). Build a finite multigraph \(H\) with vertex set \(\mathcal B\); each world \(w\) contributes one (possibly parallel) edge joining the two distinct members of \(\mathcal A_w\). No edge is a loop. Let \(c\) be the number of connected components of \(H\).

Call the supports **stable** when
\[
\forall w\in W\;\forall B\in\mathcal A_w\;\forall v\in B:\quad B\in\mathcal A_v.
\]
All representations count pairs of equivalence relations on **exactly** \(W\), without extra worlds, quotienting, or a surjective map from another frame. Pair order distinguishes the two agents; the separate quotient by the one global agent swap is explicitly indicated.

## Proof

**Minimal recovery.** Finiteness and monotonicity imply, for all \(w\) and \(S\subseteq W\), that
\[
w\in F(S)\quad\Longleftrightarrow\quad (\exists B\in\mathcal A_w)\;B\subseteq S.
\]
Indeed, from \(w\in F(S)\) choose a minimal contained witness, and the converse follows from monotonicity. Thus the full operator is determined by the two-element families.

**Necessity.** Suppose \(F=\Phi_{E,G}\) for equivalence relations \(E,G\). For each \(w\), \(\mathcal A_w=\{[w]_E,[w]_G}\), since the two classes generate the upward-closed truth family. They must be distinct and incomparable by the hypothesis that there are exactly two minimal supports. A partition block \(B=[w]_E\) persists as the \(E\)-block at every \(v\in B\), so stability holds, and likewise for \(G\). Color each vertex of \(H\) by whether it is an \(E\)-block or a \(G\)-block. A block cannot occur in both partition families: if \(B\) were such, at any \(w\in B\) the two equivalence classes would coincide, contradicting \(|\mathcal A_w|=2\). Hence this is a consistent proper two-coloring of \(H\), which is bipartite.

**Sufficiency.** Suppose stability holds and \(H\) admits a proper two-coloring. Let \(\mathcal P_0\) and \(\mathcal P_1\) be its two color classes, interpreted as families of subsets of \(W\). Every \(w\) belongs to exactly one member of \(\mathcal P_i\): its two incident supports contain \(w\) and have opposite colors, establishing existence; if two distinct blocks \(B,C\in\mathcal P_i\) both contained \(v\), stability implies \(B,C\in\mathcal A_v\), so they are joined by the edge labelled \(v\), contradicting equal colors. Thus \(\mathcal P_0\) and \(\mathcal P_1\) each partition \(W\). Their induced equivalence relations satisfy \(\mathcal A_w=\{[w]_E,[w]_G}\) at every \(w\), so the minimal-recovery identity gives \(F=\Phi_{E,G}\) on all subsets.

**Exact fiber.** Every ordered pair representing \(F\) colors the recovered graph, while every proper two-coloring constructs such a pair. These maps are mutually inverse because every vertex of \(H\) is a nonempty support block. Each connected bipartite component has exactly two proper two-colorings. There are therefore exactly \(2^c\) ordered representations. The global agent-swap involution acts freely (the two families never agree at any world), and it pairs every coloring with its complement, leaving \(2^{c-1}\) inequivalent ordered pairs.

**Sharp number of components.** Fix any vertex \(B\) of \(H\), say a block of the first partition. If all worlds in \(B\) belonged to the same block \(C\) of the other partition, then \(B\subseteq C\), contradicting incomparable minimal supports at any world of \(B\). Consequently \(B\) meets at least two distinct opposite-color blocks. In particular, every graph component has at least two vertices of each color. Every block is nonempty, and in fact every block contains at least two distinct worlds, because it meets an incomparable block at one world and has another world outside that block. Select two disjoint first-color blocks in each component: together they contain at least four worlds. Distinct components have disjoint unions of worlds since each world-edge stays in one component. Hence \(n\ge4c\).

For \(n=4q+r\), where \(q\ge1\) and \(0\le r\le3\), take \(q\) disjoint four-world grids: inside each grid the first partition is the two rows and the second partition is the two columns. Add any \(r\) remaining worlds to a fixed row-column intersection of the first grid. Every world still has exactly two incomparable supports, and \(H\) has precisely \(q=\lfloor n/4\rfloor\) components, proving sharpness. For \(n<4\), no operator satisfying the two-support hypotheses can be represented. For \(n<8\) every represented operator has \(c=1\), so its only two ordered representations differ by global exchange; at \(n=8\) two disjoint grids give \(c=2\) and two representations modulo global exchange.

**Odd-cycle boundary.** On \(W=\{0,1,2}\), prescribe \(\mathcal A_0=\{\{0,1},\{0,2}}\), \(\mathcal A_1=\{\{0,1},\{1,2}}\), and \(\mathcal A_2=\{\{0,2},\{1,2}}\), and reconstruct \(F\) from these minimal supports. All support families are stable and individually reflexive, but \(H\) is a triangle. Therefore no two equivalence relations on the same three worlds realize \(F\). This also demonstrates that stability without bipartiteness is insufficient.

## Verification

Run \(\texttt{python checker.py}\) using Python 3. The standalone exact-arithmetic checker constructs every labelled set partition and every ordered partition pair for carrier sizes \(1\) through \(6\). It groups pairs by their complete operator truth tables and independently reconstructs all representations from minimal supports and bipartite colorings. For two-support operators, the recovered fiber is compared with the entire enumerated fiber. It also checks the three-world odd cycle and the eight-world pair of disconnected grids. The completed run ended with \(\texttt{ALL_CHECKS_OK}\). The abstract proof above, rather than finite computation, establishes the all-size conclusion.

## Relationship to prior work

Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities* (arXiv:2603.26268, first public 2026-03-27), §5.1 and Lemma 5.5, establish a representation theorem and completeness for the “someone knows” bundle on \(\mathsf{S5}\). Their construction uses an unraveling onto a potentially larger set of worlds and does not give fixed-carrier identifiability or the exact \(2^c\) representation fiber. Ågotnes and Wáng, *Somebody Knows* (KR 2021), develop minimal neighborhood semantics and general correspondence with agent-indexed relational models, without the present two-equivalence-partition incidence classification in the inspected text. The result also has a dual description as the ambiguity of a union of two partition-interior operators, which was considered in terminology searches.

## Limitations

This is a theorem about complete finite **set operators** \(F:\mathcal P(W)\to\mathcal P(W)\), not identification from a finite list of formulas under one fixed valuation. It requires exactly two minimal incomparable supports at **each** world. Cases with a redundant agent, a variable number of minimal supports, more than two agents, or expanded-world modal representations are not classified. Historical originality outside the inspected primary literature, including older partition-incidence or interior-operator formulations, is not independently certified.

## References

1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268, version 1 submitted 2026-03-27; version 2 posted 2026-06-30, §5.1 and Lemma 5.5. https://arxiv.org/abs/2603.26268 ; https://arxiv.org/html/2603.26268v2 .
2. Thomas Ågotnes and Yì N. Wáng, *Somebody Knows*, *Proceedings of KR 2021*, pp. 2–11, DOI:10.24963/kr.2021/1. https://proceedings.kr.org/2021/1/ .
