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

# Reproducibility and verification

The standalone C++17 program `verify_middle_K2n.cpp` constructs \(M(K_{2,n})\) from its defining incidence and adjacent-edge rules, rather than from a precomputed certificate. For each \(n\in\{1,\ldots,8\}\), it enumerates all subsets of vertices assigned label two. For each such subset, it computes the exact-one-two-neighbor condition and gives every other vertex its unique cheapest label zero or one. It records the minimum weight and all distinct minimum labelings.

Independently, for \(n\in\{1,2,3,4\}\), the program enumerates **every** ternary labeling and checks the perfect Roman condition on each zero directly; the resulting minimum and count must match the two-support method. The recorded run covered 76,695,840 two-support subsets over eight graphs. The ternary cross-check is exhaustive only at its four stated orders.

To reproduce with a standard C++17 compiler, place `verify_middle_K2n.cpp` in a directory and run:

```sh
g++ -O3 -std=c++17 verify_middle_K2n.cpp -o verifier
./verifier
```

Expected exact output is embedded in `verify_middle_K2n_output.txt`, ending with:

```
VERIFICATION_OK n=1..8 total_two_support_subsets=76695840 ternary_crosscheck=1..4
```

The mathematical proof in `RESULT.md` covers all integers \(n\ge1\), including the exceptional cases. Neither the finite computation nor its output log alone proves this infinite assertion. The verifier uses 64-bit bitsets and is intentionally scoped to the stated small graphs; it is not presented as a general solver for arbitrary \(n\).

## Scientific limitations
The original open problem for \(K_{m,n}\) with \(m>2\) is not settled here. Bibliographic coverage is incomplete and an independent scientific audit has not been performed.
