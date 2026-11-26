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

The proof uses an exact nearest-phase lower bound on the weighted mismatch and a converse constructed by Bézout's identity. Strict concavity on the resulting segment proves the attained optimum. A uniform Taylor bound and the distance of the segment from the origin yield the large-denominator formula.

Run `python3 verify.py` with the Python standard library. It tests attained phases for admissible odd–odd pairs, finite uniform phase grids for selected small pairs, and the remainder scale on selected large pairs. These are bounded consistency tests, not a proof of the infinite family or the all-time maximum.
