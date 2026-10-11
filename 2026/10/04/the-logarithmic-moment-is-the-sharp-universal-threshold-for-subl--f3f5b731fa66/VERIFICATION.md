---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The sufficient direction is a valid geometric-subsequence Borel-Cantelli argument: finite logarithmic moment makes the sampled tail probabilities summable, while bounded upward growth fills gaps and letting the ratio tend to one forces tau_n/n to zero. For sharpness, divergence of the dyadic log-tail sum and independent block activations yield infinitely many active blocks; the constructed process respects unit upward growth, nondecreasing timestamps, and pointwise domination by T, with endpoint ratios tending to 1/2. The harmonic-window bound follows from tau_n/n to zero.

## originality

PASS

The motivating 2026 AoI paper and its 2023 predecessor use stronger positive-power moment assumptions for sublinear delay. Resultary found no equivalent logarithmic-moment threshold. The submitted theorem both weakens sufficiency and supplies a matching universal converse.

## value

PASS

This identifies a sharp structural threshold for a mechanism central to heavy-tailed asynchronous stochastic approximation, admits dominators with no finite positive moment, and gives a matching failure construction. It is a substantive boundary theorem rather than a routine weakening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
