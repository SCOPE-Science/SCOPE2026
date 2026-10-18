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

# Reproducibility checks

Run `python3 verify_universal_nuclei.py` in the directory containing this document and its sibling checker. It uses only Python 3 standard libraries. For each labelled poset on zero through four vertices, it constructs the upsets, independently evaluates all subset-indexed nuclei, checks extensivity, idempotence, meet preservation and distinctness, and compares all nucleus compositions with the bottom-only singleton-probe condition and comparability-components characterization. It also checks all pairs of singleton nuclei. A successful run prints `VERIFY_OK` and histograms by size. The run used to prepare this package reported \(1,1,3,25,543\) labelled posets and `VERIFY_OK`.

These are **finite-instance** tests. The unlimited quantification over finite posets is proved in the accompanying mathematical argument, not by exhaustively testing a bounded list. No independent external proof audit or certification has been performed.
