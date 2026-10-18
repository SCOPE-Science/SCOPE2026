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

# Exact finite verification

Run from the directory holding the complete package:

```sh
c++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
./verify_direct
c++ -std=c++17 -O2 verify_greedy.cpp -o verify_greedy
./verify_greedy
```

`verify_direct.cpp` visits all restricted-growth ternary words through length \(11\). For each, it iterates every nonempty subset of positions, recovers the corresponding subsequence, and OR-aggregates all masks by subsequence string. A string is an s-cover exactly when the accumulated mask is all ones. No heuristic candidate pruning is performed. The program checks the canonical census counts and exact unique exception. It enumerated \(72{,}517{,}166\) occurrence masks and ended with `DIRECT_CERTIFICATE_PASSED`.

`verify_greedy.cpp` separately enumerates every labeled ternary word through length \(11\) and checks candidate covers via earliest-prefix/latest-suffix embeddings. Completeness of its shorter candidate list uses published properties of shortest s-covers and \(\gamma(3)=8\) (SPIRE 2022). It independently obtained \(177{,}141\) words with one shortest cover and \(6\) words with two at length \(11\), and ended with `GREEDY_CERTIFICATE_PASSED`.

The file `verification_output.txt` contains both successful outputs as obtained by executing the supplied exact code. The two separate enumeration strategies agree; the complete mathematical justification of their finite loops is given in RESULT.md. This is finite validation, not an infinite exhaustive search, and neither externally conducted independent audit nor independent certification is asserted.
