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
# Reproduction of finite certificate

Use Python 3.9+ and run `python3 check_rarefaction.py`. The program has no nonstandard dependencies and uses integer arithmetic, not floating-point tolerances. It enumerates the complete integer partitions for each population size \(1\le N\le16\), verifies these against an independently coded multiplicity-histogram partition enumeration, and compares every unordered pair using the exact hypergeometric numerator.

The observed counts of pairs with at least two strict sign reversals are zero for every \(N\le15\) and two for \(N=16\), where there are exactly \(231\) abundance partitions and \(26{,}565\) unordered pairs. The two boundary pairs are reported in `RESULT.md`. Both are separately checked by direct enumeration of every labeled subset of the \(16\)-individual census, without using the hypergeometric formula in that subcheck.

The program was executed successfully from the packaged source in its preparation environment. The analytic justification for exhaustive domain coverage is the largest-part recursion explained in `RESULT.md`. None of these checks extends the statement to sampling with replacement, unequal total abundances or noninteger sample sizes. Source comparison is not an independent audit.
