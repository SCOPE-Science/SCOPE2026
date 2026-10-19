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

Run `python verify.py` with Python 3.10 or later; there are no external dependencies. The deterministic assertions use Python exact fractions for independent forms of the least-squares weight equation, seeded Gaussian constructions for joint-law checks, exact moment matching and numerical demonstrations of the low-dimensional and critical-window regimes. The embedded script reports its passed assertion count when successful.

The universal statements about the Gumbel law and the logarithmic sample threshold are proved analytically in `RESULT.md`, not inferred from tests. The checks are diagnostic finite instances rather than a proof for infinitely many sample sizes, and no independent audit or external validation has been performed.
