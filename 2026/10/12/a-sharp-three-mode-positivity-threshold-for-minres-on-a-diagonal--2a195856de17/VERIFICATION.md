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

The analytic proof reduces the second MINRES iterate to a two-variable residual least-squares problem in the Krylov basis \(b,Ab\). The checker reconstructs this system symbolically for \(A=\operatorname{diag}(1,2,4)\) and \(b=(1,1,\varepsilon)^{\mathsf T}\), verifies the determinant and coefficient formulas, and simplifies all three coordinates to the expressions stated in RESULT.md.

For \(\varepsilon=1/10\), exact rational evaluation gives \(x^{(2)}=(22/25,109/200,-1/80)^{\mathsf T}\) and \(x^\star=(1,1/2,1/40)^{\mathsf T}\).

The checker also verifies the irreducible tridiagonal Stieltjes witness: positivity of all leading principal minors, negative off-diagonal connectivity, the exact residual-minimizing second iterate, a negative third coordinate, and a strictly positive exact solution.

The symbolic and rational replay corroborates the proof; it does not replace the universal dimension-minimality argument. Finite precision, preconditioning, nonzero initial guesses, and other spectra are outside the verified claim.
