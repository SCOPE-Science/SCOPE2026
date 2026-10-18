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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 and the standard library. It constructs ordered-pair counts directly, without calling the asserted recurrence, for all \(k\in\{3,5,7,9\}\) and \(1\le n\le9\), then compares them with the separate symbolic recurrence implementation. The exhaustive checks cover \(36\) exponent/modulus pairs, \(4{,}088\) residue classes, and \(1{,}398{,}096\) ordered input pairs. It additionally checks the unit-permutation property and \(180\) closed-form density stabilization cases with exact rational arithmetic. The cubic moment identity is checked with rational arithmetic.

The verification run reported no mismatches. The program cannot certify all moduli or all exponents by finite enumeration. General correctness is supported by the mathematical proof in `RESULT.md`. The pointwise density is finite only away from zero; the moment classification and tail bound use Haar-measure arguments. No independent mathematical audit has been performed.
