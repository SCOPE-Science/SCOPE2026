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
The geometric input is the established rational-normal-scroll formula
\[
D_k=kd-nk(k-1),
\qquad
1\le k\le d_1.
\]

For
\[
g=\gcd(d,2n),
\]
the parity of \(k(k-1)\) gives
\[
g\mid D_k
\]
for every order in the tower. Sharpness follows from
\[
D_1=d,
\qquad
D_2=2d-2n,
\]
so
\[
\gcd(D_1,D_2)=\gcd(d,2n).
\]

The embedded checker verifies the formula
\[
\gcd(D_1,\ldots,D_{d_1})=\gcd(d,2n)
\]
over a large exact integer grid and confirms the prime-wise consequences and representative examples.

The computation is regression evidence only. The proof is symbolic and uniform.
