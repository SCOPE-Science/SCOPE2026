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
The universal statements are proved symbolically in `RESULT.md`. The standalone checker replays exact finite cases.

With
\[
X_0=I+MJ_n,
\]
write
\[
Z_k=X_k-I.
\]
The exact recurrence is
\[
Z_{k+1}
=
\frac12Z_k^2(I+Z_k)^{-1}.
\]
The lowest nonzero power of \(N=MJ_n\) in \(Z_k\) is
\[
N^{2^k}
\]
with coefficient
\[
2^{\,1-2^k}.
\]
Therefore
\[
Z_k=0
\iff
2^k\ge n.
\]

For \(n=3\),
\[
Z_1=\frac{M^2}{2}E_{13},
\qquad
Z_2=0.
\]
At \(M=10\), the spectral-error ratio is \(5\), while the squared Frobenius-error ratio is
\[
\frac{25}{2}.
\]

The checker evaluates exact nilpotent inverses and Newton updates for several dimensions and verifies the predicted first nonzero power and termination index.

Finite replay is corroborative only. No finite enumeration is used to prove the all-\(n\) law.

Unproved limits include scaled Newton variants, global fixed-condition-number extremals, and floating-point transient behavior.
