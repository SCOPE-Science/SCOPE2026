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

# Verification notes

The standalone Python 3 file `verify_translation_fixed_scale2.py` is complete and requires no third-party packages. Run it with `python3 verify_translation_fixed_scale2.py` from the same directory as this document. It directly reconstructs every orbit as a coset and independently evaluates maximum pairwise Hamming distances to determine the entire compatibility graph. It checks every nontrivial admissible binary translation subgroup in dimensions \(2,3,4,5,6\) (respectively \(4,10,20,35,56\) subgroups), for 125 total; it uses explicit coordinates to check rank-one isomorphisms with the appropriate cube and rejects all rank-two edges.

Actual completion output:

```
n= 2 short_subgroups= 4
n= 3 short_subgroups= 10
n= 4 short_subgroups= 20
n= 5 short_subgroups= 35
n= 6 short_subgroups= 56
TRANSLATION_FIXED_RIPS2_VERIFIED 125 nontrivial_subgroups {'rank1_weight2': 35, 'rank1_weight1': 20, 'rank2': 70}
```

The checker also verifies directly that every orbit of any weight-at-least-three translation contains two vertices at forbidden distance. It does not constitute an exhaustive verification over all dimensions, nor does it independently reproduce a global literature search. The mathematical proof is the orbit-simplex lemma, rank-two classification and exact coset-distance calculations given in `RESULT.md`. The abstract-only 2019 reference is an acknowledged originality risk; independent scientific validation has not been performed.
