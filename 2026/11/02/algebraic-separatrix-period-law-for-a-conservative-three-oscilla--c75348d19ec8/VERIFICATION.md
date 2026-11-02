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

The standalone file `VERIFY.py` requires Python and `mpmath`, and is run as `python VERIFY.py`. It was executed on the supplied bytes and returned a PASS after checking beta-function identities, two-root turning-point quadrature, five energy values and the linear center frequency. The computation is supporting evidence, not a proof that the limiting coefficient exists. The proof is given in `RESULT.md`, including analytical turning-point asymptotics, a dominated-convergence argument, and the beta-function evaluation.

The exact source model and prior Hamiltonian formula are in Yan, Ozawa, Kori and Sato, arXiv:2603.02135. The three-oscillator integrability background is in Ashwin, Bick and Burylko (2016), DOI 10.3389/fams.2016.00007. The new result concerns the energy-resolved **physical time** of reduced loops. Absolute full-phase periodicity is neither assumed nor proved.

Scientific limitations: this fixed three-site unit-coupling quadrature system only; no claims of larger-network persistence, perturbation stability or global dissipative transients. Originality remains provisional with respect to unindexed historical work. Independent review has not been carried out.
