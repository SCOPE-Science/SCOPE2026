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

The standalone `verify.py` enumerates all 32768 labeled graphs on six vertices and verifies pair/triple component moments for isolated-vertex, isolated-edge and isolated-three-vertex-path classes at rational edge probabilities 1/5, 1/2 and 4/5. It also runs 40 high-precision asymptotic comparisons and 12 finite sign checks at separated parameter values. Run `python verify.py` using Python 3 standard library; the expected final output begins `VERIFY_OK`. These finite and numerical checks are not proofs of any infinite limit or global uniqueness. The displayed formula and asymptotic expansion in RESULT.md are the analytic verification of the theorem.
