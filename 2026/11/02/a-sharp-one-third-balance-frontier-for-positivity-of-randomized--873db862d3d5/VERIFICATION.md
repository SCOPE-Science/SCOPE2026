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

# Reproducibility and verification

Run `python verify.py` with Python 3 standard library. The executed checker completed 4,703 supplementary checks: exact rational Runge–Kutta stage elimination versus the stationary-projector expression, exact row sums and sign inequalities, exact first positivity-boundary examples, and deterministic quadrature comparisons of the closed probability to uniform-grid counts.

The universal rate/time/parameter classification is proved analytically in `RESULT.md`, not by finite enumeration. In particular, almost-sure recurrence follows from independent draws with strictly positive failure probability; uniform cumulative positivity follows from \(q(z)<1\) and the exact product projector identity. No floating-point run can establish these infinite-domain statements alone.

The analysis is confined to fixed-step, autonomous, irreducible two-state generators, exact stages, and independent uniform tableau draws. The cited preprint supplies the numerical scheme and stability function; no independently conducted mathematical audit is asserted.
