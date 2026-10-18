# Review of the complete period-doubling cyclic BWT recurrence

## Correctness
**PASS.** The proof is self-contained and tracks all cyclic boundary cases: the substituted words avoid cyclic \(11\), the four rotation classes are strictly ordered by prefixes, each class is internally reverse-sorted relative to its source rotations, and the preceding letters give the exact complete BWT recurrence. The base \(W_1=01\) is checked separately. Letter-count and run-count inductions have explicit base cases. The independent cyclic rank-doubling and full-rotation implementations agree with the recurrence through their respective finite ranges. Residual risk is a possible unnoticed proof error; finite tests do not replace induction.

## Originality
**PASS on the available searches and source comparisons.** The closest direct sources are the 2019 Thue–Morse BWT formula, the 2022 generic purely morphic upper bounds, and the 2023 morphism BWT sensitivity study. The first concerns a different substitution, the second yields only asymptotic upper bounds rather than an exact BWT word, and the third concerns arbitrary input words under one substitution, not successive period-doubling fixed-point prefixes. Searches under “period doubling,” “dyadic iterates,” “cyclic BWT,” “run length,” and “reverse complement” yielded no equivalent full recurrence or exact \(2m-2\) theorem. General order-reversal results do not identify the crucial even/odd rotation interleaving. A bibliographic equivalent outside indexed sources remains a residual risk.

## Value
**PASS.** The complete run-length structure of the BWT on a canonical primitive substitution family has a direct role in repetitive-text compression and indexing. The result is stronger than an asymptotic upper bound: it specifies every transformed bit and sharpens the run count to \(2m-2\), exposing how source-to-image rotation interleaving governs clustering. The explicit recurrence generates the run-length profile without sorting exponentially many cyclic rotations. Scope is cyclic BWT of dyadic iterates only.

Self-review: passed. Independent audit: not yet performed.
