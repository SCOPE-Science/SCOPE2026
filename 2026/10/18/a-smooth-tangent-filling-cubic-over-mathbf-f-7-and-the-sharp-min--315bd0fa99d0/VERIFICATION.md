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
# Reproducibility and limits

Run `python3 verify_tangent.py` with Python 3 and no nonstandard dependencies. The program was executed successfully from a standalone copy and printed `VERIFY_OK`, following these checks: the explicit polynomial Bézout identity in characteristic \(7\); the list of \(57\) canonical projective points; the complete list of \(12\) cubic points and gradient tangents; pairwise distinction of tangents; the exact incidence histogram \(m=1:36,\ m=2:9,\ m=3:9,\ m=5:3\); the three noncollinear fivefold centers and their pencil intersections. No random sampling is involved.

The all-algebraic-closure smoothness proof uses the polynomial identity and the \(X=0\) case as explained in `RESULT.md`; the conic exclusion uses geometric polarity. The verifier does not purport to classify every plane cubic, and no independent audit has been performed.
