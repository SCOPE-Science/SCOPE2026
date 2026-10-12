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

# Reproducibility and boundaries

The accompanying `artifacts/check_prism.py` is complete, requires only Python 3 standard library, and can be run with `python3 artifacts/check_prism.py`. It constructs Laplacians from the graph edge list independently of the Fourier spectral reduction. It checks 80 exact Kirchhoff-index identities for integer cycle sizes 3 through 7, 200 rational stationary-optimum inequalities for sizes 3 through 10 and selected rational weights, plus 24 floating-point hyperbolic-sum comparisons for sizes 3, 4, 5, 8, 20 and 100. Observed execution:

`VERIFY_OK 80 independent exact inverse-trace identities; 200 exact optimal-root inequalities; 24 hyperbolic-sum comparisons`

The code tests finitely many values, using exact fractions where identified; the last 24 sums use floating-point tolerance. Analytical proof alone establishes existence, uniqueness, exact scalar characterization, all parameters and asymptotics. In particular, the code does not constitute exhaustive verification of arbitrary sizes or a separate independent audit. No publisher text or external code is embedded.
