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

Run `python3 verify.py` from the package directory. The expected output is `VERIFY_OK`.

The script checks the exact identities directly from the printed vector field: \(d(w-x/a)/dt=0\), the transformed affine coordinate has zero derivative, \(\varepsilon>0\) excludes equilibria, and the two published initial conditions have \(I=-2\) when \(a=0.05\).

The Lyapunov multiplicity argument is analytic rather than a finite numerical computation. In the transformed coordinates, the tangent bundle to \(K=\mathrm{const}\) is invariant and the quotient cocycle is the identity, giving one zero quotient exponent. The vector field is nonzero on compact invariant support and is mapped into itself by the derivative flow, giving a second zero exponent in the leaf. Therefore a negative total Lyapunov sum leaves room for at most one positive exponent.

The verification does not claim existence, uniqueness, or type of a chaotic invariant set for the reduced three-dimensional flow, and it does not infer asymptotic Lyapunov exponents from finite-time numerical data.
