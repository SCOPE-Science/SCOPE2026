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

# Reproducibility

Run `python -m pip install -r requirements.txt` followed by `python verify.py`. The Python script uses exact rational symbolic arithmetic and builds the full \(2^M\)-state Markov transition matrix. It verifies the beta-binomial stationary vector and computes the additive functional's asymptotic variance by the finite-state Poisson equation for eight parameter choices. It also enumerates complete binary histories to check the exact edge-count mean and covariance-sum variance expression in 34 finite graphs.

Observed checks: eight exact chain identities and 34 exhaustive finite-graph moment identities passed. These calculations do not constitute a proof of the infinite Gaussian limit, which follows instead from a finite-state Markov functional central limit theorem and a separately established absolutely convergent covariance identity. No independent audit was performed.
