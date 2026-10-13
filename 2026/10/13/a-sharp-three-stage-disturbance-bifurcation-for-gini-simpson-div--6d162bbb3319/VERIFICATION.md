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

# Exact-arithmetic verification

Execute `python verify.py` (Python 3, standard library only). The script was executed successfully after being written at its actual package path. It returned:

`VERIFY_OK discriminant_points=19 bernstein_coefficients=8 descartes_sign_change=1 gcd_certificate=1 stationary_and_reflection_cases=36 root_bracket=[0.08170337904602,0.08170337904602]`

The fourth-degree discriminant polynomial identity is checked at nineteen distinct rationals; the discriminant has degree at most eighteen in the rate ratio, so nineteen exact matches certify the identity. The remaining checks include exact Bernstein signs on the middle interval, positive translated coefficients above it, the one-change Descartes certificate below it, a coprimality calculation for the no-triple-root step, and algebraic stationary-balance and reflection checks. The report supplies proofs for root counts, sign changes and global optimality over the full real domain; numerical evaluations do not replace those proofs.

The root bracket printed with fourteen decimals is display-only; the internal bisection uses exact rational endpoints. No external, independent scientific validation is asserted.
