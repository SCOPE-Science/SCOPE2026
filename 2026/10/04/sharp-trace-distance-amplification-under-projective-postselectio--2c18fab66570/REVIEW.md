# Same-model review

## Correctness
**PASS.** The proof was reconstructed from the definitions. Pinching is a completely positive trace-preserving map, so the trace distance of the pinched states cannot exceed the original distance. The accepted and rejected blocks are orthogonal, hence their trace norms add. Their trace imbalances both have magnitude \(d=|p-q|\). For \(p\ge q\), the triangle inequality gives \(\delta_P\ge pc-d/2\), while the trace imbalance gives \(\delta_P,\delta_Q\ge d/2\). Therefore the global distance is at least \(\max\{d,pc\}\). The swapped case is identical. The diagonal three-level family attains the envelope exactly.

The packaged numerical checker independently stress-tests random noncommuting states/projectors and the exact equality family. The checker is corroborative; the universal result is analytic.

## Originality
**PASS.** The closest source, arXiv:2609.33567v1, has exactly the same projector-postselection setup but Theorem 6 bounds the normalized distance by a numerator containing \(\tau+|p-q|/2\). Its sharpness discussion uses equal acceptance and therefore does not settle the unequal-acceptance coefficient. Full-text inspection of arXiv:2011.08487v1 and arXiv:2110.02290v5 found broader postselected-operation metrics and conversion/renormalization machinery, but not an implication of the exact \(\tau/\max\{p,q\}\) state-pair envelope. Targeted literature and published-finding searches found no equivalent statement.

Residual risk: because the sharp witness is commuting and the proof uses only trace-norm structure, an equivalent classical conditioning inequality could exist in older probability literature under different terminology. No such source was located in the targeted searches.

## Value
**PASS.** The result sharpens a live 2026 postselection-stability theorem at the point where unequal acceptance probabilities previously cost an additional term. The sharp formula is useful for noise budgets because it distinguishes unavoidable inverse-acceptance amplification from mere acceptance mismatch and identifies the exact worst-case constant. The all-parameter equality family makes the improvement a boundary theorem rather than a routine tightening without an optimality interpretation.

## Closest literature and limitations
The closest direct comparison is Theorem 6 of arXiv:2609.33567v1. Gavorová's arXiv:2011.08487v1 and Shi--Waks arXiv:2110.02290v5 are broader at the postselected-operation level but do not dominate the claim. The theorem here is restricted to one common orthogonal projector and finite-dimensional states; arbitrary effects, different postselection maps, and multistage compositions are not covered.

Same-model review: passed. Independent audit: not yet performed.
