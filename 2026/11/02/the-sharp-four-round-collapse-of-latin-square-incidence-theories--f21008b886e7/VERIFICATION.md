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

The mathematical proof uses the one-point extension lemma for tuples of length at most three, classification of Latin squares of orders one through three up to isotopy, and a rank-five sentence with a direct witness in the cyclic-four table and algebraic nonexistence in the Klein-four table. The lemma covers arbitrarily large orders without any finite-size induction.

The independently written Python and C++17 programs inspect the actual stated incidence relation. The Python program enumerates all reduced Latin squares of orders four and five, including non-group squares, and checks equality of complete atomic fourth-point extension sets for every ordered triple, including repeated values. The C++ program computes recursive first-order types to quantifier rank five for both order-four group tables, obtaining equivalence exactly through rank four.

To reproduce from this directory:

```
python3 checks/latin_extension_spectrum.py
c++ -std=c++17 -O2 checks/latin_ef.cpp -o latin_ef
./latin_ef
```

Compare standard output byte-for-byte with the corresponding `.out` files. The programs corroborate, but do not replace, the general structural proof. Exhaustive priority over all earlier literature and independent mathematical audit have not been performed.
