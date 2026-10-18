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
# Verification details

Execute `python3 verify_sparse.py` using Python 3 and only its standard library.

The finite checker implements the displayed normal-form group product and inverse independently of the proof text. It also represents formal products and quotients as triples of (integer variable coefficients, coset indicator, central-involution coefficient mod two), so forced word coincidences can be tested without choosing a group order.

The executed output was:

```
VERIFY_OK symbolic_profiles=150 exhaustive_sets=78050 published_table_checks=5 sparse_exact_matches=7196 collision_examples=4
```

The 150 formal profiles cover all \(2\le k\le16\) and every split into rotation and outside elements. The exhaustive comparison covers all subsets of sizes two through six in the groups \(\operatorname{Dic}_{4n}\) for \(2\le n\le5\). Five source-table entries for \(n=5\), subset sizes two through six, are reproduced. The 7,200 sampled subsets in a much larger group have four incidental collisions; the checker records them rather than treating them as impossibilities.

**Proof dependence.** The asymptotic statement depends on the uniform affine-congruence collision bound and the exact coset-profile probability identity in the mathematical proof. No finite enumeration can establish the universal quantifier in \(n\), and the observed collision count is not used as a theoretical probability estimate.

**Scope.** The computation checks the chosen multiplication convention and asymptotic formula numerators; it does not verify all historical literature, assert an independent proof, or give an explicit crossover index for each fixed subset size.
