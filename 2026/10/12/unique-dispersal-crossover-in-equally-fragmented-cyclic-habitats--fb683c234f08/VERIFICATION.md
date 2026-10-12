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

# Reproducible verification of the cyclic-habitat theorem

Using Python 3 standard library only, run `python3 verify_model.py` in the directory containing the attached verifier.

The verifier independently rebuilds two symbolic bivariate characteristic polynomials by exact integer continuants and compares their coefficient dictionaries to the claimed factored polynomial. A separate integer Bareiss eliminator checks 24 actual cyclic determinants without using continuants. It checks both rational Rayleigh witnesses, the rational inequality \(62/101>3/5\), the strict test \(474/941>1/2\), the favorable-site and interface counts, and the elementary spectral-gap inequality. It also performs supplementary numerical Perron power iterations for dispersal intensities \(1,2,4,5,10\) and verifies the eigenvalue comparison for two and three repeats at intensities \(1\) and \(5\). Numerical bisection approximates the unique crossover within \((4.0025,4.0026)\).

Expected successful output:

`VERIFY_OK exact_determinant_identity=1 direct_bareiss_checks=24 rayleigh_witnesses=2 edge_counts=2 periods=1,2,3 unique_root_bracket=(4.0025,4.0026)`

The coefficient identity and rational tests are exact. Power iteration and the narrow numerical root interval are **not** infinite proofs and cannot establish uniqueness or the classification for all positive intensities. The all-parameter classification follows analytically from the continuity, strict monotonicity, determinant identity, and eigenvalue-gap argument in the main proof. No independent audit has yet been carried out.
