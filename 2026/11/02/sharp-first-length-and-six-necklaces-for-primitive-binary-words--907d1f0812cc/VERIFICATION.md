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

# Verification of the finite classification

The scripts `verify.py` (Python 3 standard library only) and `independent_check.cpp` (C++17, standard library only) were executed from the supplied source files. Both reported `VERIFY_OK` and agreed that there are no qualifying primitive binary words for \(1\le n\le15\), and exactly \(96\) at \(n=16\), comprising precisely the six listed primitive necklaces. The Python code tests two mathematically equivalent predicates written separately—substring Parikh comparisons and circular centered-height comparisons—for every primitive word in the exhaustive domain, and generates all sixteen shortest-border witnesses for each canonical representative.

Reproduce with:

```sh
python3 verify.py
c++ -std=c++17 -O2 independent_check.cpp -o independent_check
./independent_check
```

The exhaustiveness is finite and explicit: for each \(n\in\{1,\dots,16\}\), each of the \(2^n\) bit strings is visited exactly once and every cyclic root is tested. The divisibility/primitivity test and shortest-border-length reduction are proved in the main text. Neither random sampling nor an unreported table is used. The result makes no claim about complete classifications at lengths greater than sixteen.

The length-sixteen existence case already appears through the earlier 2015 block construction. Historical-priority review of the exact lower bound and six-necklace classification is limited by inaccessible full text of one relevant 2014 article and possible unindexed earlier work. Independent mathematical validation has not been performed.
