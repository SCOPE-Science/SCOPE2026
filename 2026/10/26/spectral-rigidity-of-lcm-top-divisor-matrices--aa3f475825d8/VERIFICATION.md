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

# Reproducibility

Run `python3 verify.py` using standard Python 3. The script builds exact binary matrices on divisor sets; checks all integer power traces against tensor-local predictions; obtains characteristic polynomials by exact Newton identities; checks cospectral and noncospectral comparator pairs; and exercises inverse reconstruction with high-precision decimal numbers, including repeated factors. Successful output:

`VERIFY_OK: exact integer trace/characteristic certificates for 16 divisor lattices; 2 cospectral pairs; five repeated-factor reconstruction cases`

The exact theorem is proved by tensor decomposition of exponent-coordinate matrices and an ordered-multiset pairing lemma. The decimal inversion tests and finite enumerations are consistency checks, not proofs for all integers and not certificates of numerical conditioning. There has been no independent external audit. The accessible source comparison does not rule out an unlocated stronger statement in the join-matrix literature.
