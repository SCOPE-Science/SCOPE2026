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

The proof is the elementary case analysis in `RESULT.md`; the following are independently executable checks, not external formal certificates.

From a directory containing all of these files, execute:

```sh
python3 check_clique_support.py
c++ -std=c++17 -O2 -Wall -Wextra -pedantic check_clique_direct.cpp -o check_clique_direct
./check_clique_direct
```

The Python program enumerates all 21 possible nonempty support/leaf relative-color classes (seven supports times three colors), verifies their actual first-entry and least-period pairs, and verifies the exact symbolic population formulas for all widths \(1\le r\le15\). The C++ program separately constructs the original graph and update map, without using the support quotient, and enumerates all \(2{,}391{,}471\) states with \(1\le r\le11\), checking the six classes and every individual attractor-basin size. The captured actual standard outputs are `clique_support_output.txt` and `clique_direct_output.txt`. Recompilation is required; the executable is not embedded.

Neither finite test proves the infinite-size theorem on its own. The analytic proof checks every support and leaf phase, with multiplicities counted by inclusion-exclusion, for all permissible integer widths. No results are claimed for other rules or additional leaves.
