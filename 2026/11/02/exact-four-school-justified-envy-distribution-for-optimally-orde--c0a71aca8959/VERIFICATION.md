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

# Reproducible verification

The source file `verify_kemeny.cpp` is standalone standard C++17. Build and run it in its directory:

```sh
c++ -O2 -std=c++17 verify_kemeny.cpp -o verify_kemeny
./verify_kemeny
```

It independently constructs the set of \(24\) permutations, tabulates the Kendall distances, visits every quadruple of four strict school priority rankings, compares all \(24\) serial orders, and asserts both complete expected histograms and sum \(2{,}488{,}608\). In particular, there are exactly \(331{,}776\) labeled priority profiles and exactly \(2{,}376\) constant-score cases.

As a distinct check, run `python verify_pairwise.py` with Python 3 and NumPy. It constructs pairwise majority margins for six unordered pairs, rather than using a pairwise permutation distance matrix, and recomputes the full score and number-of-minimizers histograms. It additionally verifies one direct expected-justified-envy identity by summing envy over all \(24\) possible shared student preference orders. Both source files have been executed as embedded and their assertions passed.

**Proof boundary.** The finite census is exhaustive because its four nested loops each visit all \(24\) school priority permutations and compare all \(24\) candidate serial orders. This is not a claim about arbitrary numbers of students. The direct analytical proof of the shared-preference expectation identity, pairwise-tie equivalence and random-order baseline is in `RESULT.md`. The code does not establish novelty, priority, or independent external validation.
