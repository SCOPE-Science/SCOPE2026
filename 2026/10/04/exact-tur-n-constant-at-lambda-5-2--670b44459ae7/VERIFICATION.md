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

The proof is analytic and exact. The companion checker `verify_turan_5_2.py` uses only the Python standard library.

It verifies the polynomial identity
\[
32r_a(x)^2
=
(128a^6-20a^2+5)T_0(x)
-4a(64a^4-40a^2+5)T_1(x)
+4(5a^2-1)T_4(x)+4aT_5(x)+T_6(x),
\]
so the forbidden \(T_2\) and \(T_3\) coefficients vanish identically.

After clearing denominators in the dual quadratic, the checker performs exact polynomial division modulo the cubic and verifies the \(T_1\), \(T_4\), and \(T_5\) moments exactly. For \(T_6\), the residual is exactly a multiple of
\[
F(a)=256a^7+256a^6-96a^5-80a^4+40a^3+30a^2-15a-5,
\]
and therefore vanishes at \(a=a_\ast\).

Exact rational interval arithmetic verifies
\[
0.53305<a_\ast<0.53306
\]
with \(F'(a)>71\) throughout the bracket, as well as the three simple-root brackets
\[
-0.9163<x_1<-0.9161,\quad
-0.4146<x_2<-0.4143,\quad
0.7975<x_3<0.7978.
\]
On those brackets the signs of the cleared dual quadratic match the signs of the cubic derivative, so every dual weight is strictly positive.

The displayed decimal values are calculated only after all exact checks pass. They are not used to prove equality.

Checker output is stored in `verification_output.txt`.
