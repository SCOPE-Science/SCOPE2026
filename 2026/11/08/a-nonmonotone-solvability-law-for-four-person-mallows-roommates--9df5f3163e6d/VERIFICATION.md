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

# Verification of the mathematical result

`python3 verify.py` enumerates all 1296 possible final strict profiles and all three perfect matchings, checks the two disjoint 24-profile unsolvable orbits, computes each reduced ranking's four insertion weights from full four-name Mallows permutations, verifies all 25 inversion coefficients, and checks the simplified rational function and differentiated identity using only integer polynomial operations. Expected leading output: `VERIFY_OK`.

`c++ -O2 -std=c++17 verify_independent.cpp -o check && ./check` independently traverses all 331776 tuples of full four-name rankings, deletes each participant's own name, checks the three candidate matchings, and reproduces the 25 unsolvability coefficients. Expected leading output: `VERIFY_INDEPENDENT_OK`.

The unique-maximum proof additionally uses reciprocal symmetry and Descartes' rule of signs on an explicitly displayed degree-twelve integer polynomial; numerical root approximations are not relied upon for the uniqueness statement. The exact finite exhaustive counts are specific to four agents; neither program verifies an assertion about larger instances. Independent scientific validation has not been performed.
