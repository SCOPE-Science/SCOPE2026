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

The stand-alone `check.py` is executable with Python 3 and `mpmath`. It uses high-precision bisection to locate the exact stationary root, piecewise integration of the signed kernel, and a separately integrated absolute kernel after removal of the weak singularity by a power substitution. It checks sampled orders, sampled evaluations, the special Abel radical, and the small-parameter asymptotic. The packaged replay produced `PASS: 125 independent mathematical/numerical assertions`.

The mathematical proof in `RESULT.md` uses exact integration, kernel monotonicity, strict convexity of the remaining row branch, weighted arithmetic–geometric mean, and explicit asymptotic analysis. This proof is necessary for the full continuum and uniqueness statements; 125 finite assertions cannot certify those quantifiers. No external or independent audit has been performed. Literature search is necessarily non-exhaustive, and some specialty sources were only accessible through abstracts.
