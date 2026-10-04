# Review of Exact uniform released packing on complete bipartite graphs

## Correctness
**PASS.** The proof partitions all feasible functions into four exhaustive cases according to whether the two bipartition sides contain a vertex at the upper bound \(u\). In each case, the released condition reduces to a side-sum inequality that gives the stated upper bound, and the proof supplies an explicit attaining assignment. The both-saturated case correctly requires \(k\ge2u\), because each saturated side contributes at least \(u\) to the other side's active closed-neighborhood sum. No infinite conclusion is inferred from the finite computation.

The standalone verifier reconstructs the released condition from the definition and exhaustively compares the formula against all assignments for \(1\le a,b\le3\), \(1\le u\le3\), and \(0\le k\le u(a+b+1)\).

## Originality
**PASS.** The initiating preprint arXiv:2608.11169v1 introduces the invariant, gives complexity and polyhedral results, and discusses paths, cycles, and wheels, but does not state an arbitrary-\((a,b,k,u)\) complete-bipartite formula. Searches for the invariant together with complete-bipartite, biclique, saturation, and conditional-capacity terminology found no covering result. A contemporary review, pith:6OPKYP2C, already identifies a \(P_3\) counterexample to the preprint's Observation 2.2(iii); therefore the present claim does not count the mere falsity of that observation as original. The new content is the exact four-phase formula on all complete bipartite graphs.

The principal residual risk is terminological: an older optimization result could encode the same formula without using the 2026 invariant name. No such result was located, and older classical packing results impose constraints at every vertex, so they do not directly imply this conditional-saturation formula.

## Value
**PASS.** Complete bipartite graphs are a canonical dense bipartite family, and the theorem gives a full exact non-binary phase diagram for the newly introduced released-packing rule on that family. It separates the four qualitatively different saturation regimes and, at \(k=u\), quantifies the broad failure of an optimality assertion made in the initiating paper rather than supplying only an isolated counterexample. The result is a reusable benchmark for testing formulations and for comparing released and classical packing behavior.

## Closest literature and limitations
The closest source is arXiv:2608.11169v1 itself. Its Proposition 3.3 identifies the special case \(u=1\) with dependent sets, but that does not cover general \(u\). Its general ILP formulation can compute instances but does not imply the closed biclique formula without the structural argument given here. The public review pith:6OPKYP2C overlaps only with the fact that Observation 2.2(iii) is false, not with the all-parameter classification.

Same-model review: passed. Independent audit: not yet performed.
