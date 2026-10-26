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

# Reproduction and limits

Compile and execute the complete standalone `verify.cpp` with any conforming C++17 compiler, e.g.:

```
c++ -std=c++17 -O2 verify.cpp -o verify
./verify
```

Observed output starts with:

```
VERIFY_OK length=16 canonical_count=4 labeled_count=480
CANONICAL_SQUAREFREE_DEPTH_COUNTS n13=209190 n14=690853 n15=2278400 n16=7421303
```

The program uses direct integer symbol-frequency differences, not hashes, randomized trials, floating point, or symbolic assumptions about unseen cases. It visits every first-occurrence-canonical Abelian-square-free word through length \(16\), tests both possible extension sides for each symbol on full-support words, and checks all four representatives against a second explicit expected list. All shorter lengths are asserted empty. `witnesses.csv` independently exhibits the obstruction half-lengths for each of the ten extensions of every listed word.

A separately implemented six-bit-lane prefix-Parikh checker returned the same length-\(13\) to length-\(16\) census and same four words; its arithmetic is valid because every symbol count through length \(17\) is less than \(64\). Finite proof completeness follows from the canonical recursion and terminal-square lemmas in RESULT.md. No claim for alphabets other than five, longer minimal spectra, or independent external validation is made.
