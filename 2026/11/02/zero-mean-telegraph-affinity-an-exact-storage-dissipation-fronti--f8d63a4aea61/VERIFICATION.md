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

# Reproducibility and limitations

Execute the included standalone checker with `python verify.py` in an environment with Python and SymPy. Its 339 deterministic checks include symbolic verification of the explicit stationary distribution for the complete four-state Markov generator; exact comparison of all four stationary edge currents; the normalized charge–entropy frontier and derivative signs; and 54 independently solved four-state rational generators (6 assertions each). These tests can detect algebraic and factor-of-two mistakes, but they do not establish novelty or replace the all-parameter analytic proof in RESULT.md.

The exact valid domain is \(\beta,E,a,k,\nu>0\). All equilibrium, low-switching and rapid-switching statements must be read with their specified limits. Entropy production is defined for the full four-state Markov path and excludes unspecified extra fuel/switching-control expenses. The scientific comparison relies on the cited accessible primary text; not all potential broader theorems have been excluded. Independent mathematical and priority audits have not been performed.
