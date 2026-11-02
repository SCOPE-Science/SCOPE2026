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

# Verification record

Run the self-contained rational-algebra checker with `python3 check.py` in the directory containing the six text files. Execution of that command against the exact embedded checker content reported `PASS: 2796 exact rational assertions`. The checker tests three rational zero locations, dimensions from one through twelve, and three exact rational evaluation points. It verifies the operator's action on rational basis functions; the matrix inverse; the tridiagonal covariance inverse; and the singular-matrix identity. These checks support, but do not replace, the analytical proof.

The fixed-rank limit is proved through Hilbert–Schmidt convergence of scaled lower-triangular matrices to a Volterra operator. The exponentially small last singular value is proved by Hilbert–Schmidt convergence of scaled inverses to a geometric rank-one operator. Those analytical arguments have no finite verification cutoff. No independent mathematical audit has been performed.
