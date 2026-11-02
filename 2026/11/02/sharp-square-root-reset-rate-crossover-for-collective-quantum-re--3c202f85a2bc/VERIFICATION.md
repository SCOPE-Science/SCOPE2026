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

Run `python verification.py` with NumPy and SciPy available. For every listed parameter set, the script compares the exact integral, the modified-Bessel series, and an independent collective-Fock Poisson double sum. Additional tests check ordering under larger reset rates, purity's strict Jensen comparison with independently reset product states, the fixed-rate coefficient, and nontrivial \(\sqrt n\) crossover. The executed program reported **120 passed deterministic checks**.

The script truncates a convergent series and integral numerically and so cannot establish the infinite-dimensional statements. Proofs and bounds in `RESULT.md` establish those. There is no external audit or independently certified publication priority.
