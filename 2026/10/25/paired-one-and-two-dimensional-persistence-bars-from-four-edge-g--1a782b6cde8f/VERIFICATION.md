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
# Reproducibility and proof checks

Run `python3 verify.py` with Python 3.8 or later. It reports five test cases and ends with `CHECKS_PASS`. The script uses only the Python standard library and enumerates simplices, computes mod-two chain ranks, tests the graph-metric isometry, the private-center four-cycle links, the octahedral six-vertex subcomplex, and domination at radii two and three. The verified finite cases include a tree, a cycle, repeated endpoint pairs, and overlapping endpoints. The source of the all-parameter guarantee is the mathematical proof in `RESULT.md`, not these finite examples. The persistence splitting is additionally checked logically by the explicit nonexpanding graph retraction; no claims are made about floating-point metric spaces or independent audit.
