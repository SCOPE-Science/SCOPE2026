# Scientific review: least odd three-prime-support ample integer

## Correctness — PASS
The result defines the recursive-divisor function and strict ample inequality, proves deficient integers cannot be ample using divisorwise abundancy monotonicity and strong induction, and reduces any odd three-prime ample candidate to three explicitly listed supports. Its seven-term coefficient recurrence follows from an exact rational formal generating function. The `verify.py` artifact exhaustively checks every positive exponent triple on these supports at or below the proposed witness: 4,650, 3,718, and 3,459 triples, respectively. Exactly one qualifies, and independent proper-divisor and ordered-factorization calculations confirm its exact recursive-divisor count. No finite experiment is used to exclude unbounded candidates without the preceding analytic sieve and strict candidate upper bound.

## Originality — PASS, with residual literature risk
Fink's 2020 full paper provides a different five-prime-factor odd minimum and no least three-prime-support result; Fink's 2023 full paper gives generating functions and ordered factorizations, not this minimizer. The published finite-support existence theorem does not supply any quantitative minimality bound and explicitly disclaims one. Other published nearby results constrain total prime multiplicity or discuss unrelated almost-practical integers. Actual published research search records and accessible previous claims were compared for implication; no inspected statement provides this minimizer or a stronger covering classification. An equivalent computation in unindexed literature remains possible.

## Value — PASS
The number of distinct prime divisors is the first natural sparsity parameter for odd ample integers. The theorem identifies the exact smallest integer at its minimum possible support, using a rigorous structural sieve and a finite complete certificate rather than an arbitrary numerical slice. It addresses the effective-minimum gap explicitly left open by the finite-support existence theorem; no downstream general theorem is asserted.

## Limitations and references
The result does not imply an elementary closed form for all three-prime-support ample integers. The exact certificate is required for the finite exclusion. Primary references: Fink, arXiv:2008.10398v1 and arXiv:2307.09140v1; the full published “Finite abundant prime supports force ample numbers”; Liyanage–Ranasinghe's 2022 conference abstract; OEIS A067824.

Self-review: passed. Independent audit: not yet performed.
