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

# Reproduction and limits

Execute `python verify_cyclic.py` with Python 3 and SymPy. The expected terminal message is:

`AGR_CYCLIC_DISCRIMINANT_TORUS_CHAIN_MU_EXTENSION_DISTRIBUTION_PASS`

The verifier computes exact Jacobian Gröbner bases in the cases \((d,m,p)=(4,3,2),(3,4,3),(4,5,2)\) with quotient lengths \(7,5,61\). It checks integer-weight Euler identities for those cases, the finite-field support-stratum counting identity in ten examples, and a full finite enumeration for the split three-coordinate \(\mathbb F_8\) case. These tests are reproducible finite or polynomial calculations; they do not independently certify the universal all-parameter assertions, which follow from the mathematical proof in RESULT.md. The exact support counts must not be confused with singular-locus dimensions at multiple-zero coefficient strata.

Only the reduced discriminant is classified, not the scheme-theoretic discriminant multiplicity. At the generic geometric boundary, the isolated Jacobian singularity and its algebraic colength are proved in arbitrary permitted characteristic. Independent mathematical validation has not been performed.
