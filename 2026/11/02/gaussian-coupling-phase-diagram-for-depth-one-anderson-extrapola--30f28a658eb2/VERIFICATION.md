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

# Reproduction and limits

Run `python verify.py` with Python 3 and standard-library modules. It performs exact rational identities for the proposed two-sample mixing formula, endpoint-correlation cancellations, deterministic Gaussian algebra substitutions, finite correlation-maximum comparisons, and numerical Gaussian-window integrations of the ratio-tail coefficient. At manuscript verification the result was `VERIFY_OK 7987 finite checks`. The limiting reciprocal tail follows from a bounded-density dominated-convergence argument, not numerical extrapolation; moment finiteness is proved by a tail-integral identity. These tests are self-review reproduction only and are not independent scientific validation.
