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

# Verification and scope

The standalone checker was executed on the embedded code with successful output `HYPERQUIVER_FULL_RANK_NULLCONE_EXACT_OK 16 test_formats`. It verifies exact integer flattening ranks and determinant-one one-parameter weights in the tested finite dimensions. The infinite-parameter theorem is established by derivative linear independence and the symbolic inequalities in RESULT.md, not by extrapolating checks. The only external theorem required beyond basic matrix algebra is the standard affine GIT semi-invariant/Hilbert--Mumford semistability criterion. A general historical all-format equivalent statement has not been ruled out conclusively.
