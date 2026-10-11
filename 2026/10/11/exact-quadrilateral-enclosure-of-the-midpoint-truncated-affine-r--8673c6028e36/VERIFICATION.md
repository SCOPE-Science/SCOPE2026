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

# Algebraic verification

The included `verify_midpoint_truncation.py` requires Python 3 and SymPy. It computes all supporting-line and intersection data in the exact field \(\mathbb Q(\sqrt5)\), enumerates 320 structurally exhaustive candidates according to the cited DePano lemma, checks algebraic sign conditions for feasibility, and verifies that all admissible areas are at least \(2+3\sqrt5/4\). The actual execution returned:

```
VERIFY_OK {'total': 320, 'valid': 35, 'edge': 20, 'vertex': 15, 'equal': 1}
q= 3*sqrt(5)/4 + 2 hexarea= sqrt(5)/2 + 9/4 ratio= 11*sqrt(5)/61 + 42/61
equality_candidates= [((1, 2, 3), ('vertex', (0, 2), 0, -1))]
```

All geometric decisions after ordering are exact. The numerical angle used to propose a normal ordering is checked by exact determinant and half-plane inequalities. The checker establishes only this five-vertex core and enclosing-hexagon configuration, not a general sharp four-gon enclosure theorem and not any claim about arbitrary truncation proportions.
