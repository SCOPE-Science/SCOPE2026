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

The exact-artifact reproducer consists of `verify.cpp` and `check_arithmetic.py` in this package. Compilation with `g++ -std=c++17 -O2 -Wall -Wextra -Werror verify.cpp -o verify` and execution of `./verify` gives counts for all eight smooth companion representatives in extension degrees one through six and terminates with `VERIFY_OK`. Running `python3 check_arithmetic.py` checks the eight cubic parameters, their two affine orbits, irreducibility of the six field moduli, Newton identities, Weil duality, and irreducibility of the claimed numerator factors; it terminates with `ORBIT_AND_WEIL_CHECK_OK`.

The proof additionally relies on the cited published completeness and equivalence results for the matrix representation. The programs prove exact finite computations and polynomial identities, not independently the global classification of plane-filling curves or the completeness of all published literature. No independent audit has been performed.
