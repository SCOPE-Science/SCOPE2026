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

The formula uses one ordinary binary relation and no equality. The main proof is structural: (i) preservation under every nonempty disjoint union, (ii) direct evaluation on the three- and four-point structures, and (iii) induction for existential formulas with two-way guarded universal quantifiers under induced two-way neighborhood-closed embeddings. The induction is the necessary infinite-language argument.

Run `python3 check.py` in the same directory. The checker uses Python's standard library only. It rebuilds the two separating frames, computes the locally defined predicates and the sentence's truth value, checks the complete ordered pairs of satisfying structures on one to three vertices, and generates 15,000 bounded-depth syntactic instances with a fixed random seed. Observed successful output:

```text
UNION_PRESERVATION_OK 155236 ordered small-model pairs; satisfying_counts={1: 0, 2: 7, 3: 387}
FRAGMENT_TRANSFER_OK 15000 randomly generated formulas
SEPARATION_OK A_size=3 B_size=4
```

The finite tests do not decide equivalence for every formula and do not establish any upper bound on arbitrary countermodels. The scientific source comparison and its residual priority risks are in REVIEW.md and AUDIT.json. Independent validation has not been performed.
