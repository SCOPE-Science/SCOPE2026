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

The variance polynomial in `RESULT.md` follows from independent primary-block disappearance indicators and a generalist extinction indicator equal to their product. Its derivative is controlled symbolically at the rational checkpoints \(a_i=s_i/(s_i+2)\) and \(b_i=5s_i/(5s_i+1)\), using an upper bound for the geometric-exponential tail and explicit bounds for the connected generalist's covariance contributions. The argument applies to every integer \(k\ge2\), without extrapolating from a finite computation.

The standalone Python 3 script `verify.py` was executed from its packaged directory. It first independently enumerates all block-extinction states at \(q=2/3\) and compares the exact variance with the polynomial; it then clears positive denominators before testing the sign of \(qV'(q)\) at all checkpoints for \(k=1,2,3\). Output:

```
VERIFY_OK [(1, 2, [(1, -1)]), (2, 8, [(1, -1), (1, -1)]), (3, 11, [(1, -1), (1, -1), (1, -1)])]
```

The finite checker does not certify all \(k\), locate each actual extremum, assert uniqueness within the indicated intervals, or imply empirical ecological applicability. Those finite-versus-infinite distinctions are preserved in the mathematical statement.
