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

# Verification and limits

The proof directly computes the logarithmic curvature of the normalized two-component Gamma density and reduces its sign to the unique maximum of a strictly log-concave one-variable function. At the critical value the maximum and derivative equations give the location \(t=2\sqrt\alpha\) and the exact normalized weight threshold. Monotonicity in the log-amplitude ratio and the unique maximum establish necessity, sufficiency, and the single positive-curvature interval. The calculation separately treats \(\alpha\le1\), coincident rates, and pure components.

Running `python verify.py` reproduces 196 finite consistency cases, including exact rational algebra and numerical shape/weight examples. These calculations are not substitutes for the universal analytic argument. The assumptions are \(\alpha>0\), positive distinct rates, and strictly interior mixing weights; no conclusions are asserted for higher-component mixtures. Primary-source comparison did not include the complete 2022 hyper-Erlang conference paper; historical priority therefore retains a documented risk. Independent audit has not been performed.
