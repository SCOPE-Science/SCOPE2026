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

# Reproducible computational checks and mathematical limits

Use Python 3 with the pinned-lower-bound dependencies in `requirements.txt`, and execute `python verify_cycle_jamming.py` from this directory. The program independently implements a finite labeled-state continuous-time Markov generator using sparse matrix exponentials for cycles of 4 through 10 vertices, and compares finite-time availability to the exact infinite-line benchmark where relevant. It also independently sorts first Poisson arrival clocks to simulate later jammed configurations on cycles with 256 and 1024 vertices.

Observed recorded output: for 256 vertices over 5,000 realizations, the empirical probability of being jammed at time \(\log n\) was 0.87100 and the mean available-pair count was 0.13700; for 1,024 vertices over 3,500 realizations these quantities were 0.87714 and 0.13286. The respective predictions are 0.87342 and 0.13534. The program returned `PASS: 71 deterministic and stochastic assertions`.

The numerical checks establish neither a proof for arbitrary cycles nor an exact asymptotic error constant. The theorem's proof instead uses the first-arrival graphical construction, exact half-line vacancy probability, decreasing-clock localization, the standard Stein–Chen dependency-neighborhood inequality, and mixed factorial-moment convergence. No independent audit or external validation has been performed.
