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

The claim is verified algebraically from the printed ODE.

`verify.py` performs the following exact checks using only the Python standard library:

1. builds \(\lambda I-J_s\) for \(J_s\) at an equilibrium;
2. expands the \(4\times4\) determinant exactly;
3. reduces \(s^2=b\) and matches the coefficients \(A_1,\ldots,A_4\);
4. expands \(\Delta_3=A_1A_2A_3-A_3^2-A_1^2A_4\) and matches the displayed strictly negative polynomial;
5. checks the exact Routh signs at \((a,b,c)=(1,1,2)\).

The remaining parameter-uniform step is analytic: \(\Delta_3<0\) excludes nonzero imaginary roots, \(A_4>0\) excludes zero, and the positive parameter octant is connected. Therefore the right-half-plane root count cannot change away from the sample point.

The result does not use finite-time integration as evidence for an infinite-time dynamical claim. It does not verify the source’s numerical attractors or Lyapunov-exponent maps.
