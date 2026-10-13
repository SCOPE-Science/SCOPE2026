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

# Reproducible verification

Run `python3 verify.py` with standard Python 3. The verifier independently checks the central-binomial representation against the factorial formula, exact rational normalization and endpoint maximality for integer input photons from \(n=1\) through \(n=17\). It also computes finite-\(n\) consistency checks for the von Neumann entropy shift, logarithmic-negativity coefficient, bulk Rényi moment, logarithmically corrected critical moment and edge Rényi moment. On its tested environment it produced:

`VERIFY_OK exact_distribution_n=1..17 mass_normalization=passed endpoint_max=passed`

`VERIFY_OK negativity_linear_coefficient=0.914218823 target=0.913893162`

`VERIFY_OK entropy_constant=-0.237012554 target=-0.241564475`

`VERIFY_OK q2_logarithmic_trend=passed q3_edge_scaling=passed`

The slowly convergent critical quotient is checked only for improvement toward its theoretical limit, not incorrectly certified equal at finite sample size. These checks are supporting finite evidence; the infinite limits are proved in RESULT.md via uniform binomial-coefficient bounds, harmonic sums and dominated convergence. No external validation has been performed.
