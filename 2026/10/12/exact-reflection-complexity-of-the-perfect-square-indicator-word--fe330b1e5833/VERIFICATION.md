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

# Verification of the exact perfect-square reflection formula

From this directory execute `python3 verify.py` using Python 3.8 or later; it uses the standard library only. Its successful output is:

```text
VERIFY_OK direct_reversal_census_lengths=0..100 gap_count_lengths=101..2000 ordinary_even_lengths=2..2000
```

The direct census constructs the first sufficiently many symbols with marked positions \(0,1,4,9,\ldots\) and builds the complete set of length-\(n\) factors at \(0\le n\le100\). For those lengths, the final chosen square gap is larger than \(n\), so all one-mark placements occur and every factor with at least two \(1\)'s has its first pair earlier in the prefix. Canonical representatives are the lexicographic minima of each word and its reversal; their set size is compared to the formula.

A different routine implements the independent gap-parameter counting rule, including duplicate reversal pairs. It is compared with the closed formula for \(101\le n\le2000\) and with the ordinary-even-count formula for \(2\le n\le2000\). Runtime and computing environment may vary; these are finite checks, not infinite completeness certificates. The infinite assertion follows from the bijective gap analysis and finite symbolic sums in `RESULT.md`. Independent scientific review and external certification have not been performed.
