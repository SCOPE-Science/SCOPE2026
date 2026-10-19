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

Run `python verify.py` using standard Python 3. The independent exact geometry enumerator iterates the two inverse branches of the doubling map and intersects with the living intervals using rational endpoints; it neither invokes the five-state matrix nor assumes the answer. For the first twelve survival horizons it agrees exactly with the matrix-derived rational probability. Thirty horizons agree with the rational generating-function recurrence, and eight additional horizons agree with the upstream-to-downstream first-switch decomposition. Output: `VERIFY_OK: 30 transfer-vs-generating-function, 12 independent exact-geometry, 8 exact phase-decomposition checks`.

This finite replay corroborates the direct interval graph, coefficients, and phase decomposition. It does not certify the all-horizon formulas or weak limit: those follow from the matrix identity and primitive-block Perron asymptotics in `RESULT.md`. The source's original defective eigenvalue is prior work. Independent audit has not been performed.
