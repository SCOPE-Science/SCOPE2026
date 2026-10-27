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

# Verification and reproducibility

Use Python 3 with no third-party packages. In the directory containing the files, run `python3 verify.py`. The observed return from the packaged program is:

`PASS 17040 exact/non-twin and limiting checks across 770 connected graphs`

## Executed checks

The program enumerates **all 770 connected labeled simple graphs** on vertex counts three through five, every edge and every sector with one through \(N-1\) particles. For fixed unequal positive rational rates \(p=7/5\), \(q=2/5\), it uses exact rational finite Markov generators to assert that the linear-density stationary residual is zero if and only if the selected edge's endpoints are adjacent true twins. It confirms normalization and positivity for all these configurations. Separate exact calculations on four six- and seven-vertex connected examples check all-state stationary residuals, each oriented edge current, and the total-variation formula. A stationary entropy-production identity is checked by enumerating reversible transition pairs. Large complete-graph examples check the explicit asymptotic formulas numerically.

## Limits of checks

The rational enumeration tests specific rates and finitely many graphs; it does **not** prove all positive rates, all \(N\), a global historical novelty claim, or a hydrodynamic theorem. Those general mathematical conclusions rely on the complete analytic argument in `RESULT.md`. No independent review or external formal certification has been undertaken.
