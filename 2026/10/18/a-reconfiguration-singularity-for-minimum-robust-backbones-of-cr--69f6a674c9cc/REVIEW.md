# Scientific review

## Correctness — PASS

The claim distinguishes the exact graph, vertex-connectivity thresholds, domination, minimizer cardinalities, polynomial coefficients and token-jumping move rule. The proof reconstructs connectivity of bipartite matching deletions, treats the four-vertex disconnected exception, handles the exact equality threshold, and gives a constructive exchange proof when at least one index is unused. All stated boundary cases \(n\ge3\), \(2\le k\le n-1\) were checked. Direct exhaustive computations independently verify a finite range; they are not substituted for the proof.

## Originality — PASS, subject to bibliographic risk

The connected-domination reconfiguration literature in 2019 and 2022 establishes the token-move framework and general computational-complexity questions, but not this exact optimizer graph. The 2025 crown paper gives an induced-subgraph connectivity lemma and the ordinary connected domination minimum, so neither general crown connectivity nor the ordinary minimum is claimed to be new. That literature does not state the bivariate \(k\)-robust selection enumerator or classify the token-jumping graph of all minimum robust backbones. The one-hole phase transition uses a separate optimizer analysis and exchange proof, not merely the terminology of prior work. This assessment is based on actual cited queries and inspected portions of full primary sources; undiscovered reconfiguration results remain a risk.

## Value — PASS

The exact disconnected-to-connected-to-connected transition identifies a sharp brittleness threshold for optimal connected sensing/backbone choices, not merely another scalar graph invariant. It records how many optimal configurations are available, their permitted local adaptations, and the whole selection distribution for each robustness level. This is a natural complete classification for an infinite two-parameter family.

## Limits

No conclusions are asserted for domination after failure of selected vertices, non-minimum intermediate configurations, token sliding, or other graphs. All finite checks are evidence of consistency only. Independent review is pending.

Self-review: passed. Independent audit: not yet performed.
