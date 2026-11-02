# Three-agent knowing: the sharp six-world Latin-square ambiguity

## Finding
Fix a nonempty finite labelled set of worlds \(W\), and three equivalence relations \(E_1,E_2,E_3\) on \(W\). Their anonymous *someone-knows* operator is
\[
S(X)=\{w\in W:\exists i\in\{1,2,3\},\ [w]_{E_i}\subseteq X\}\qquad (X\subseteq W).
\]
Assume **local irredundancy**: at every world the three equivalence classes are pairwise incomparable by inclusion. Form a simple graph \(G\) whose vertices are the distinct blocks appearing in the three partitions, with an edge whenever two distinct blocks intersect.

**Reconstruction theorem.** Every ordered triple of equivalence relations on the same labelled \(W\) that induces exactly the same operator \(S\), even without an a priori irredundancy assumption, corresponds bijectively to a proper three-colouring of \(G\). Thus the exact number of realizations is the chromatic-polynomial evaluation \(P_G(3)\). The equality is of Boolean set operators for all inputs and therefore also preserves every nested formula in the single bundled-modality language under every valuation.

**Sharp finite threshold.** For \(1\le |W|\le5\), every locally irredundant three-agent operator has precisely six ordered realizations whenever one exists. At \(|W|=6\) there are exactly \(825\) such operator signatures: \(815\) admit six realizations and \(10\) admit twelve. Those ten exceptional signatures are precisely the sets of all nine edges of a labelled complete bipartite graph \(K_{3,3}\) on \(W\); the twelve ordered realizations correspond to its twelve proper three-edge-colourings (the order-three Latin squares). In each exceptional case the join of the three equivalence relations is connected, but the realization is not unique modulo global agent permutation. Hence six worlds is the least size permitting this connected nonidentifiability.

## Assumptions and scope
Worlds are **fixed and labelled**. All three agent accessibility relations are equivalence relations (\(\mathsf{S5}\)). All propositional valuations are allowed, and the only observable modality is anonymous \(S\), not any individual agent's box. Local irredundancy means that for each \(w\), no one of the three sets \([w]_{E_i}\) contains any other. The graph \(G\) is an ordinary simple intersection graph of the **distinct** class-sets; a world creates a triangle among its three classes. The chromatic polynomial counts colourings with three specified colours, not colourings modulo permutation.

## Proof
1. **Recover the local minima.** For each world \(w\), the family \(\{X\subseteq W:w\in S(X)\}\) is upward closed. Its inclusion-minimal elements are exactly the three pairwise incomparable sets \([w]_{E_1},[w]_{E_2},[w]_{E_3}\). Hence equality of bundled operators uniquely recovers the unordered triple of blocks at each world. Any alternate *three*-agent realization must use precisely these three blocks at each world; in particular it is automatically locally irredundant.

2. **Colour consistency.** Regard each recovered distinct block as a vertex. In any realization, a block assigned to one agent is that agent's equivalence class at every world in the block, so the block has a single agent colour throughout. Intersecting distinct blocks cannot receive the same colour: two distinct classes of one equivalence relation are disjoint. Thus every realization gives a proper three-colouring of \(G\).

3. **Converse.** Every world belongs to exactly three distinct recovered blocks, forming a triangle in \(G\). In a proper three-colouring, this triangle receives all three colours. Thus each colour class of vertices partitions \(W\) into pairwise disjoint, nonempty subsets covering every world exactly once. Take these three partitions as three equivalence relations. Their unordered triples of local classes agree with the recovered triples, so their bundled operators agree pointwise for all input subsets. The two constructions are inverse. This proves the chromatic-polynomial formula for every finite \(W\).

4. **Sharp six-world census.** The accompanying standalone `checker.py` enumerates every labelled set partition of \(\{0,\ldots,n-1\}\) exactly once, by adding the last element as a singleton or to each existing block. For each ordered triple of partitions it computes all three classes at each world, retaining it exactly when the three local classes are incomparable. It groups these triples by the resulting unordered local triple at every world. The exhaustive finite certificate reports no irredundant cases below four worlds; at four worlds one signature of size six; at five worlds thirty signatures all of size six; and at six worlds \(825\) signatures of which \(815\) have size six and \(10\) have size twelve. It also checks, for every size-twelve signature, that its nine distinct recovered blocks are precisely the nine two-element edges of a labelled \(K_{3,3}\). There are \(\binom63/2=10\) such bipartitions. The proper three-edge-colourings of \(K_{3,3}\) are bijective with order-three Latin squares, of which there are twelve (choose the first row in six ways and then one of two cyclic orientations). All three equivalence relations join to a universal relation because the nine edges form a connected \(K_{3,3}\). The twelve ordered realizations break into two distinct orbits under the six permutations of agent names, proving the connected ambiguity and minimality.

5. **Explicit witness.** On \(W=\{0,1,2,3,4,5\}\), take the three partitions
\[
\begin{aligned}
\mathcal P_1&=\{\{0,4\},\{1,2\},\{3,5\}\},\\
\mathcal P_2&=\{\{0,1\},\{2,3\},\{4,5\}\},\\
\mathcal P_3&=\{\{0,3\},\{1,5\},\{2,4\}\}.
\end{aligned}
\]
Their nine blocks are the edges of a \(K_{3,3}\), so the operator has exactly twelve ordered decompositions despite connected joint accessibility. Since each is a different ordered choice of partitions, exactly two remain after globally permuting the three agent names.

## Verification
Execute `python3 checker.py` using Python 3.9 or later. It exhaustively compares all ordered partition triples through six worlds (there are \(203^3=8{,}365{,}427\) for six worlds) and checks the complete fiber-size distribution. It independently verifies the \(K_{3,3}\) description of every exceptional signature, directly enumerates the twelve proper three-colourings of its nine-block intersection graph, and compares the minimal-generator interpretation with all \(64\) Boolean input sets for an explicit witness. Expected final output: `ALL_CHECKS_OK`. This finite certificate proves only the declared cutoff census; the all-size graph reconstruction is an abstract argument given above.

## Relationship to prior work
Ågotnes and Wáng (2021) introduced and analysed the somebody-knows modality and its neighbourhood semantics. Ding, Liu and Wang (2023) developed a hypergraph and weak-aggregation framework; the freely accessible publisher abstract discusses representation, not this exact six-world inverse census. Ding and Yang (2026, Section 5.1) give semantics and an axiomatization of the someone-knows bundle on \(\mathsf{S5}\) models. Their generated-neighbourhood treatment supports recovery of minimal neighbourhood data, but does not state this realization enumeration or the order-three Latin-square threshold. The familiar two-agent bipartite colouring argument is not enough: already for three agents, a connected overlap graph can admit more than six proper colourings. The new part is the sharp six-world transition and complete finite classification for three anonymous equivalence relations.

## Limitations
This result is restricted to locally irredundant triples; if one agent's local class contains another's, its contribution can be observationally redundant and the formula need not apply. The assertion of a first threshold is proved in the sense of fixed labelled finite frames and this exact bundled operator, not arbitrary modal equivalence on different carriers. The six-world census has a replayable exhaustive finite certificate rather than a case-free hand classification. The 2023 journal full text was not available for complete priority checking; an older equivalent formulation under different terminology cannot be excluded. No independent review has been performed.

## References
1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268 (first posted 27 March 2026), esp. Sections 3 and 5.1; https://arxiv.org/html/2603.26268v2.
2. Thomas Ågotnes and Yì N. Wáng, *Somebody Knows*, KR 2021, DOI:10.24963/kr.2021/1; https://proceedings.kr.org/2021/1/.
3. Yifeng Ding, Jixin Liu and Yanjing Wang, *Someone knows that local reasoning on hypergraphs is a weakly aggregative modal logic*, Synthese 201, article 46 (2023), DOI:10.1007/s11229-022-04032-y; https://link.springer.com/article/10.1007/s11229-022-04032-y.
