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
The proof is symbolic and uses only the bracket
\[
[\alpha t+u,\beta t+v]=\alpha A(v)-\beta A(u).
\]

The packaged checker `artifacts/verify.py` constructs the Lie algebra from \(A\), enumerates every element, forms every adjoint matrix, and computes ranks by Gaussian elimination in the ground field.

It verifies the following cases:

- a rank-\(1\) nilpotent map over \(\mathbf F_2\);
- a rank-\(2\) semisimple map over \(\mathbf F_3\);
- a rank-\(2\) nilpotent map in dimension \(3\) over \(\mathbf F_3\);
- a rank-\(2\) nonsemisimple invertible map over \(\mathbf F_4\);
- rank-\(1\) and rank-\(3\) maps in dimension \(3\) over \(\mathbf F_5\).

For every case it checks the exact adjoint-rank histogram and independently enumerates all commuting ordered pairs. The observed probability agrees with
\[
d(L)=\frac{q^r+q^2-1}{q^{r+2}}.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.
