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

For the trapezoid
\[
K=\operatorname{conv}\{(-1,-1),(1,-1),(1/2,1),(-1/2,1)\},
\]
the area is \(3\). Reflection uniqueness gives
\[
x_p=(0,t_p).
\]

Using the defining probability measure and support ratio,
\[
6\mu_p(K,(0,t))^p
=
2(1+t)^{1-p}(1-t)^p
+
(1-t)^{1-p}(1+t)^p
+
(3-t)^{1-p}(5+t)^p.
\]

For positive affine \(a,b\),
\[
\frac{d^2}{dt^2}\left(a^{1-p}b^p\right)
=
p(p-1)a^{1-p}b^p
\left(\frac{a'}a-\frac{b'}b\right)^2.
\]
Hence the objective is strictly convex on \((-1,1)\).

At \(p=2\), the derivative has the sign of
\[
q_2(t)=15t^4+12t^3-78t^2+60t+7,
\]
and exact rational evaluation gives
\[
q_2(-103/1000)<0<q_2(-102/1000).
\]

At \(p=3\), the derivative has the opposite sign of
\[
q_3(t)=45t^7+169t^6-507t^5+681t^4-1153t^3+1155t^2-561t-85,
\]
and exact rational evaluation gives
\[
q_3(-119/1000)>0>q_3(-118/1000).
\]

The embedded `verify.py` was replayed from its actual package path. It performs the bracket tests with exact rational arithmetic, checks that the intervals are disjoint, numerically confirms local minimization of the original objective, and re-evaluates the strict-convexity identity.

The replay output was:

`VERIFY_OK p-critical trapezoid counterexample`

The numerical bisections are not the proof of separation. Exact rational signs and strict convexity certify the two disjoint minimizer intervals.
