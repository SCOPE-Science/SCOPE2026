# Scientific review

**Correctness — PASS.** The proof treats every positive integer triple, establishes three independent sharp obstructions, and constructs a valid one-traversal embedding for every target via explicit greedy transition inequalities. The critical \(m=3\) equality case is handled by changing the starting offset for alternating targets. A definition-level exhaustive checker independently corroborates 144 parameter triples and 14,270 maximal-length targets. Computations do not replace the proof.

**Originality — PASS, conditional on available literature.** The closest 2020 and 2021 primary works use a single common rotation, while the present problem allows a separate rotation for each target. The 2025 regular-language and 2026 Parikh-matrix papers concern other quantifier structures/word classes. No exact three-parameter formula was found in the examined sources or targeted record searches. A differently named cyclic subsequence coverage theorem could remain unindexed.

**Value — PASS.** The target-dependent rotation variant is a natural distinction for cyclic storage and deletion-tolerant pattern coverage. The complete classification is sharp for three independent parameters, identifies the saturation threshold at homogeneous block length three, and gives an explicit bounded-displacement embedding certificate. Neither a routine parameter renaming nor a restatement of single-rotation universality, it also supplies a concrete separation (`000111`) of two frequently confusable quantifier orders.

**Limitations.** Binary two-block periodic cycles only; independent audit is absent. Existing general decision procedures may establish individual instances but were not found to give this exact family formula. Wider prior-work coverage cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
