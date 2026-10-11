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

The accepted formula was checked symbolically from the definition. After the rank-one normal form, the rotated real part is Hermitian and has exactly two possibly nonzero eigenvalues
\[
\frac{\|T\|}{2}\left(r\cos\theta\pm\sqrt{1-r^2\sin^2\theta}\right).
\]
Their maximum absolute value gives the integrand used in the proof. Squaring separates a zero-mean \(\cos(2\theta)\) term from one positive cross term, and quarter-period symmetry reduces the latter to
\[
\int_0^1\sqrt{1-r^2u^2}\,du.
\]
The elementary antiderivative yields the claimed \(r\sqrt{1-r^2}+\arcsin r\) expression.

Boundary checks are exact. At \(r=0\), the formula gives \(\omega_2(T)=\|T\|/2\), equal to the classical numerical radius of a rank-one nilpotent. At \(r=1\), it gives \(\omega_2(T)=\|T\|/\sqrt2\), equal to \(\omega(T)/\sqrt2\) for a scalar multiple of a rank-one projection. These match the two sharp constants in the focal source.

The proof does not establish any analogous formula for rank greater than one. No computational certificate is required, and no unproved infinite extrapolation is used.
