# Self-review

## Correctness
PASS. The common-shift invariance is exact: adding one affine logit function to every tier cancels from the softmax. Equality of gate probabilities gives equality of every log-odds function, and full affine covariate rank makes the common shift the only softmax coefficient ambiguity. A reference-tier constraint therefore removes exactly this obstruction. The same invariance makes the unconstrained log-likelihood flat in at least \(p+1\) directions. The packaged checker verifies the algebra numerically and reconstructs the BIC parameter counts.

## Originality
PASS. Proposition 3 of the primary source claims parameter identifiability up to label switching without stating a gating normalization. Focused source-specific searches located no correction. Broader mixture-of-experts literature explicitly fixes a baseline gate block to zero, but does not make the source-specific theorem/table reconciliation. A previous same-source result concerns tail asymptotics and does not imply coefficient identifiability.

Residual risk remains that a recent unindexed correction exists and that other mixture-identifiability issues, outside the gating block, may require separate analysis.

## Value
PASS. Identifiability is a headline theoretical property of the model. The omitted normalization produces an exact likelihood ridge and singular observed information, not a minor notation issue. The repair is simple, mathematically complete for the gating representation under full affine rank, and matches the baseline convention already visible in the source's numerical tables.

Self-review: passed. Independent audit: not yet performed.
