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

# Verification evidence and limits

The standalone standard-library file `verify.py` runs exact rational reconstruction of the two-by-two Gram update (including \(\det Q=-14/3\), the eigenvalue \(-7/3\), and a negative eigenvalue \(-71/87\) under positive core ridge). It verifies rank-one trace and determinant identities on a grid of rational points and four Cauchy event probabilities against fixed-seed Gaussian simulations totaling 480,000 trials; it checks ten numerical large-threshold evaluations against the analytically derived sharp tail coefficient and verifies the unique-root global optimum.

Command: `python3 verify.py`

Observed successful final line:

`VERIFY_OK exact_fraction_identity=true gaussian_trials=480000 tail_formula_cases=10 global_supremum_verified=true`

Experiments do not prove universal properties; analytic diagonalization, the Cauchy integral, polynomial monotonicity, and positive-density pole geometry provide the complete proof. The random trials use a fixed pseudorandom seed and a deliberately coarse sampling-tolerance check, not an exact statistical certificate. Independent audit: not performed.
