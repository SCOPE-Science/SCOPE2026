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

The supplied `verify.py` checks the algebraic identity
\[
F(a^2/t)+(a/t)F(t)=(a+t)(a^2-bc)/(at),
\quad F(t)=(t+b)(t+c)/(t-a),
\]
and the polynomial form obtained by clearing denominators. It checks sample involution calculations for degrees \(m=6,7,8,11\), with \((a,b,c)=(2,1,4)\).

The universal claims are justified by the explicit projective-line puncture model, the standard classification of finite subgroups of \(\operatorname{PGL}_2(\mathbb C)\), and a complete scaling/inversion case split. Finite examples do not prove those statements by themselves. The paper establishing the original smooth curve family is arXiv:2610.15607v1, Theorem 3.1; the added automorphism theorem does not assert independent validation or independent historical priority.
