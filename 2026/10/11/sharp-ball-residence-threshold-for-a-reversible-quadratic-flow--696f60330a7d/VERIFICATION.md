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

# Verification and scope

The attached `check.py` is a standalone symbolic verifier. On execution with SymPy, it checks \(\dot P=y^2-a\) and the exact sum-of-squares formula for \(\dot G\), its stationary reformulation, and ten exact equilibrium examples. The full proof is in RESULT.md: it gives explicit uniform bounds for every confined trajectory segment and derives the equality classification for compactly supported invariant measures. These analytical steps, rather than numerical exploration or finitely many substitutions, establish the global conclusions.

The checker is not a proof of historical priority, invariant-set existence beyond the displayed equilibria, global completeness of all unbounded trajectories, or the existence of chaotic dynamics. No independent external audit has been performed.
