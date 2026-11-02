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

# Reproduction

From the same directory as these files:

```sh
python3 verify.py
g++ -std=c++17 -O2 -Wall -Wextra verify_alt.cpp -o fano_check
./fano_check
```

The Python program computes the complete \(458\)-element state space, checks the rank-toggle and minimal-complement definitions agree on every ideal, enumerates all \(168\) collineations, checks commutation, and verifies the seven representative cycles and their disjoint group orbit partition. It prints `FULL_CERTIFICATE_OK` only after asserting the cycle histogram, orbit order, and total coverage.

The C++17 program independently generates the Fano lines using sums of nonzero vectors, checks all \(2^{14}\) masks for downward closure, computes the toggle permutation, and reproduces the cycle length and ideal-cardinality sum distributions. It prints `INDEPENDENT_VERIFY_OK` after assertions succeed. Here independent means a separate implementation, not independent scientific validation.

The proofs in RESULT.md use these finite exact certificates. No unresolved infinite extension, statistical estimate, or external certification is claimed. Independent scholarly audit has not been performed.
