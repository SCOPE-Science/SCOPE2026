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

# Reproduction and limits

Run `python3 verify.py` with standard Python 3. The program validates its eight finite-field bases by exhaustive monic-factor testing, then enumerates the exact fibres of the Artin–Schreier map in each field of size \(3^n\) for \(1\le n\le8\). A separate image-histogram count for \(y\mapsto y^3-y\) agrees with the absolute-trace count. All ramification points above finite poles and all points above infinity are included. It verifies \(N_1,N_2,N_3,N_4=(6,12,42,132)\), the genus-four Weil coefficient symmetry, and the complete numerator square.

The same program checks the exhibited polynomial Bézout relation proving that \(u^5+u^4+u^2+1\) is squarefree, enumerates \(5\) and \(11\) points over the first two extension fields of the genus-two curve, and reconstructs its quartic L-polynomial. It checks the resulting \(225\)-point Jacobian order.

The genus calculations use standard ramification formulas. The isogeny inference uses Tate's finite-field theorem, not a constructive map; the isogeny degree, kernel, and polarization compatibility remain unspecified. The finite computations are exhaustive for the specified finite fields, while global equality of the zeta polynomials uses the mathematical Weil functional equation, not empirical extrapolation. No independent audit has been conducted.
