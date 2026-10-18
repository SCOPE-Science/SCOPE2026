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

# Reproduction notes

From the directory containing the package, run `python3 verify.py` with Python 3.9 or newer. No third-party libraries or datasets are required.

The finite checker independently evaluates the payoff-difference identity at 100 exact rational grid points, the endemic equilibrium constraints, four exact Jacobian characteristic identities, and critical strip inequalities over four rational sharpness parameters. It also performs numerical inequality samples. In the present completed execution it printed: `PASS: 136 exact rational checks; 5320 sampled inequalities`.

These computations **do not** prove a continuum bound or asymptotic periodicity. The formal argument in `RESULT.md` supplies the universal logit derivative estimate, the strictly negative Dulac divergence, equilibrium uniqueness, the repeller spectrum, a global low-infection barrier, and the hypotheses of Poincaré–Bendixson. The theorem does not assert uniqueness, period, orbital stability, or empirical observability of individual cycles.

The primary model and its assumptions were checked against the full open HTML arXiv manuscript (arXiv:2610.03173v1). The nearest general no-cycle theorems inspected have different behavioral dynamics. Residual literature-overlap risk remains and no independent scientific audit has been performed.
