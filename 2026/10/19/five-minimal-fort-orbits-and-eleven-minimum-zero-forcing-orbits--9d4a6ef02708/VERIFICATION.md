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

# Verification and scope

Run `python3 verify_minimum_orbits.py` in the directory containing `CLASSIFICATION.json` (Python 3.10 or later; no third-party dependencies). The verifier checks every one of the 65,536 initial subsets by direct synchronous forcing on the explicitly labelled cube. It checks the inclusion-minimal family by single-vertex deletions, confirms it agrees with the minimum sets, and recomputes the canonical representatives, orbit sizes, times, and time multiplicities under all 384 automorphisms. The equality with the labelled table is asserted in the code. The argument in `RESULT.md` justifies the forcing dynamics, the deletion criterion, and exhaustiveness of the group. This finite check is limited to ordinary zero forcing on \(Q_4\).
