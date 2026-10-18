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

# Verification instructions and actual checks

The result is a combinatorial theorem. Its critical deductions are independently accessible from the axioms: (i) the point/line geodetic interval containment, (ii) \(v\le a+1+qb\) and \(v\le b+1+qa\), (iii) the maximal-union concurrency equality, (iv) direct flag coverage, (v) exact intersections of two different flag sets, and (vi) flag-graph connectivity by shared point/line and opposite-flag two-step paths.

Run `python3 verify_small_planes.py` and `python3 verify_flags.py` with Python 3 and no external libraries. Compare standard output byte-for-byte to `small_output.txt` and `flags_output.txt`, respectively. The first program computes shortest-path intervals independently and exhaustively tests all subsets of sizes up to four for order two and up to six for order three. The second independently constructs incidence geometries over fields of orders two, three, four and five, validates plane axioms, and verifies every geometric witness and its full pairwise distance spectrum.

The exhaustive searches report, at order two, zero geodetic sets of sizes one to three and 21 of size four; at order three, zero for sizes one to five and 52 of size six. The resulting minimum simultaneous-exchange thresholds are two and four. The second program reports 105 flag witnesses and threshold five at order four, and 186 witnesses and threshold six at order five. These tests cover the stated small instances, not all projective planes, and do not certify non-Desarguesian instances computationally.

No externally certified proof, formal prover, independent audit, or additional evidence channel is asserted.
