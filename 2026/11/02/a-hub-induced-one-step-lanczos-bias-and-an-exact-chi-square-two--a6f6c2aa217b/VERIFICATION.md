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

Execute `python3 verify.py` using the Python 3 standard library from the directory containing this file and the script. The program uses the rational class in `fractions` to compare the star-Laplacian matrix-vector action, an independently solved shifted system, moment-derived two-step coefficients, pointwise finite residual identities, and finite exact expectations. It checks all \(3\le n\le20\) and all sign-counts \(0\le k\le n-1\) at six rational shifts, followed by asymptotic diagnostics for three larger dimensions. Observed output: `VERIFY_OK exact_and_asymptotic_diagnostic_groups=1410`.

The strict finite bias and the limiting \(\chi^2_1\) law are **not** inferred from this enumeration; they follow from the nonnegative closed formula and central-limit/uniform-integrability proof in RESULT.md. This test is deterministic and uses no external data. The output is a self-review replay, not an independent audit, infinite certificate, or floating-point stability experiment.
