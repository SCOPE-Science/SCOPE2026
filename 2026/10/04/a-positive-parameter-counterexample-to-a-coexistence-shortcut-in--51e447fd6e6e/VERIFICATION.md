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
The source formulas were evaluated with exact rational arithmetic in `verify.py`.

The checker verifies:

- all chosen biological parameters are positive;
- \(r>\beta_1\eta\), \(\gamma_1>\beta_2\), and \(\beta<C_1\);
- \(C_1=21/10\), \(C_2=-1\), \(L=-11/10\), \(L_0=0\), \(U=9/10\), and \(\Theta=11/10\);
- \(A_q=-1\), \(B_q=-1/5\), and \(C_q=-341/100\);
- \(f(L)=f(U)=-22/5\);
- \(A_q<0\), \(B_q<0\), and \(C_q<0\), which proves \(f(u)<0\) for every \(u>0\).

The last step is symbolic and universal on the positive half-line; no finite grid is used to establish absence of admissible roots. The verification does not assess nonhomogeneous equilibria or any later stability calculation.
