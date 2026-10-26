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

# Reproduction and boundaries

The executable `verify.py` uses only Python 3 standard-library facilities. Run `python3 verify.py` in the directory containing the program. It first checks that six templates partition their own consecutive blocks and have the stated ordinary-length vectors. It then builds and validates every constructively feasible length multiset for \(3\le n\le60\) (20,309 cases). An independent bitmask dynamic program enumerates all possible count triples for perfect matchings having only lengths \(1,2,3\) for \(3\le n\le10\), checking equality with the predicted classification.

The observed output was:

```
n 3 admissible_multisets 5 exhaustive_ok
n 4 admissible_multisets 9 exhaustive_ok
n 5 admissible_multisets 12 exhaustive_ok
n 6 admissible_multisets 15 exhaustive_ok
n 7 admissible_multisets 20 exhaustive_ok
n 8 admissible_multisets 25 exhaustive_ok
n 9 admissible_multisets 29 exhaustive_ok
n 10 admissible_multisets 36 exhaustive_ok
CONSTRUCT_OK 20309 instances checked for 3<=n<=60
VERIFICATION_OK
```

The output is a finite regression check rather than an exhaustive proof over all orders. The all-order result uses an explicit six-tile construction, the modular residue obstruction, and an elementary Hamiltonian-cycle argument, all given in RESULT.md. No randomized search, external package, or unexplained numerical certificate is needed. The bitmask recurrence independently explores perfect matchings at the stated small orders but does not cover larger orders.
