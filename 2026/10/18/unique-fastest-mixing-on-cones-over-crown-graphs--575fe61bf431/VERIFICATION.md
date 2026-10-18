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

# Verification methods and limits

The accompanying standalone script `verify_cone_crown.py` reconstructs the entire nonnegative stochastic matrix from graph edges rather than reading stored matrices. It checks exact rational spectral identities for \(4\le m\le30\), independently computes numerical eigenvalues of full matrices for \(4\le m<40\), factors five exact characteristic polynomials for \(4\le m\le8\), and compares 840 sampled feasible symmetric stochastic matrices with the proposed global optimum. The script needs NumPy and SymPy and prints counts and failures. Its observed counts were 324, 72, 5, and 840; every test passed.

Finite tests do not prove a universal statement or uniqueness. The mathematical certificate is the five-subspace eigenvalue decomposition, the exact weighted-eigenvalue lower-bound identity, attainment with nonnegative holding probabilities, and the positive-semidefinite equality argument forcing every feasible optimum to coincide with the proposed kernel. The proof covers all integers \(m\ge4\). It does not address nonsymmetric or nonuniform-stationary chains. Independent audit has not been performed.
