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

The analytic proof uses only identities from the printed six-variable ODE system.

Checks performed:

1. The factorization \(A'=A(\omega V/(h_2+A)-d_A)\) makes \(A=0\) invariant.
2. On \(A=0\), the equilibrium equations reduce to \(V=kI/d_V\), \(I=I(E)\), the displayed expression for \(S\), and one scalar equation \(F_\beta(E)=\lambda\).
3. \(I'(E)=(d_E+s h_1/E^2)/c>0\); the factors in \(F_\beta(E)\) are positive and strictly increasing in \(E\).
4. The endpoint value is \(F_\beta(s/d_E)=\lambda\beta_c/\beta\), which yields the exact branch condition \(\beta>\beta_c\).
5. The antibody transverse derivative at \(A=0\) is \(r_A=\omega V/h_2-d_A\).
6. Substituting the unique viral load \(V=d_Ah_2/\omega\) into the same equilibrium identity gives the stated finite \(\beta_A\) exactly when \(\lambda>D_AI_A\).
7. The included `verification/verify.py` reconstructs a positive-parameter instance, solves the scalar branch independently, evaluates all six equilibrium residuals, and verifies the predicted antibody-eigenvalue sign on both sides of \(\beta_A\).

Unproved limits: no full local-stability classification of the antibody-free branch, no transcritical-bifurcation theorem at \(\beta_A\), and no global classification of the positive-antibody dynamics are asserted.
