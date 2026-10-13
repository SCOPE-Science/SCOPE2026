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
The proof has two symbolic stages.

First,
\[
c(TY_d)=\frac{(1+H)^{d+2}}{1+3H}
\]
and
\[
\int_{Y_d}H^d=3
\]
give
\[
\chi(Y_d)=\frac{(-2)^{d+2}-1}{3}+d+2.
\]

Second, the cubic/Fano relation and the Euler characteristic of a symmetric square give
\[
\chi(F_d)=\frac{\chi(Y_d)(\chi(Y_d)-3)}2.
\]

For even \(d\),
\[
\nu_2(\chi(F_d))=\nu_2(3d-4)-1,
\]
and for odd \(d\),
\[
\nu_2(\chi(F_d))=\nu_2(3d+5)-1.
\]
The inequalities
\[
|3d-4|<2^{d+2}
\]
and
\[
3d+5<2^{d+2}
\]
ensure that the linear term and the power-of-two term cannot have equal valuation.

The bundled exact checker independently reconstructs the Chern-class coefficient through dimension two hundred and checks the valuation theorem through dimension five thousand. It also verifies the first several residue-class strata.

Finite computation is used only as regression evidence.
