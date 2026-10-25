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

# Reproducible checks and scope

The theorem holds for all real relative angles, all integer side counts at least three, and arbitrary positive circumradii. Its analytic certificate is the mixed-area identity, a coprime residue bijection, the finite cosine progression, and the congruence of outward facet normals. These steps are written out in `RESULT.md` and do not depend on experiments.

Execute `python3 verify.py` from the directory containing this file to perform an independently coded pairwise-vertex-sum convex hull and shoelace check using the standard library only. The program enumerates 3,696 numerical checks: 3,179 area comparisons for side counts between 3 and 19, 512 exact phase side-count comparisons, and five finite-sample orientation moments. Expected success message begins `PASS: 3696`; the observed worst numerical absolute area error was less than \(2.14\times10^{-14}\).

The computation uses floating-point arithmetic and cannot prove exact equality for untested orders, all radii, or all angles. Analytic limit uses \(\sin x/x\to1\) and \((1-\cos x)/x^2\to1/2\). The uniform-angle law is a direct change of variables; the result does not assert a packing theorem or independence of scientific audit.
