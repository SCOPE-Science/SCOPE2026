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

Put
\[
e=\varepsilon^2,
\qquad
a=\frac{\varepsilon^4}{1+\varepsilon^2},
\qquad
s=z^2.
\]
The source identities imply the certificate
\[
B(s)
=
\frac{1-s}{8}
-
\frac{\tau(1-3s)}{1+a\tau s}
-
\frac e2.
\]

The checker verifies symbolically
\[
B''(s)
=
-\frac{2a\tau^2(3+a\tau)}
{(1+a\tau s)^3},
\]
so the minimum on \(0\le s\le1\) is an endpoint. It verifies
\[
B(0)
=
\frac18-\tau-\frac e2,
\qquad
B(1)
=
\frac{2\tau}{1+a\tau}-\frac e2.
\]
The strict inequalities \(B(0)>0\) and \(B(1)>0\) are algebraically equivalent to
\[
\tau<
\frac{1-4\varepsilon^2}{8}
\]
and
\[
\tau>
\frac{\varepsilon^2(1+\varepsilon^2)}
{4(1+\varepsilon^2)-\varepsilon^6}.
\]

For the uniform curvature lower bound, the checker verifies the endpoint-crossing polynomial
\[
1+(a-24)\tau-8a\tau^2=0
\]
and the positive root
\[
\tau_*
=
\frac{2}{24-a+\sqrt{(24-a)^2+32a}}.
\]
It also verifies that the lower-endpoint branch of the bound has derivative numerator
\[
2+ae+a^2e\tau-4a\tau,
\]
which is strictly positive in the stated parameter range, while the upper-endpoint branch is strictly decreasing.

Finally, exact series expansion gives
\[
\tau_*
=
\frac1{24}
+
\frac{a}{864}
+
\frac{a^2}{62208}
+
O(a^3),
\]
and hence
\[
\tau_*(\varepsilon)
=
\frac1{24}
+
\frac{\varepsilon^4}{864}
+
O(\varepsilon^6).
\]

All infinite-parameter conclusions are proved symbolically. No finite sampling is used as a substitute for proof.
