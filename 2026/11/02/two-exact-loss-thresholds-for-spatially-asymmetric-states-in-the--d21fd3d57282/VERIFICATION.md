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

The checker `verification.py` uses exact SymPy identities for the transformed ODE, the Jacobian conditions, and the exact gradient potential; it then substitutes seven positive rational migration rates covering all open regions and both thresholds, verifying every explicitly enumerated equilibrium. It checks the cubic center-manifold coefficient \(+8\) analytically by a symbolic limit. The analytic proof in `RESULT.md` establishes the universal claim. The checker requires SymPy, does not enumerate all real parameters, and does not replace the center-manifold argument.

The open mathematical comparison includes the 2010 original model's relevant arXiv full-text sections. The 1999 biparental Allee source was only accessible at the abstract level; its full text and broader bistable-lattice classifications require independent priority checking. No independent audit has been performed.
