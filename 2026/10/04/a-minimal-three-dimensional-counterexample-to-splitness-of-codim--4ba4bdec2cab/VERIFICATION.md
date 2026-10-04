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

The exact proof uses the basis \(e,f,x\) with \(e^2=e\), \(f^2=f\), \(fx=xf=x\), and all other basis products zero. This immediately verifies the grading, \(A_0\cong k\times k\), the central-idempotent ideal \(J=ke\), and \(A/J\cong k[\varepsilon]/(\varepsilon^2)\). The map \(A_0\to A/J\) has kernel \(ke\), hence is not an isomorphism. Also \(J^2=J\), so \(J/J^2=0\).

Minimality is analytic. In total dimension at most \(2\), if \(\dim_k A_0=1\), any one-dimensional quotient receives the unit nontrivially from \(A_0\cong k\), forcing the map to be an isomorphism. If \(\dim_k A_0=2\), then \(A=A_0\) and the quotient-dimension equality forces \(J=0\). Thus no smaller counterexample exists.

`artifacts/verify.py` independently checks the algebra over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), including associativity, grading compatibility, the two-sided ideal property, quotient dimension, nonsplitness and idempotence of \(J\). `artifacts/verification_output.txt` records a successful replay ending in `CHECK_OK`. These finite checks do not prove the arbitrary-field or minimality statements; those are established by the exact argument above.
