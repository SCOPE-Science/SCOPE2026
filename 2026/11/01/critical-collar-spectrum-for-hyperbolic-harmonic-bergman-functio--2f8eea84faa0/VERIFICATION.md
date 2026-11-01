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

Run `python check.py` from this directory with Python 3 and SciPy installed. The recorded execution completed with `PASSED 54 finite numerical tests`; it also printed the critical profile \(G_1(1)\approx0.374604950008548\) and the large-collar coefficient \(19.79625=15837/800\). The checks include direct \(t=|x|^2\) radial integration against the independently transformed \(s=\ell(1-t)\) formula, multiple weights and angular degrees, finite multiplicity-weighted projection defects, and the exact exponential-polynomial endpoint calculation.

The proof of the all-degree limits relies on dominated convergence and weighted Riemann sums, and the endpoint limits are successive limits. Finite tests cannot establish either convergence for all degrees or historical novelty. The radial-mode normalization and zero-exclusion hypotheses can be checked directly in `RESULT.md`. Independent validation is unperformed.
