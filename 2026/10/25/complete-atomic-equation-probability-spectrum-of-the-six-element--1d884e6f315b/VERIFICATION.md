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

Execute `python3 s3_equational_checker.py` with a standard Python 3 interpreter. In the checked run the program printed:

```
S3_EQUATIONAL_WORD_MAP_OK 972 maps 6 probabilities 124 local_ranks 828 evaluations
```

The program starts from the two independent free generators, multiplies their exact finite word-map signatures, and exhaustively explores all \(972\) resulting distinct functions of two group variables. Positive-generator closure is complete because inverses are fifth powers, by the exponent-six identity for \(S_3\). Their complete probability set is \(\{1/6,1/3,1/2,2/3,5/6,1\}\). Independently, over \(2\le k\le6\), the checker verifies the rank of the square/commutator coefficient vectors at all \(124\) sign assignments, matching the syzygy dimensions. A third check performs direct semidirect multiplication for \(828\) group-variable assignments and compares the results with coefficient-form evaluation.

The unrestricted classification for all \(k\ge2\) is **not** inferred from these finite checks. It is derived from the semisimple character-idempotent projection argument and local-span proof in `RESULT.md`. No formal external certificate or independent human audit is claimed. The main source of residual uncertainty is historical priority, not an observed failure of the algebraic identities.
