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
# Reproducibility and limits

Run `python verification/check.py` at the package root. The code requires the Python standard library; if SymPy is already present, it additionally rechecks the exact symbolic derivative, stationary relation and radical closed form.

A completed run checked the extremal identity to more than fifty decimal places, 3,969 nonzero integer-vector pairs on a three-category grid, 9,977 pseudorandom profile pairs in dimensions 3, 4, 6 and 12, and the exact zero-to-one upward-change witness. It confirmed the Schoener monotonic comparison on the same profiles. All checks passed, including the SymPy symbolic identities.

The unrestricted inequality is proved analytically in RESULT.md. The finite checker does not certify the infinite domain or bibliographic originality, and the numerical random tests are diagnostics rather than exhaustive verification. No external validation has been carried out.
