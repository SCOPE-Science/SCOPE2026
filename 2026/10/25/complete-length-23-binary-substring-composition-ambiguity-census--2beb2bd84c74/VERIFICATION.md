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

# Reproducibility of the exact binary length-23 census

This finite theorem is checked by the complete source `verify.cpp` and the whole-table artifact `quadruple_classes.csv`. Both files are needed, and both are embedded in the same delivery item as this note.

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
./verify
```

The verifier iterates over every 23-bit word. It computes an additive bucket key over all substring composition counts. Equal true multisets *necessarily* have equal key; the program verifies all larger buckets using an independent exact prefix-sum histogram, so it detects rather than assumes away hash collisions. It constructs all nonpalindromic two-factor interleavings allowed by the factor-length equation, compares complete 160-row tabulation against exhaustive classes, and asserts exactly eight exceptions.

Expected completed output:

```text
CHECK_OK n=23 words=8388608 singleton_classes=4096 double_classes=4191936 quadruple_classes=160 interleaved_classes=152 exceptional_classes=8 distinct_profiles=4196192 max_ambiguity=4
```

The indicated output was actually obtained by executing the complete C++17 source with the listed CSV. RAM use is of order eight million compact key-word records plus sorting overhead. No random seeds, external libraries, external source papers, online search, or downloaded data are required. This is an exhaustive finite certificate, not an assertion for all input lengths. Independent scientific audit has not been performed.
