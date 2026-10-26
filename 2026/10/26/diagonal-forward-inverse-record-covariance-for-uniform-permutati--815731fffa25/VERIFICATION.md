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

Run `python verify.py` with Python 3 standard library only. It enumerates all \(46{,}233\) permutations across \(1\le n\le8\), builds each permutation and its inverse separately, and checks \(204\) exact rational cross-covariance entries. It also sums the closed formula for total covariance and checks positivity through \(n=100\) using exact rational arithmetic. For \(n=2,3,4\) the exact total covariances are \(1/4,11/36,41/144\). These are computational consistency checks, not exhaustive checks for \(n>8\) and not independent certification of the infinite theorem. The all-size proof is the conditional-independence argument in `RESULT.md`.
