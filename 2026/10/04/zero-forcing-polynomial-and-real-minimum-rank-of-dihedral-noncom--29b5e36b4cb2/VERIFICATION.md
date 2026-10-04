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

For each tested \(n\), it constructs \(D_{2n}\) from pairs \((i,\varepsilon)\) representing \(r^is^\varepsilon\), computes the center by direct commutation, and builds the noncommuting graph without using the theorem's decomposition.

It independently constructs the two-dimensional symmetric bilinear witness and checks every off-diagonal zero/nonzero entry against the direct group graph. Exact rational row reduction confirms rank \(2\).

For every tested graph with at most \(14\) vertices, all vertex subsets are exhaustively enumerated. The resulting zero forcing counts have nonzero terms only in degrees \(N-2\), \(N-1\), and \(N\), with the claimed parity-dependent coefficient in degree \(N-2\).

Exact replay output:

```text
n=3: |V|=5, Z=3, min_sets=6, polynomial_terms={3: 6, 4: 5, 5: 1}, rank_witness=2
n=4: |V|=6, Z=4, min_sets=12, polynomial_terms={4: 12, 5: 6, 6: 1}, rank_witness=2
n=5: |V|=9, Z=7, min_sets=20, polynomial_terms={7: 20, 8: 9, 9: 1}, rank_witness=2
n=6: |V|=10, Z=8, min_sets=36, polynomial_terms={8: 36, 9: 10, 10: 1}, rank_witness=2
n=7: |V|=13, Z=11, min_sets=42, polynomial_terms={11: 42, 12: 13, 13: 1}, rank_witness=2
n=8: |V|=14, Z=12, min_sets=72, polynomial_terms={12: 72, 13: 14, 14: 1}, rank_witness=2
VERIFY_OK
```

The exhaustive tests are finite corroboration only. The arbitrary-\(n\) result is proved symbolically by the dihedral commuting relations, explicit rank-two matrices, and the complete classification of all two-white configurations.
