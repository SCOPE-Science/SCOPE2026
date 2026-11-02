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

The finite checks are reproducible from `verify.py` and `certificate.json` using Python 3 with only its standard library. The verifier enumerates faces independently from the mathematical proof, computes exact membership traces on all three-point supports for \((d,k)=(4,3),(5,3)\), checks explicit maximal-support witnesses, verifies a complete depth-four tree in \((5,3)\) with distinct terminal faces, and checks the two-branch construction in further finite parameter ranges. It does not replace the all-parameter proof, and it does not resolve historical priority beyond the cited comparisons. No independent audit was performed.
