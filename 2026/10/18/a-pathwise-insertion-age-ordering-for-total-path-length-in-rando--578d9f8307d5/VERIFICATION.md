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

The proof is analytic and finite-size exact. Run `python check.py` from the directory containing this document, using only the Python standard library. The script builds every search tree separately for every permutation of \(n-1\) keys, \(2\le n\le8\), evaluates each possible insertion slot of the largest key, and checks all claimed deterministic depth-increment and monotonicity formulas. It compares exact enumerated frequencies with the binomial decrement tail formula, the independent record-count/prefix-maximum distribution, and the harmonic expectation identity using `fractions.Fraction`. A completed execution printed `ALL PASS`.

The verifier cannot establish the all-order theorem by enumeration; the full proof is in `RESULT.md`. It does not check earlier literature priority, a separate scientific undertaking. Independent audit has not been performed.
