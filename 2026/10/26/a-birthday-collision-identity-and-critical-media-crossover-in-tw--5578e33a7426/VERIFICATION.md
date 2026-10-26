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

# Verification record

Run `python verify.py` with Python's standard library. The program checks the exact transition law by enumerating all ordered distinct-voter triples for populations from 3 through 9, derives an independent exact rational linear-system solution to each finite absorption problem, and tests all interior states for media probabilities 1/4, 1/2, 2/3 and 3/4. It also verifies the birthday-tail weights and tests numerical convergence in the moving critical window for population sizes 1000 through 64000, three media offsets and three scaled seed counts.

Observed result: `PASS 336 independent finite-chain and critical-window checks`.

These finite calculations test specific parameters; they cannot prove asymptotics. The infinite-population claims rely on the logarithmic product estimate and Gaussian dominating bound in the written proof. Sampling is without replacement. No external scientific validation or independent audit has been performed.
