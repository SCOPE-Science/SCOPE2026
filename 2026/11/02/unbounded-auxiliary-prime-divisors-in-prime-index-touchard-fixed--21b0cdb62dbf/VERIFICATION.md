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

# Reproducibility

Run `python3 verify_touchard.py` with Python 3 standard library. Successful actual execution printed:

`VERIFY_OK finite_difference_primes=18 fixed_divisor_examples={5:10,29:174} modular_periods={2:3,3:26,5:3124} algebra_finite_fields={2,3,5,7,11}`

The script computes the fixed divisors from integer values and independently from finite differences for 18 small prime indices, verifies the two named examples, exhaustively checks the modular residue-function tables at auxiliary primes two and three (and the period at five), and verifies the polynomial finite-field identity at every nonzero residue for auxiliary primes two, three, five, seven, and eleven. These checks have finite coverage; the infinite theorem depends on the proof and Dirichlet's theorem in RESULT.md, not on extrapolation. This artifact is a self-review, not an independent audit.
