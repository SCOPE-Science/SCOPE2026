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

The algebraic replay is `verify.py`. It uses only the Python standard library and exact rational polynomial arithmetic.

Checks performed:

- reconstruction of \(\det(\lambda I-J_s(r))\) for both \(s=1\) and \(s=-1\);
- equality with \(\lambda^3+(1-r^2)\lambda^2+(1-r)\lambda+(1-2r)\);
- exact factorization \((1-r^2)(1-r)-(1-2r)=r(r^2-r+1)\);
- exact boundary factorizations at \(r=-1,0,1/2,1\).

Run `python3 verify.py`; the expected output is `VERIFY_OK`.

The interval root counts are proved by the cubic Routh criterion and sign analysis in `RESULT.md`, not inferred from finite experiments. The fractional-order extension uses the commensurate criterion stated in the cited source. No claim is made for incommensurate orders or for global attractor basins.
