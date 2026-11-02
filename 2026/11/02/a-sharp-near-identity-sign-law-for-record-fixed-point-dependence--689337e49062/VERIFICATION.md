---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Standalone checks

Execute `python verify_record_fixed_signs.py` with Python 3 and no nonstandard dependencies. The script's most recent run returned `PASS: 31317 exact assertions; exhaustive permutations n=2..9; entire 2x2 minor tables n=2..4; symbolic integer checks to n=249`.

The program independently creates every permutation through nine labels and computes upper records and fixed points directly from the one-line permutation. It tests the two near-identity formulas, adjacent minor identity, positivity of all minors at the finite sharpness boundary, and the covariance identity as an exact rational number. It tests the algebraic identities for larger sizes without enumerating permutations.

## Proof limits

The program does not certify infinitely many cases. General correctness relies on the transposition and oriented three-cycle counting proof, algebraic minor cancellation, and conditional-record indicator argument in `RESULT.md`. The test of full TP2 for all sizes is replaced by a proof of failure at every size \(n\ge5\); only positivity at \(n\le4\) needs finite exhaustive checking.

## Audit status

A self-review was completed. Independent audit has not been performed.
