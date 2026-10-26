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

# Reproducibility and limits

Execute `python check.py` in an environment with SymPy. The code checks the polynomial change of coordinates in characteristic two; that the displayed quartic linear system maps to the surface; the four partial derivatives; all 12 basepoints over \(\mathbf F_4\), including their transversality; the intersection matrix of the three \((-3)\)-curves and the SNC star; and the finite monomial basis of the local length-16 Jacobian quotient. The exact proof of geometric completeness and cohomological geometric genus is given in `RESULT.md` and is not represented as an output of the finite checker.

The singularity is not an ordinary rational double point. Potential prior equivalent treatment of this specific degenerate Schur surface remains an originality risk. The scientific review is not independent.
