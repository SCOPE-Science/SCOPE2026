# Scientific review

## Correctness: PASS

The three-by-three witness follows from direct exact preference comparisons: its unique complete-market stable matching is \(\mu=(2,1,3)\), its exact radius-one prediction windows remove only \((H_3,R_1)\), hospital-proposing DA returns \(\nu=(1,2,3)\), and that omitted pair blocks. The two-pair impossibility uses survival of a stable perfect matching, proposer-optimality, and a complete dichotomy between identical and swapped perfect matchings. The universal lower-tail pruning result uses a sandwich between pruned hospital-optimality and original hospital-optimality. The included standard-library verification program independently tested 290 small-market pruning cases and 1,531,392 three-pair safe-deletion cases, plus the witness. The general statements depend on the proofs, not extrapolation from these finite experiments.

## Originality: PASS, subject to publication-priority risk

The motivating 2026 preprint already exhibits the qualitative failure with **four** pairs; this report makes no novelty claim about that fact. The focused claim concerns the minimal three-pair market and one-edge deletion under exact unit-radius prediction, the impossibility under two pairs, and the all-size lower-than-reference deletion safeguard for potentially noncontiguous lists. The source's Section 4 prefix guarantee is already known and is not repackaged as new. Read comparisons covered the motivating paper's model, Lemma 3.1, Theorem 3.4, and Section 4; literature and mathematical-result searches found no equivalent exact minimum-boundary theorem. Prior sources on stochastic short lists and nearby three-by-three matching classifications neither imply nor enumerate this deterministic deletion boundary. Unindexed counterexamples or future revisions remain plausible.

## Value: PASS

A single omitted acceptable pair is the least possible deletion budget, and three per side is the least market size that can make an otherwise exact, stable-reference-preserving prediction window dangerous to the proposing side. This gives a precise warning against relying on prediction accuracy alone, with a contrasting safe tail-pruning rule valid even for irregular lists. The object and quantitative cutoff arise naturally from the published proposal-pruning model, rather than from an arbitrary enumeration.

## Limits

Strict complete one-to-one original lists, bilateral edge deletion, and hospital-proposing DA only; stable reference survival is essential. No claims are made for ties, capacities, preferences with missing original acceptabilities, unilateral omission, or approximate prediction centers. Equivalent exact small examples in unindexed literature remain a risk.

Self-review: passed. Independent audit: not yet performed.
