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

# Reproducibility and verification

The proof is the character-product and polynomial argument in `RESULT.md`. The accompanying `verification_check.py` is an independent finite diagnostic, not a proof for all degrees.

Run `python verification_check.py` with Python 3 and NumPy. It checks \(0\le n\le30\) against exact integer tensor-product decompositions, all four mixed sixth-moment coefficients, the unique maximizing root, 124 independent Gaussian quadrature evaluations of complex-phase sixth moments, and 1581 deficit grid evaluations. The quadrature uses normalized Chebyshev nodes and weights on \(SU(2)\), rather than the tensor-product expansion.

The analytic proof covers **every** integer \(n\ge0\). No finite testing, publication-priority claim, or independent audit is used in place of proof. Historical specialized Chebyshev norm results have not been comprehensively audited.
