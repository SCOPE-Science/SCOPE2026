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

# Reproducible finite verification

The standalone `verify_paluniversal.c` enumerates each possible balanced binary length-\(2k\) host in lexicographic recursion, except that infeasible prefixes are removed with a mathematically proved necessary condition. It records one greedy prefix-match state for each of the \(2^{\lceil k/2\rceil}\) targets and counts accepted hosts by number of complete binary arches. Complements are counted by symmetry, with the first symbol fixed to zero in the search. It outputs exact integer totals for every \(1\le k\le15\).

Build with a C11 compiler: `cc -std=c11 -O3 -Wall -Wextra -pedantic verify_paluniversal.c -o verify_paluniversal`, and invoke `./verify_paluniversal K` separately for all `K` from `1` through `15`. The terminal outcome at `K=15` is:

`k=15 checked_half=380442 accepted_half=380442 total=760884 classes iota_11=72 iota_12=29640 iota_13=352672 iota_14=345732 iota_15=32768`

The independent script `verify_paluniversal_independent.py` enumerates **all** balanced words without pruning and independently performs direct target-by-target greedy embedding tests for \(1\le k\le10\). The result is:

`VERIFY_INDEPENDENT_OK unpruned_complete_length_k=1..10 palindrome_index_distributions=true`

Correctness rests on the mathematical induction proving the branch-pruning condition, not on sampling. The verification does not address lengths beyond the stated scope and does not establish independent external audit.
