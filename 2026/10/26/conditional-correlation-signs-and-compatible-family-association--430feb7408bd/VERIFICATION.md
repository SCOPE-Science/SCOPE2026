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

# Reproduction and scope

Run `python check.py` with Python 3.8 or newer. The program uses only `functools`, `itertools`, and `math` from the standard library; no downloaded data, random seed, or external library is required. It exhaustively generates triangulations of labeled convex polygons having \(4\) through \(9\) vertices, checks extension products, all compatible-set inequalities, and the conditional covariance sign classification. It separately tests strict Catalan log-convexity for an explicit finite parameter grid.

Observed execution: `PASS: 1983545 exact assertions (exhaustive triangulations through 9 vertices)`.

The unrestricted proof is mathematical and uses the Catalan quotient identity, exact conditioning, and the chain rule. The finite checker does **not** establish the infinite quantifiers or historical originality. No independent validation has been performed.
