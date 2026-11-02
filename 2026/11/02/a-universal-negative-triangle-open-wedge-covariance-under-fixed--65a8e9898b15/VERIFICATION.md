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

# Reproducibility and verification

## Analytic evidence

The proof in `RESULT.md` defines the two motif counts and the hypergeometric inclusion probabilities, enumerates exactly three overlap classes for triangle–non-induced-wedge pairs and three classes for triangle–triangle pairs, and uses the induced-wedge identity \(S=W-3T\). Rational cancellation yields the displayed closed form. The affine factor \(Q_{n,m}\) is positive on the strict interior and the other five factors determine every endpoint. The independent-edge identity follows from the same overlap classes with \(f_j=p^j\). Those finite enumerations and algebraic identities prove all specified parameter values; numerical checks alone would not.

## Machine checks

Run `python check.py` using Python 3.10+ from the same directory. This performs exhaustive enumeration of all labelled graphs for \(n=4,5,6\), rational arithmetic comparisons of empirical covariances to both the overlap and closed forms, sign checks, explicit independent-edge weighting for five rational probabilities at those orders, and a complete edge-count sweep of the overlap identity and sign for each \(4\le n\le30\). It reports `PASS: 9187 exact comparisons; n=4..6 exhaustive; n=4..30 symbolic-ratio grid.`. An additional separate symbolic rational simplification of the overlap covariance and the displayed factored covariance returned zero identically; the standalone finite checker requires no third-party libraries.

## Limits

Exhaustion covers only the named small graph orders; the universal assertion rests on the written combinatorial proof and symbolic algebra, not extrapolation. The random-graph models, motif normalization and boundary cases are exactly those in `RESULT.md`. The literature comparison is not a substitute for independent historical-priority verification.
