---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 check_maximal.py` with Python 3.10 or later. For every graph order from 5 to 16, the script constructs the antihole, computes distances by the Floyd–Warshall algorithm, and builds general-position sets by adding only vertices that do not complete geodesic triples. It counts a set as maximal only if no legal addition exists, including additions with smaller labels than its final vertex. The script compares the complete labeled counts by size with the formula in `RESULT.md`. It is a finite check of the maximal-set theorem, not a proof at untested orders. The all-order argument is given in `RESULT.md`.
