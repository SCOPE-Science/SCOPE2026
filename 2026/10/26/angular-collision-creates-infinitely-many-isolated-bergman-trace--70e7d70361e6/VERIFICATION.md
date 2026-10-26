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

# Verification of analytic claim
The derivation requires no unproved spectral regularity or experimental extrapolation. The direct kernel calculation uses the probability-normalized \(A^2_\alpha\) Bergman kernel. The coordinate change \(x=\tanh u\) turns the one-chord \(RR^*\) kernel into \(\operatorname{sech}^{\alpha+2}(u-v)\); the Fourier symbol is a beta integral. Its positive continuous range is the spectral band \([0,C_\alpha]\).

For distinct rays, the entire cross kernel is square integrable because \(|1-xy e^{-i\theta}|\) has positive minimum on the real square. Consequently their positive Gram operators multiply compactly. The exactly checked inequality \(2I_{2\lambda}>I_\lambda\) comes from \(\cosh(2u)>\cosh^2u\), not numerical observation. The strong operator limit and the finite-dimensional min–max argument complete the eigenvalue count statement for every fixed threshold.

The supplied `checker.py` was executed successfully for six representative parameters, checking exact beta/gamma coefficient agreement with numerical integrals and positivity of the Rayleigh gap. It cannot independently establish the essential spectrum or eigenvalue-count divergence. No independent audit has been performed.
