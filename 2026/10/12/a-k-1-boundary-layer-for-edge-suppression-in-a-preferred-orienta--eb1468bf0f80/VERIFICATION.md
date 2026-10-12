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

The proof uses exact algebra. With \\(q=e^{ik\ell_2}\\) and \\(z=e^{i\theta}\\), the two solved amplitude ratios have denominator
\[
D=k^2z(q^2-1)+2kq(1-z^2)-q^2z+2qz^2+2q-3z.
\]
The triangle inequality gives \\(|D|\ge2k^2|\sin(k\ell_2)|-4k-8\\), which is the only estimate needed for the shrinking-window theorem. The boundary-layer limit is obtained by setting \\(q=s e^{i\delta}\\), \\(k\delta\to\xi\\), and taking the limit of the exact rational expressions.

`verify.py` independently evaluates the exact scattering equations and the solved ratios at deterministic finite points, then checks convergence to the limiting formula for both parities. A successful run prints `VERIFY_OK`. These computations are corroborative only and do not certify spectral existence on the excluded pole curve.

Unproved limits: the singular curve \\(s\xi=2\sin\theta\\), full-strip spectral realization of arbitrary boundary-layer parameters, the right-boundary analogue, and the brick-lattice analogue are not claimed.
