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

Run `python3 verify.py` in the same directory.

The checker uses exact rational arithmetic for the published parameter vector and performs the following checks:

1. Reconstructs the nonzero equilibrium \(E_*\) exactly and substitutes it into all four differential equations.
2. Builds the published Jacobian at \(E_*\).
3. Expands \(\det(\lambda I-J(E_*))\) directly by permutation arithmetic over rational polynomials.
4. Reduces the result to the primitive integer polynomial
\[
10440125\lambda^4+423869075\lambda^3+4674655710\lambda^2+12506994792\lambda+643445784.
\]
5. Checks coefficient positivity and the exact quartic Routh–Hurwitz determinants
\[
\Delta_2=1850867402738339250,
\]
\[
\Delta_3=23033184284619159659128251000.
\]
6. Computes approximate roots as a nonessential readability check and verifies their real parts are negative.

Successful replay ends with `VERIFY_OK`.

The exact Routh–Hurwitz inequalities, not the floating-point roots, are the proof of local asymptotic stability. No global basin size, global attractor classification, or cryptographic security theorem is verified by this package.
