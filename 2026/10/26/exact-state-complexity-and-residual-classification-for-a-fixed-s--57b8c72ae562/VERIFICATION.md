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

# Verification of the exact-count scattered-pair formula

The proof uses the exact cross-boundary formula for scattered \(01\) occurrences, reaches every stated residual by a concrete prefix, and separates residuals by constructive one-one or two-one suffixes. Each statement holds for every positive integer \(k\), not only the tested range.

Run `python3 verify_exact01.py`; it prints `VERIFY_OK` after checking complete reachable bounded-count automata for \(1\le k\le60\), independently refining states to a fixed partition, matching the closed form and the classified residual types, and checking the statistic on binary input words through length \(11\). The verifier uses no external packages, network resources, or retained files. These finite checks do not independently certify the infinite theorem.
