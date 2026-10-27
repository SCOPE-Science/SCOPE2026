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

# Verification notes

The exact diagonal expression is derived analytically and does not depend on the checker. The independent oscillatory-integral route uses the change of variables \(v=(1-t)^{-1}\) in the beta moment and quadrature with sine and cosine weights on \([1,\infty)\). The second route integrates the exact Macdonald/gamma representation over \(s\), which follows from a separate Laplace transform. The checker compares these routes in nine small-degree cases and compares its integral representation to the fully normalized asymptotic formula in twelve large-degree cases.

Run `python3 verify_chirp.py` in an environment with NumPy and SciPy. The successful execution returned `VERIFY_OK independent_oscillatory_vs_bessel=9 asymptotic_comparisons=12`. Exact arithmetic is not used by this floating-point check. Its tolerance is recorded in the source code. Finite numerics cannot establish asymptotics or uniqueness; the proof in `RESULT.md` establishes the universal statements.
