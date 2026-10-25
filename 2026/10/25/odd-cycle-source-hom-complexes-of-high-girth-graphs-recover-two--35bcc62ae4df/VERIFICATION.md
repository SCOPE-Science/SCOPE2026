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

# Reproducibility

Run `python checks/hom_cycle_verifier.py` using Python 3. The program enumerates all graph homomorphisms and admissible coordinate-change simplices for each named finite input, compares computed connected components, Euler characteristics and isolated vertices with the two cycle-count formula, and fails on an unexpected multi-coordinate cell. Included targets are a pentagon, branched pentagons, the Petersen graph, a bridged pentagon/heptagon, a pentagon/heptagon wedge, a heptagon and a nonagon.

The computation has finitely many instances and verifies neither all graph orders nor an infinite theorem by itself. The proof in RESULT.md supplies the all-parameter argument. No independent audit or external certification has been performed.
