# Scientific review

**Correctness — PASS.** For each query before any positive label, viable intervals are exactly those inside the surviving gaps. The positive branch factors into independent left and right endpoint threshold classes; their Littlestone ranks sum. Standard tree-rank recursion therefore gives an all-length, decreasing-size recurrence. The standalone script replayed its values against an independent full-hypothesis computation through length 16, checked both sides of ten sharp thresholds, and enumerated valid witnesses for every one of the corresponding complete shattered trees (up to 1024 leaf paths). The proof, not those finite checks, covers every length.

**Originality — PASS with priority risk.** The closest inspected sources concern general stability/Littlestone theory (Malliaris–Moran), general Boolean-aggregation bounds (Ghazi–Golowich–Kumar–Manurangsi), and coarse ranks/oracle algorithms for \(k\)-intervals (Attias–Hanneke–Ramaswami). None of their inspected mathematical statements implies the exact negative-gap partition recurrence or the enumerated sharp initial cutoffs. Direct searches for equivalent interval incidence rank, endpoint splitting, and exact online mistake bounds returned no decisive prior coverage. This is a qualified literature comparison, not a proof of global priority.

**Value — PASS.** Finite-chain intervals are the canonical two-endpoint concept family, yet counting hypotheses alone does not give their sharp adversarial online mistake bound. The recurrence replaces a general exponential-size hypothesis-subset computation by one state per integer partition, works at every finite length, and supplies exact first ten learning thresholds. It offers a reproducible benchmark for finite-model stability rank and finite-domain online interval learning, without claiming a universal closed form.

Residual risks: an unindexed equivalent exact formula in online interval learning; algorithmic verification of ten thresholds is finite, not a derivation of thresholds at every depth.

Self-review: passed. Independent audit: not yet performed.
