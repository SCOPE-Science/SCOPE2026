# Review: exact dependence phases of elementary cellular-automaton Bernoulli images

## Correctness

**PASS.** The endpoint-bit covariance identity reduces the infinite one-dependence question to one-sided conditional independence, with no assumptions about pairwise-independence sufficiency. The four-state weighted predecessor automaton supplies an exact length-three test because its reachable row/column spans have dimension at most four. All 256 rules and all interior Bernoulli parameters are treated by exact rational-polynomial greatest common divisors. The independently implemented direct nine-input-bit check confirms the 56/32/32/32 classifications at the four rational test biases, while the explicit Rule-22 obstruction is the nonzero rational number \(32/6561\). The generated per-rule table gives the reproducible finite certificate. No finite sampling is used as an infinite proof.

## Originality

**PASS, subject to historical-priority limitations.** Inspected primary literature on ECA statistical mechanics addresses random-state behavior, Gibbs and Bernoulli invariance, temporal randomization, and numerical information classes, rather than this exact classification of one-dependent one-step *image laws* at every input bias. The strongest relevant overlap is the established preservation of fair Bernoulli input by surjective rules, which implies independent output for those individual rules; it does not classify non-surjective rules with one-dependent but non-iid image laws or the pairwise resonances. Related scientific literature and accessible mathematical claims were compared by mathematical statement, including Bernoulli correlations of specific rules and finite CA censuses; no claim covering this theorem was found. Relevant unindexed work, including the possibility of an earlier exhaustive table of special input biases, remains a genuine residual priority risk. See `AUDIT.json` for individual comparisons and access limitations.

## Mathematical value

**PASS.** One-dependence is the correct sigma-field notion for a finite-range output process; vanishing two-point correlations is not a substitute. This theorem gives its full phase diagram across a canonical 256-rule family, proves that fairness is its only exceptional parameter, and contrasts it with seven exact algebraic resonances visible to a two-point test. Rule 22 at input density \(1/3\) exhibits a concrete false negative for pairwise dependence detection. These are structural facts about when finite-observation statistics recover actual independence, not arbitrary classifications of unnamed truth tables.

## Scope and verification limits

The theorem concerns the first update under independent binary input and a radius-one, centered cellular automaton. It does not address repeated updates, general Markov inputs, or larger rule neighborhoods. The exact table and checker are internally reproducible, but no independent external mathematical review is represented.

Self-review: passed. Independent audit: not yet performed.
