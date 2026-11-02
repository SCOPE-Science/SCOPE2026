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

# Verification of the classification and counting formulas

Run `python3 verify.py` with Python 3 standard library. The program first implements the exact closed-neighborhood double-domination predicate in occupancy coordinates and enumerates *every* unordered multiset of nonsingleton block occupancies consuming the prescribed excess. Residual singleton blocks are forced; each block's distinct coalition partners are tested. It then checks every member of the stated family and its exact labeled-partition multiplicity against all occupancy profiles for all 68 integer pairs with \(3\le r\le10\), \(r\le s\le14\), including the nine bounded cases essential to the general proof. Independently, for \((r,s)=(3,3),(3,4),(4,4),(5,5)\), the program enumerates all partitions of *labeled graph vertices* and directly checks closed-neighborhood double domination for each candidate pair of blocks.

Observed output:

```text
VERIFY_OK 68 exact occupancy parameter pairs; 9 finite exceptional parameter pairs; 4 independent labeled-partition enumerations
K_3,3: 20 K_4,4: 82 K_5,5: 1152 K_6,6: 3600
```

The proof uses exact structural arguments for all larger parameters and a complete finite case certificate for the nine bounded cases. The finite program alone does not prove infinitely many instances and is not an independently authored audit.
