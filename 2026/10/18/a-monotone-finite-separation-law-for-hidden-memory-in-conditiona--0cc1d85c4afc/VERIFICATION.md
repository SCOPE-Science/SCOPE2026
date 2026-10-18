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

Run the included `verify.py` with Python 3, NumPy and SciPy: `python verify.py`. The script tests the exact Bessel-flux derivative at several site distances and times; agreement of the direct Bessel-square flip integral with the exact exponential-sinh coupling; strict increasing-distance correlations at fixed scaled reset parameter; approach to the \(K_0\) crossover from below; the explicit inverse-square correction at multiple positive arguments and site distances; and the fixed-site high-rate limit. Execution of the packaged script produced: `PASS: 81 numerical assertions`.

The proof in `RESULT.md` independently establishes all-site identities and strict inequalities using Bessel recurrences and a positive integral representation, and the uniform asymptotic remainder by an explicit integrable-density expansion. Numerics do not establish infinite-parameter statements or global literature priority. The physical-time correlation, noisy measurement errors, nonsymmetric geometries, non-exponential resets, and independent external validation are not established.
