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
# Verification and scientific limits

The analytic proof is in `RESULT.md`. The executable symbolic checker `verify.py` was run successfully with Python 3 and SymPy; its actual console output is in `verify_output.txt` and includes exact verification of the inverse-branch cubic coefficient, inverse Bernoulli mixture formula, exact two-atom discriminant and one rational numerical-parameter example.

The checker verifies finite algebra, not the infinite-time stationary-density existence, inverse-cylinder density, universal Peano remainder or the claim of novelty. The first analytical input is Oltiboev--Vafoyev, arXiv:2610.23180v1, which guarantees a nonnegative normalized W^{2,1} density for sufficiently small Bernoulli parameter. Continuity, positivity, regularity transfer and endpoint asymptotics are proved in RESULT.md. The third asymptotic coefficient is Peano-only, not an asserted classical third boundary derivative.

The rational example with mixing probability one third tests only the coefficient identities and must not be interpreted as showing that one third belongs to the small-mixing existence interval. Independent audit and independent validation have not been performed.
