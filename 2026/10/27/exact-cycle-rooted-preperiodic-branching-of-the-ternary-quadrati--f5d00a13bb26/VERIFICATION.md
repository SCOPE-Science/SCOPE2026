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

The bundled `verify.py` was executed using Python 3 with exact integer arithmetic and no external dependencies. It directly built all directed functional graphs over \(\mathbb Z/3^k\mathbb Z\) for \(1\le k\le8\). It checked the depth strata, unique depth-one predecessor, every depth-two fibre, invariant fibre size along cycles and exactly one rich cycle per even valuation.

Observed output: `VERIFY_OK [(1, 1), (2, 3), (3, 7), (4, 11), (5, 15), (6, 19), (7, 23), (8, 27)]`.

The computation is only finite corroboration; the valuation and Hensel-lifting proof handles arbitrary \(k\).
