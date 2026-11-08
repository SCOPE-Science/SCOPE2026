---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For a pair u≠v a set is nonresolving exactly when contained in its distance bisector, so the threshold is 1+maximum bisector size. I checked the proof’s odd/even single-cycle distance-difference histograms, including antipodal and triangular cycles: every nonzero shift histogram is majorized by shift one. For displacements in both coordinates the convolution is bounded by rearrangement, and the shifted-one largest entries align at ±1 (with the shared zero entry for odd cycles), giving the sharp diagonal count. For a zero displacement, the zero-difference histogram gives exactly n or 2n (or m or 2m), producing the m=4 or n=4 mixed-parity exception. The stated six cases hold for m,n≥3; neither a finite grid search nor a mere generic bisector identity alone proves the unrestricted classification.

## originality

PASS

Qualified PASS for the complete all-parity largest bisector/threshold of C_m □ C_n, not for the preexisting general reduction to maximal bisectors or the classical minimum metric dimension. Inspected primary definitions and product literature do not give this six-case universal torus formula; unidentified stronger graph-product results remain possible.

## value

PASS

The Cartesian toroidal grid is a canonical network topology and the universal threshold answers an explicit fault-tolerant landmark-placement question: how many arbitrarily placed observers always resolve? The full parity law and exceptional C4 factor are a natural complete classification rather than a small-example check or simple restatement of the known max-bisector reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
