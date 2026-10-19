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

# Reproducible mathematical checks
Run `python verify.py` with Python 3, SymPy and mpmath installed. It performs exact rational symbolic Legendre/Jacobi kernel integrations, mass and endpoint reconstructions through several degrees; it also solves threshold equations with 50-digit mpmath precision and verifies completely monotone endpoint moment conditions over representative inputs. The observed outcome was `PASSED 236 consistency checks`.

These computations do not exhaust all possible degrees or all positive step sizes. Exact universal statements are established by the Markov–Lukács interval representations, finite-dimensional minimum-norm interpolation, strict monotonicity of the explicit cutoff functions, and complete-monotonicity coefficient equivalence in RESULT.md. No independence, formal proof certification or external validation is claimed.
