# Review

**Correctness (C): PASS.** The counterexample sentence is satisfiable exactly when monotonicity fails. The rank-profile theorem bounds satisfiability by an exponential-size profile; symbolic evaluation of ordinary and infinity quantifiers gives a \(2^{O(n^2)}\) verification bound after guessing the profile. The reduction from monadic satisfiability establishes matching hardness, including the empty-domain boundary. The claim is limited to combined complexity with an unbounded finite unary vocabulary.

**Originality (O): PASS.** The closest primary source, Carreiro et al. (2021 online), proves decidability and the positive-fragment characterization, but explicitly leaves complexity questions unexplored. Its rank-profile result is used as a premise, not presented as the complexity classification itself. Lewis (1980) supplies satisfiability hardness but does not address semantic monotonicity. Targeted database and literature searches returned no directly matching complexity classification; this is not treated as proof of novelty by itself. Residual risk: the literature search was targeted rather than exhaustive.

**Value (V): PASS.** This gives a tight algorithmic classification for a central semantic property whose foundational treatment left complexity open. Hardness persists even when the designated predicate occurs only negatively, showing that polarity inspection alone cannot decide semantic monotonicity. The result has a precise boundary: fixed-vocabulary and finer-grained complexity variants remain open here.

Closest literature: Carreiro et al., DOI 10.1007/s00153-021-00797-0; Lewis, DOI 10.1016/0022-0000(80)90027-6.

Self-review: passed. Independent audit: not yet performed.
