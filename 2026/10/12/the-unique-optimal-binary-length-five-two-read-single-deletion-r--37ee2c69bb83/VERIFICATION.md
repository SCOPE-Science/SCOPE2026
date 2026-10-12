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

`verify.py` is the authoritative executable check for the finite claim. It performs the following operations from scratch:

1. Generates all \(32\) binary length-five words and their sets of distinct one-deletion outputs.
2. Builds the conflict graph directly from deletion-ball intersections.
3. Independently rebuilds the same graph by grouping length-five parents around unordered pairs of shared length-four traces and asserts graph equality.
4. Solves the maximum-independent-set problem by a memoized include/exclude recurrence.
5. Independently enumerates maximal compatible sets with Bron--Kerbosch search on the complement graph.
6. Requires both methods to return maximum \(20\), exactly one maximizer, and the stated codeword list.
7. Directly checks pairwise read coverage, reversal and complement invariance, and the weight profile.

A successful replay begins with `VERIFY_OK maximum=20 labeled_maxima=1 read_coverage=1 reversal_invariant=true complement_invariant=true weight_profile=1,3,6,6,3,1`.

The computation is exhaustive only for binary length five. It does not certify any statement for other lengths, alphabets, or channels. Independent audit has not been performed.
