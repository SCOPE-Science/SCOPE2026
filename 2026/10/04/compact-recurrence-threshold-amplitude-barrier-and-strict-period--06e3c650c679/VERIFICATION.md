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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic over rational coefficients.

It verifies the polynomial certificate
\[
6L H_1
=
6b(x+z)^2-6a(b+1)y^2,
\]
where
\[
6H_1=6(b+1)xy+2y^3-3ay^2-3(x+z)^2.
\]

It also verifies the denominator-free cubic certificate
\[
L K=6a\,y^2(a+by),
\]
with
\[
K=
6ab\,yz-6a\,xy-2a\,y^3
+3a(a+b^2)y^2
+3a(x+z)^2
+3b(b+1)x^2.
\]

Finally, it verifies the eliminated scalar equation
\[
y'''+b y''+a y'+a(b+1)y-2yy'=0.
\]

The stored checker output is `VERIFY_OK`.

The checker certifies the critical algebraic identities. The measure classification uses \(\int Lh\,d\mu=0\), support invariance at the critical parameter, and nonnegativity. The strict period argument additionally uses the classical equality case of Wirtinger's inequality.
