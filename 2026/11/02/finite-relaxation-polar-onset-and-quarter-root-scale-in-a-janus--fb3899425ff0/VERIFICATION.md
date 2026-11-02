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

# Verification and boundaries

Execute `python checker.py` from the extracted files with Python, NumPy and SciPy installed. The program performs 220 deterministic numerical assertions and constructs its own one-dimensional finite-volume time-dependent solute generator. It checks the exact stationary threshold against direct scalar root finding, compares the equation characterizing the unique wavenumber against independent minimization, checks complex transfer signs and its long-wave asymptotic, and compares growing eigenvalues with finite-volume spectra on both sides of threshold.

The analytical proof in `RESULT.md` is needed for all positive parameters, uniqueness and nonoscillation. Finite-volume eigenvalues and floating-point calculations are not exhaustive proofs; no machine-formal or independent mathematical certification is claimed. The first-order surface dipole model is an approximation whose physical use requires sufficiently small displaced-source wavenumber. Full translationally driven Janus clustering, nonlinear saturation and arbitrary finite horizontal domains are not covered.
