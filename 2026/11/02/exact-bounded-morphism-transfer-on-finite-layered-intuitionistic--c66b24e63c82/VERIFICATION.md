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

# Verification and reproducibility

Run the standalone \(\texttt{checker.py}\) with Python 3 and no third-party libraries. The script (i) computes the source-layer Stirling-number transfer with exact integers, (ii) independently enumerates functions on 449 source/target shapes and explicitly tests surjectivity, order preservation, and every back-condition witness, and (iii) tests the thick-target product formula for widths two through four and heights through four. Its required last line is \(\texttt{ALL_CHECKS_OK}\).

This is finite corroboration, not infinite enumeration and not independent mathematical validation. The all-size claim is justified by the completed-suffix and eligible-point proof in \(\texttt{RESULT.md}\). It does not extend to arbitrary finite posets. Published record comparisons include two summary-only items for which complete text was unavailable.
