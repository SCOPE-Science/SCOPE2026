# Self-review

## Correctness
**PASS.** In a balanced study with \(m\) cases and \(m\) controls, Youden's index is exactly \((TP+TN-m)/m\), while the diagnostic odds ratio is \(TP\cdot TN/(FP\cdot FN)\). At fixed \(TP+TN=s>m\), the latter equals \(p/[p-m(s-m)]\) with \(p=TP\cdot TN\), so it strictly decreases as the sensitivity-specificity split becomes more balanced. Complete exact enumeration gives zero strict reversals through \(m=9\) and six at \(m=10\). The displayed witness and the all-\(m\) family are verified algebraically and by the packaged replay.

Risk: the minimum is a balanced finite-count boundary and should not be generalized to unequal case-control designs without a new analysis.

## Originality
**PASS.** Youden's original paper defines the index and its case-control-size invariance. Glas and coauthors explicitly present the diagnostic odds ratio as a separate prevalence-independent single indicator and list Youden's index in the same comparison framework. A later diagnostic-accuracy review discusses both measures and notes Youden's insensitivity to how sensitivity and specificity are split. Those sources motivate the comparison but do not state the sharp balanced finite-sample reversal threshold, first-layer count, or continuation family. Published-result, alias, exact-table, and implication searches did not locate equivalent coverage.

Risk: the formulas are classical and the finite problem is elementary enough that an unindexed teaching exercise or software test could contain the witness. Search failure is not a proof of bibliographic uniqueness.

## Value
**PASS.** Both measures are used as single prevalence-independent summaries of diagnostic discrimination, and the literature explicitly presents them as tools for comparing tests. The sharp boundary shows that even after balancing cases and controls and excluding zero-cell pathologies, the two summaries can make opposite comparative judgments because one is linear in sensitivity and specificity while the other multiplies their odds. The exact witness is a compact benchmark for interpretation and diagnostic-software validation.

Self-review: passed. Independent audit: not yet performed.
