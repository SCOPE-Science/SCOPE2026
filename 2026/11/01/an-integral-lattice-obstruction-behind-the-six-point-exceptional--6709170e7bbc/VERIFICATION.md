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

Run `python3 check.py` in a directory containing the standalone program. Standard-library Python 3 suffices. A successful run writes deterministic JSON to standard output with `"checks": "VERIFY_OK"`, matching `verification-output.json`. No external data files, scientific databases, network calls, or third-party packages are required for the computations.

The computation enumerates all 15 one-factors, 6 complete one-factorizations, 191 nonempty simplices, and 720 label symmetries, checking every alleged incidence and signed action. It verifies the rational traces and integer augmentation-exterior matrices directly and computes binary ranks of the two ten-dimensional lattices. It also independently computes finite-field simplicial boundary ranks for three primes. Exactness of the **integral** homology, including absence of torsion, follows from the star-cover and relative-chain argument in RESULT.md; finite-field agreement alone would be insufficient.

The character comparison is a rational isomorphism, not an integral one. The differing characteristic-two ranks show nonisomorphism of the two *specified* natural integer lattices, not classification of all possible integral forms. No independent external mathematical audit has been performed.
