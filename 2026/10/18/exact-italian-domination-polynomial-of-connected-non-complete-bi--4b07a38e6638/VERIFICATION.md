---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks and limits

The accompanying `verify.py` is a standalone Python 3 program using only the standard library. In the same directory, run:

```
python3 verify.py
```

The program independently generates each graph from its complete bipartite class-adjacency rule, loops over all \(\{0,1,2\}\)-labelings, and checks the definition of an Italian dominating function directly at every zero. Every accepted labeling is classified by its first zero-containing \(A\)-class and last zero-containing \(B\)-class. It compares the exact integer polynomial for **each** such pair against the theorem's product-and-truncation formula, and independently sums the pair contributions.

The expected totals from the packaged script count repeated list entries: 76 profile visits, 1143 profile/frontier-cell comparisons, and 793620 examined labelings. Two profiles occur twice. Counting each ordered profile once gives 74 profiles, 1111 cells, and 754254 examined labelings. The list includes non-complete bipartite chain graphs and the \(p=1\) complete-bipartite boundary. Two six-vertex examples with equal bipartition sizes have weight-four counts of four and six, respectively, as stated in the result.

These finite checks are not a proof for arbitrary positive class sizes; that unrestricted claim depends on the zero-frontier necessity-and-sufficiency argument in `RESULT.md`. The script makes no claim about bibliographic priority or independent validation.
