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
# Reproducible checks and scope

Run `python3 verify_uv.py` with Python 3 and no additional packages. Expected exact output: `UV_CERTIFICATE_OK: 13 allowed Stanley--Reisner zero monomials`. This integer-polynomial certificate checks the normal-form identity giving \(uv=0\in H^4(B;\mathbb Z)\). It is based on the nine-ray fan and three linear divisor relations in Gong–Li, arXiv:2609.39707v1, §2.1.

The computer check is **not** a finite substitute for the general infinite-family assertion about complex-oriented theories. For that assertion, the written symbolic proof separately checks: (1) the torsion-free \(MU^*(B)\) consequence of the even-degree cellular Atiyah–Hirzebruch spectral sequence; (2) the rational Chern–Dold lift of the ordinary vanishing product; (3) the universal divisibility
\[
F(x,U)F(x,V)-xF(x,F(U,V))\in(UV)
\]
for every formal group law \(F\), by setting either input to zero; and (4) the rank-two projective-bundle theorem with bases \(\{1,x\}\). Tangent Chern classes follow from the relative complex tangent line's determinant; the \(K^0\) \(\lambda\)-ring check uses its two identical projective relations and their line-element generators.

Gong–Li's nonhomotopy Theorem 4.1 is used as published mathematical input, not reproved by this certificate. The theorem makes no claim about equivariant, unoriented, or real generalized cohomology, nor that the displayed ring isomorphisms are induced by continuous maps.
