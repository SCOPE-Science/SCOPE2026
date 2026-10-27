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

The scientific theorem is derived from the exact prefix/middle/suffix factorization and a complete 27-element subset optimization. To reproduce the finite certificate, run the included `verify_overlap.cpp` file with a standards-compliant C++17 compiler:

```sh
c++ -O3 -std=c++17 verify_overlap.cpp -o verify_overlap
./verify_overlap
```

Successful execution produces:

```text
OVERLAP_Q3_K3_PASS maximum=72 maximum_codes=42 symmetry_orbits=6+12+12+12 exhaustive_prefix_families=134217728 profiles=(6,12):6,(8,9):15,(9,8):15,(12,6):6
```

The finite certificate enumerates all \(2^{27}\) subsets twice, by mutually different algorithms: a recursion accumulating forbidden-suffix bit masks and an incremental Gray-code walk maintaining suffix-coverage multiplicities. Both methods agree on the optimum and the entire list of 42 maximizing subsets. Additional checks verify their prefix/suffix size profiles, alphabet/reversal orbits, and all \(72^2\) ordered pairs in a concrete length-six witness. The checker uses 32-bit masks for 27 triples and 64-bit counters for the full power set. No search pruning, randomization, or timeout-dependent rejection enters the proof.

**Limit.** Finite enumeration establishes the 27-variable extremal subproblem, not the infinite statement alone. The mathematical factorization proved in `RESULT.md` transfers its output to every \(n\ge6\). There is no independent mathematical audit; the full-text-access limitation for a related primary paper is recorded in the review.
