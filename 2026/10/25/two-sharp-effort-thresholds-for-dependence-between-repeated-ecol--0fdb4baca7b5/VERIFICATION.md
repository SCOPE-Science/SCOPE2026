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
# Reproducibility and evidence limits

The local program `python3 verify.py` uses the Python standard library only. It reproduces the exact conditional-Poisson covariance identity, numerical root brackets for two critical mean abundances, derivative checks against finite differences in 3,000 deterministic-pseudorandom cases, phase diagrams on numerical grids, the exact \(\lambda=3\) strict witness, and large-mean asymptotics. The complete mathematical proof is in RESULT.md; grids, approximate roots and finite computations do not establish the theorem for every positive real parameter.

The scientific comparison inspects the foundational Royle–Nichols (2003) abstract, the conditional-occupancy derivation in the 2007 Donovan–Hines teaching chapter, the full accessible 2014 Moore survey-optimization study, and the full published statement of the related nonparametric repeated-count identification result. The original 2003 paper's entire full text was not accessible for direct inspection; historical priority remains provisional. No external independent audit was conducted.
