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

# Reproducibility and scope

The companion standalone `verify.py` uses only Python's standard library. Run `python3 verify.py` from the directory containing the extracted package; it prints a PASS line on completion or raises an assertion if any checked equality or inequality fails.

The program constructs the exact binomial-sum success probability for a vaccine completing \(h\) exponential stages before the infection traverses \(d\) edges, and independently obtains the same probability by a finite-state race recurrence. It checks strict log-concavity of depth rewards for every nontrivial sampled index, identifies maximizers by exact rational comparisons, tests the universal one-stage first-layer result and the complete two-stage branching/height classification, and verifies the exact witness and threshold tie.

Parameters checked: \(b\in\{2,3,4,5\}\), \(H\in\{2,\ldots,11\}\), \(h\in\{1,\ldots,8\}\), and \(q\in\{1/10,1/3,1/2,2/3,3/4,9/10\}\), giving \(1{,}920\) exact parameter families. All checks passed in the packaged program execution. The arbitrary-positive-rate and arbitrary-height results are proved analytically in `RESULT.md`; sampled computations cannot establish them on their own.

No independent scientific audit or external formal proof has been performed. Publication-priority claims are bounded by the cited original manuscript, related accessible descriptions and the documented literature comparison.
