# Scientific review

## Correctness
**PASS.** The result is proved for every stated parameter by exact arithmetic invariants and a residual-function separation argument. Distinct carry values are separated by comparing two continuations around successive powers of two; equal carries are separated by prescribed trailing-one runs. Counting the reachable dyadic levels yields the displayed sum and the isolated additional state. The saved checker independently tests finite instances, but the stated universal quantifiers rest on the proof rather than on enumeration.

## Originality
**PASS within the examined evidence.** Hendel's all-one-pattern paper establishes the base \(2m\)-state construction and related combinatorial properties, not the shifted two-parameter optimum. Zantema and Bosma establish general complexity bounds for shift operations, not the exact formula. Moradi, Rampersad, and Shallit discuss general state-complexity transformations with a different principal focus. Previously known special cases at \(m=2\) are not sufficient to derive the explicit formula or the parity-transition mechanism for every \(m\ge3\). Searches of equivalent phrases, generalizations, records, and relevant sources did not locate a covering theorem. The main remaining risk is equivalent work not indexed or accessible in the inspected literature.

## Mathematical value
**PASS.** This is an exact two-parameter state-complexity law for a recently studied natural generalization of the Thue–Morse and Rudin–Shapiro sequences. It identifies a nontrivial transient profile, one exceptional carry-parity transition, and the sharp eventual linear regime; minimality is proved rather than inferred from a construction. The broad no-merging lemma also permits exact state counting for arbitrary shifts. No claim about most-significant-digit-first automata or other patterns is made.

Self-review: passed. Independent audit: not yet performed.
