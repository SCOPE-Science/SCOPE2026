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
The proof is symbolic and does not depend on finite enumeration.

For a nonzero matrix \(A\in M_n(\mathbf F_u)\), the linear functional
\[
C\longmapsto\operatorname{tr}(AC)
\]
is nonzero: if \(a_{ij}\ne0\), then
\[
\operatorname{tr}(AE_{ji})=a_{ij}.
\]
Hence its kernel has \(u^{n^2-1}\) elements.

For a product-field vertex \(X=(A,B)\), the two trace equations are independent across the two factors. This yields exactly the orthogonal-set sizes
\[
(qr)^{n^2-1},\qquad
q(qr)^{n^2-1},\qquad
r(qr)^{n^2-1}
\]
according to whether both components, only the second component, or only the first component are nonzero. Removing the zero matrix and, when appropriate, \(X\) itself gives the claimed degree pairs.

The packaged checker `artifacts/verify.py` directly enumerates \(2\times2\) matrices over
\[
\mathbf F_2,\ \mathbf F_3,\ \mathbf F_4,\ \mathbf F_5.
\]
It counts every trace-functional kernel, constructs every product-field degree from those exact counts, and verifies the claimed degree set and reconstruction map for
\[
(q,r)=(2,2),(2,3),(2,4),(3,4),(3,5).
\]
The \(\mathbf F_4\) implementation uses
\[
\mathbf F_2[t]/(t^2+t+1).
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the theorem.
