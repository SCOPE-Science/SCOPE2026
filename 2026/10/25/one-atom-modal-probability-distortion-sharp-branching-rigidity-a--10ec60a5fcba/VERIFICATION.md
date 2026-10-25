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
# Reproducibility and limits

Use a standard Python 3 installation and run `python3 checker.py` in the directory containing this file. No third-party packages or network requests are needed.

The code independently recomputes the possibility image for every subset of an \(n\)-point set and evaluates the maximum absolute cardinality discrepancy. It exhausts all binary relations through four worlds, then all two-predecessor-per-world relations through five worlds. It verifies the sharp four-world split into 312 star and 144 triangle cases, and the five-world count of 4200 with no triangle exception. It checks zero discrepancy gives \(n!\) relations through four worlds, and separately verifies the labelled counting identity using a dynamic-programming Stirling-number recurrence through twelve worlds.

Expected terminal marker: `ALL_CHECKS_OK`. The general theorem for arbitrary \(n\ge5\) is established by the explicit combinatorial proof, not by these bounded experiments. There is no external independent audit or expert certification.
