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

# Reproducibility and verification
The proof in RESULT.md is analytic. Finite independent checks in `verify.py` confirm Wigner normalization by direct Hermite-Gaussian quadrature for five fixed examples (largest absolute error about \(3.77\times10^{-37}\)), the leading Laguerre and first-order correction exactly in degrees 1–30, and connected components and planar area at small amplitude for degrees 1–5. Numerical discrete counts are illustrative, not an exhaustive proof. Running `python verify.py` with the versions specified in `requirements.txt` recreates the log in `checker_output.txt`.

The limit theorem fixes the Hermite order before taking the amplitude to zero. The full text of a potentially relevant 2025 nodal-set paper was not inspected, leaving a publication-priority risk, while known n=2 special-case results are explicitly credited. No independent mathematical audit is claimed.
