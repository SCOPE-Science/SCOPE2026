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

# Reproducibility and scope

Execute `python3 CHECK.py`. It requires the Python 3 standard library only and terminates with `CHECK_OK assertions=6246`. The checks use independent bilateral Zak sums, an independent polyphase formula, spectral enclosures on a fixed numerical grid, and rational tests of geometric tails. These are regression and arithmetic checks, not an exhaustive numerical or formal verification of all real parameters.

The universal proof uses Zak diagonalization, exact geometric series, positivity in the cosine phase, strict convexity at the positive phase, and a one-positive-root quadratic argument at the negative phase. No independent mathematical audit is claimed.

