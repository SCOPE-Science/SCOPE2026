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

# Verification

The exact ODE and parameter assumptions appear in `RESULT.md`. Executing `python3 verify_hopf.py` (with SymPy installed) checks the all-parameter identity for the real resonant cubic coefficient and the positive linear crossing speed. It also computes the cubic coefficient independently using the three-dimensional real multilinear Hopf formula for three distinct exact rational parameter triples; these finite checks do not establish the parameter-universal claim by themselves.

The analytic proof in `RESULT.md` establishes the center-manifold identity, quadratic normal-form elimination, strict sign of the factored coefficient for all admissible parameters, and the standard Hopf consequences. The claimed oscillation amplitude is local as the forcing approaches either threshold from the unstable-equilibrium side. No global attractor classification or independent audit is claimed.
