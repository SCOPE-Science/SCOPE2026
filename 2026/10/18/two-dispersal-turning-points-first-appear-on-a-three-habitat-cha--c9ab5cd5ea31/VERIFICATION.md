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

# Computational verification and limits

Invoke `python verify.py` with SymPy available. It solves the three-node stationary covariance Lyapunov equation symbolically and verifies the exact rational regional variance and derivative identities in `RESULT.md`. It checks the exact polynomial coefficient signs and the inequalities at the three rational dispersal rates \(0\), \(1/10\), and \(3\). It also symbolically verifies the generic two-node variance derivative and two noise-ratio threshold-order identities.

The positive-root count follows mathematically from Descartes' rule and the intermediate value theorem, not solely from the optional decimal roots. The robustness argument uses strict rational signs and continuity. Numerical roots are for communication only. This verification is a self-review; independent scientific audit has not been performed.
