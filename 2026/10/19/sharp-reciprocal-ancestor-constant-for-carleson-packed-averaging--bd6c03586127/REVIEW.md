# Review of the sharp reciprocal-ancestor constant

## Correctness — PASS

For a fixed member, all its ancestors form a single ordered sequence; finiteness of every bounded-measure initial segment follows directly from Carleson packing. The proof applies the packing condition to each ancestor, derives a sharp monotone recurrence, establishes coordinatewise dominance, solves the recurrence exactly, and builds finite measure-space examples whose least Carleson constant is the stated parameter. The endpoint \(\Lambda=1\) is handled separately. The standard-library exact-rational verifier independently checks 35 parameter samples, finite witness Carleson inequalities for every subset, and finite feasible prefixes. These checks supplement rather than replace the analytic proof.

## Originality — PASS with bibliographic uncertainty

The closest primary statement is Proposition 1.2 of Conde Alonso–Monti–Rizzo, arXiv:2610.08211v1: the same reciprocal-ancestor sum is bounded there by \(\Lambda^2\), and the displayed proof makes no best-constant assertion. The new bound is strictly stronger except at \(\Lambda=1\), and finite examples prove optimality. The mathematical statements and relevant sections of Honig–Lorist (arXiv:2501.07943) and Hänninen (arXiv:1709.10457) address Carleson constants/sparse equivalence, not this sharp inverse-mass functional. Searches for exact formulas, synonyms, and stronger covering bounds disclosed no covering result. An older equivalent inequality outside indexed records remains possible.

## Value — PASS

The sharp dependence replaces the central quantitative ancestor lemma's quadratic \(\Lambda^2\) factor with a universal factor of linear order, while identifying the precise integer-transition corrections. It provides a concrete best-possible kernel constant for sparse averaging estimates on general possibly atomic nested measure spaces, not merely a new parameter name or a finite table lookup. It does not establish improved optimal norms for any specific Bergman projector.

Self-review: passed. Independent audit: not yet performed.
