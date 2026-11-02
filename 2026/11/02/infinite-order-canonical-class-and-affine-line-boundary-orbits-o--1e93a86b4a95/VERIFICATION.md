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

Run `python3 artifacts/verify_boundary.py` with SymPy. The program was run from the supplied file and printed `VERIFY_OK` for n in (1,2,3,5). Checks cover the defining-equation derivation, invariant coordinates, inverse boundary parametrization, boundary translation modulo the hypersurface equation, and leading differential coefficient. They support but do not replace the general algebraic proof.

The Picard localization argument and the assertion that *every* additive-group action preserves the boundary rely, respectively, on a mathematical proof and Nikitina's published Proposition 8; neither is certified by finite computer evaluation. Independent audit has not been performed.
