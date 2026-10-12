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
# Reproducible verification

Run `python3 verify.py` from the directory containing this file and the standalone script. No packages beyond the Python standard library are required. The script (i) constructs and canonicalizes the multiplication table for every nonempty loopless digraph on three vertices, with isomorphism checked using all permutations of all five semigroup elements; (ii) constructs the additional two-output class; (iii) checks the complete size-four classification; (iv) independently checks semigroup associativity, exact cubic nilpotency and zero element squares for every constructed table; (v) checks the four infinite obstruction families at selected sizes, and (vi) checks the six-element example and its mutual homomorphisms with the transitive tournament.

Expected output:

```
VERIFY_OK
order4_classes=2 order4_finitely_based=1
order5_classes=16 order5_finitely_based=4
order6_nontransitive_finitely_based_example=present
```

Finite executions do not verify the infinitude of the obstruction families, the nilpotent equational criterion, or all possible larger semigroups. Those points rely on the mathematical proof and published source. No independent audit has been performed.
