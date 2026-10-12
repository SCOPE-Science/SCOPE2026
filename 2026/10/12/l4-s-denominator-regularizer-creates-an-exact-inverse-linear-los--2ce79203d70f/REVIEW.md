# Review

## Correctness

PASS. The source minimum-loss clamp and forgetting rule give an exact scalar ratio recursion. Under the stated source-relevant parameter range, every parameter multiplier lies strictly between zero and one, so the tracker reaches the current loss in finite time and remains locked. The post-lock reciprocal-state increment tends to a constant, proving the sharp inverse-linear loss asymptotic.

Risk: the theorem is scalar and deterministic and does not include L4Mom or L4Adam's additional moving-average states.

## Originality

PASS. The defining L4 paper explicitly says it provides no theoretical guarantees and treats the denominator constant as a numerical-stability device. Its full text does not state the finite target-lock law or the resulting inverse-linear tail. Later stochastic Polyak-stepsize theory uses different target information, and the closest exact quadratic published record omits L4's practical state and additive denominator constant.

Residual risk: an equivalent regularized-Polyak calculation may exist in unindexed notes.

## Value

PASS. L4's central purpose is automatic loss-based step adaptation. The theorem shows that its adaptive minimum-loss state disappears after a finite transient on the canonical scalar quadratic, while the tiny numerical denominator constant eventually becomes the exact rate-limiting mechanism. This gives a sharp mechanistic boundary between the ideal loss-based rule and the practical implementation.

Self-review: passed. Independent audit: not yet performed.
