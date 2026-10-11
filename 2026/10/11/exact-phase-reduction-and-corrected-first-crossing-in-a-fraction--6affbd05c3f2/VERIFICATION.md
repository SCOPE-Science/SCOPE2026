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

The calculation begins from the printed Example 4.1 rather than from the paper's numerical threshold. At \(E_*=(2/3,1/3)\), direct differentiation yields
\[
B(k)=\begin{pmatrix}k-2/3&-2/3\\2/3&-1/3\end{pmatrix},
\]
so the exact characteristic quasipolynomial is
\[
s^{2q}+(1-k)s^q e^{-s\tau}+\frac{2-k}{3}e^{-2s\tau}.
\]
The substitution \(z=s^q e^{s\tau}\) is therefore an identity, not a numerical approximation.

The standalone checker verifies the quadratic discriminant and roots, the common modulus, the exact formulas for \(\omega(k)\) and both first phase branches, the ordering that makes \(\tau_*(k)\) the first positive imaginary-axis crossing, and the derivative formula
\[
\operatorname{Re}\frac{ds}{d\tau}=\frac{q\omega^2}{q^2+\tau^2\omega^2}.
\]
At \(k=-1/2\) it directly evaluates the original quasipolynomial at \(s=i\omega_*\), \(\tau=\tau_*\) and checks a residual below \(10^{-12}\). It also checks that substituting the source's \(\tau=1.0229\) at the same frequency leaves a nonzero residual.

The checker evaluates the corrected first crossings for \(k=-0.2,-0.4,-0.6\), and \(-0.8\). These numerical evaluations are consequences of the exact phase formula, not empirical fits.

The verification establishes only the spectral statement in the finding. It does not establish nonlinear Hopf direction, periodic-orbit stability, global stability, or the accuracy of the source's time-stepping scheme.
