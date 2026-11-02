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

# Reproducibility and scope of checks

Run `python verify.py` with Python 3, NumPy, SymPy and mpmath installed. Its checks include three exact rational Markov-precision identities; 280 numerical inverse comparisons across several sample sizes and decay rates; 36 isolated-collision limits; nine two-site tail constants; three uniform-spacing Monte Carlo diagnostics; and four two-site regularized spectral-moment quadratures.

The successful checked output is:

`VERIFY_OK exact_precision=3 direct_precision=280 single_collisions=36 exact_two_node_tails=9 min_spacing=3 nugget_integrals=4`

The general fixed-count tail law, all real moment exponents, and nugget asymptotics are established by the written finite-dimensional factorization, collision-inclusion arguments, and analytical integration. Diagnostic calculations are not an infinite proof. Results are in exact real arithmetic and do not constitute a validated numerical error bound for floating-point solvers.

Independent audit: not performed. This file contains no independent validation evidence.
