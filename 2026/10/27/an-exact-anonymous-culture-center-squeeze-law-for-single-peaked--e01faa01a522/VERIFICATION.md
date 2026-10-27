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

# Reproduction and limits

Run `python3 verify.py` using the Python standard library only. The executable constructs all four strict preference rankings explicitly and computes head-to-head majorities; it then simulates every possible first-round elimination tie resolution. It compares the resulting tie-independent Condorcet failure condition against the two-sum formula for every odd electorate from 1 through 17. It checks larger exact integer counts independently by direct iteration and verifies convergence numerically toward the analytically established rational limit.

The evidence establishes finite enumeration independently of the symbolic derivation; the asymptotic limit is proved by the Riemann-volume argument in RESULT.md, not by numerical convergence. External priority and empirical electoral applicability are unproved. Independent audit: not performed.
