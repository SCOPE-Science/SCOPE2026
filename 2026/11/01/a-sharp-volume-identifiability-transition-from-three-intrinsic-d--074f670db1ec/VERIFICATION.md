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
# Reproducibility and checks

Run `python3 verify_torus.py` with Python 3 standard library from the directory containing this file. The standalone program independently derives weighted squared-uniform moment formulas by exact rational multinomial expansions, compares all first three cumulant identities, checks cubic Newton identities and the two-moment volume-fiber trigonometric parameterization, verifies positive-arc endpoints at both sides of the collapse boundary, and checks exact two-moment collisions with distinct volumes and third moments. The observed result on extraction from the reviewed source directory was:

`VERIFY_OK 23434 exact independent integration, positive-fiber, and cubic-collision checks`

These are finite deterministic and seeded tests, not an infinite-dimensional symbolic certification. The analytic argument supplies the proof for every positive triple of circle lengths. The mathematical cutoff and sharp inverse exponent are established by exact families; root perturbation is proved in `RESULT.md`. The 1978 primary paper was not available as a full text and priority remains provisional. All claims are self-reviewed only; no independent audit was performed.
