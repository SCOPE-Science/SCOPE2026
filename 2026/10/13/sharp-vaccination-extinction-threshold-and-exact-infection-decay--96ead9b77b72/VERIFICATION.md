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

# Mathematical and computational verification

The analytical proof covers every finite nonnegative initial state and the complete parameter family given in `RESULT.md`; computations here test exact identities and illustrative trajectories only.

Run `python3 verify.py` with Python 3 and standard library, from the same extracted directory as `verify.py`. The program independently constructs exact fractions for \(S_0\), \(V_0\), \(\mathcal R_c\), and \(\mathcal J_c\), checks the determinant and full characteristic polynomial of the infected block for the two rational witnesses, verifies the critical positive left null vector, and runs two distinct nonnegative initial states for each of two transmission strengths with fourth-order Runge–Kutta time stepping. Output on the tested interpreter:

`VERIFY_OK: exact rational matrices, critical kernel, and non-proof trajectories`

Expected exact subcritical identities: \((S_0,V_0)=(4/31,18/31)\), \((\mathcal R_c,\mathcal J_c)=(15/31,3/2)\), characteristic polynomial \(\lambda^3+5\lambda^2+(218/31)\lambda+64/31\).

Expected critical identities: \((\mathcal R_c,\mathcal J_c)=(1,31/10)\), \(B_0=[[-2,2,2],[1,-2,0],[0,1,-1]]\), and characteristic polynomial \(\lambda(\lambda+2)(\lambda+3)\), with left zero eigenvector \((1,2,2)\).

The numerical runs are not exhaustive, prove neither positivity for arbitrary time steps nor the global result, and cannot establish any asymptotic logarithmic exponent. The proof's critical steps are the Metzler comparison envelope, integral saturation-dissipation inequality, uniform-continuity limit, and positive spectral sandwich, all written in `RESULT.md`.
