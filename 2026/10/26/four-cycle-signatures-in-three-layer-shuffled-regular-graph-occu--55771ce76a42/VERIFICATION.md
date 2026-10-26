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

# Reproduction

Place `verify.py` and `verify_output.txt` alongside this file and execute `python verify.py` with the standard library. The verifier enumerates uniform support pairs and later uniform incoming pairs independently of the symbolic proof, computes exact rational second-layer empty-count means and variances, and checks third-layer empty fractions for every unordered cycle partition of orders seven through seventeen. It additionally verifies the exact seven-vertex examples and both graph-sensitive gaps. The actual checked output is retained in `verify_output.txt`.

The closed formulas for every \(d\ge7\) follow from finite-population subset counting and the cycle-codegree identity in `RESULT.md`, not extrapolation from these finite checks. No external proof assistant or independent reviewer has been used. The priority of a previously unlocated identity is not certified.
