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

Run `python verify.py` from this directory. The verifier uses no third-party dependencies. It checks the Green-kernel mean, recurrence, and energy in dimensions \(3\) through \(100\); reconstructs support-line polygons to check perimeter/area identities; tests noncentrally symmetric Wigner area identities; tests inequality samples; and checks positive-edge-length equality witnesses attaining the optimal ratio. It also tests the constant's continuous limit.

The proof of the universal statement is given in RESULT.md. Finite floating-point checks alone do not establish the universal inequality, nor can these calculations certify bibliographic priority. The original paper's Wigner oriented-area normalization is used: the midpoint chain is traversed once through half the facet pairs.
