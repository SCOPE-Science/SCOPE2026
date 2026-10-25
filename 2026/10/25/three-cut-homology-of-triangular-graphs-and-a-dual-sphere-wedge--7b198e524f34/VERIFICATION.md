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

# Verification

The attached `CHECK.py` uses only Python's standard library. Run `python3 CHECK.py` to enumerate all nonempty dual faces for \(n=5,6,7,8\), reconstruct direct connectivity of each selected triple in the triangular graph, check every generated face, produce matching pairs, and topologically sort the complete directed Hasse incidence graph after matched-arrow reversal. It reports the exact face and critical-cell counts in RESULT.md and ends with `PASS` when every check succeeds. This check was executed on the supplied script.

The all-parameter mathematical verification is the argument in RESULT.md: opposite pairs in four-vertex supports, contractible spoke fibers, cross-polytope boundaries, CW cofiber wedges, and integral Alexander duality. No finite enumeration alone establishes the result for arbitrary \(n\), and no integral homotopy type is asserted for the original cut complex.
