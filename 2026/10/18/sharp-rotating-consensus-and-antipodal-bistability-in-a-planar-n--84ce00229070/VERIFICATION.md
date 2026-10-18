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
# Verification protocol

Run `python3 verify.py` in the same directory as this document. Expected output: `CHECK_OK finite_diagnostics=20057`.

The script directly constructs and normalizes complex two-agent updates, then compares them with the independent half-angle expressions over 10,000 seeded random configurations. Other diagnostics cover monotonicity signs, the mixed-regime fixed separator, critical asymptotic square decrements and the exact identity boundary. The proof of global convergence, the complete list of basins, and the limiting escape-time coefficient are analytic and do not follow from numerical sampling. The script uses only the Python standard library and reproducible seed 731405; no external data or downloaded dependencies are required. Independent mathematical audit has not been conducted.
