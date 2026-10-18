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

# Reproducible checks and limits

The included `verify.py` is standalone apart from the open-source Python package SymPy. Running `python verify.py` reproduces exact identities for the Hessian, the polar-coordinate formulas, the chart Jacobian, the two discriminants, three auxiliary resultants, the critical-image resultant, and the explicit nonempty-parameter example. No floating-point root finding or partial enumeration is used in the proof. The algebraic arguments in `RESULT.md` explain why the exact identities give conclusions for all parameter values satisfying the hypothesis.

The independent audit is not yet performed; no external validation or external certificate is claimed. In particular, the theorem makes no claim about scheme-theoretic critical-value multiplicities introduced by blowing up the rational map's base locus, nor about degenerations on the excluded parameter hypersurfaces.
