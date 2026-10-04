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

The proof uses only Nielsen majorization and an explicit ordering of the top \(N+2\) product Schmidt coefficients.

`verify_self_catalysis_bound.py` uses exact rational arithmetic. For all five multi-copy rows of the source table, it constructs every tensor-product coefficient, sorts both sides, verifies successful majorization at the stated \(N\), and verifies failure for every smaller positive \(N\). It also checks that the analytic \(N+2\) prefix obstruction yields the exact fractions
\[
\frac{18}{11},\quad
\frac{227}{105},\quad
\frac{459}{140},\quad
\frac{296}{63},\quad
\frac{928}{165}.
\]

The finite replay is supplementary to the continuous analytic lower bound and endpoint asymptotic in `RESULT.md`.

No independent audit has been performed.
