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

The standalone Python standard-library program `verify.py` builds the completed [2/2] Padé diffusion matrix through exact rational 3-by-3 matrix inversion, independently of the closed-form off-diagonal formula. Running `python3 verify.py` on the supplied source returns `VERIFY_OK 30485 exact rational checks`. The test ranges and explicit counterexample are documented in RESULT.md. The proof of the all-real-weights, all-real-steps statement is algebraic: an annihilating polynomial reduces the matrix rational function and an edgewise quadratic sign test is exact. Finite tests are corroboration, not a substitute for that proof. The package has no external dependencies, and independent mathematical audit has not been performed.
