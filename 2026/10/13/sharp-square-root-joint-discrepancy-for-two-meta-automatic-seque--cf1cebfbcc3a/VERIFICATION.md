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

The exact standard-library verifier `verify.py` reconstructs the two published four-state morphisms and their sixteen-state joint transfer. It computes the entire characteristic polynomial over the integers using Newton trace identities, matches its explicit factorization, compares both defining nested recurrences against their automata at 262144 successive indices, tests complete base-four blocks through exponent 12, and checks the prefix decomposition at 271 positions.

Run: `python3 verify.py`. Its recorded output is in `verify_output.txt`. The finite runs test the algebra and indices but are not a proof of the global asymptotic. The proof depends on the separately demonstrated simple modulus-two eigenvalues, annihilation of the eigenvalue-four direction, and nonzero oscillating component after exponent eight. No independent audit has been performed.
