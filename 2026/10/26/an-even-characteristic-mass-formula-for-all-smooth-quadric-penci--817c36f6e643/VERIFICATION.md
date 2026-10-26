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

# Verification of the exact counts

Execute `python3 verify_even_quadric_pencils.py` and compare standard output byte-for-byte with `expected_counts.txt`. Execute `python3 verify_base_geometry.py` and compare with `expected_geometry.txt`. These two tests were run on the embedded script bytes. Both programs use exact arithmetic and only the Python standard library. The first independently enumerates normalized Pfaffian anisotropic planes and directly evaluates the discriminant of all lifts for two small even fields. The second substitutes into the geometric Jacobian singularity conditions rather than reusing the discriminant test.

Both tests cover \(q=2\) and \(q=4\), not arbitrary powers of two. The general validity depends on the normal form and counting proof in `RESULT.md`, not on extrapolation from a finite sample. No independent external audit has been performed.
