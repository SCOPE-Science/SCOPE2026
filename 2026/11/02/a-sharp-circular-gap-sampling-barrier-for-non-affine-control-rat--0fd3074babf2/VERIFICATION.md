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

# Reproduction and boundaries

Run `python checker.py` with Python 3.10+ and no third-party modules. The checker tests exact-rational two-node Radau identities, seeded finite circular meshes, sampled phase maxima, and the equispaced minimax inequality; its confirmed output is `PASS 11313 reproducibility checks, seeded; N=2 fLGR ratio = 29/2.`. For proof of the universal statements, use the physical-time chain rule and largest circular gap argument in `RESULT.md`. The computations do not certify any untested grid, high-order control, or complete optimized trajectory.
