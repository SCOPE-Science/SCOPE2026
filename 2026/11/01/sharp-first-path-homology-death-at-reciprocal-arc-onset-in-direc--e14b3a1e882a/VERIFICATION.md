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

## Reproducible finite checks
Run `python3 verify.py` with the Python standard library, with no other dependencies. The checker constructs the allowed directed one- and two-paths and reconstructs the integral two-path boundary group by explicitly handling forbidden shortcuts. It verifies boundary-span ranks over primes 2, 3, 5, and 101 for 65 parameter pairs, and checks literal integer boundaries of the displayed explicit death-chain for 28 sizes. The command executed and returned:

`VERIFY_OK low_degree_models= 65 boundary_generators= 16096 explicit_integer_fillings= 28 four_prime_fields=2,3,5,101`

The script's finite field checks cannot establish the all-parameter integral statement; the proof in `RESULT.md` establishes that by exact one-chain shortening, an integer winding obstruction, and a uniform integral death-chain. Independent mathematical audit remains unperformed.
