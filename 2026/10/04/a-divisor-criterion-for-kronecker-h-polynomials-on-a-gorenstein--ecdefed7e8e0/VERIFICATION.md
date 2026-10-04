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
The proof has two logically separate parts.

First, the singularity and Gorenstein conditions are symbolic. The Reid--Tai ages in the two heavy charts reduce canonicality to \(b-a\le r\) and \(a\le r+b-a\), with terminality given by the strict inequalities. Intersecting the boundary with \(a\mid r+a+b\) and \(b\mid r+a+b\) gives the equal-weight point and \((c,c+r)\) for \(c\mid2r\).

Second, the exact floor formula for \(h^*\) is grouped into residue classes. For \(c\mid r\), it becomes a product of three geometric series. For \(c\mid2r\) but \(c\nmid r\), it contains the factor \(C_t=(1+z)(1+z+\cdots+z^t)+2z^m\) with odd \(t=2m-1\). On the unit circle, a root of \(C_t\) must have nonnegative real part, but the sum of all roots is \(-2\); hence not all roots can lie there.

`artifacts/verify_kronecker_boundary.py` uses only Python's standard library. It reconstructs every relevant \(h^*\)-coefficient from the floor formula for \(2\le r\le240\), checks both closed factorizations, the equal-weight case, and the divisor counts. Its success message is `VERIFY_OK`.

The computation is a regression check, not the proof of the infinite statement. No claim is made outside the stated weighted-projective family.
