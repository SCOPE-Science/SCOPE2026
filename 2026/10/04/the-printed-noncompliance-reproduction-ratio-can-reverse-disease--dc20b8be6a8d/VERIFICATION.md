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

The analytic check reconstructs the infected next-generation matrices directly from the current autonomous equations. The crucial structural point is that behavioral transfer occurs at \(q=\mu^*-\mu\), so the same \(q\) must appear in the infected transfer matrix \(V\).

The bundled `verify.py` uses only exact rational arithmetic. For the witness
\[
b=\delta=\gamma=1,\quad \xi=0,\quad \mu^*=4,\quad \mu=1,\quad \nu=1/2,
\quad \alpha=1/2,\quad \eta=0,\quad \beta=16/5,
\]
it checks the disease-free equilibrium \((s,s^*)=(1/2,1/2)\), reconstructs \(F\) and \(V\), confirms \(\mathcal R_{\rm print}=39/40\), confirms \(\rho(FV^{-1})=41/40\), and confirms \(\det(F-V)=-1/5\). Because the Jacobian determinant is negative, the two real eigenvalues have opposite signs, so local instability does not depend on a floating-point eigensolver.

The general formula is proved by symbolic matrix inversion in `RESULT.md`; the checker is an exact witness, not a substitute for that universal algebraic proof.
