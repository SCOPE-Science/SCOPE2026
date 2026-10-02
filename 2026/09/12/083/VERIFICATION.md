---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

The exact verification command is python artifacts/verify_finite.py. It checks all 12 globally shortest lattice-class representatives, all 48 sector minima/top dimensions, the grade-at-representative bound 2, all earlier-grade zeros there, the squared-top sum 149, and vacuum coefficients through grade 6.

The all-grade conclusion also requires the lattice-decomposition proof in RESULT.md. The computation is finite and is not itself an infinite verification. The support bounds prove that the grade-2 box 14 and vacuum grade-6 box 20 contain every contributing weight. Later exploratory coefficients are not certified here.
