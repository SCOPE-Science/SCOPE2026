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

Execute `python3 verify.py` from the extracted package directory with SymPy, NumPy and SciPy installed. The program independently constructs the degree-three and degree-one generator resolvents, checks the exact rational transform and convolution decomposition symbolically, tests the analytic threshold comparisons in 22 integer dimensions, and checks twelve numerical finite-lag parameter settings against direct matrix exponentiation.

The exact all-dimensional sign theorem is proved in `RESULT.md` using positive exponential convolutions and strict monotonicity of their ratio. The finite numerical samples alone do not establish the absence of further crossings. Equality thresholds and open parameter boundaries are handled in that proof, not extrapolated. Source comparisons were performed against the cited scientific works, with residual priority risk described in `REVIEW.md` and `AUDIT.json`. No independent scientific audit has been performed.
