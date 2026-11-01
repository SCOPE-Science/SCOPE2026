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

The standalone program `verify.py` uses Python's standard library and deterministic seeds. It verifies the direct linear-programming optimum by enumerating all cube vertices and hyperplane intersections with single edges in small dimensions; it does not simply compute the closed-form answer twice. It checks rational boundary witnesses and Euclidean maximizers and compares seeded Gaussian samples against the analytically proved law and normal critical-window profile.

A local execution passed 623 exact rational cases, 3,050 deterministic Euclidean checks, and 14,400 seeded Gaussian trials. The latter tests are statistical corroboration only. The proof in `RESULT.md` establishes all dimensions and limiting distributions without treating any finite experiment as exhaustive. No formal or independent mathematical validation is claimed.
