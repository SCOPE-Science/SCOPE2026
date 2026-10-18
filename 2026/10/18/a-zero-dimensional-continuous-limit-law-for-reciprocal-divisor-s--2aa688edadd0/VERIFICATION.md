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

# Reproducibility and mathematical limits

Run `python verify.py` in an ordinary Python 3 environment. The program uses Python's standard library, exact integer polynomial arithmetic over prime fields, and rational fractions. Its final expected output is `VERIFY_OK`. It exhausts degrees zero through eight over the two-element field and zero through five over the three-element field, checking both exact moments against explicit generating functions.

This is a consistency check of finite-degree identities. The assertions of convergence, absence of atoms, and Hausdorff dimension zero are proved in `RESULT.md` by a uniform large-factor tail estimate, an independent Bernoulli decomposition plus Sperner's theorem, and a summable small-prime histogram covering argument. These infinite assertions cannot be proved by the finite program. The analysis applies to every prime-power field size, while the executable samples only prime fields.

No external independent mathematical validation has been performed.
