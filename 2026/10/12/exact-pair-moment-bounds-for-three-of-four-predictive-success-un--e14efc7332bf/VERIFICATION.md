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

## Mathematical checks

The verifier `artifacts/verify_exact.py` uses SymPy and should be run with `python3 artifacts/verify_exact.py`. It checks that all contact polynomials have degree at most two and that their differences from the binomial tail polynomial factor into the claimed nonnegative expressions. It symbolically checks first and second moment matching of all extreme supports, and checks 297 feasible interior rational pairs exactly. It reported `PASS: 2988 symbolic/rational checks; 297 feasible interior rational moment pairs`.

The bounds for all real feasible parameters are established analytically by the sign of the factors, not by extrapolating the finite grid. The source comparisons distinguish unrestricted finite exchangeability, moment-only infinite exchangeability, and the two-moment infinite-exchangeability class; complete verification against older, potentially equivalent moment-problem literature is not asserted. Independent validation has not been performed.
