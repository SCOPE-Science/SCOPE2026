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

# Reproducing the exact finite checks

The C++17 source `verify_characteristic13.cpp` is self-contained and requires no input files. Compile it using:

```sh
c++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_characteristic13.cpp -o verify_characteristic13
for a in $(seq 1 12); do ./verify_characteristic13 "$a"; done
```

Each invocation enumerates exactly \(11!=39,916,800\) single thirteen-cycles with prescribed first successor, computes all twelve shortest closed-walk lengths, checks all twelve characteristic inequalities, and counts extremizers and the nearest nonmaximal deficit. The twelve complete results are given in `census.tsv`, totaling \(12!=479,001,600\) checks, no violations, twelve maximal modular shifts, and two cycles with deficit exactly one.

For a literal implementation of the convex-hull iteration, run `python3 check_direct.py`. This uses no graph-breadth-first-search optimization and compares every shortest return on all single cycles through eight sites and ten thousand pseudorandom thirteen-site cycles. Actual execution printed: `Independent convex-hull/graph comparison passed for 15912 cycles`.

The main exact enumeration was executed once on each of the twelve successor blocks using the source embedded here, and the near-extremal representatives were replayed with the independent convex-hull checker. This is a finite exhaustive computational proof, **not** an extrapolation to larger orders. Compiler correctness, hardware reliability, and independent mathematical review are outside this package's verification scope.
