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

# Verification and scope

Reproduction: install dependencies from `requirements.txt` and execute `python verify.py` in a directory containing both files. The observed result was `VERIFY_OK 31124 checks`.

The checker constructs exact rational transition matrices for all mixed factor tuples with 2–4 coordinates drawn from sizes 2–5 and total size no greater than 100. It checks entrywise nonnegativity, symmetry, all row sums, the predicted holding threshold and Fourier subset multiplicities; it then compares the complete predicted spectrum with independently computed symmetric-matrix eigenvalues. It also independently solves the reduced linear program for two-factor sizes 2–13 and checks random unaveraged feasible matrices on selected products. Finite checks are not a proof of the unrestricted uniqueness assertion; the analytical fiber-Laplacian argument supplies that step.

Critical analytical checks: the norm of a symmetric row-stochastic matrix centered by the uniform rank-one projector is convex under automorphism averaging; the tensor eigenvalues are exactly \(1-\sum_{i\in A}q_iw_i\); the two lower bounds are simultaneously attained; and equality of a positive-semidefinite quadratic form on a saturated coordinate eigenspace forces individual fiber Laplacians. There are no unproved conjectural extrapolations in the stated theorem.

Scientific scope: only finite Cartesian products of complete graphs with every factor size at least two, with individually chosen symmetric edge weights and permitted self-loops. No independent external mathematical validation is included.
