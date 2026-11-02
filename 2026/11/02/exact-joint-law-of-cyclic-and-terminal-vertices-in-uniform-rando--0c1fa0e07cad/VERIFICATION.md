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

The independent audit has not been performed. Exact direct enumeration was run from the packaged `verify.py` file for all uniformly weighted mappings on 2 through 7 vertices: 873,611 individual functions, 333 exact-rational assertions, all passed. The checker independently extracts cycle membership by path traversal and terminal count by empty-image detection, comparing all joint frequencies with the finite-sample formulas.

The all-size claims require the proof given in RESULT.md; finite enumerations alone cannot establish them. The asymptotic constants were also examined numerically at sample sizes 5, 10, 100, 1000 and 5000; these are diagnostics, not proof. No source-based historical uniqueness or external certification is asserted.
