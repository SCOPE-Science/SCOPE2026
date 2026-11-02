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

# Reproducible mathematical checks

Run `python verify_figure8.py` with Python 3.10 or newer. It uses only standard-library rational arithmetic, numerical loops, and deterministic pseudorandom sampling, and printed:

`VERIFY_OK 54 exact rational equalities/inequalities, 12 independently integrated or sampled tests`

Exact rational assertions independently recompute the moment integrals from conditional uniform distributions for multiple positive rational length pairs. They check the three closed forms, cubic contrast, positivity, and algebraic feasibility. A separate midpoint double-integration routine computes shortest routes directly in circle coordinates rather than using the derived moment expression; a seeded random graph sampler provides an additional numerical cross-check. The proof for all positive real lengths is in RESULT.md. These finite tests do not establish the universal identity, historical originality, statistical estimation guarantees, or independent mathematical certification.
