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

# Verification

Run `python3 CHECKER.py` using the Python 3 standard library; the check has no external dependencies. It groups all coordinate-rank permutations by their complete-bipartite edge-sign arrays, sums their preimage multiplicities to the second, third and fourth powers, and compares each exact rational result to an independently computed factorial block-composition sum. The test covers 57 exhaustive triples of small parameters and 15 leading-family lower-bound cases, totaling 72 assertions at the scenario level. It reports `PASS 72 independent exhaustive collision-moment and leading-term checks`.

Analytical checks: count permutations sharing one cross-edge orientation by alternating monochromatic blocks; all weights are factorial products. Bound positive factorial composition sums by induction and \(\sum_{r=1}^{m-1}\binom mr^{-1}\le4/m\); the latter forces every additional large-side block to be smaller by a power of the large part size. Divide by \((p+q)!^t\) to normalize. The collision-conditional law and Rényi entropy follow from exact normalization, not from simulation.

The script is not a formal certificate for unbounded parameters and independent audit has not been performed. Bibliographic noncoverage is qualified in the accompanying scientific review.
