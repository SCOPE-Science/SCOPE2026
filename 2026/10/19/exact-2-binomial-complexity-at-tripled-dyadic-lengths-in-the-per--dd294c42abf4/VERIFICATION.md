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
# Verification

The standalone Python 3 artifact `verify_period_doubling.py` has been run as `python3 verify_period_doubling.py 13`, yielding `VERIFY_OK`. Every integer \(k\) from \(0\) through \(13\) is checked at length \(3\cdot2^k\), with expected total class count \(2^{k+1}+k+3\), all three exact weight-group sizes, and the central weighted-position arithmetic progression.

For each tested length, the factor cover is mathematically exhaustive, not a sampled prefix: each length \(3\cdot2^k\) factor is inside the image under \(k+2\) substitutions of two consecutive letters, and the complete allowable adjacent-letter list is \(00,01,10\). An independently generated 2-adic valuation prefix agrees on every factor signature through \(k=10\).

The analytic proof uses the complete even/odd factor decomposition and an induction on \(k\); it is the basis for the all-exponent claim. The numerical tests do not extend the range by extrapolation. No independent external examination of the proof has been performed.
