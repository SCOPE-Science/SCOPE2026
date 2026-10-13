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

The mathematical reduction enumerates exactly \((q-2)!\) affine-normalized evaluation vectors for each field \(\mathbb F_q\). For every vector it tests all \(q(q-1)-1\) nonidentity affine maps. The maximum LCS converts to the insertion–deletion correction radius via \(\tau=q-1-L\). Constant codewords are covered by the proof separately.

## Reproducible checks

Compile the two included C++17 programs with a standard compiler:

```sh
g++ -std=c++17 -O3 -Wall -Wextra rs_lcs_census.cpp -o rs_lcs_census
g++ -std=c++17 -O3 -Wall -Wextra rs_independent.cpp -o rs_independent
for q in 2 3 4 5 7 8 9 11; do
  ./rs_lcs_census "$q"
  ./rs_independent "$q"
done
./rs_independent 13
```

Check that the distributions agree exactly with `COUNTS.tsv` after replacing each maximum LCS value \(L\) by \(\tau=q-1-L\). The programs were compiled and executed from their supplied source files. The independent verifier printed `VERIFY_OK` for every enumerated field and the explicit field-thirteen witness. Its field-thirteen output was `q13 witness maxLCS=6, affine LCS histogram: 3:6 4:37 5:73 6:39`. This sum is \(155\), the complete set of nonidentity affine maps over \(\mathbb F_{13}\). It checks that every multiplier is a permutation of the field and compares ordinary longest-common-subsequence dynamic programming against the separate LIS calculation for every witness transform. The main verifier additionally compares ordinary dynamic programming against its bit-parallel recurrence throughout all finite cases with \(q\le7\).

## Scope and limitations

The complete-census proof applies only to field orders \(2,3,4,5,7,8,9,11\). For \(q=13\), only the stated explicit witness is completely certified; no exhaustive classification of all \(11!\) normalized orderings is claimed. The finite enumeration is reproducible but remains an internal scientific check, not independent external validation. The absence of an earlier equivalent result cannot be formally certified by database searches.
