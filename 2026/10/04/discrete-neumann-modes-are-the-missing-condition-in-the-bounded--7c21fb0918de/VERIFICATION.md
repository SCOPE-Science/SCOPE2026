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

The accompanying `verifier.py` reconstructs all witness quantities using Python `fractions.Fraction`; no floating-point value is used to establish a sign.

Checks performed:

- exact coexistence identity \(h(x^*)=c\xi F(x^*)\);
- exact coefficients \(a_1,a_2,b_1,b_2\);
- \(R_1<0\) and \(R_2>0\);
- \(B>0\) and \(S=B^2-4d_1d_2R_2>0\), so the source condition \(R_5\) holds;
- the vertex \(B/(2d_1d_2)\) is below \(100\);
- \(D(100)>0\), hence every admissible nonzero mode on \(l=1/10\) has positive determinant because \(z_k=100k^2\ge100\) and \(D\) is increasing there;
- \(D(4)<0\) and \(D(9)<0\), hence modes \(k=2,3\) are unstable on \(l=1\).

The proof is limited to linear stability of the homogeneous equilibrium. No nonlinear branch or attractor is certified.
