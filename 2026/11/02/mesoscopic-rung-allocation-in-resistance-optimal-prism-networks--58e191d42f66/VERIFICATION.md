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

The accompanying `VERIFY.py` was executed using Python, NumPy, SciPy and SymPy, returning `PASS 57 exact, direct-matrix, and numerical checks` in the local numerical tests. The executable source in this package is the checked artifact; finite checks supplement, rather than replace, the analytic proof in `RESULT.md`.

Checks comprise 15 exact rational trace identities obtained by a full Laplacian and a separate cycle block calculation; 18 unrestricted per-edge SLSQP solves matched against the orbit-symmetric scalar optimum; 20 comparisons of the closed resolvent identity with the finite Fourier sum; one exact unit-price cube check; and three asymptotic numerical comparisons at graph sizes 1000, 10000 and 100000.

The proof of strict global uniqueness and the fractional scaling is mathematical rather than computational. The asymptotic error term is not certified by finite experiments. A published 2017 prism formula paper was located, but its full text was not accessible for detailed inspection; the readily available abstract specifies unit edge resistances, not optimization. Independent mathematical audit has not been performed.
