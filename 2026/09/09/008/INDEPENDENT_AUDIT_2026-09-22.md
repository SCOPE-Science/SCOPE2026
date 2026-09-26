# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/008`  
**Audited source tree:** `02096fead028351486be397cdc0a56ba57a4d6ae`  
**Date:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS. Replayed the stdlib grid enclosure at 3,001 times per dimension: the five lower/upper replays are 25.119968/25.984259, 89.016946/92.406642, 323.053933/336.488000, 1191.256879/1244.739720, 4443.282968/4656.702415, within the claimed intervals. The exact exponential Toeplitz formula follows from nilpotence; the Frobenius derivative bound with ||T||F²=5n−4 and h/2=0.005 covers between-grid times. At t≥30 all nonzero entry magnitudes decrease, and the certified tail is below each lower bound. Thus the global ratio lies in [170.895,185.464]. Decimal rounding relies on the verifier's explicit 0.1% and 1e−9 margins, which dwarf its 80-digit errors.

## Originality

PASS, narrow. Mitchell's Kreiss-constant algorithms and adjacent GMRES literature supply general methods and bounds but no five finite-horizon peak enclosures for this Jordan-block family. The nilpotent exponential is elementary; originality is the specific two-sided numeric certificate, not a general theorem.

## Scientific value

PASS, limited. These tight finite-horizon bounds are a reusable stable nonnormal-matrix benchmark. This is a toy Jordan-block sequence; the record establishes no asymptotic growth law or Orr–Sommerfeld result.

## Prior work

- https://arxiv.org/abs/1907.06537
- https://arxiv.org/abs/2312.15022

## Scope

The pass applies to the stated finite record. Limitations and prior overlap above are part of the verdict; no limiting, general-family, or inaccessible-full-text claim is inferred.
