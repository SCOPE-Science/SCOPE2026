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

The proof uses exact differentiation and algebra. In the published SODE phase variables \(x,v,z,w\), the defect \(Q=w+cz-hx^2\) has Lie derivative \(cQ\). Therefore \(Q=0\) is invariant and every off-constraint defect equals \(Q(0)e^{ct}\).

The reconstruction \(y=x+v/a\) recovers \(\dot x=a(y-x)\) and \(\dot y=bx-kxz\); imposing \(Q=0\) recovers \(\dot z=-cz+hx^2\). The explicit family \(x=v=0\), \(z=Ae^{ct}+Be^{-ct}\) verifies that the full SODE has extra solutions whenever \(A\ne0\).

At the origin, the physical Liu characteristic polynomial is \( (\lambda+c)(\lambda^2+a\lambda-ab)\). The extended SODE characteristic polynomial is \((\lambda^2-c^2)(\lambda^2+a\lambda-ab)\), so the extension adds exactly the eigenvalue \(+c\) while retaining \(-c\).

The packaged `verify.py` checks these algebraic identities symbolically with a small dependency-free polynomial engine and returned `VERIFY_OK`. No finite numerical experiment is used as evidence for the general statement.
