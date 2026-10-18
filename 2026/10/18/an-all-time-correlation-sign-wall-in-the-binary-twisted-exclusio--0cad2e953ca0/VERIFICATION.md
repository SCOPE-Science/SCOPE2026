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

The exact theorem is proved in `RESULT.md` by a closed first-moment generator identity, a discrete antiperiodic heat semigroup, positivity of an irreducible Metzler subsystem and an explicit inverse-Laplacian Green function. All assumptions and boundary conventions are part of that proof.

Run `python verify.py` with NumPy and SciPy installed. It enumerates the **full** configuration-space generator independently, in each parity sector, for every integer \(3\le L\le8\). It computes time-\(0.73\) covariance matrices using full Markov matrix exponentials, checks the generator-to-spin intertwining, compares with the antiperiodic heat semigroup, computes zero-mode-excluded integrated covariance from a separate eigendecomposition, and tests all sign and integrated-response formulas. All twelve sector-size cases passed. The matrix-exponential comparison tolerance is \(2\times10^{-13}\); the inverse-response tolerance is \(10^{-10}\); these are numerical tolerances for finite checks.

This code does not certify every ring or all positive times by enumeration; the mathematical argument in `RESULT.md` covers those quantifiers. This is not a claim of independent external validation, nor of a spectral-gap theorem for the full Markov generator.
