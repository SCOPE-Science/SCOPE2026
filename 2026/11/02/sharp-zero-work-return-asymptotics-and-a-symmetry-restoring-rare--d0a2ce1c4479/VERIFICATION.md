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

# Reproducibility and limits

The exact transition kernel is reconstructed from equations (6)–(7) of the cited quantum-engine model. All analytic identities are proved in `RESULT.md`, including the tilted characteristic polynomial, the zero-current saddle, both parity saddles, the explicit right/left eigenprojector, the weak-feedback expansion, and the strict entropy-rate minimization.

Run `python3 verify.py`. It performs independent finite-cycle probability propagation and 42 diagnostic assertions over several parameter pairs, including odd parity, the sharp prefactor at even cycle counts, the entropy minimum and the weak-feedback crossover. No external packages are required. These checks are finite and do not themselves certify the infinite limits. Independent scientific audit has not been performed.
