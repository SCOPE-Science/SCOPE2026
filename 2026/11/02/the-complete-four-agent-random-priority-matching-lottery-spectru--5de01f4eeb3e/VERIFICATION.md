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

# Reproducibility and scope of verification

The claim is a finite classification of four-by-four complete strict preference profiles under uniform random serial dictatorship, not a theorem for all market sizes. Full verification requires only the files alongside this document, Python 3's standard library and a C++17 compiler; no remote data or third-party packages are involved.

Run the following in the containing directory:

```sh
python3 verify.py
python3 verify_pareto.py
c++ -std=c++17 -O2 verify_full.cpp -o verify_full
./verify_full > full_output.csv
tail -n +2 spectrum.csv | diff - full_output.csv
```

The first script checks 13,824 canonical profiles, representing 331,776 labeled profiles by **unique** object relabeling, and on each independently compares a direct 24-order priority simulation with a recursive choice-tree evaluator. It verifies all 57 exact multiplicity signatures, the complete support histogram, all constructive witnesses, and rational mean \(1597/288\) and variance \(684839/82944\).

The second script compares the entire RSD matching **set** to all undominated complete allocations, testing all \(24\) perfect matchings under direct Pareto comparisons at every canonical profile. This independently verifies the matching-support interpretation.

The C++ script enumerates all \(24^4=331{,}776\) labeled preference profiles without exploiting object symmetry, generates a complete matching multiplicity counter from all 24 priority permutations and prints the sorted-signature frequencies. The final diff confirms byte-for-byte correspondence with the 57 data rows in `spectrum.csv`. This route separately checks that the support histogram matches the stated 16 values and that all signature counts sum to the full domain size.

`support_histogram.csv` contains 16 support counts, `support_witnesses.csv` contains a profile for each attainable support size (rank indices are zero-based lexicographic permutations), and `spectrum.csv` contains all 57 weakly decreasing positive integer partitions of 24 that actually occur, with their exact labeled multiplicities.

A further direct argument proves that the support is one exactly for mutually distinct first choices, whose count is \(4!6^4\). The converse that serial dictatorship can produce every Pareto-optimal perfect matching is classical, not a new mathematical result.

The proof of each finite frequency depends on exhaustiveness and correctness of explicit short integer programs; the fact that a run terminates is not used to infer a claim beyond their finite loops. No numerical floating-point simulation, unseen database result, unprovided certificate or independent external audit is relied upon.
