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

# Reproducible mathematical checks

Run `python verify.py` with Python 3 and no third-party packages. The verification program was run after assembling the proof and returned:

`VERIFY_OK 503211`

The executable independently builds complete multipartite Laplacians, inverts their resolvents by exact rational Gaussian elimination, and checks the vertex-class diagonal identities. It checks positivity of all matrix entries around the explicitly bracketed critical steps, exact sign changes of the defining quadratic, and the fixed-budget graph ranking across all integer partitions through order eighteen. It also compares each balanced fixed-part-count candidate for orders through one thousand. Counts are defined by the script's own assertion counter, with all assertions active in ordinary Python execution.

These finite tests are sanity checks, not an exhaustive verification of infinitely many graph orders or budgets. The universal proof rests on the analytic spectral projectors, exact diagonal factorization and the continuous-derivative plus edge-deficit argument in `RESULT.md`. Inputs require at least three vertices, positive total budget, uniform positive conductance over all installed cross-part edges, and connected complete multipartite graphs. Claims about nonuniform conductance design, arbitrary graph topology, nonnegativity of internal Runge–Kutta stages, nonlinear diffusion, and independent publication-priority certification are outside the result.
