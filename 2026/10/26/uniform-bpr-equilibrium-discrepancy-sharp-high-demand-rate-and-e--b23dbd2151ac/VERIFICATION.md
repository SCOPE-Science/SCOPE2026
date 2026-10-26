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

# Computational verification and scope

Run `python verify.py` in a Python 3 environment with SciPy. It checks 284 finite numerical inequalities and equilibrium identities against independently solved two-parallel-link cases and a finite scalar grid. A successful run reports its actual assertion count. Exact theorem proof is in RESULT.md: finite tests do not establish convexity or semialgebraic nonrecurrence for arbitrary graphs. The fourth-power identity `t**3*delta+4*t*delta**3=1` is algebraically exact, while high-traffic numerical tests have floating-point limitations.

Independent audit: not performed.
