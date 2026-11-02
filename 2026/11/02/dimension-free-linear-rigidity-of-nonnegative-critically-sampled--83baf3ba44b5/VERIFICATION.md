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

# Verification instructions and scope

The algebraic derivation in `RESULT.md` establishes the universal theorem. Running `python CHECK.py` with the dependency in `requirements.txt` produces deterministic supplementary checks of finite matrices, Fourier spectra, exact transversals and small perturbations; observed result: `CHECK_OK 576`.

The numerical code samples only finitely many dimensions and does not prove the theorem for all parameters. The nonnegative hypothesis is used essentially to control the off-peak masses by the zeroth Fourier mode. The stated \(4/3\) estimate is a sufficient bound; optimization of the coefficient and independent review have not been performed.
