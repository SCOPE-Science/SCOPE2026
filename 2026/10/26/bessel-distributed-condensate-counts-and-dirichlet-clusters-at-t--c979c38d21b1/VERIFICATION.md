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
# Reproducibility checks

The mathematical proof is in `RESULT.md`. The standalone `checker.py` uses exact integer convolution to compute canonical bulk coefficient arrays and log-domain evaluation for cluster-count probabilities. Three small-system cases are separately checked against direct enumeration of every nonnegative configuration with the prescribed particle number. No external libraries or files are needed.

Execute `python checker.py`. On successful execution it prints the independent finite-enumeration identity checks, all three sequences of predicted and exact probabilities for cluster counts 1–4 at \(L=40,80,160\), and the decreasing \(\ell^1\) errors. These calculations establish the finite coefficient identity in tested cases and are consistent with the asymptotic statement. They do not replace its analytic factorial domination, bulk large deviations, or conditional Dirichlet-limit proof.

The law is valid only for fixed \(A\), fixed positive bulk weights, excess density above the bulk mean, and a strictly finite positive limit of \(	heta_L/L^2\). Independent external validation has not been performed.
