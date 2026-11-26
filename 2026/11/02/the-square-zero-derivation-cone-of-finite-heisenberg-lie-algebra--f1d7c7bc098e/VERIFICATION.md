---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility record

The proof in `RESULT.md` uses the derivation equations, an incidence bundle over the Lagrangian Grassmannian, and explicit coordinates for the scroll when \(r=1\). The arbitrary-field geometric claims do not depend on a computation.

The unchanged standard-library `verify.py` is a finite regression check of the ordinary derivation equations and previously known finite-field counts. The frozen execution reported full-rank histograms \((1,9)\), \((1,32)\), and \((1,75)\) in Heisenberg dimension three over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), respectively, and \((1,45,330)\) in dimension five over \(\mathbb F_2\). These bounded checks neither establish the geometry nor constitute a new rank census.
