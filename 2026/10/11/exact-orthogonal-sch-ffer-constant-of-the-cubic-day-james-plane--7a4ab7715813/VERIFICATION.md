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

For the cubic-arc parameter \(t\),
\[
\|x-y\|^3=1+F(t),
\]
with
\[
F(t)=
\frac{3t(1+t^3)^{2/3}}{(1+t^2)^2}
+
\frac{1-t^6}{(1+t^2)^3}.
\]
Exact differentiation factors as
\[
F'(t)=
-\frac{3H(t)}
{(t+1)^{1/3}(1+t^2)^4(t^2-t+1)^{1/3}},
\]
and the proof gives \(H(t)>0\) on \([1/2,1]\). The other smooth stratum is monotone directly, and axes have a strict \(4/3\) lower bound.

At the balanced pair,
\[
(\alpha+1/2)^3+(\alpha-1/2)^3
=
1+\frac{3}{2^{4/3}},
\qquad
\alpha=2^{-1/3}.
\]
The included `algebra_check.py` was executed successfully and verifies the cubic expansion and derivative factorization by exact symbolic simplification. No numerical optimizer is used as proof.
