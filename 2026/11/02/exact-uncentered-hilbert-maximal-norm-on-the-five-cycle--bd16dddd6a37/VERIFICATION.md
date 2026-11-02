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

The standalone Python 3 checker `check_c5_uncentered.py` reconstructs all legal averaging sets from the cycle, not from a stored spectrum. It enumerates all \(5^5=3125\) selected-row matrices and uses exact integer fraction-free determinants with Sylvester's criterion for the strict spectral cutoff \(5/3\). It identifies 3120 strict cases and exactly five non-strict cases, checks the five-row exceptional matrix, and verifies its characteristic polynomial by six exact evaluations. Rational interval arithmetic at the isolated algebraic root proves all twenty row-activity inequalities strictly.

Successful execution prints `CERTIFICATE_OK selections=3125 strict=3120 exceptional=5 characteristic=exact active=20`.

This is a finite exact certificate for the specified five-vertex operator. It does not certify any broader graph family or publication priority. Independent scientific audit has not been performed.
