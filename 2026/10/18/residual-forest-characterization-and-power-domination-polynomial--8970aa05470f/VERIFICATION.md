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

Run `python3 verify_compact_polynomial.py` with Python 3.10 or newer. It compares the new single-sum coefficient formula with exact enumeration by direct labelled line-graph observation and forcing, including the empty-set and star boundaries and the mixed example. The test caps root graphs at thirteen edges and is not used in the proof. The earlier `verify_power_multipartite.py` and `verification_output.txt` pertain to the two-sum formula and its rook and triangular specializations; they do not check the compact weight directly.

The all-parameter argument is the exact forest criterion followed by subset-lattice inversion and the explicit summation over empty, one-part and two-part supports in `RESULT.md`.
