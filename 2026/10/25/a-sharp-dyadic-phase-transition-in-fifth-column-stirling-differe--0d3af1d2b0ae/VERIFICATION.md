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

The accompanying `verify.py` is a standalone Python 3 verifier using only the standard library. Run `python3 verify.py` in the same directory. It reconstructs the numerator of the difference using modular exponentiation and checks the valuation exactly for 119 \((n,q)\) parameter pairs, including all transition boundaries for \(3\le n\le8\). It independently uses the Stirling-column recurrence for six cases, with a direct check of \(n=4,q=12\).

Recorded replay output: `VERIFY_OK: 119 exact modular checks; 6 independent Stirling-recurrence checks; n=4,q=12 valuation 14`.

These tests are finite. The universal proof rests on the explicit four-summand valuation comparison and the normalized congruence at the unique tie. No independent audit is claimed.
