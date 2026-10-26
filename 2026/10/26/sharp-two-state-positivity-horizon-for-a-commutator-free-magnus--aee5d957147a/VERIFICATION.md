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

# Reproducible verification

Run `python verify.py` with the SymPy version specified in `requirements.txt`.

The script recomputes exact algebraic identities with \(lpha,eta\in\mathbb Q(\sqrt3)\), including generator multiplication, the two-exponential endpoint, the coefficient ratio, the sharp threshold, and the negative-entry witness. It also checks the exact column budget and off-diagonal criterion for 4096 deterministic seeded numerical test cases and verifies both sides of the calculated horizon.

Expected final diagnostic: `VERIFY_OK: exact two-state products, coefficients, sharp universal threshold, counterexample, 4096 numerical crosschecks`.

The analytical proof establishes universal and sharp statements for all eligible real parameters; numerical examples alone cannot establish those quantifiers. The separately specified full multi-stage method and arbitrary higher-dimensional problems are not verified by this package.
