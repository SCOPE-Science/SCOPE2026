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

The analytic finite-dimensional decomposition and the tridiagonal eigenvalue identity establish the entire singular spectrum for every admissible \(b\) and \(h\). The geometric-mixture arguments prove weak convergence, convergence of each fixed nonnegative power moment, the exact upper-tail rate, and the mass at singular value \(1\). A separate row-squares computation supplies the Hilbert–Schmidt norm independently of diagonalization.

A reproducible NumPy checker accompanies this package as `artifacts/check.py`. It independently constructs full small matrices on actual tree vertices and compares their complete singular-value lists against the theoretical multiplicity formula. It also checks the exact Frobenius norms and evaluates the limit quadratic moment via its infinite mixture truncated at \(L=109\). All checks passed on test configurations \(b=2,3,4\), with 13 full singular-multiset comparisons. Such finite tests cannot verify the all-height or tail limits; those follow from the proof.

No external or independent mathematical or bibliographic audit has been performed. The scope excludes irregular trees, jointly growing branching factors, and weighted variants of the operator.
