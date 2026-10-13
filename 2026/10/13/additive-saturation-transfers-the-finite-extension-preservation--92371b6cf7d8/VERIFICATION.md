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

The mathematical argument uses a Boolean-support homomorphism, a finite additive-saturation identity, monotonicity under extensions, and the published Dawar–Sankaran classical finite preservation hierarchy. The last input is a literature theorem, not an experimentally established fact.

Run `python3 aux/verify.py` using the packaged file. The reproduced output is:

```
SEMIRING_AXIOM_TRIPLES 2024
MODEL_DEFINING_VALUATIONS 13948
FORMULA_SUPPORT_AND_SATURATION_TESTS 83688
ALL_FINITE_CHECKS_PASSED
```

The test enumerates all model-defining unary-predicate annotations for small universes and uses seeded random annotations for larger finite cases. It exhaustively checks the displayed semiring laws for the stated finite caps. It cannot establish the general theorem, the absence of an equivalent first-order formula, or literature originality. Those assertions depend on the paper-level argument and the explicitly identified published premise. Independent audit has not been performed.
