---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read frozen RESULT.md blob ff5bcdb... and reconstructed λ_n=(1/n!)∫_s^t e^(−u)u^n du; adjacent difference [e^(−s)s^(n+1)−e^(−t)t^(n+1)]/(n+1)! has sign L−(n+1), giving one or two top degrees. Area under perturbing squared outer radius t+εh is unchanged since ∫h=0. Coherent-state integral is trace-norm C² near fixed t; first-variation matrix element e^(−t)t^((j+k)/2) hhat_(k−j)/sqrt(j!k!). Compressing to tied degree m−1,m yields offdiagonal γ_m hhat_1, eigenvalues ±γ_m|hhat_1|; largest branch switches with sign ε, yielding cusp. Independent calculation verified four resonances, top ties, and directly integrated a finite Toeplitz perturbation with matching two-sided slope ~0.001950454499.

## originality

PASS

Classical Daubechies and Svela radial/Reinhardt localization diagonalization supplies λ_n. General isolated selfadjoint eigenvalue perturbation supplies the principle of splitting, but complete explicit integer log-mean resonance curves and fixed-area nonradial angular cusp coefficient require combining and computing the compressed boundary operator. A historical explicit shape calculus could imply this as corollary; risk retained.

## value

PASS

Exact resonance threshold and first angular Fourier mode control the nonanalytic first-order shape response of optimal Gaussian concentration. Supplies natural sharp shape derivative and local spectral sensitivity, distinct from radial eigenvalue diagonalization alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
