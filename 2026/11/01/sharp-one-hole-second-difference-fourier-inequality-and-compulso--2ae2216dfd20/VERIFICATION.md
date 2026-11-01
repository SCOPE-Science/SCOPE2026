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

# Verification and reproducibility

The self-contained analytical certificate is in `RESULT.md`. Its pivotal identities are the fourth-difference quartic and cubic Green responses, strict positivity of the finite fourth-difference Green matrix established by a Cauchy--Binet complementary-minor argument, and the exact rank-one block inverse for the forced internal zero. Together they establish the sharp inequality and characterize every equality case for all integers \(L,R\ge1\).

Run `python verify.py` with SymPy installed for finite exact-rational replay. This script verifies the local response identities through length eighteen and the coupled sharp constants and strict optimizer signs for all \(1\le L,R\le8\). Finite tests cannot establish the universal inequality independently; the proof is analytical.

Independent mathematical audit: not performed. All originality conclusions are conditional on the inspected literature and searchable records, and earlier implicit derivations remain possible.
