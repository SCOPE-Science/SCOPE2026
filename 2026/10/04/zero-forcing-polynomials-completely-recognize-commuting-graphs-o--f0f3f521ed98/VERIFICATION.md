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

The standalone `verify.py` artifact was read from its packaged path before replay.

It constructs five finite groups directly from multiplication:
\[
S_3,\quad D_8,\quad D_{10},\quad D_{12},\quad Q_8.
\]
For each group it computes the center and every noncentral centralizer, verifies that all such centralizers are abelian, removes duplicate centralizers, and checks that the sets
\[
C_G(g)\setminus Z(G)
\]
partition the noncentral elements into complete connected components.

It then exhaustively tests every vertex subset for zero forcing and compares the resulting coefficient dictionary with the factorized polynomial. The minimum-set count is checked independently.

Finally, a block all-ones matrix is built on every nontrivial clique component and a zero block on every singleton component. Exact rational row reduction confirms the claimed witness rank, and its off-diagonal pattern is checked entry-by-entry.

Exact replay output:

```text
S3: profile=[1, 1, 1, 2], |V|=5, Z=M=4, mr=1, min_sets=2, polynomial={4: 2, 5: 1}
D8: profile=[2, 2, 2], |V|=6, Z=M=3, mr=3, min_sets=8, polynomial={3: 8, 4: 12, 5: 6, 6: 1}
D10: profile=[1, 1, 1, 1, 1, 4], |V|=9, Z=M=8, mr=1, min_sets=4, polynomial={8: 4, 9: 1}
D12: profile=[2, 2, 2, 4], |V|=10, Z=M=6, mr=4, min_sets=32, polynomial={6: 32, 7: 56, 8: 36, 9: 10, 10: 1}
Q8: profile=[2, 2, 2], |V|=6, Z=M=3, mr=3, min_sets=8, polynomial={3: 8, 4: 12, 5: 6, 6: 1}
VERIFY_OK
```

These finite checks corroborate the group-to-graph decomposition and the parameter formulas. The general theorem follows from the published AC-group clique decomposition and the componentwise proofs in `RESULT.md`.
