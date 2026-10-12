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

The 20-element witness in `witness.txt` was checked against all 128 length-seven binary targets by deleting each of the seven possible positions. There are 98 targets with one witness subsequence, 28 with two, and 2 with three; none has zero.

Compile and run `verify.cpp` with GCC or Clang supporting `unsigned __int128`. The code explicitly generates all 64 binary centers and all 128 target words and proves that none can be covered by 19 centers. Exact branch count: 81,671; `k=19 feasible=0` and `VERIFY_OK`. A successful 20-center branch is also constructed and its full union rechecked. The recursion checks every possible next center covering its chosen uncovered target, while the pruning bounds are upper bounds on possible additional coverage. Therefore the test covers all possible 19-element sets. No continuous or probabilistic numerical approximation enters the certificate.

The classification makes no assertion at other block lengths, alphabet sizes, or insertion radii. Literature incompleteness remains possible and independent validation was not performed.
