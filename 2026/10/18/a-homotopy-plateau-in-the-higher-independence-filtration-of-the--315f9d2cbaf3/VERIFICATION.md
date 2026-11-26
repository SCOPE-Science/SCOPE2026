---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

# Reproducibility

Run `python3 verify.py` (Python 3.10+; standard library only). Compare the parsed output to `certificate.json`. The calculation generates the connected five-vertex masks, excludes their supersets, builds the specified vertex-toggle matching, and verifies global acyclicity and the dimensions of all unmatched faces. The homotopy argument is in `RESULT.md`: the critical vertex and the 21 critical seven-cells constitute the entire ordinary Morse CW model. The computation is exhaustive only for the specified graph and cutoff four.
