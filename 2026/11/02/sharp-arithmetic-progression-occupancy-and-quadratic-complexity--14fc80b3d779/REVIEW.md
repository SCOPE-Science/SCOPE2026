# Scientific assessment

## Correctness — PASS
The normalized gcd identity for differences of integer powers is verified algebraically and leads to the sharp geometric minimum span. Equality forces the claimed critical one-positions. The first-two-mark encoding and positivity restriction rigorously count *all* possible arithmetic-progression factors, not merely a finite experiment. The proof explicitly handles the one- and two-marker boundary cases. The standalone finite checker returned `VERIFY_OK 639077 assertions; finite tests only`.

## Originality — PASS (qualified)
Konieczny and Müllner (arXiv:2309.03180, first public 6 September 2023) establish a general subexponential bound for effective-alphabet-one automatic sequences, but not the quadratic estimate or exact maximal support for this characteristic word. The published 2026 note *Sharp logarithmic support envelope for Abelian pattern Sturmian words* bounds ordinary prefix occupancy of the particular base-two support; it does not address arbitrary arithmetic-progression sampling. The earlier exact formulas of Avgustinovich, Cassaigne and Frid apply to other Toeplitz families. Accessible existing work on reflection complexity and string attractors of the same power-indexed word likewise does not imply the present theorem. Relevant full mathematical statements were compared by implication, not merely by title. Unindexed equivalent results remain a residual risk.

## Mathematical value — PASS
The arithmetical subword language of an automatic sequence is a standard complexity object. A uniform quadratic bound, compared to the general subexponential guarantee, is a meaningful strengthening; the accompanying exact maximum-one occupancy and rigid critical patterns describe a natural extremal invariant for all integer bases. The proof isolates the number-theoretic mechanism behind both phenomena.

## Limits and references
The quadratic upper bound is not established as an optimal order, and all-length novelty has not been independently determined. The verifier is not a formal proof. Core literature: Konieczny–Müllner, *Arithmetical subword complexity of automatic sequences* (arXiv:2309.03180); Avgustinovich–Cassaigne–Frid, *Sequences of low arithmetical complexity* (2006); *Sharp logarithmic support envelope for Abelian pattern Sturmian words* (2026 public research note).

Self-review: passed. Independent audit: not yet performed.
