---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The distinct isolation events share one incident edge exactly for adjacent vertices, giving the stated positive diagonal congruence to B(t). Its signless-Laplacian quadratic form vanishes only for zero: a vertex of degree at least two has strictly positive diagonal excess for t>1, and the edge sums propagate zero from it. In a bipartition, switching signs gives an irreducible positive-definite matrix with nonpositive off-diagonal entries. The convergent nonnegative Neumann series for its inverse has strictly positive entries by the existence of paths, yielding the stated opposite precision sign. The hub Schur complement has equal diagonal h-r/(t+1) and off-diagonal 1-r/(t+1); positive diagonal scalings cancel in the partial correlation. Its denominator is positive and its numerator changes sign exactly at t=r−1 when r≥3. The hub marginal covariance is pq^(2r+1)>0. A fresh exact replay (not the frozen checker) exhausted 4 and 38 connected labelled graphs at n=3 and 4 and tested their 12 and 228 unordered pair cofactors in z=t−1. Each polynomial is nonzero with coefficients of one weak sign; hence no interior zero. A separate sum over 128 retained-edge configurations per parameter gave hub partial correlations −27/491, 0, 1/211 at p=1/4, 1/2, 3/4, with strictly positive marginal covariances. Replay: python3 /workspace/branches/19f50411-cd78-4d11-8632-08cf4764744b/replay_check.py; full_replay.log records the results. The finite checks are not the proof for arbitrary bipartite graphs or all books. Connected graphs of fewer than three vertices have singular isolation covariance. No inference to conditional independence is made.

## originality

PASS

Within the checked literature and catalogue, neither the sharp graph-order boundary for isolation indicators nor the book-family law is covered. The covariance-congruence reduction and inverse-positivity argument use standard methods; the similar five-vertex threshold in a matching model does not establish this one.

## value

PASS

This establishes a sharp obstruction to inferring the adjusted sign from the fixed positive marginal sign of adjacent isolation indicators. The bipartite parity theorem identifies a broad rigidity regime; the book computation provides a structural mechanism, a full family and the first possible order, not only a numerical crossing in a hand-picked graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
