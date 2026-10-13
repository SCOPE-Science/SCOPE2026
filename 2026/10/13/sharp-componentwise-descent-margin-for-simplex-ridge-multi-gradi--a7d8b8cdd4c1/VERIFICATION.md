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

# Reproducibility of the sharp simplex-ridge inequality

The proof is analytic and valid for every \(m\ge2\), every \(\rho>0\) and \(\sigma>0\), and arbitrary finite-dimensional real gradient columns. Its two nonstandard arithmetic points are the exact simplex maximum \(\max_{\Delta_m}(\lambda_i-\|\lambda\|^2)=(m-1)/(4m)\) and the explicit all-\(m\) KKT witness. Both are established in RESULT.md without relying on numerics.

Run the standalone standard-library file with `python verify.py`. The exact-rational regression checks cover \(9216\) two-gradient geometry instances, explicit all-\(m\) equality families for \(2\le m\le12\) under multiple rational \(\rho\) and \(s\), and the objective differences of the strongly convex quadratic example. Expected output:

`VERIFY_OK 9216 rational geometry instances; witness objective increase 27/196`

`SHARP_CERTIFICATE_OK m=2..12, exact KKT, noncollinearity, quadratic ascent`

The \(27/196\) test concerns an additional rational biobjective instance; the main theorem's strongly convex example has exactly \(3/8\) first-objective increase and \(-13/8\) second-objective change. These finite tests do not independently certify the infinite claim, nor do they constitute an independent scientific audit. Stochastic gradients, nonexact simplex solves and constrained projections were not tested or claimed.
