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

# Finite verification and analytical limits

`python3 verify.py` returned `PASS 850 exact assertions`. It exhaustively enumerated all \(3,15,105,945,10395,135135\) matchings at sizes \(n=2,3,4,5,6,7\), checking means, variances, crossing/nesting mixed covariances and the exact factor-\(n\) ratio with rational arithmetic. Independently, it recalculated the edge weights, conditional crossing/nesting sums, and span second moments for every integer \(2\le n\le200\).

A separate symbolic summation of the piecewise span weights checked four polynomial identities (total weight, weight-square, crossing attachment, nesting attachment), with each difference simplifying identically to zero. This algebraic test corroborates the formulas; the displayed finite-sum evaluations and direct conditional matching argument in `RESULT.md` constitute the all-size proof.

The verifier uses only the Python standard library. No simulation, heuristic asymptotic fit, timeout, or independent certification is used. The covariance limits are derived from the explicitly proved finite formulas. Historical originality remains subject to literature priority.
