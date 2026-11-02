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

# Reproducibility and limits

Execute `python3 CHECK.py` with dependencies in `requirements.txt`. The program evaluates the exact one-variable integral defining \(D_\alpha(r)\), using a connection formula for the endpoint-singular primitive and scalar optimization. It checks beta-function coefficients at the threshold, the deficit slope for three small positive values of \(h\), and the monotone approach of four positive-parameter numerical maximizers and normalized excesses to the two claimed limits. The last evaluated offset \(\varepsilon=0.002\) gives \((1-r)/\varepsilon^2\approx0.48318\) and excess/\(\varepsilon^2\) \(\approx2.99252\). These finite calculations do not establish an infinite limit; the analytic proof in `RESULT.md` establishes that limit by uniform estimates.

The stated independence status is not a scientific certification.
