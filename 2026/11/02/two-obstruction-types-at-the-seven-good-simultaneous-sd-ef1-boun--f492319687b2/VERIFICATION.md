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

# Verification summary

The substantive computation is exact integer enumeration, not simulation and not a claim about arbitrary numbers of goods. Every strict singleton order of seven goods is represented in the full enumeration. Fixing the market order causes no loss because goods can be relabeled simultaneously.

Run with Python 3.10 or newer:

```
python3 verify.py
```

Expected checked totals: 630 distinct paired subjective rankings per agent; 396900 paired-ranking profiles; 96 profiles without a compatible allocation; two disjoint obstruction orbits of 48 profiles each; 6144 incompatible strict-ranking pairs; probability 8/33075; mean compatible allocation count 128/25. The script tests each representative against every one of the 128 possible complete allocations in addition to the structured market-split test.

Run with a C++17 compiler:

```
g++ -O2 -std=c++17 independent_full.cpp -o independent_full
./independent_full
```

Expected full-ranking totals: 25401600 subjective-ranking pairs; 6144 with zero compatible allocations; 130056192 compatible allocations summed over all pairs (each feasible allocation counted once per profile). The program independently uses a direct prefix-difference predicate rather than the paired-order orbit calculation. Both verifiers completed with their assertions satisfied from the included source files.

The proof of the prefix reduction and symmetry group action is in `RESULT.md`. The programs exhaust their specified finite domains, but neither proves analogous results for eight or more goods, tied rankings, or additional agents. No independent scientific audit or certification has been conducted.
