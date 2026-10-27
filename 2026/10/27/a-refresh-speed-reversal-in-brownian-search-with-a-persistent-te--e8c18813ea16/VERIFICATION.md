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
# Reproducibility and proof limits

The standalone program `check.py` evaluates the exact mean-first-passage formula by symmetric diagonalization of a \(2\times2\) positive matrix. For each sample, it separately evaluates the environmental renewal kernel \(L R\) and checks the match to the backward-equation solution. It also constructs a spatially discretized absorbing Markov generator, retaining independent environmental transitions and state-dependent resets, and compares its mean absorption time with the continuum expression. This finite-volume check uses lattice spacing \(0.04\) and reflecting cutoff \(8\), with the target at \(0\).

Run `python check.py` with NumPy and SciPy installed. An actual execution passed 176 deterministic assertions. The example \(D=a=1\), mean rate \(m=5\), intensity half-gap \(\delta=2\) has a numerically located comparison equality near \(\nu=4.4682413\). The numerical critical dimensionless constant is \(z_*=1.593624260040\ldots\). Four lattice-generator comparisons differed from the continuum result by less than \(0.0024\), within the finite spatial discretization error.

The numerical program does not establish positivity for all parameters, uniqueness of the positive threshold root, or the order of the asymptotic remainder for all large switching rates. Those conclusions require the analytic generator, convexity, spectral expansion and continuity arguments given in `RESULT.md`. No independent external proof check or certification has been performed.
