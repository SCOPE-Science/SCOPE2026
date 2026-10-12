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

# Reproducibility and scientific boundaries

Run `python verify.py` in the directory containing `requirements.txt`; install the listed NumPy and SciPy packages in a suitable Python environment. The script independently forms complete-bipartite Laplacians, diagonalizes them, groups degenerate eigenspaces, forms the spectral-pinched density matrix, and computes squared fidelity against the uniform classical limit. It also evaluates direct finite-time quantum dynamics and classical matrix exponentials for deterministic weighted graphs, comparing slopes with the analytical weighted-degree formula.

The executed verification result is:

`VERIFY_OK pinching=576 topology=9998 weighted_short_time=225 reversal=12`

There are 576 localized-site matrix reconstructions, 9,998 fixed-order topology comparisons, 225 numerical weighted short-time slope checks, and 12 illustrative small-time bipartite class-order comparisons. These are finite corroborations, **not** a proof of the full all-graph or all-parameter statements. The mathematical proof derives the eigenvalue expansion, terminal spectrum, monotonicity, and crossover analytically and covers every indicated integer pair and real positive noise rate. Independent assessment has not been performed.
