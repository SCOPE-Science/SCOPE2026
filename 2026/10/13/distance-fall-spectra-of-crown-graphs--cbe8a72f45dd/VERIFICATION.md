---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a_i,b_i a path a_i–b_j–a_k–b_i with i,j,k distinct establishes distance 3, since they are in opposite shores and not adjacent. Any two same-shore vertices have a common neighbor and nonmatched cross-shore vertices are adjacent. Thus the closed radius-2 ball at any vertex omits only its unique antipode. A set of size at least two meets every such ball, and a singleton misses the ball of its antipode. This proves the iff for proper colorings and the upper limit n. To realize q=2,…,n, use q−2 matched nonedges as classes and two residual shores each of size n−q+2≥2, valid also at n=3. At distance 1 an independent dominating class is either a whole shore (all same-shore vertices must be dominated) or one matched nonedge (the only mixed independent class). A whole-shore class forces the other whole shore; otherwise all classes are matched nonedges. At d≥3 the fall condition is automatic, and splitting shores with disjoint palettes gives all proper color counts 2,…,2n. The packaged artifacts/verify.py was inspected, not executed; its finite enumeration is optional corroboration and does not replace the structural proof.

## originality

PASS

The distinct claim is the complete radius-2 spectrum and the characterization of the colorings that realize it. Existing general theorems give a 3-class partition, not the full spectrum or all allowed classes. The ordinary radius-1 endpoint is explicitly not claimed as new, and the d≥3 endpoint is an elementary diameter consequence. No inspected catalogue result or full-text passage covers the radius-2 claim; historical priority is not certified.

## value

PASS

The crown is a natural test family just beyond the diameter-2 case in distance-fall theory. The radius-2 result detects and exactly describes the obstruction to automatic feasibility, gives all attainable color counts rather than a single existence statement, and exhibits a full transition between ordinary fall and unrestricted proper coloring. The value is in that structural middle regime, not in recomputing the conventional endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
