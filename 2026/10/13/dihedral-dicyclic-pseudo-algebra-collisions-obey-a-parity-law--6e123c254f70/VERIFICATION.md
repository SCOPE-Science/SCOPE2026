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
The proof is symbolic.

The packaged checker `artifacts/verify.py` runs through
\[
2\le n\le80.
\]
For each \(k\in\{1,\ldots,n-1\}\), it computes the degree-two codegree
\[
\frac{2n}{\gcd(2n,k)}
\]
and checks that the multiplicity of each divisor \(d>2\) of \(2n\) is exactly
\[
\frac{\varphi(d)}2.
\]

It appends the parity-dependent linear-character contributions and verifies
\[
C(\operatorname{Dic}_n)=C(D_{4n})
\]
if and only if \(n\) is even.

It also verifies
\[
4+(n-1)4=4n
\]
for the irreducible degree squares and checks the involution counts \(1\) versus \(2n+1\).

The checker returns `VERIFY_OK`.

Finite arithmetic checks are not used to prove the theorem.
