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

# Reproduction and verified scope

From the directory containing `verify.py`, using Python 3, NumPy and SciPy, run `python verify.py`.

The actual package code was executed with output `VERIFY_OK exact_householder=28 numerical_spd=490 plus exact two-mode extremizers`.

The script checks 28 exact-rational Householder-conjugated matrices, the exact joint coupling, exact expectations and variance bounds, four convex powers, and the exact spectrum \((9,1)\) extremizers. It also checks 490 numerical positive-definite instances in dimensions two through eight, six convex functions, and orthogonal zero-diagonal constructions for arbitrary positive spectra. All stated infinite-dimensional-parameter quantifiers and all convex test functions are supported by the proof in `RESULT.md`, not by the finite tests. No independent audit has been performed.
