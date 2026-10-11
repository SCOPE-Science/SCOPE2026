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

Run `python verify.py` with a standard Python 3 interpreter. The script has no third-party dependencies. It performs exact commutative-polynomial expansion after multiplying the Lyapunov identity by \(k\), so no numerical tolerance or floating-point arithmetic is involved. The expected output is `VERIFY_OK`.

The checked identity is
\[
k\frac{d}{dt}(x^2+y^2)+s\frac{d}{dt}(u^2)
=-2k\left(ax^2-2hxy+by^2\right).
\]
The checker also verifies the algebraic identity \((a+b)^2-4ab=(a-b)^2\), used only to compare the source's equal-feedback Hopf inequality with the strict stability region.

The checker does not certify LaSalle's invariance principle, global existence, or the invariant-measure argument; those steps are proved explicitly in `RESULT.md`. The theorem does not cover \(h^2=ab\) or unequal feedback coefficients.
