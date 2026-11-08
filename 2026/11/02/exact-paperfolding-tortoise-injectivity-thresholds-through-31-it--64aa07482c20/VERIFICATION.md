---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

PASS. In binary words T^k deletes the first min(k,#ones) ones and appends them. For n<2^h, each length-n paperfolding window has at most one position divisible by 2^h; all other digits are determined by starting residue mod 2^(h+1). Shifts through five periods realize both values at that possible exception, making factor enumeration mathematically exhaustive. The prefix-heredity lemma proves that injectivity at length m and at least k ones in each m-factor propagate to every longer n. Fresh independent generation of the paperfolding prefix through 5P, for all 31 thresholds, explicitly found a predecessor collision and injectivity at each threshold with the one-count condition and correct 4n factor counts: 62 decisive lengths. These finite exhaustive certificates together with the covering/inheritance proofs establish all n, not a finite extrapolation.

## originality

PASS

PASS, best of knowledge. Campbell-Rampersad 2026 Section 5 proves s(1)=8, lists k=2..5 thresholds 13,14,25,26 as computer observations, and raises the higher-iteration question; those numerical values alone are prior but their all-length proofs were not given. This record proves those four and supplies 26 more certified values for k=6..31. Defant-Kravitz define tortoise/hare on words, and Allouche gives paperfolding 4n factor complexity. An unpublished high-k table or newer manuscript could overlap.

## value

PASS

PASS. The invariant is explicitly asked about in a contemporary study of paperfolding factors under iterated sorting, and the 31 exact sharp thresholds include multiple dyadic jumps, not just a trivial first case. Exhaustiveness and an infinite-length propagation argument convert finite observed data into logically certified cutoffs for 31 natural depths; no arbitrary all-k theorem is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
