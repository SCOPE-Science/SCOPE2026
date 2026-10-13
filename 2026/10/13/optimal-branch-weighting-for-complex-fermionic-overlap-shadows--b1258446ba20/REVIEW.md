# Self-review

## Correctness
PASS. The proof uses the source's exact Haar normalization and exact diagonal second-moment spectrum. Replacing the equal coherent branch amplitudes changes both the Born weights and the estimator normalization; carrying both changes through gives the stated first and second moments. Strict convexity supplies the unique average-variance optimizer, and an admissible trial-equals-target Slater pair supplies the matching minimax lower bound.

Risk: the result assumes ideal preparation and Haar orbital rotations exactly as in the source. The verifier checks algebraic instances but is not the proof.

## Originality
PASS. The two same-object primary sources inspected use the equal coherent augmentation only. The 2026 anchor derives a sharp equal-weight variance theorem and explicitly notes the fixed reference weight in its lower-bound discussion; it does not analyze an unequal branch probability. The older Low paper introduces the same equal augmentation and mentions possible variations without solving this one. The closest 2026 particle-preserving-shadow comparison treats squared overlaps, not the phase-sensitive complex overlap.

Residual risk: the anchor is extremely recent, so an unindexed contemporaneous analysis could exist. A closely related squared-overlap paper was compared through its primary abstract and the anchor's explicit discussion; its full PDF was not retrievable in this run.

## Value
PASS. A single global unequal branch weight can strictly reduce the average noise of a reused shadow data set for a known nontrivial target ensemble, with an exact optimizer and exact gain. The companion minimax theorem explains why the source's equal superposition remains the right robust default. The result therefore separates average-case tuning from worst-case robustness in a way directly relevant to the protocol design.

Self-review: passed. Independent audit: not yet performed.
