# Review

## Correctness

PASS. The SPD quadratic decouples orthogonally into scalar curvature modes. The modal Grokfast-EMA state matrix has an exact quadratic characteristic polynomial, and the degree-two Schur conditions leave one and only one nontrivial inequality. The boundary produces an exact \(-1\) root, so the condition is both necessary and sufficient.

Risk: the formula is specific to plain gradient descent as the base optimizer and to constant parameters.

## Originality

PASS. The defining Grokfast paper gives the EMA amplifier, transfer-function viewpoint, hyperparameter recommendations, and linear-filter equivalence, but the inspected full text contains no quadratic stability analysis or learning-rate ceiling. Focused published-record searches found no implication-equivalent Grokfast result. The closest indexed stability theorems concern different update maps.

Residual risk: a similar control calculation could exist in unindexed notes about filtered-gradient descent.

## Value

PASS. The finding connects the source method's central frequency-domain design directly to optimization stability. It shows that the relevant safety quantity is Nyquist gain rather than DC gain, quantitatively explaining why a high-\(\alpha\) slow amplifier can strongly boost low frequencies while barely shrinking the quadratic learning-rate margin, and also identifying aggressive recommended settings where the margin shrinks substantially.

Same-model review: passed. Independent audit: not yet performed.
