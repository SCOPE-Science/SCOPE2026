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

The real-valued equality is derived from the reset-renewal mean first-passage formula, then transformed to a unique positive hyperbolic root for the parameter regime. Coefficient signs, exact finite-dimensional normalization, existence, and uniqueness are demonstrated analytically in the accompanying RESULT.md, not inferred from a numerical plot. The logarithmic inversion is uniform on fixed-factor brackets around the root.

The standalone Python script `queue_crossover_checker.py` was executed with its declared dependencies and passed 75 assertion groups on multiple independent \(D,L,\mu\) values, six increasing server counts per value, and seven coefficient-variation parameter values per value. Numerical checks support but do not replace the proof, do not provide independent audit, and do not establish guarantees at arbitrary finite server counts.
