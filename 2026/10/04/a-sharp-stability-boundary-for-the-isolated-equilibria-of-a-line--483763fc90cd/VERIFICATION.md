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

The bundled `verification/verify.py` reconstructs the showcased characteristic polynomial in exact arithmetic over \(\mathbb Q(\sqrt{10})\). It checks that the radical part cancels and that
\[
p(\lambda)=\lambda^3+7\lambda^2+\frac{2312}{25}\lambda+\frac{4624}{5}.
\]
It also checks the exact Routh determinant
\[
7\frac{2312}{25}-\frac{4624}{5}=-\frac{6936}{25}<0,
\]
and approximates all three roots independently with a dependency-free Durand--Kerner iteration, verifying small residuals and exactly two positive real parts. The recorded checker output is `VERIFY_OK`.

The symbolic parameter classification itself is proved algebraically in `RESULT.md`; the finite numerical root calculation is not used as a proof for the full parameter range. No global-attractor, fractional-order, or nonlinear boundary-bifurcation assertion is verified here.
