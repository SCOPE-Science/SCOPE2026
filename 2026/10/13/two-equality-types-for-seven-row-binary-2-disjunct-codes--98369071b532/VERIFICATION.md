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

Run `python3 verify.py` with the standard Python library. The program generates all nonempty supports on seven points, performs a definition-level backtracking enumeration for target sizes eight and seven, and then reconstructs the equality structure.

Expected terminal line:

`VERIFY_OK target8=0 nodes8=116093 maximum=7 maxima=31 singleton=1 fano=30 row_group=5040 orbits=2 orbit_sizes=1,30 stabilizers=5040,168 nodes7=134096 census_sha256=c6d843cb81ba620e9f5dec28c20e01b50e3c2ce72e1f2616971ea0f0c2d78027`

The target-eight search is exhaustive, so its zero count is the upper-bound certificate. The target-seven search is exhaustive, so the 31-family census is complete. Each nonsingleton maximum is then checked to consist of seven triples in which every point pair occurs exactly once. Finally all \(5040\) row permutations are applied to a fixed Fano representative, producing exactly the \(30\) nonsingleton maxima and stabilizer order \(168\).

No randomized step, timeout inference, or extrapolation to larger parameters is used.
