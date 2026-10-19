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

# Reproducible checks

Run `python verify.py` in this directory with SymPy installed (see `requirements.txt`). The checker independently builds the stationary mixed-moment generator equations in degrees one through four, solves the symbolic rational systems and verifies the displayed exact variance and factorized fourth cumulant. It then reconstructs four exact-rational stationary generator systems with different damping and switching parameters, checking the cumulant in each. It confirms the zero-damping factorization and one exact-rational negative-polyomial witness.

The existence and uniqueness of the damping threshold and the two-root/zero-root dichotomy follow analytically from the positive coefficients of the relevant polynomial derivatives, continuity and monotonicity of its minimum, and strict convexity. Finite tests do not prove these unrestricted statements. The decimals printed in the result are approximate solutions, not rigorous interval bounds. No independent review or external validation was performed.
