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

The standalone `CHECK.py` requires only Python 3 standard-library `fractions` and verifies the exact projected edge-flow matrices for every `3 <= n <= 7`, `1 <= r <= 4`. Run `python3 CHECK.py` in the directory containing this document and the checker. It verifies idempotence, path-constancy, original-vertex incidence conservation, permutation covariance under generators, and both full absolute column sums in exact rational arithmetic. Replay output: `CHECK_OK 94060 exact rational assertions, all pairs 3<=n<=7,1<=r<=4`.

These finite checks are not an exhaustive proof for unbounded `n` or `r`. The unrestricted argument uses an exact divergence formula, finite-group averaging, a one-dimensional stabilizer-fixed circulation space, and a row-sum inequality valid for every real weight vector. No external formal or independent validation is asserted.
