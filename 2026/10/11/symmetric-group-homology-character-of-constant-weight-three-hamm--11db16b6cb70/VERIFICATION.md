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

Use Python 3.9+ with no extra packages:

```
python3 verify.py
```

The program generates the star and top facets of \(\operatorname{Cl}(J(n,3))\), enumerates all faces exactly, computes ranks of mod-two simplicial boundary matrices, and compares the direct signed action on face chains with a separately evaluated virtual-representation character for each partition of \(n=5,6,7,8\). The checked nonempty-face totals are 75, 260, 756, 2002; degree-two mod-two Betti numbers are 4, 19, 55, 125; every other reduced mod-two Betti number is zero. There are 55 tested conjugacy-class representatives and no character discrepancies. Expected terminal marker: `VERIFY_OK`.

The infinite proof uses nerve theorem and equivariant Euler identities not certified solely by these finite tests. Rational representation-ring formulas do not imply integral module decompositions or persistent statements. Independent auditing is not performed.
