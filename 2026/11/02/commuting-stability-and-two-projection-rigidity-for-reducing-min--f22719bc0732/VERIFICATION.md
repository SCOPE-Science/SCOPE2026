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

The theorem is proved in `RESULT.md` using the positive reducing-minimum spectral characterization, a finite-product well-order argument, and the Halmos canonical form. On the generic two-projection part, direct multiplication gives the quadratic identity and the two characteristic roots; both spectral branches are necessary to rule out an infinite principal-angle spectrum. The counterexample has explicit rank-one projection blocks and summable angle differences.

Execute `python3 verify.py` with Python 3 and no external dependencies. The program performs 1,120 checks for exact rational projection matrices, characteristic and polynomial identities, and finite numerical geometric-angle tests. These are bounded finite checks, not an exhaustive verification of all operators, Borel functions, or infinite Hilbert-space decompositions.

Known scientific limits include separability, finite arity for the commuting assertion, and two projections for the complete noncommuting classification. The stated first-public source date is the original 2026-08-19 preprint submission, not the later revision. Full historical priority and independent mathematical validation remain unperformed.
