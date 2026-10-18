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

# Verification record

The literal diagonal automorphism equation for the row-by-source structure matrix is \(M_{ij}(d_j-d_i^2)=0\). The exact mean follows from color-preserving block permutation matrices. The asymptotic also requires the separately proved minimal-cycle event characterization and a uniform bound on all longer-support scalings; an exhaustive finite experiment is not an infinite proof.

Run `python verify.py` without dependencies. The script enumerates all invertible matrices and all diagonal tuples directly in six instances: \((q,n)=(2,3),(3,3),(4,2),(4,3),(5,2),(7,2)\). It independently implements the exact moment's finite squaring-orbit sum and compares it with the direct distribution. It also checks an explicit three-cycle and all its diagonal scalings over \(\mathbb F_8\). The actual replay succeeded and reported `VERIFY_OK`.

Selected exact empirical distributions were: \(q=4,n=2\): stabilizer orders \(1:171,3:9\); \(q=4,n=3\): \(1:181359,3:81\); \(q=7,n=2\): \(1:1980,3:36\). Fields with \(q-1\) a power of two showed only trivial diagonal stabilizers. Finite enumeration checks definitions and small cases, not the proof of the all-dimension formulas or fixed-field limit.

No human or independent audit has been performed. No group-scheme or full automorphism-group calculation is claimed.
