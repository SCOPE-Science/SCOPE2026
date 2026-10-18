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

Run `python3 check.py` with a standard Python 3 interpreter. Exact rational arithmetic checks conditional covariance on every labeled tree of orders up to five and selected six-vertex trees; the uniform-tree averaging identity is independently checked by enumerating Prüfer codes through order six. A finite rational Poisson-tail bound certifies that the asymptotic constant is strictly negative.

The finite enumeration is not used as a proof of the infinite-size result. The latter follows from the displayed tree enumeration and Poisson limit. The reported coefficient is an averaged conditional covariance, *not* the covariance when the random tree is also integrated out before computing covariance. No external independent scientific audit has been performed.
