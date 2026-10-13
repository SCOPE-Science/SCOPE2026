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

# Verification of the rhombic-chain capture theorem

The theorem concerns each \(N\ge2\), every upper cell index \(j\), all real magnetic phases \(\phi\), and strictly positive detector rate \(\gamma\). Its analytic justification is Steps 1–6 in `RESULT.md`: spectral dark/bright decomposition; Jacobi Gram matrix; one visible zero energy; generic-flux nonvanishing of a complex determinant overlap; zero-flux sine divisibility; and half-flux flat-band collapse. These are exact, not sampled.

Run `python verify.py` with the two dependencies listed in `requirements.txt`. The code generates each matrix from its declared four hopping amplitudes rather than importing a previous computation. It compares Gram–Schmidt Krylov ranks with an independently grouped Hermitian-eigenvector spectral support, for all \(2\le N\le8\), four indicated flux values, and every upper-rim site. It also checks several mixed-state long-time survival probabilities by exponentiating the lossy Hamiltonian. The expected successful output is `VERIFY_OK rank_cases=140 independent_spectral_rank=140 loss_dynamics=3`.

The spectral eigenspace threshold and long-time convergence checks use floating-point tolerances, so they provide finite corroboration only. No finite enumeration certifies the infinite or continuum cases. The theorem does not provide a flux-uniform finite-time convergence rate. The proof itself does not depend on the numerical tolerances.
