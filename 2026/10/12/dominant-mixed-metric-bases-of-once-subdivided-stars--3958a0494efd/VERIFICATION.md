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

The verifier constructs the once-subdivided star \(S_q\) for
\[
3\le q\le8.
\]
It computes all vertex-to-vertex distances and represents every graph vertex and edge against each candidate landmark set. It independently checks mixed resolvability and domination.

All subsets of size at most \(q+1\) are exhausted. The complete minimum family is compared with
\[
\{v_1,\ldots,v_q\}\cup\{x\},
\qquad
x\in\{c,u_1,\ldots,u_q\}.
\]

Recorded output:

```text
VERIFY_OK
q=3: gamma_mr=4, minimum_bases=4
q=4: gamma_mr=5, minimum_bases=5
q=5: gamma_mr=6, minimum_bases=6
q=6: gamma_mr=7, minimum_bases=7
q=7: gamma_mr=8, minimum_bases=8
q=8: gamma_mr=9, minimum_bases=9
candidate_subsets_checked = 120444
all minimum dominant mixed bases matched leaves plus center-or-one-support classification
```

The finite computation is corroborative only. The arbitrary-\(q\) theorem follows from the unique-leaf distinguisher lemma and the explicit mixed representations to the full leaf set.
