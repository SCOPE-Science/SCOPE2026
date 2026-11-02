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

# Verification and scope

Run `python3 verify_pal3.py` in the directory containing the code. Only the standard library is required. The output begins `VERIFY_OK` after all assertions. The algorithm implements the mathematically specified finite recurrence; it is not a heuristic search. The independent generator constructs every length-\(3q\) multiset word exactly once for \(q\le4\) and directly checks each pairwise subsequence witness.

Checked recurrence counts: \((1,14,690,80016,17825160)\) for \(q=1,\ldots,5\). The exhaustive direct checker checks \(1,20,1680,369600\) distinct words for \(q=1,2,3,4\), respectively. Memoized recurrence-state counts are \(4,21,192,2849,62388\). The program independently checks that shortest full-universal covers are at most the palindromic-only counts and that the latter divide by the alphabet relabeling group size.

The recurrence is proved by an induction in the accompanying result, so computation supplies exact finite values rather than an extrapolation from small cases. There is no full independent manual derivation of the five-letter integer and no assertion that a failed external literature search is proof of novelty. Independent scientific validation has not been performed.
