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

The exact-arithmetic checker `check.py` reconstructs the independent-with-replacement batch kernel. It verifies the zero-multiplier event probabilities for integer batch sizes \(2\le q\le9\), the inclusion-exclusion survival identities, and exact state distributions through five iterations at \((q,\alpha)=(4,4)\) and \((4,19/5)\). It recomputes the squared-error multiplier and the rational product entering the logarithmic Lyapunov exponent.

The infinite-time almost-sure statements are not established by finite tests. They follow analytically from geometric waiting times and the strong law of large numbers, respectively. The checker is supporting exact-arithmetic evidence rather than an independent audit.
