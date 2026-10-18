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

# Reproducibility and proof boundary

Run `python3 verify.py` using Python 3 standard library. The verifier constructs exact, integer-valued appending edges for integer bases 2–2000 on the first 220 indexed Lucas values, checks all represented three-term paths have no successor, confirms their structural classification above the initial values, tests 561 instances of the explicit infinite family, and checks index-gap exclusion in 3036 small cases. Expected output begins with `VERIFIED` and reports diagnostic counts. These computations are finite; the complete unbounded proof is in `RESULT.md`, Steps 1–4.

Critical symbolic steps independently checked algebraically: the lower-minus-upper estimate in the greater-gap case is \(5F_{k+1}/7>0\); the smaller-gap case is an exact equality in the bounding expressions; both contradict the strict digit ratio constraints. Lucas product signs are checked against the first values and by exact recurrence identities. No computer-assisted infinite certificate or independent audit is claimed.
