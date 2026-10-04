# Same-model review

## Correctness
PASS. The matching hypothesis makes the sampled matrix a weighted signed partial permutation, so its singular directions are exactly the observed coordinate pairs and are preserved by singular-value shrinkage. The matrix recurrence therefore reduces without approximation to independent scalar shrinkage recurrences. The activation index follows from the strict threshold inequality, the post-activation error multiplier is exactly \(1-\delta\), and \(|1-\delta|<1\) together with the activation bounds proves that an active direction never deactivates. The \(\delta=1\) settling index handles integer and noninteger threshold ratios explicitly. A dual-norm certificate plus strict Frobenius equality proves that the reached sparse matrix is the unique minimizer of the finite-\(\tau\) regularized problem. The exact-rational packaged checker returns `VERIFY_OK`.

## Originality
PASS with residual risk. The primary SVT paper already states empirical rank nondecrease and derives the duration of the initial all-zero phase, so neither fact is claimed as new. Targeted published-finding corpus and literature searches did not surface an implication-equivalent theorem giving every direction's activation time, the exact rank staircase, the post-activation recurrence, and the \(\delta=1\) finite-settling law for matching observations. Related linearized-Bregman work covers shrinkage, convergence, and kicking techniques but the inspected material does not state this matrix-specialized result. Unindexed notes or more specialized support-identification analyses remain a plausible residual risk.

## Value
PASS. Rank growth is one of the two practical features singled out in the original SVT paper, yet it is described there as empirical in general. A matching observation graph is the simplest nontrivial sparse matrix-completion pattern that preserves singular directions exactly. On that natural class, the finding turns the empirical phenomenon into a complete activation schedule, identifies an exact finite-termination resonance, and supplies a closed-form diagnostic benchmark for implementations and for studying what coupling destroys once observations share rows or columns.

Same-model review: passed. Independent audit: not yet performed.
