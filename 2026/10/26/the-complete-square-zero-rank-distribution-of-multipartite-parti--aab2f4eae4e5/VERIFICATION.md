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

# Reproducible finite checks

Run `python3 check_multipartite.py` from the directory containing this file and the script. The script defines two separate count procedures: one evaluates the closed part-injection formula, and the other directly enumerates all partial bijections with disjoint domain and image and filters by equality of graph distances. For bipartite graphs, it also compares an independently coded two-pattern formula and verifies the maximum-rank expression. No external packages are required.

The output file `checks.txt` records all cases and ends with `ALL_MULTIPARTITE_SQUARE_ZERO_CHECKS_PASSED 19 6119`.

These finite checks do not establish the theorem for all vertex numbers; the arbitrary-size assertion follows from the bijection and independent selection counting proof in `RESULT.md`. There is no external independent audit or certification.
