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

## Checks performed

Exact rational elimination for degrees zero through eight establishes ranks 1, 3, 5, 6, 9, 9, 10, 12, and 11. The degree-eight alternating sign null vector, its zero sum, and the nonzero constant-sector eigenvalue are checked independently from the rational Gram matrix. Modular elimination over the prime 1000003 certifies full rank for every integer degree from nine through 134; all rational denominators are invertible modulo that prime. The Bernstein–Szegő inequality and strict diagonal dominance supply the analytic proof for all degrees at least 135. Running the included `CHECK.py` reproduced the declared checks.

## Boundaries

No finite calculation is treated as a proof for infinitely many degrees. The infinite-degree proof invokes a classical, cited inequality. No numerical approximation, unattested full-text inspection, or independent audit is claimed.
