# Exact agent-reconstruction fibers of two-agent \(\mathsf{S5}\) someone-knows bundles

## Finding
Let \(W\) be a nonempty finite labelled set and let \(E,F\) be equivalence relations on \(W\). For each \(U\subseteq W\), define the single bundled operation
\[
B_{E,F}(U)=\{w\in W:[w]_E\subseteq U\ \text{or}\ [w]_F\subseteq U\}.
\]
Call \((E,F)\) **transverse** if for each \(w\in W\), the two equivalence classes \([w]_E\) and \([w]_F\) are incomparable by inclusion. Let \(c(E,F)\) denote the number of equivalence classes of the join \(E\vee F\) (the transitive closure of \(E\cup F\)).

**Theorem (exact reconstruction fiber).** For every transverse ordered pair \((E,F)\), the set of **all** ordered pairs \((E',F')\) of equivalence relations on the **same labelled set** satisfying \(B_{E',F'}=B_{E,F}\) contains exactly \(2^{c(E,F)}\) elements. They are precisely those obtained by interchanging the two relations independently within each \((E\vee F)\)-component. Thus a join-connected transverse pair is determined up to one global agent exchange; the number of inequivalent reconstructions modulo that global exchange is \(2^{c(E,F)-1}\).

Every join component of a transverse pair has at least four worlds. Consequently such pairs exist exactly when \(|W|\ge4\), and the maximum reconstruction fiber over transverse pairs on \(n\ge4\) worlds is
\[
2^{\lfloor n/4\rfloor}.
\]
The first failure of identification up to one global agent exchange occurs at **eight** worlds, with four ordered reconstructions (two after global exchange).

## Assumptions and scope
The semantics of each individual knowledge modality is ordinary Kripke \(\mathsf{S5}\), so both relations are reflexive, symmetric and transitive. The whole Boolean operation \(B:\mathcal P(W)\to\mathcal P(W)\) is observable, meaning membership of each world in \(B(U)\) is known for **every** subset \(U\) of \(W\). This is stronger than equivalence of the formulas satisfied under a single fixed propositional valuation. Worlds remain individually labelled, whereas the two agent labels are hidden. All candidate representations, including potentially nontransverse ones, are included in the fiber. No assumption of properness (trivial intersection of individual relations) is imposed.

## Proof
**Step 1: recover the unordered two-class data at every world.** Given \(B\), consider
\[
\mathcal N_w=\{U\subseteq W:w\in B(U)\}.
\]
By definition \(\mathcal N_w=\uparrow\{[w]_E,[w]_F\}\). Since these two classes are incomparable, the set of inclusion-minimal elements of \(\mathcal N_w\) is exactly \(\{[w]_E,[w]_F\}\), and the two are distinct. If another pair \((E',F')\), with no transversality assumed in advance, has the same operator, its two classes at \(w\) must have the same two distinct inclusion-minimal generators. Hence it is transverse and
\[
\{[w]_{E'},[w]_{F'}\}=\{[w]_E,[w]_F\}\quad\text{for every }w.
\]
This is equality of subsets of the fixed set \(W\), not merely equality of cardinalities.

**Step 2: the recovered incidence multigraph.** Collect all distinct sets occurring in the recovered pairs into a vertex set \(\mathcal C\). For each world \(w\), place a labelled edge \(w\) between its two distinct recovered sets. Call the resulting loopless multigraph \(H\); parallel edges are allowed. Each \(E\)-block and each \(F\)-block is a vertex of \(H\). No \(E\)-block equals any \(F\)-block: equality would imply equality of the two classes at a world in that block, contradicting transversality. The original division of vertices into \(E\)-blocks and \(F\)-blocks therefore makes \(H\) bipartite.

Any alternative representation from Step 1 supplies a proper two-colouring of \(H\): give the same colour to blocks belonging to the same equivalence relation; the endpoints of each labelled edge receive different colours. Conversely, **every** proper two-colouring of \(H\) yields two equivalence partitions. Indeed, vertices of a fixed colour are pairwise disjoint subsets of \(W\), because any world belonging to two such vertices would create an edge between them. They jointly cover \(W\), because every edge has one endpoint of each colour. Thus each colour consists of the blocks of an equivalence relation. At world \(w\) its two blocks are exactly the endpoints of edge \(w\); the reconstructed pair consequently gives precisely the same \(B\). Distinct ordered colourings give distinct ordered pairs, because the classes are determined by their subsets of \(W\).

**Step 3: count colourings.** A connected bipartite multigraph with at least one edge has exactly two proper two-colourings: choose one vertex colour, then all others are forced by edge paths. Every vertex of \(H\) belongs to at least one labelled edge because its block is nonempty. Therefore if \(H\) has \(c_H\) components, it has exactly \(2^{c_H}\) proper two-colourings. Two worlds lie in the same \(E\vee F\)-class exactly when they can be linked by a chain of worlds in which consecutive worlds share an \(E\)- or \(F\)-block. Such a chain is equivalent to an edge-path within one connected component of \(H\), so \(c_H=c(E,F)\). Exchanging the colours independently on each component is exactly exchanging the two agent relations within each join component. The global interchange acts freely on the set of colourings and pairs them into \(2^{c-1}\) orbits.

**Step 4: sharp finite size.** Every vertex of \(H\) meets at least two *distinct* vertices on the other side. If an \(E\)-block met only one \(F\)-block, it would be contained in that \(F\)-block, violating transversality; the converse is symmetric. Thus every connected component of \(H\) has at least two vertices of each colour and at least four edges, i.e. at least four worlds. Hence \(n\ge4c\) and \(2^c\le2^{\lfloor n/4\rfloor}\).

For sharpness, take \(c=\lfloor n/4\rfloor\) disjoint grids of four worlds indexed by \((i,j)\in\{0,1\}^2\). In each grid let \(E\) identify equal row indices and \(F\) identify equal column indices. Each recovered incidence component is \(K_{2,2}\), which is transverse. Distribute any remaining \(n-4c\) worlds by duplicating one existing grid cell in the first component (the new worlds belong to both that row and that column). This does not alter either transversality or the number of connected components. The fiber therefore has exactly \(2^c\) members. At \(n=8\), swap agents in only one of the two grids: that gives the same bundled operator but neither the original ordered pair nor its global reversal. If \(n\le7\), then transversality forces \(c=1\), so global exchange is the only ambiguity. For \(n<4\), no transverse pair exists. \(\square\)

## Verification
Run `python3 verification/check_bundled.py` with a standard Python 3 interpreter (no third-party packages). The program generates **every set partition** of a labelled \(n\)-element carrier for \(n=1,\ldots,6\), every ordered pair of partitions, and the full \(2^n\)-input truth table of the bundled operation. It groups equal operations and tests that any fiber containing a transverse pair contains no nontransverse pair and has cardinality exactly \(2^{c(E,F)}\). It reports respectively \(1,4,25,225,2704,41209\) ordered partition pairs, with transverse-pair counts \(0,0,0,6,60,630\); all assertions passed. A separate construction checks maximal-ambiguity examples on \(4,\ldots,12\) worlds, including a genuinely nonglobal eight-world exchange, and directly checks the two local minimal generators in each construction. These are finite consistency checks, not substitutes for the general proof above.

## Relationship to prior work
Ågotnes and Wáng (2021), Section 4, introduced the neighborhood-core semantics of the somebody-knows operator and proved that an unlabelled neighborhood frame admits an agent-indexed relational interpretation; minimal neighborhood generators are therefore **not** claimed new here. Ding, Liu and Wang (2023) connect the operator to hypergraphs, weak aggregation and coloring axioms; the accessible publisher preview does not resolve exact inverses of two \(\mathsf{S5}\) equivalence partitions. Ding and Yang (2026), Sections 3 and 5.1, establish general bundled bisimulation machinery and a complete \(\mathsf{S5}\) axiomatization. Those results concern expressive equivalence, axioms and existence of representations, rather than the **number and structure of all ordered representations on a fixed labelled carrier**. Chromatic simplicial-complex correspondence likewise treats equivalence of **already colored** multi-agent frames with chromatic complexes, rather than recovery of the hidden colouring from a bundled operation. The additional assertion proved here is that the \(\mathsf{S5}\) coherence constraints turn local unordered generators into a bipartite incidence graph with exactly \(2^c\) global agent assignments, with an optimal size threshold.

## Limitations
Transversality is essential to the stated classification: when one agent class contains the other at a world, the bundled operation can conceal the larger class entirely. No classification of such degenerate fibers is asserted. The count is for labelled worlds and **ordered** agent relations; an unordered or isomorphism-quotient census requires additional group actions. Equality of the full powerset operator must not be confused with modal equivalence under a fixed finite vocabulary or valuation. The 2023 journal paper's full text was not accessible through the permitted sources; an equivalent unindexed special-case reconstruction theorem remains an originality risk.

## References
1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268 (first public version, 2026-03-27), especially Sections 2, 3 and 5.1. https://arxiv.org/abs/2603.26268 ; https://doi.org/10.4204/EPTCS.447.17
2. Thomas Ågotnes and Yì N. Wáng, *Somebody Knows*, KR 2021, pp. 2–11, especially Definitions 2–4 and Lemmas 2–6. https://doi.org/10.24963/kr.2021/1
3. Yifeng Ding, Jixin Liu and Yanjing Wang, *Someone Knows That Local Reasoning on Hypergraphs is a Weakly Aggregative Modal Logic*, Synthese 201 (2023), 46. https://doi.org/10.1007/s11229-022-04032-y (publisher preview only inspected).
4. Éric Goubault, Roman Kniazev and Jérémy Ledent, *A Many-Sorted Epistemic Logic for Chromatic Hypergraphs*, CSL 2024. https://doi.org/10.4230/LIPIcs.CSL.2024.30
