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

# Verification of the weighted-star observability classification

The package includes `verify.py`, a standalone program using only the Python standard library. Run `python3 verify.py` from a directory containing that file. It computes the weighted-star Krylov observability matrices and their determinants by exact rational Gaussian elimination, rather than relying on rounded eigensolvers.

The actual packaged source was executed and returned `VERIFY_OK` with 247 rational-weight observability cases, including repeated conductances, and 36 constructed strict-optimum rank examples for stars with 2 through 9 leaves. These checks validate both Vandermonde determinant identities in the stated test cases and illustrate the ranking existence construction. They are not exhaustive over arbitrary dimensions or real weights.

The proof of the general result is analytic: a simple-spectrum eigenvector factorization gives every finite-horizon determinant ratio, the characteristic polynomial evaluates explicitly at leaf conductances, and the polynomial Krylov determinant extends the statement to conductance collisions. The rank realizability theorem follows from a strictly positive one-sided logarithmic derivative. These steps—not finite testing—establish the universal quantifiers and boundary cases.

No independent audit has been performed. The possibility of an equivalent prior specialized weighted-star formula is a literature-comparison limitation, not an assertion of mathematical independence.
