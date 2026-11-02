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

# Reproducible mathematical verification

The standalone `verify.py` uses Python's standard-library `fractions.Fraction` for exact matrix inversion, exact hitting-transform calculations, and exact comparison of nonnegative entries. Its `returning_transform` constructs the first-return Laplace transform by solving the killed-state equations, not by reusing the occupation-renewal formula in its expression for the resolvent. It compares the two constructions for nine irreducible generators and six positive rational resolvent parameters, including unequal-rate directed cycles and an asymmetric fully connected example. It also checks stochasticity and the diagonal criterion, and brackets the cycle thresholds for dimensions \(3\) through \(15\).

Execute `python verify.py` from the extracted package directory. The checked output is:

`VERIFY_OK: exact_first_return_checks=222; directed_generators=9; cycle_boundaries=13`

The analytical proof, not the numerical bounds or finite cases, establishes strict monotonicity and sharp positivity for arbitrary finite irreducible Markov generators. Approximate floating-point use near a sharp threshold is unverified. Publication priority and independent validation are not certified by this mathematical check.
