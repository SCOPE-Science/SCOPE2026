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

# Verification record

Execute `python verify.py` with Python 3.8 or later; no external packages are needed. The script enumerates each relevant diagonal torus \((\mathbb F_q^\times)^m\), computes every edge ratio, and applies the exact two-variable commuting linear equation on each edge. It independently sums the resulting commuting-pair counts to recover conjugacy-class numbers. It tests four graph configurations over \(q=2,3,4,5\), including the quadratic extension field of order four, then constructs and checks the explicit group-level torus map between two nonisomorphic six-vertex examples. Expected termination marker: `VERIFY_OK`.

The general proof uses the spanning-tree monomial coordinate isomorphism, the single cycle-character relation, and a finite combinatorial expansion valid for every prime power. The finite verifier confirms examples and catches normalization mistakes; it is not a proof for arbitrarily large graph sizes. The result is not independently audited.
