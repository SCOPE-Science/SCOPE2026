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

# Verification and scope

Run `python3 verify.py` with Python 3.9 or later. The checker constructs every maximal chain of connected mixed proper tubes for each positive ordered part-size pair with total size four through eight. It indexes every two-face by its fixed subchain after deleting two tube ranks, and counts all maximal chains extending each fixed subchain. Each resulting number must be four, six, or eight; the checker then compares the complete observed histogram to the three closed formulas and checks incidence totals.

The successful run printed `VERIFY_OK instances 25 total_polygon_faces 216147` after exact comparisons for all 25 parameter pairs. The checksum verification of embedded file bytes is separate from these mathematical checks. No floating-point arithmetic, external data, or third-party package is required. Finite enumeration does not prove all-dimensional completeness: the proof in RESULT.md counts every possible pair of omitted tube ranks for arbitrary sizes.

Publication-date evidence is the initial public posting of Galashin's arXiv:2110.07257 on 2021-10-14; later revisions are not substituted for that date. Independent mathematical audit has not been performed.
