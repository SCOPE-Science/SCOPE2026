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

# Reproduction and boundaries

Run `python verify.py` using Python 3 with no external libraries. The script constructs every one-step output for all words for \(q=2\), \(2\le n\le12\); \(q=4\), \(2\le n\le7\); \(q=6\), \(2\le n\le5\); and \(q=8\), \(2\le n\le4\). It independently compares every pair of insertion positions against the stated exact collision criterion, computes exact sphere-size histograms, verifies the two-state transfer-matrix counts, checks the rational-moment formulas, and checks the polynomial recurrence induced by the bivariate generating function through \(n=35\) for each tested alphabet size.

The exhaustive computations support but do not replace the proof for arbitrary \(n\) and even \(q\). No bound for multiple duplications, no claim about optimal code sizes, and no independent audit is supplied.
