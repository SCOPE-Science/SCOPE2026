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

# Verification and limits

Execute `python verify.py` with a standard Python 3 interpreter. The provided verifier recomputes all finite model steps directly, including 60 exact rational equality and sign comparisons against the derived multiplier for the squared-odds observable. It also checks 14,448 finite iterates against the rigorous all-time logarithmic bound over multiple growth constants, signed perturbations and initial population pairs, plus 16 positive- and negative-perturbation shrinking-scale first-passage tests. The observed output was:

`VERIFY_OK: 60 exact rational multiplier/sign identities; 14448 finite drift-bound checks; 16 crossover first-passage trajectories`

These computations do not certify the full infinite-horizon theorem or establish novelty. The analytic proofs of the global bound, drift sign, limiting profiles, and first-passage times are provided in `RESULT.md`, including the necessary quantifiers and perturbative error terms. A separate independent audit has not yet been performed.
