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

The proof is analytic. Its critical checks are:

1. Wick's formula gives \(\mathbb E[X_1^2X_2^2X_3^2]=1+2S+8P\), with \(P=\rho_{12}\rho_{13}\rho_{23}\).
2. Positive semidefiniteness gives \(1+2P-S=\det R\ge0\).
3. Arithmetic-geometric mean gives \(|P|\le(S/3)^{3/2}\).
4. The two lower bounds for \(P\) cross only at \(S=3/4\).
5. The family \((\rho_{12},\rho_{13},\rho_{23})=(t,t,-t)\), \(0\le t\le1/2\), attains the first branch.
6. The family \((\rho_{12},\rho_{13},\rho_{23})=(t,t,2t^2-1)\), \(1/2\le t\le1\), is singular and continuously attains every \(S\in[3/4,3]\).
7. The ratio of the exact envelope to \(S\) has minimum \(2/3\) at \(S=3/4\).

The bundled `verify.py` checks the explicit families exactly where rational arithmetic applies and stress-tests the inequalities over a rational grid. Its expected terminal output is `VERIFY_OK`.

Limits: finite grid checks are supplemental only. They do not establish the all-parameter theorem or the literature comparison.
