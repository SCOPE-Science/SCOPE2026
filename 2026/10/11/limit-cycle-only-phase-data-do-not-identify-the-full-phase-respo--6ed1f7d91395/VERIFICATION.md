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

The accepted claim is the exact non-identifiability statement in `RESULT.md`.

## Direct algebraic checks
Starting from the polynomial Cartesian vector field and writing \(x=r\cos\theta\), \(y=r\sin\theta\), the radial and angular equations are
\[
\dot r=\lambda r(1-r^2),\qquad
\dot\theta=\omega+c(1-r^2).
\]
At \(r=1\), the motion and the vector field are independent of \(c\), while the radial linearization is \(-2\lambda<0\).

For
\[
\Phi_c(r,\theta)=\theta-\frac{c}{\lambda}\log r,
\]
one has, identically for \(r>0\),
\[
\frac{d}{dt}\Phi_c
=\omega+c(1-r^2)-\frac{c}{\lambda}\lambda(1-r^2)
=\omega.
\]
Thus it is an asymptotic phase function on the basin of the attracting cycle. Its on-cycle gradient is
\[
Z_c(\theta)=(-\sin\theta,\cos\theta)-\frac{c}{\lambda}(\cos\theta,\sin\theta).
\]
The radial coefficient \(-c/\lambda\) is arbitrary although the full on-cycle dataset is unchanged.

## Source checks
The focal preprint was inspected at its phase definition, PRC definition, on-cycle differential loss, statement that the main first step needs no off-cycle samples, acknowledgement that transversal gradients are not explicitly constrained, Neural-ODE extension, comparison with adjoint methods, and adjoint-regularized extension. The predecessor phase-autoencoder paper was inspected at its phase/PSF definitions, training-data construction, and Stuart-Landau experiment. Its data construction deliberately perturbs initial states off the cycle and reports that removing this displacement impairs PSF recovery.

## Limits
No claim is made about the numerical error of the focal trained models. The theorem only establishes non-uniqueness from information supported exactly on one periodic orbit. It is removed when genuinely transverse information or a restrictive justified model class is supplied.
