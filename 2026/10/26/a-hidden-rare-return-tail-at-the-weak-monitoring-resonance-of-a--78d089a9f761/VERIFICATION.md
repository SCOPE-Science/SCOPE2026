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

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy. The program reproduces the exact symbolic integrated-density identities for arbitrary nonzero coupling, compares the explicit limiting survival with two-dimensional matrix exponentials over 42 cases including the defective exceptional point, checks 48 finite-step weak limits and 16 exact discrete-mean identities, and checks 12 numerical rare-tail spectral-projection cases.

The proof of the continuum limit, moment convergence, strict exponential decay, normalized late tail, and divergent variance is analytic and given in `RESULT.md`. The finite script checks are not an exhaustive proof of asymptotic or all-parameter claims. The exceptional case, the exactly resonant no-hopping case, and arbitrarily small positive hopping are distinguished explicitly. Independent audit has not been performed.
