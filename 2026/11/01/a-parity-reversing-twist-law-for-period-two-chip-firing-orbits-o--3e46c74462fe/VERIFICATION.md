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

# Reproducible checks and scope

The provided verification artifacts are `verify_transfer.py`, `verify_direct.cpp`, `transfer_output.txt`, and `direct_output.txt`.

Run `python3 verify_transfer.py` with Python 3 and SymPy available. The script builds the complete sixteen-state transfer matrix, independently builds the row-swap matrix and its symmetric/antisymmetric basis, checks commutation, computes and factors both exact characteristic polynomials, and verifies the closed expressions for rung numbers three through ten. The output is `transfer_output.txt`.

Compile the separate implementation with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct` and execute `./verify_direct`. It independently constructs each graph's actual adjacency lists and enumerates all labelled firing sets for rung numbers three through ten. For rung numbers three and four, it constructs all eligible nonnegative integer chip-height assignments and directly verifies two updates, least period two and firing indicators for every assignment. Its output is `direct_output.txt`.

The all-size theorem is proved by the weighted transfer matrix and its sixteen-dimensional exact characteristic computation, not by extrapolating the finite verification tests. The checks do not establish priority over any unexamined source or certify any behavior for other eventual periods.
