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

# Verification and limitations

The provided `verify.py` is a dependency-free exact arithmetic checker. Running `python3 verify.py` verifies the normalized positive interaction, exact Fourier coefficient, matrix entries, characteristic polynomials, discriminant, both Routh–Hurwitz margins, and the uniform high-frequency bound. Successful execution was observed. The two-phenotype determinant identity and spectral conclusions require the written proof, not finite tests.

The heat kernel \(\widehat K(n)=2^{-n^2}\) is smooth, positive, even and has mass one. The result is local linear spectral stability/instability around the constant state. It does not establish nonlinear persistent oscillations, global dynamics, or historical priority. The cited 2020 cross-diffusion study was not examined in full text; its published bibliographic description refers to a different model.
