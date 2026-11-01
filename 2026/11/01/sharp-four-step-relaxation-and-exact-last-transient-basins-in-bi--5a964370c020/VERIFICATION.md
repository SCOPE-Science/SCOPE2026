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

The proof certificate is `symbolic_checker.py`, a pure Python exhaustive enumerator of 80 admissible linear extensions and 56 pairs of threshold cuts. It validates the precise identity and last-transient criterion on all 4,480 formal comparison types and includes all tie-boundary possibilities by linear extension. It does not use finite-size sampling.

`direct_checker.cpp` implements the original closed-neighborhood vertex update independently, without symbolic population labels. For all shores of orders 1 through 7, all thresholds from 1 through the maximum shore order plus 2, and every labelled initial bit string, it checks the global identity, the individual-state last-transient criterion and the binomial counting formula. It covers 2,632 parameterized graphs and 4,884,036 initial states.

Run with `python3 symbolic_checker.py` and `g++ -std=c++17 -O2 -o direct_checker direct_checker.cpp && ./direct_checker`. The recorded outputs are bundled as `symbolic_output.txt` and `direct_output.txt`.

The exact universal theorem depends on the reduction to 7 comparands and the completeness of the ordering/threshold cut argument. No heterogeneous-threshold or asynchronous claim is made. An independent external mathematical audit has not been conducted.
