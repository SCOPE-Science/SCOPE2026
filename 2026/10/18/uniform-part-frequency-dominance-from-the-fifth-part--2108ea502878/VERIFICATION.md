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
The proof uses formal power series, a unique binary expansion, and two finite integer-polynomial coefficient checks. The provided verifier reconstructs the two polynomial coefficients exactly and checks comparisons for a finite parameter range; finite enumeration alone is not used to infer the universal statement.

Run `python3 verify.py` in the directory containing the standalone script. The finite polynomial certificates are the only computer-assisted steps needed to check the symbolic factorization; the full finite comparison range is additional corroboration. An independent audit has not been performed.
