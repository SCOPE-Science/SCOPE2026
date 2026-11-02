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

## Reproduction
Run `g++ -O3 -std=c++17 CHECKER.cpp -o checker && ./checker` with GCC/libstdc++. The recorded output is in `OUTPUT.txt`.

The checker constructs each binary one-deletion, up-to-one-substitution ball in two independent ways: by integer bit deletion and by string erasure followed by optional bit flips. It asserts equality for all \(480\) input words of lengths five through eight. Every pairwise overlap is counted as a set intersection; every stored lower-bound clique is checked for compatibility.

An exhaustive color-bounded maximum-clique search then rules out clique sizes exceeding \(18,26,26,24\) on the respective graphs. The coloring bound is admissible because each color class is an independent set; removing previously processed vertices and intersecting with neighborhoods gives exhaustive branching over candidate cliques. Successful completion is the upper-bound certificate, not merely a solver log or a failed timeout.

## Recorded checks
- Length \(5\): \(69\) forbidden pairs, \(19\) search nodes, optimum \(18\).
- Length \(6\): \(555\) forbidden pairs, \(23\) search nodes, optimum \(26\).
- Length \(7\): \(2{,}373\) forbidden pairs, \(820\) search nodes, optimum \(26\).
- Length \(8\): \(7{,}835\) forbidden pairs, \(6{,}756{,}323\) search nodes, optimum \(24\).

For lengths one through four, the elementary bound from the total output alphabet proves that every word is compatible with every other word. These are finite exact results only. The source code does not assess priority, prove an infinite-length formula, or replace independent mathematical auditing.
