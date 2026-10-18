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

# Reproducible checks and limits

The accompanying `verify.py` is a standalone Python 3 program using only the standard library. In the same directory, run:

```
python3 verify.py
```

The program independently generates each graph from its complete bipartite class-adjacency rule, loops over all \(\{0,1,2\}\)-labelings, and checks the definition of an Italian dominating function directly at every zero. Every accepted labeling is classified by its first zero-containing \(A\)-class and last zero-containing \(B\)-class. It compares the exact integer polynomial for **each** such pair against the theorem's product-and-truncation formula, and independently sums the pair contributions.

Expected numerical checks from the packaged script: 76 class-size profiles, 1143 distinct frontier cells, and 793620 examined labelings; all comparisons pass. The connected, non-complete bipartite profiles used in the theorem are included, and the \(p=1\) complete-bipartite boundary is tested as an independent consistency check. Two six-vertex examples with equal bipartition sizes have weight-four counts of four and six, respectively, as stated in the result.

These finite checks are not a proof for arbitrary positive class sizes; that unrestricted claim depends on the zero-frontier necessity-and-sufficiency argument in `RESULT.md`. The script makes no claim about bibliographic priority or independent validation.
