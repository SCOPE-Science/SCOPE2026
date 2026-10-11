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

For
\[
F(\theta)=
(\cos\theta+a\sin\theta)^{-2}
+
(\cos\theta-b\sin\theta)^{-2},
\]
direct differentiation gives
\[
F'(0)=2(b-a).
\]
Hence \(a\ne b\) forces a strict local decrease in one angular direction.

When \(a=b=q\), writing \(u=\tan^2\theta\) gives
\[
F(u)=\frac{2(1+u)(1+q^2u)}{(1-q^2u)^2},
\]
and
\[
F'(u)=
-\frac{
2(q^4u+3q^2u+3q^2+1)
}{
(q^2u-1)^3
}.
\]
The numerator is strictly positive for \(u\ge0\), so the only candidates for the global minimum are the original basis value \(2\) and the quarter-turn value \(2/q^2\). Thus
\[
R(q,q)^2=\frac{2}{\max\{1,q^2\}}.
\]

The accompanying checker verifies these symbolic identities and stress-tests representative parameters numerically. Numerical sampling is supplemental and is not used to establish the infinite family.

The proof does not establish an exact formula for nonsymmetric matrices, global optimality of the avoidance radius, or any higher-dimensional equality classification.
