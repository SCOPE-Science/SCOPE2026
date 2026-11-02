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

# Reproducibility
Execute `python3 verify_peirce.py` with Python 3 (standard library only). The script constructs downset Heyting implications from their adjunction and compares the directly evaluated Peirce equation against the independent minimal-excluded-point predecessor criterion, for all ordered pairs.

Recorded successful execution:

```text
POSSET_SIZE 1 CHECKED 1
POSSET_SIZE 2 CHECKED 2
POSSET_SIZE 3 CHECKED 7
POSSET_SIZE 4 CHECKED 40
POSSET_SIZE 5 CHECKED 357
POSSET_SIZE 6 CHECKED 4824
ROOTED_AND_COROOTED_CHECK_PASS total_posets= 5231 antecedents= 101658 rooted= 408 corooted= 408
BOTH_STAR_FAMILIES_PASS k=1..9
COMPLETE_BIPARTITE_LEVEL_FORMULA_PASS r,s=1..5
ALL_PEIRCE_CHECKS_PASS
```

The enumeration is of naturally labeled finite posets, not of all labelings or all isomorphism classes. The equality tests include every such poset through six points; neither the enumerated range nor the larger star instances proves the universal claims. The mathematical proof in `RESULT.md` supplies the all-size argument. External independent validation has not been performed.
