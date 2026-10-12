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

# Exact verification

The companion `verify.py` reconstructs all Jacobian matrices directly from the defining polynomial using exact characteristic-zero symbolic arithmetic. It checks two parameter-polynomial determinants that together exclude all extra cubic-or-lower syzygies away from \(t\in\{0,1,2\}\), checks universal quartic and two exceptional syzygy identities, and verifies the specialized full-column minors. It also checks the conic discriminants, intersection-multiplicity accounting, and numerical free/nearly-free equalities.

The embedded `verify.py` was extracted from the finalized serialized record and run using `python verify.py`. Result: `VERIFY_OK`. The computation verifies polynomial identities and finite matrix certificates, while Bézout counting, local analytic type classification, and application of the known freeness criteria are mathematical arguments in `RESULT.md`. This is not an independent audit.
