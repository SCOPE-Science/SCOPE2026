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

The proof was checked from the displayed definitions and identities. In particular:

- Expanding the rank-two Gram determinant after \(a=-1/2+x\), \(b=-1/2+y\), \(c=-1/2+z\) gives exactly \(3s=\Delta^2+s^2-4xyz\).
- In a sufficiently small equilateral neighborhood, the all-positive squared sum is near zero and the other three are near four, so their maximum is exactly \(4+4m-2s\).
- For three zero-sum real coordinates, \(\max q_i\ge\|q\|_2/\sqrt6\); the equality pattern is proportional to \((1,1,-2)\) up to permutation.
- These facts give \(s=\Delta^2/3+O(\Delta^3)\) and the uniform lower expansion analytically.
- `verify.py` symbolically checks the determinant reduction, signed-sum formulas, and the sharp symmetric-family series. A successful replay prints `VERIFY_OK`.

The checker does not certify literature novelty and does not replace the local analytic estimates by numerical sampling. The neighborhood size and cubic remainder constant are not optimized.
