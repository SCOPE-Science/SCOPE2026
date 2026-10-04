# Directional localization of the three- and four-dimensional hypercubes
## Finding
In the partial-feedback directional localization game, the binary hypercubes satisfy
\[
\operatorname{dirloc}(Q_3)=3,\qquad \operatorname{dirloc}(Q_4)=4.
\]
Thus the conjectural value \(\operatorname{dirloc}(Q_n)=n\) holds for the first two dimensions not settled by the elementary cases.

The upper bounds are constructive in the game-theoretic sense: there is a three-cop strategy on \(Q_3\) that wins in at most two probe rounds, and a four-cop strategy on \(Q_4\) that wins in at most three probe rounds. The complete finite policies are recorded in `strategy_certificate.json`.

## Assumptions and scope
The graph \(Q_n\) has vertex set \({0,1}^n\), with two vertices adjacent when they differ in exactly one coordinate. Vertices are encoded in the certificate by integers from \(0\) through \(2^n-1\), with bit \(i\) representing coordinate \(i\).

The game is the partial-feedback version introduced by Jones and Kinnersley. In each round the cops simultaneously probe vertices. If a probe equals the robber's current vertex, that probe identifies the robber. Otherwise the robber may answer that probe with any one neighbor of the probe lying on a shortest path from the probe to the robber. After all responses, if the robber's location is not uniquely determined, the robber may stay put or move to a neighboring vertex before the next round. The number \(\operatorname{dirloc}(G)\) is the least number of cops having a guaranteed winning strategy.

The claim is only about \(Q_3\) and \(Q_4\). It does not assert a strategy for \(Q_n\) when \(n\ge5\), and it does not concern a distinct full-feedback variant.

## Proof
Jones and Kinnersley prove that for every hypercube \(Q_n\), the directional localization number is either \(n\) or \(n+1\). In particular,
\[
\operatorname{dirloc}(Q_3)\ge3,\qquad \operatorname{dirloc}(Q_4)\ge4.
\]
It remains to prove matching upper bounds.

For a fixed number of cops, let \(R\) be the set of robber vertices still possible immediately before a probe round. For a simultaneous probe tuple \(P\) and a possible response tuple \(a\), let \(C(R,P,a)\subseteq R\) be the vertices for which every component of \(a\) is a legal partial-feedback response. If \(C(R,P,a)\) is a singleton, the robber has been located. Otherwise, after the robber's optional move, the next contaminated set is the closed neighborhood \(N[C(R,P,a)]\).

The file `strategy_certificate.json` supplies, for every reachable pair consisting of a contaminated set and a remaining-round budget, a simultaneous probe set. The root for \(Q_3\) probes the integer-encoded vertices \(0,3,5\); its complete policy has four state-budget pairs and wins within two rounds. The root for \(Q_4\) probes \(0,3,13,14\); its complete policy has twenty-seven state-budget pairs and wins within three rounds.

For every policy state, `verify.py` reconstructs every simultaneous response tuple that the robber can legally return from every currently possible vertex. It recomputes each exact consistency class \(C(R,P,a)\). Singleton classes are terminal wins. Every non-singleton class is expanded to the exact closed neighborhood allowed by the robber's stay-or-move step, and the resulting state is checked against a child certificate with one fewer remaining round. Hence every adversarial response branch is covered. This proves \(\operatorname{dirloc}(Q_3)\le3\) and \(\operatorname{dirloc}(Q_4)\le4\), which combine with the published lower bounds to give equality.

## Verification
`verify.py` is a standalone standard-library verifier. It does not search for a strategy; it checks the supplied finite strategy certificate directly against the game rules. On the packaged certificate it checks 81 legal response tuples for the \(Q_3\) policy and 1,790 legal response tuples for the \(Q_4\) policy, including every nonterminal transition. Its stored output is in `verification_output.txt` and ends with `ALL CHECKS PASSED`.

The computation is exhaustive for the two finite certified games, not a sampling argument. The published lower bound is used only to rule out two cops on \(Q_3\) and three cops on \(Q_4\); the computational certificate supplies only the matching upper bounds.

## Relationship to prior work
Jones and Kinnersley introduce the directional localization game in arXiv:2609.01745v1. Their hypercube result narrows \(\operatorname{dirloc}(Q_n)\) to \(n\) or \(n+1\), and their open-question section asks for the exact value, conjecturing \(n\). The inspected full text does not give exact values for \(Q_3\) or \(Q_4\).

Searches for the parameter name together with hypercube aliases, small cube dimensions, partial feedback, and the \(n\)-versus-\(n+1\) dichotomy found no published statement settling these two cases. Nearby hypercube records concern other invariants such as edge multiset dimension, mutual visibility, or monophonic position and therefore do not imply the claim here.

## Limitations
The result settles only the first two unsettled hypercubes and does not resolve the general hypercube question. The strategy trees establish existence of winning strategies with the stated round bounds; no claim is made that those round bounds are minimum. Because the initiating preprint is very recent, an unindexed or later follow-up could create literature overlap; no such overlap was found in the searches performed for this result.

## References
John Jones and William B. Kinnersley, “The directional localization game on graphs,” arXiv:2609.01745v1, first public 2026-09-01, https://arxiv.org/abs/2609.01745.
