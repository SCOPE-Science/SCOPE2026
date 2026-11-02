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

# Reproducibility of the finite-field classification

Run `python3 verify.py` from the directory containing this file. Python 3's standard library suffices.

The verifier represents elements of \(\mathbb F_{25}=\mathbb F_5[u]/(u^2-2)\) as pairs of residues modulo five, and constructs multiplication from \(u^2=2\). It independently computes the thirteen-square set and checks agreement with the criterion that a difference is zero or has norm \(1\) or \(4\) modulo five.

It then inspects **every** third-center choice for both possible normalized pair classes, totaling 46 options, and asserts all uncovered-set size frequencies. A separate pass examines every one of the 2300 unordered three-element subsets using the explicitly multiplied squares, not the norm predicate, and directly checks the claimed covering count and nonsquare-difference property. All 300 square-affine transformations of the representative are generated; their image orbit is compared exactly with the 100 computed covering subsets. The proposed order-three stabilizer generator is checked on each representative element.

Actual execution output:

```
VERIFY_OK field=25 total_triples=2300 covers=100 minimum_size=3
pair_census_adjacent= {2: 11, 3: 10, 4: 2} pair_census_nonadjacent= {0: 2, 2: 13, 3: 8}
extensions_per_nonadjacent_pair=2 unique_affine_square_orbit=PASS
all_covering_triples_independent=PASS stabilizer_order=3 norm_square_crosscheck=PASS
```

The exhaustive finite checks are conclusive only because the theoretical square-affine normalization covers **all** unordered center pairs. Neither this program nor any finite enumeration proves a claim about arbitrary larger finite fields. Prior-literature originality has only self-review scrutiny; independent assessment is not performed.
