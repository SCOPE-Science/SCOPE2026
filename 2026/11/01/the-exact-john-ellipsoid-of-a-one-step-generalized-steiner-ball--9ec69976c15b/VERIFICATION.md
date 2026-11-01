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

The included `verify_john.py` was executed with the standard Python interpreter. It passed 14,526 deterministic high-precision diagnostics: equality identities for the proposed axes, positive John contact weights, sampled upper/lower inclusion inequalities, normalization, the exact shaking endpoint, and the dimension-crossover limit. Reproduction command: `python3 verify_john.py`.

The universal inclusion claim is established by the displayed quadratic certificates in `RESULT.md`, not by the finite sampling grid. The global maximality/uniqueness claim uses the standard John contact characterization and a regular simplex of contact points. The limiting statements follow from direct radical expansions, rather than numerical extrapolation. No independent mathematical review has been performed.
