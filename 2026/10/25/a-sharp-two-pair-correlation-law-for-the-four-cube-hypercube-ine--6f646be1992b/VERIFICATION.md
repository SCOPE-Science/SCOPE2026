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

`python3 verify.py` verifies the complete finite determinant identity on the Boolean four-cube with exact integer operations. It loops through each of the \(\binom{16}{5}=4368\) five-vertex subsets and checks agreement between two determinant computations; the coefficient census has exactly sixteen nonzero monomial coefficients, tabulated in `RESULT.md`. It verifies the displayed symbolic factorization by coefficient comparison, without floating-point determinant arithmetic. Its rational-parameter evaluations are diagnostic, not substitutes for proof.

The analytic argument independently normalizes the eight facet sums and differentiates the exact closed expression in squared correlations. That derivative proves the universal sharp bound, its unique equality case and the monotonicity claims for all strictly positive weights in the stated family.

Unrestricted sixteen-variable Hypercube inequality is not proved. Historical originality is supported by the source comparisons described in `REVIEW.md` and `AUDIT.json`, but independent scientific audit and independent historical-priority certification have not been performed.
