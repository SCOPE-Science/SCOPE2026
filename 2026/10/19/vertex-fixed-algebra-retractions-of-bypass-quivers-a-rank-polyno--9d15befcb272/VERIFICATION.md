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

The standalone file `check.py` uses Python 3 without third-party dependencies. Run `python check.py`. It independently enumerates all matrices describing maps of the three arrow-corner spaces, extends them multiplicatively to the path basis, checks every ordered basis product, checks \(F^2=F\) on the entire basis, computes ranks by finite-field row reduction, and compares the complete observed histogram with the stated Gaussian sum.

Exact checks passed for \((q,r,s,t)\) equal to \((2,1,1,1)\), \((3,1,1,1)\), \((4,1,1,1)\), \((2,2,1,1)\), \((2,1,2,1)\), and \((2,2,2,1)\). The last case comprises 8,192 maps; its 728 retractions have ranks and multiplicities \((3:1),(4:28),(5:194),(6:104),(7:288),(8:48),(9:48),(11:16),(12:1)\). The output ends in `ALL_EXACT_CHECKS_PASSED`.

The checks are finite tests only; the general theorem depends on the algebraic proof in `RESULT.md`. No independent mathematical audit or formal proof-assistant certification was performed.
