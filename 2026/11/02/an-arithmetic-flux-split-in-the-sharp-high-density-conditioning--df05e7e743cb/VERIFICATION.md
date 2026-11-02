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

# Verification and reproducibility

The proof checks the normalization of the first Hermite function, the exact first dual-lattice shell in Janssen's operator series, the universal convergent estimate \(\|R_q\|\le100q e^{-\pi q}\), the spectral symmetry, and both sharp magnetic nearest-neighbor norms. It establishes positivity for every indicated \(q\ge3\) and obtains the two sharp condition-number limits by spectral perturbation.

Run `python3 CHECK.py` using Python 3 and its standard library. The recorded execution passed 20,430 finite assertions covering the finite-sum tail diagnostics, exact magnetic two-band formulas, and asymptotic normalizations. These are **supplementary** finite checks, not an exhaustive spectral proof, and are not evidence of independence or novelty.

The scope excludes non-square lattices, other Hermite orders, and arbitrary-flux asymptotics. The originality comparison used accessible first-Hermite, Hermite safety, Gaussian, and Gabor-bound papers, but unpublished or incompletely indexed equivalent results cannot be ruled out. Independent mathematical audit is not performed.
