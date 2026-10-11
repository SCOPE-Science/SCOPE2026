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

`verify.py` starts only from the fifteen K6 edge labels printed in the exact construction. It reconstructs both facet orbits, checks that there are 150 facets and face vector \(f=(16,120,330,375,150)\), and confirms that the one-skeleton is complete.

For correctness, it builds every mod-two boundary of a triangular face as a 120-bit edge vector. Gaussian elimination gives rank 104. Since the complete graph on 16 vertices has one-cycle dimension \(120-15=105\), the quotient has dimension one. The script enumerates all 230 missing triangles and checks that every boundary has the same nonzero normal form modulo the boundary span.

As a second detector, it constructs the gauge-fixed cochain \(w\) with \(w(Ax)=0\) and \(w(xy)=1\) exactly when \(\{A,x,y\}\) is missing. It verifies on all triples that \(w\) evaluates zero on each of the 330 face triangles and one on each of the 230 missing triangles. Thus the homology conclusion is not inferred only from a rank log.

For symmetry, the script recovers each numeric vertex as an unordered 3-plus-3 bisection of the six letters. It then enumerates all 720 letter permutations, checks that each induced permutation preserves every facet, and exhausts their orbits on the missing triangles. The orbit sizes are 20, 60, 90, and 60, with the four representatives stated in the finding.

The verifier is deterministic, uses only the Python standard library, and makes no claim beyond this finite complex.
