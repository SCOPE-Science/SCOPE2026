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

# Verification

Run `python verify_colored_mapping.py` with Python 3 and the standard library. The checker enumerates all functions and colourings at parameters `(n,q)=(2,2),(3,3),(4,3)` and tests every possible permutation for colour-preserving map automorphisms; there are 16, 729 and 20,736 expanded maps respectively. It checks that every same-colour leaf-twin event implies nonrigidity, and independently compares the enumerated expectation of leaf-twin pairs with the exact rational formula. It also simulates seeded samples at `n=100,300,1000` with `q=n`. The actual successful final line is `COLOURED_RANDOM_MAP_RIGIDITY_OK`.

The proof of the asymptotic limit is mathematical: exact factorial moments show a Poisson law, cyclic permutation symmetries are ruled out by expected-count bounds, and other non-leaf symmetries force a four-vertex pattern of vanishing expected count. Enumerations do not prove asymptotics and simulations are not exhaustive. There is no independent scientific audit or external certification.
