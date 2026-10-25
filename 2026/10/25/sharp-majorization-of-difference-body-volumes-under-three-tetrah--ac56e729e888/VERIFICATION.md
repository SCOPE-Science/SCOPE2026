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

The accepted claim is proved in `RESULT.md`. The companion `verify.py` is an independent exact-arithmetic consistency check, not a formal proof assistant and not a substitute for the algebraic argument.

Run `python verify.py` in a Python 3 environment with NumPy and SciPy installed. It reconstructs the clipped tetrahedron and its difference body from rational vertices; floating-point convex hulls only propose facet triangles. Every proposed supporting plane, every pyramid volume, and every comparison to the analytic formula is checked exactly with `fractions.Fraction` arithmetic.

Expected output: `VERIFY_OK exact_hulls= 112 rational_triangles= 6060 mixing_derivative_checks= 75`.

The proof covers all real depth triples with nonnegative entries and sum less than one. The finite checker covers only its enumerated rational examples; the strict majorization and exact equality classifications are analytical. The checker requires access to SciPy and NumPy and is supplied in full.
