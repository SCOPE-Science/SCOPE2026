# Correcting the internal Shapley term for directed trust games

## Finding

Let \(G=(N,E)\) be a finite simple directed graph with arc weights \(a_{pq}\in[0,1]\). In the trust game of Ryzák and Kroupa, write the coalition worth as \(v=v_{\mathrm{int}}+v_{\mathrm{ext}}\), where

\[
v_{\mathrm{int}}(S)=\sum_{(p,q)\in E,\ p,q\in S}a_{pq}
\]

is the internal term and \(v_{\mathrm{ext}}\) is the stated external-minimum term. For every player \(i\in N\), the internal contribution to the Shapley value is

\[
\phi_i(v_{\mathrm{int}})=\frac12\sum_{j:(i,j)\in E}a_{ij}+\frac12\sum_{j:(j,i)\in E}a_{ji}.
\]

Thus every directed arc contributes half its weight to each endpoint, whether or not its reverse arc exists. The first term displayed in Corollary 3.3 of the 2026 preprint counts only reciprocal pairs and omits positive one-way arcs. In the directed cycle \(1\to2\to3\to1\) with every arc weight equal to \(1\), the displayed formula gives \(0\) for each player, whereas the exact Shapley value is \(1\) for each player.

Equivalently, the corrected total value is \(\phi_i(v)=\phi_i(v_{\mathrm{int}})+\phi_i(v_{\mathrm{ext}})\), with the internal term replaced by the all-incident-arcs expression above. This finding concerns that internal term; it does not assert a correction to every other formula in the source.

## Assumptions and scope

The graph is finite and loopless; arc weights are nonnegative. The characteristic function is the trust game defined in Definition 2.1 of Ryzák and Kroupa (2026), whose internal component sums the weights of all directed arcs with both endpoints in the coalition. The Shapley value is the standard transferable-utility value. The result is independent of tie-breaking among equal incoming weights because the internal term does not use the incoming-weight ordering.

## Proof

For each arc \((p,q)\in E\), define the two-player unanimity game \(u_{\{p,q\}}(S)=1\) when \(p,q\in S\), and \(0\) otherwise. Then

\[
v_{\mathrm{int}}(S)=\sum_{(p,q)\in E}a_{pq}u_{\{p,q\}}(S).
\]

By linearity of the Shapley value, it suffices to compute the value of one summand. In a unanimity game supported on two distinct players, each of those players is pivotal in exactly half of the two possible relative orders; equivalently, the Shapley value assigns \(1/2\) to each endpoint and \(0\) to every other player. Hence arc \((p,q)\) contributes \(a_{pq}/2\) to player \(p\) and \(a_{pq}/2\) to player \(q\). Summing over all arcs proves the formula.

The source's Corollary 3.3 instead includes only arcs whose reverse is also present. On the directed 3-cycle with unit weights, the internal value is \(1\) for each player: each vertex is incident to two directed arcs, each contributing \(1/2\). For the external component, every singleton coalition has value \(1\), every two-player coalition has external value \(1\), and the grand coalition has external value \(0\). The external Shapley value is therefore \(0\) for each player (the marginal contributions across the three positions are \(1,0,-1\)). The full coalition worths are \(v(\varnothing)=0\), \(v(\{i\})=1\), \(v(\{i,j\})=2\), and \(v(N)=3\); each player's marginal contribution is \(1\) in every position, so the exact total Shapley value is \(1\). With no reciprocal arcs, the printed internal term is zero, giving the stated discrepancy.

## Verification

The included `verify_trust_game.py` uses exact rational arithmetic. It checks all eight coalitions of the three-player witness, enumerates all six player orders, computes the internal and external Shapley components separately, and confirms that the corrected formula gives \(1\) per player while the reciprocal-only term gives \(0\). The computation is a finite exact check of the witness; the general identity is proved above by unanimity-game linearity.

## Relationship to prior work

Bandhana, Kroupa, and García (AAMAS 2024) introduced the same trust-game construction and define internal trust as the sum of local trust weights on all arcs within a coalition. Ryzák and Kroupa (arXiv:2605.18157v1, 18 May 2026) restate this internal term and express it as a sum of two-player unanimity games in Lemma 3.2, but the reciprocal-edge-only term in their Corollary 3.3 does not account for one-way arcs. The correction follows from the standard Shapley value of a two-player unanimity game; the source-specific contribution here is the exact identification of the omitted term and the three-cycle witness. published-finding corpus semantic searches and the accessible research ledger found no directly matching correction; those searches do not establish global novelty.

## Limitations

The result corrects the internal contribution in the displayed Corollary 3.3 and demonstrates its consequence on one exact witness. It does not assess unrelated claims in the preprint, establish any empirical effect on peer-ranking data, or constitute an independent audit. A later author revision or correction could change the source text; the inspected version is arXiv v1.

## References

1. David Ryzák and Tomáš Kroupa, “A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value,” arXiv:2605.18157v1, first public version 18 May 2026. Relevant locations: Definition 2.1, Lemma 3.2, and Corollary 3.3.
2. Arti Bandhana, Tomáš Kroupa, and Sebastián García, “Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network,” Proceedings of the 23rd International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2024), pp. 132–140, DOI 10.5555/3635637.3662860. Relevant location: Section 3, Definition 3.1.
3. Mathematics Subject Classification 2020, code 91A12 (Cooperative games).
