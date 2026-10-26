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

# Verification instructions and boundaries

The standalone `verify.py` requires only Python 3 and its standard library. Run `python3 verify.py` in the same directory as this file. The script rebuilds graph edge sets and tree-copy edge masks independently of the analytic conditioning proof. For orders 4–6 it enumerates every simple labeled graph, groups results by exact edge count, counts isolated vertices and copies of path or star trees, and compares an empirical exact-rational factorial mixed-moment ratio with the claimed product formula. It then checks the direction and shape of the exact finite-size ratio for all tested factorial orders through graph size 64 and numerically checks the limiting transition's order-one correction.

Observed execution: `PASS exact random-graph enumeration: 69 parameter/motif comparisons over 33856 labeled graphs`; `PASS adjacent-ratio and unimodality tests: 39711 comparisons`; `PASS critical root numerical checks: 8; rho=0.796812130020020`; `TOTAL CHECKS: 39788`.

This is a finite diagnostic, not a proof for arbitrary graph order. The infinite exact and asymptotic claims are established separately by the counting argument and uniform analytic expansion in `RESULT.md`. Numerical root checks are approximate, not rigorous interval certificates. Independent audit: not performed.
