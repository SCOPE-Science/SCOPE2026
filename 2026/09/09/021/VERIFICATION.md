---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Fresh reconstruction from the committed 995-row table recomputed every denominator from the clique vector with zero mismatches; an independent Sturm implementation found no non-tree positive root at or below 1/5; exactly eleven seven-vertex trees have denominator 1-5t and rate 5; the next rate is 2+2*sqrt(2). This checks the finite extremal rather than trusting the saved verifier.

## originality

PASS

Best-of-knowledge originality passes for the complete evaluated 995-type rational-series table and its exact extremal profile. General growth formulas and monotonicity are prior art and make the tree extremal unsurprising, but the checked sources did not supply this full graph-by-graph table or the exact runner-up stratum.

## value

PASS

A complete exact small-graph spectrum is a natural benchmark for Coxeter-growth conjectures and arithmetic questions, rather than an arbitrary parameter slice; it includes all connected defining graphs through seven vertices and exposes exact extremal and runner-up strata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
