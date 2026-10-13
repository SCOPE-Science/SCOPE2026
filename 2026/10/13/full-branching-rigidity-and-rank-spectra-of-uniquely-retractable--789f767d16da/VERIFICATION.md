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

Direct exhaustive checks ran with Python 3 using `verify.py`, an entirely self-contained program. The program generates all unordered rooted branching hierarchy shapes with up to five leaves, constructs ultrametric distances from lowest common ancestors, and checks every candidate self-map by all pairwise distances. Every idempotent nonexpansive map is grouped by its concrete image; the count is compared against the full-branching criterion for each nonempty subset. It computes the independent tree-polynomial product from recursively constructed shapes and compares every rank coefficient. It also tests three additional explicit hierarchies (including a six-leaf irregular hierarchy) and regular-polynomial recurrences for arities 2–5 through height four.

Actual replay output:

```
SHAPES 1 1
SHAPES 2 1
SHAPES 3 2
SHAPES 4 5
SHAPES 5 12
REGULAR 2 1 [(0, 0), (1, 2), (2, 1)] 3
REGULAR 2 2 [(0, 0), (1, 4), (2, 4), (3, 4), (4, 1)] 13
REGULAR 3 1 [(0, 0), (1, 3), (2, 0), (3, 1)] 4
REGULAR 3 2 [(0, 0), (1, 9), (2, 0), (3, 27), (4, 0), (5, 27), (6, 0), (7, 9), (8, 0), (9, 1)] 73
VERIFY_OK 24 finite ultrametric shapes; 550 image-subset tests; 85778 total map candidates; 1887 idempotent maps; regular rank recurrences q=2..5,d=1..4
```

Exhaustive checking is only finite and does not establish the all-height theorem; its proof is the hierarchy induction and strict entropy argument in RESULT.md. The verifier does not establish originality, and no independent audit or mathematical certification was performed.
