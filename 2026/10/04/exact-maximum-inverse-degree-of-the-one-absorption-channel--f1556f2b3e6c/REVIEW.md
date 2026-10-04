# Same-model review

## Correctness
**PASS.** Every parent is either an ordinary insertion supersequence of the received word or arises from a genuine split in which neither input symbol equals the absorbed output. The insertion sphere has exactly \(q+(n-1)(q-1)\) members, and each received symbol has at most \(\binom{q-1}{2}\) genuine splits. The saturated word attains both contributions without overlap. `verify.py` independently reconstructs the channel in forward and inverse directions and checks the finite instances reported in `verification_output.txt`.

## Originality
**PASS.** The primary full text, its zero-deletion hypergraph section and conclusion, the closest later absorption-code abstract, targeted public searches, published-results searches under inverse-ball/preimage/list-size/degree aliases, and the previously published finding set were compared. No inspected statement implies the exact incoming-degree formula. The closest previously published absorption finding concerns short ternary correcting-code cardinalities, a different invariant. The main residual risk is the unavailable full text of the 2024 follow-up and unindexed or differently phrased literature.

## Value
**PASS.** The maximum number of possible transmitted parents of a fixed received word is the worst-case ambiguity of the channel and the maximum incoming degree of its incidence graph. The result is an exact all-\(q\), all-\(n\) structural law with an explicit extremizer, not a routine finite increment. It does not claim an optimal code-size consequence or solve the distinct forward-ball problem.

Same-model review: passed. Independent audit: not yet performed.
