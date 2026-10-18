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
# Verification and reproducibility

The package includes `volterra_selfcommutator_check.py`, a standalone Python 3 standard-library checker. Run `python3 volterra_selfcommutator_check.py`. Its 948 checks include independent exact expansions of \(J^mJ^{*m}\) and \(J^{*m}J^m\) for \(m=1,\ldots,6\), their rational kernel values, symmetry and reflection, rank \(2m\) of rational evaluation matrices, and coefficient nonvanishing for a sample of fractional orders.

The analytical proof, not computation, establishes the theorem for all real \(\alpha>1/2\). In particular, the finite computation does not certify an infinite-rank property or exhaustive novelty. Critical analytical checks are the distributional derivative identity for integer orders, endpoint jet divisibility, the nonzero generalized-binomial coefficients for noninteger orders, and independence of arbitrarily many kernel sections by a Vandermonde determinant. The trace and inertia statements then follow from Hilbert–Schmidt composition and the reflection unitary.

The checks do not cover \(0<\alpha\le1/2\), any complex integration order, singular-value magnitudes, or independent priority verification.
