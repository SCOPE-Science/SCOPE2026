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

Run `python3 verify.py`. A successful replay prints `VERIFY_OK`.

The verifier performs these checks:

1. It confirms from exact Table 1 fractions that \(\eta+d+\alpha_2=19/50=0.38\), distinct from the printed coefficient \(12/25=0.48\).
2. It reconstructs the unique positive equilibrium of printed (5.1) with exact rational arithmetic and checks all four equilibrium equations.
3. It evaluates the reported rounded point and verifies that its quarantine residual cannot be removed by rounding at the displayed precision, under either coefficient convention.
4. It reconstructs the exact polynomials \(P\) and \(Q\) from the rank-one delayed infection block and confirms that no quadratic power of \(e^{-\lambda\tau_1}\) is generated.
5. It checks the exact zero-delay Hurwitz determinants.
6. It derives the exact quartic \(F(\omega^2)=|P(i\omega)|^2-|Q(i\omega)|^2\), verifies \(F'(u)>0\) for \(u>0\), and verifies exactly that the reported \(\omega=0.0786\) does not solve it.
7. It brackets the unique positive root of \(F\), reconstructs \(\omega_*\) and the smallest positive phase delay \(\tau_{1,*}\), checks the characteristic residual numerically, and verifies positive transversality.

The finite-precision part only locates the unique root whose existence and uniqueness were already proved by the exact coefficient signs. It does not certify a nonlinear Hopf coefficient or simulate trajectories.
