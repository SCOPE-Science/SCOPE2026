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

The self-contained verifier `verify.py` calculates exact rational covariances by enumerating every independent parent-choice vector for tree sizes 3 through 9. It checks 46,232 trees across those sizes against the displayed harmonic formula and tests the finite sign switch for each integer tree size through 999. Observed output ends `VERIFY_OK`.

The unlimited statement does not follow from those finite calculations. Its proof is the independent-parent covariance decomposition, telescoping harmonic sums, and positive rational first difference in RESULT.md. No external or independent validation has been undertaken.
