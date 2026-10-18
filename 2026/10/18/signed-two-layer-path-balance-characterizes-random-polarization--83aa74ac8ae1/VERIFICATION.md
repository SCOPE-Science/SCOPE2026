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
# Reproducibility

Run `python3 verify.py` using only Python 3 standard library. The program checks the exact finite identity relating gauge balance and singularity for 1,367 seeded irreducible matrix pairs of sizes 2–4, plus an exact four-state primitive-product example with martingale first-step variance \(1/16\).

Mathematical verification beyond finite checks: the proof establishes (i) spectral necessity and sufficiency of signed-path balance for eigenvalue one, (ii) Lyapunov-supermartingale convergence in the stable regime, (iii) bounded martingale convergence and transverse stability in the balanced regime, and (iv) strict conditional variance of the first increment. Finite tests neither establish novelty nor replace the almost-sure proof. Independent audit has not been performed.
