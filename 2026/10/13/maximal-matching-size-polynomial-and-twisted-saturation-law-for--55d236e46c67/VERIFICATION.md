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

## Reproduction
Run `python verify.py` with Python 3 and SymPy. The script constructs the nine allowed column states and verifies both symmetry-block determinant identities with exact symbolic arithmetic, independently enumerates all matchings and tests inclusion maximality for Möbius ladders of orders \(3\le n\le10\) rungs, recomputes graded polynomials through \(n=40\), checks the three lowest-excess coefficient series through order 54, and compares known scalar totals against OEIS A284710 through \(n=28\).

Observed execution: `VERIFY_OK states=9 symmetry_blocks=6+3 exact_determinants=2 brute_ladders=3..10 cardinality_coefficients=all extrema=3..40 excess_series=1..54 OEIS_totals=3..28`.

## Scope and limitations
Exhaustive checks cover only the stated finite sizes; they are not themselves a proof of the all-order claim. The proof of the unrestricted statement uses the bijective nine-state encoding, exact determinant identities, and formal coefficient extraction. Reproduction depends on SymPy for exact determinants. No independent mathematical audit has been performed.
