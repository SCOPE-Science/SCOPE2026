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

The checker constructs each spider from its arm lengths and simulates the standard zero forcing rule directly on every vertex subset. Inclusion-minimality is tested by deleting every initially blue vertex in turn. This definition-level computation is independent of the structural theorem used to generate the predicted minimal sets.

Recorded output:

```text
VERIFY_OK
spider_isomorphism_types_checked = 223
vertex_subsets_checked = 890320
minimal_zero_forcing_sets_checked = 7453
orders = 4..13
all minimal-set classifications matched exactly
all upper-zero-forcing formulas matched
minimum zero forcing number k-1 matched
```

The exhaustive computation is finite corroboration only; the arbitrary-leg classification and upper-number formula follow from the proof.
