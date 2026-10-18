# Self-review

## Correctness — PASS

The theorem's quantifiers range over all integers \(k\ge1\) and team bounds \(r\ge1\), with one fixed set of \(k+1\) Boolean variables. The proof explicitly treats the exceptional singleton case. For all larger cutoffs, forbidden two-teams force each classical summand into a partial Boolean-function graph. Extending these partial graphs and ranging over every size-\(s\) consistent team produces a covering array; conversely rows of any covering array give flat graph formulas representing every consistent team at that cutoff. The missing-small-pattern issue is handled by extending any pattern of fewer than \(s\) columns to \(s\) columns. Every inconsistent team is excluded by every row graph. Full-strength and pairwise extremes are then exact. The checker exhaustively reproduces representative small parameter cases. Computation alone is not asserted to prove the general result.

## Originality — PASS, with residual risk

Yang and Väänänen (arXiv:1412.7998v3, Section 3) establish flat classical disjunctive normal forms on *all* teams. Barbero, Girlando, Müller and Yang (arXiv:2606.31860v1, Section 2) supply the contemporary proof-theoretic setting and semantics. Lawrence et al. (DOI:10.37236/571, Section 3.2.1) supply the *previously known* sharp strength-two covering-array formula. Neither original result directly quantifies the minimum number of classical disjuncts subject to an upper bound on team size. The bidirectional reduction to covering arrays across all strengths is the claimed contribution; it is not credited with discovering known combinatorial minima. Targeted published-record and literature searches found no dominating statement. Residual risk: an unindexed logical optimization or an equivalent independent covering interpretation could already exist; parts of the bridge are straightforward consequences of existing flat-normal-form technology.

## Value — PASS

The restriction to information states of bounded cardinality gives a natural logical resource measure: classical disjuncts are the alternative complete functions able to resolve observed partial assignments. The exact correspondence identifies the design-theoretic cost for all cardinality bounds. Its sharp extremes include the one-disjunct singleton regime, logarithmic-in-number-of-input-patterns pairwise regime, and a doubly exponential full-team regime. The result is useful even where the associated higher-strength covering-array optimum is not known, by enabling direct transfer of combinatorial bounds and algorithms.

## Scientific limits and literature

This is a conditional width measure for *flat* global-disjunctive translations on the fixed variables; it is not a formula-size lower bound, a split-disjunction statement, or an answer to general higher-strength covering-array optimization. The original sources materially inspected were Yang–Väänänen (2016), Barbero et al. (2026), and Lawrence et al. (2011). Unknown prior equivalent formulations and unindexed work are residual risks. There was no independent audit.

Self-review: passed. Independent audit: not yet performed.
