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

Run `python verify.py` using Python with `mpmath`. The implementation uses 60-digit arbitrary precision and checks the Lambert-root equation and branch ordering for six agent counts, representative real and complex parameter regimes, two double-distance regimes with explicit critical separations, leading large-delay asymptotics for two versus three-plus agents, and the large-population critical-distance identities. On the provided environment the run printed `ALL CHECKS PASSED`.

The formal mathematical proof is in `RESULT.md`. Numerical spot checks do not establish the full quantified theorem or historical novelty. The characteristic equation is a velocity-variational equation near a resting regular simplex; it cannot be used to infer nonlinear global stability of the complete positional system. The full spectral calculation and the cutoff calculus are the logically decisive evidence.
