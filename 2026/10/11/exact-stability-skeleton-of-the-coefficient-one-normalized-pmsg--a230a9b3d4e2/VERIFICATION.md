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
The proof uses exact algebra. For \(0<b<1\), direct differentiation of the stated quadratic function gives a negative-definite derivative; at \(b=1\), the only invariant subset of the zero-derivative set is the origin. This establishes the global claim without simulation.

For the nonzero branch, substitution of \(z=xy\) yields the stated one-parameter equilibrium representation. The cubic characteristic polynomial is then checked by direct determinant expansion. Its Routh-Hurwitz determinant at \(a=109/20\) reduces exactly to the stated rational function whose numerator is the negative of
\[
552000s^3+6016800s^2+394580s-228364701.
\]
The derivative of this cubic is strictly positive on \(s\ge0\), so the positive root is unique. The packaged `verify.py` reconstructs the specialized polynomial with exact rational arithmetic, isolates that root by bisection, and reproduces the stated values of \(s_H\), \(b_H\), and the imaginary frequency.

No finite integration, sampled Lyapunov spectrum, or numerical root finder is used to justify the infinite-time stability statements. The decimal values are presentations of algebraically defined quantities only. No claim is made about attraction basins of the nonzero equilibria or nonlinear Hopf criticality.
