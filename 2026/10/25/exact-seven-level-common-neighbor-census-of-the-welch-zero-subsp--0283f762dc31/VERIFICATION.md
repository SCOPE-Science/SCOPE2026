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

# Verification details

Use `python3 certificate_welch127.py` and `python3 crosscheck_intersection.py`. They run with Python 3 standard library only; no downloaded data or extra package is required.

The main certificate verifies: polynomial irreducibility and all 127 nonzero inverses; both exhaustive 11811-member Grassmannian enumerations; exactly 127 zero Welch sums; 127 distinct scalar translates of the explicit seed; 42 connection multipliers; all 126 codegree multipliers; the exact seven-class table; 15113 triangles; and independent Kloosterman consistency via \(\mathrm{Kl}_7=-13\).

The crosscheck constructs the graph from direct intersections of the 127 zero-sum spaces and directly counts common-neighbor sets for all 8001 unordered vertex pairs. Both verifiers were executed from their package paths with matching exact integer output. Finite enumeration is exhaustive for this *finite* theorem; neither verifier supports claims outside the specified field or exponent.

No independent audit was performed.
