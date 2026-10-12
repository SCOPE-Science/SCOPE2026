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

# Reproduction and analytical limits

The accompanying standalone script `checks/verify_exact.py` uses Python 3 and SymPy. Execute it as `python checks/verify_exact.py` from the extracted package root. The observed output from the exact script is `VERIFY_OK symbolic_drift=1 symbolic_moment_matrix=1 exact_cases=2800`.

The symbolic part independently recomputes the conditional squared-state and cross-state expectation polynomials, verifies the exact quadratic-energy drift for formal parameters, verifies the second-moment transfer determinant, and checks the energy-matrix determinant. The finite part enumerates 2,800 exact-rational cases, with two positive scalar curvatures of equal probability and independently sampled Bernoulli lag, comparing the expectation of the quadratic energy against its proved drift formula. It also checks the specified rational stable/unstable witness.

The infinite-parameter claims and the strict boundary follow from the analytical proof in `RESULT.md`: positive definiteness for \(p>0\), summability under negative drift, and obstruction from nondecreasing energy at and above the threshold. These logical steps, not the finite test suite, establish the theorem. The checker does not certify any real-world asynchronous system, correlated sampling scheme, convergence rate, or unpublished-priority claim.
