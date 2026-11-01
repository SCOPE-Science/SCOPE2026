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

The mathematical theorem and its proof are in `RESULT.md`. The single standalone `CHECK.py` requires only the Python 3 standard library. Run it with `python3 CHECK.py`; its executed run returned `PASS: 85 assertions; tested exact Fourier spectrum and fixed-rho asymptotics.`

The checker computes the eigenvalue formula in log-space by summing Poisson masses on residue classes, and independently compares small examples against the direct complex discrete Fourier transform of the Gram kernel. It also checks the balancing-point equation for supercritical ratios and compares finite values against the subcritical and supercritical leading asymptotics at several dimensions.

Finite checks neither establish a universal inequality nor prove the asymptotic remainder. The proof in `RESULT.md` supplies the infinite-dimensional quantifiers through Stirling asymptotics, rate-convexity localization, and uniform control of remote Poisson aliases. The original exact spectrum is independently known in the 2016 circular-state article; verification must not misattribute that identity as new.

The asymptotic error is allowed to depend on fixed \(\rho\), and there is no guarantee uniform in \(\rho\) as it approaches \(e^{-1}\). Full independent scientific examination has not been performed.
