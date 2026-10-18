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

# Verification of the fourth-power parity cutoff

Run `python3 verify.py` with Python 3 and no external dependencies. The script checks (i) all 1,024 subsets of the ten permitted base weights, (ii) the eleven exact merged components of 64 interval blocks, (iii) all 35 zero positions below 145 and coverage through 661, (iv) the first 2,049 coefficients of both a signed-partition recurrence and a separate distinct-subset recurrence, and (v) thirteen finite dyadic bridging scales. The checks passed when executed from the delivered package.

The infinite proof does not follow from these tests. It follows from the formal generating-function product and from the stated ratio bound, which holds for every bridge scale \(r\geq3\) by the exact ratios \(81/64,2,128/81\), combined with the elementary interval-extension induction. The verifier is useful for reproducing finite certificates and for catching normalization or endpoint errors; it does not constitute independent mathematical validation.
