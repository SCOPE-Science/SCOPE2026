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

The proof is symbolic and uses only the complete-split adjacency pattern and the secure Italian one-unit transfer definition. The critical distinction is the number \(q\) of independent-side zeros before and after a transfer.

The included checker does not use the theorem when deciding whether a labeling is valid. It builds the graph, tests the Italian neighbor-sum condition directly, and for every zero vertex tries every adjacent positive vertex as a moving neighbor and retests Italian domination after the transfer. It then compares that definition-level truth set with the profile criterion and the closed weight enumerator.

Recorded output:

```text
VERIFY_OK
complete_split_types_checked = 28
ternary_labelings_checked = 191916
orders = 3..9
all-set criterion matched
all weight-enumerator coefficients matched
minimum-weight corollary matched
```

The finite computation is corroborative only; the formula for arbitrary \(m\ge1\) and \(n\ge2\) follows from the proof.
