# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `6de9349664dcb736170d331e4481c9a296a925e2`, verified unchanged on current `main`.

## Correctness

I independently transcribed the five displayed Pfaffians into a separate computer-algebra calculation over `F_3`. A fresh Gröbner basis gives standard-monomial Hilbert function `(1,3,5,5,3,1)` and no standard monomials in degree 6 or higher. The five generators have degree pattern `2,3,3,4,4`; the quotient length is 18, matching the claimed Artinian grade-three setting and the Buchsbaum–Eisenbud self-dual resolution shifts.

I then built multiplication matrices from the independently reduced standard-monomial basis for all 26 nonzero `F_3`-rational linear forms. The Jordan census is exactly the seven partitions and multiplicities stated in RESULT: `(6,4,4,2,2):10`, `(6,4,4,2,1,1):4`, `(5,5,4,2,2):4`, `(5,5,4,2,1,1):2`, `(6,4,4,1,1,1,1):2`, `(6,4,3,3,2):2`, `(5,5,3,3,2):2`. For the complete intersection `(x^2,y^3,z^3)`, the separate computation gives `[3^6]` on 24 forms and `[2^9]` on 2 forms, and every one of the 26 pairs differs. These checks independently reproduce the record's central separation.

## Originality

I searched the codimension-three Artinian Gorenstein, Pfaffian, Hilbert-function `(1,3,5,5,3,1)`, characteristic-3, WLP and Jordan-type literature. The known Boij–Migliore–Miró-Roig–Nagel–Zanello result isolates the complete-intersection exception, while later Jordan-type papers treat broader or characteristic-zero families. I found no prior publication of this explicit non-CI Pfaffian example or the all-26-form Jordan separation from the characteristic-3 CI exception.

## Scientific value

The record gives an explicit, fully replayable non-complete-intersection point at a published exceptional Hilbert function and distinguishes it from the CI exception both homologically (Betti ranks) and dynamically (all rational linear-form Jordan types). That is a useful finite-field boundary example for Lefschetz/Jordan investigations, not merely a random example with one checked invariant.

## Disposition

**PASSED unchanged.**
