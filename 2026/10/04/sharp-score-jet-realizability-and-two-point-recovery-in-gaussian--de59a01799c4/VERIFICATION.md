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

The analytic theorem is proved in `RESULT.md`. The accompanying `VERIFY.py` performs finite regression checks of the algebra: exact Pearson equality for a nondegenerate two-point posterior, exact support/mass recovery, strict inequality for a three-point posterior, and violation by the smooth density proportional to \(\exp(-y^4/4)\) at \(y=0\) despite a positive variance surrogate.

The verifier uses Python standard-library rational arithmetic for the discrete identities. These finite checks are not used as an infinite proof.

Run `python VERIFY.py`. A successful replay prints `VERIFY_OK`.
