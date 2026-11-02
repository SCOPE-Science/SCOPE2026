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

# Reproducing the mathematical checks

The accompanying `verify.py` is self-contained Python 3 code requiring only the standard library. Run `python verify.py` from the extracted file directory. The executable independently implements the three-level Gibbs moments, the factored variance and third-cumulant formulas, and central finite-difference derivatives. It also tests the rational uniform sign bounds, stationary branches and exact inter-peak value.

At packaging time the checker reported 256 successful arithmetic, moment, derivative and branch checks, and printed the exact lower bounds \(294424/789173\) and \(1341440000/2975509823\). Replay after extraction is required to establish that this accompanying code, not a stale local file, runs. These computations are **not** a proof of the infinitely many cases \(M\ge256\); the uniform proof is in `RESULT.md`. Numerical examples do not certify that the system has exactly two peaks. The proof treats at least two maxima with the asymptotic locations stated, not a complete mode count.
