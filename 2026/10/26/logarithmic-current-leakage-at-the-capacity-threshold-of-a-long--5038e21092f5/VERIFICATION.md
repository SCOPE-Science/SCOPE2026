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

Execute `python verify.py` with NumPy and SciPy installed. The checked run reported `PASS: 86 independent deterministic assertions`.

Checks include small-system canonical enumeration, finite-state Markov generator stationarity, exact bond-current comparison, reciprocal-bias particle–hole identity, and centering of the critical occupancy distribution under increasingly large ratios of branch and backbone length.

The infinite-volume asymptotics are proved in `RESULT.md` from an exact log-concave weight ratio and uniform Gaussian-tail bounds. A finite calculation cannot certify an asymptotic limit or novelty. No independent scientific audit was conducted.
