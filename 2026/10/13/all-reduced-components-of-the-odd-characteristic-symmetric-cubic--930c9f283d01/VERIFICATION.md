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

# Verification

The proof reconstructs the gradient of \(e_3\), shows that every critical point has at most two distinct coordinate values, solves the resulting derivative constraints exactly, and checks the all-equal boundary. That yields the set equality for the reduced critical locus over an algebraically closed field. The component count follows from irredundant equal-dimensional linear components, and Hessian ranks prove generic smoothness.

To replay corroborating computations, run `python3 verify.py`. The program uses only the Python standard library. It checks every point of \(\mathbb F_p^n\) in the tested ranges for \(p\in\{3,5,7\}\), compares the direct gradient and the proposed classification, checks component counts, and computes the generic Hessian ranks by modular row reduction. The output ends in `VERIFY_OK`.

These finite-field computations do not establish the algebraically closed or arbitrary-dimensional theorem. The exact algebraic proof is in RESULT.md. Computations do not assess nonreduced structure, embedded primes, hypersurface singularities, or originality. No independent audit has been performed.
