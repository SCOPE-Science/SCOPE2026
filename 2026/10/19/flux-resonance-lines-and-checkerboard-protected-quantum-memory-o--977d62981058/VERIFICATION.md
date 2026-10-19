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

# Reproduction and limits

Execute `python verify.py` after installing the dependencies in `requirements.txt`. The recorded verification run returned:

`PASS: 36 independent Fourier/physical zero-mode and length-two connectivity comparisons; ten stationary-state tests.`

The verifier checks all 36 size/twist combinations for six even rectangles and six twist pairs, numerical singular values of the bipartite coupling matrix, length-two even-site connectivity, dark-projector idempotence and trace, stationarity of the explicit limiting density matrices, and the return formula at monitored and unmonitored vertices. Its numeric tolerance is \(10^{-8}\). It is a finite consistency check, not an exhaustive proof of all sizes or irrational fluxes. Analytic proof covers every real flux in the domain without extrapolating from those checks.

The formulas are for an ideal flat nearest-neighbor connection with positive sitewise dephasing only at even checkerboard sites. No statement is made about gap uniformity as size grows or robustness to imperfect flux, missing monitors, onsite disorder, or intersite dissipation. Independent validation has not been performed.
