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

`verify_trace_ranges.py` was run with NumPy and completed 5,580 finite assertions: randomized Takagi forms with independent skew-symmetric perturbations; explicit radius-maximizing frames; zero-valued frames in both parity regimes, including odd full dimension; upper bounds on random frames; and inversion of cumulative disk radii to singular values. Tested dimensions were 2–10, 20 samples each. The numerical tolerances are stated in the code.

The general theorem is established analytically in `RESULT.md`: (1) polar factorization of antilinearly self-adjoint operators with conjugation commuting with the modulus; (2) the Ky Fan variational principle and its spectral-multiplicity equality criterion; (3) connectedness, rotation symmetry and explicit zero-frame constructions; (4) consecutive-difference recovery of generalized singular values. No finite run proves an infinite-dimensional statement. Analytical examples distinguish attained and unattained disk boundaries.

Independent mathematical validation has not been performed. Residual novelty risk concerns possible equivalents in older matrix congruence and generalized numerical-range literature.
