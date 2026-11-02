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

# Verification and limitations

The result is a symbolic exact theorem about six parties in three distinct lower-quota pairs with strictly ordered residues and three extra seats. Seven inversion-free count patterns are exhaustive. The four necessary/sufficient inequalities follow from the nonnegative all-singleton mass and the Hall inequalities for a three-row off-diagonal transportation network. Every feasible table has an edge-extremal version with at most five nonzero transportation arcs. In the rational witness the complete flow interval is \([-2,1]\), and each endpoint has exactly one zero entry; hence at least five arcs plus the positive all-singleton mass are unavoidable.

Run `python3 verify.py` using Python 3 without third-party packages. An exact-arithmetic replay performed for the packaged source printed:

```
VERIFY_OK grid_profiles=18169 feasible=7854 infeasible=10315 zero_envy_patterns=7 sharp_support=6 support_interval=[-2,1]
```

The script independently implements integral max-flow and compares it with the symbolic inequalities on 18,169 integer-grid profiles, including some tied-residue boundary profiles for which it tests the **fixed-priority inversion-free extension**, not literal envy equivalence. The claimed literal zero-envy classification assumes strict within-pair inequalities. Finite enumeration does not prove the all-real theorem. The full primary literature and all possible implicit corollaries have not been exhaustively ruled out, and no independent scientific audit has occurred.
