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

# Verification

Run `python3 verify.py` with Python 3 and SymPy. The program builds the four-dimensional exterior multiplication and all nonzero rank-one tensors satisfying the incidence equation. For fields of size \(2,3,5,7\), it checks the weight-zero Rota–Baxter identity on the entire set of sixteen ordered basis pairs for every candidate, and checks the exact total count. For \(2,3,5\), it enumerates every algebra automorphism and verifies that the six representative conjugacy orbits are pairwise disjoint, exhaustive and of their predicted sizes. It differentiates the local equation \(a\beta+b\gamma=0\) and checks nondegeneracy of the corresponding quadratic form.

Observed output:

```
node_gradient_and_quadratic_rank: PASS
orbit_decomposition: 2 [3, 1, 3, 6, 6, 6] aut 24
orbit_decomposition: 3 [8, 2, 16, 24, 24, 48] aut 432
orbit_decomposition: 5 [24, 4, 96, 120, 120, 480] aut 12000
rank_one_points: 7 3030
VERIFY_OK
```

The mathematical proof, rather than finite enumeration, establishes the claims for arbitrary fields and all finite-field sizes. This check does not test arbitrary higher-rank operators or the nonreduced operator scheme. No independent audit has been performed.
