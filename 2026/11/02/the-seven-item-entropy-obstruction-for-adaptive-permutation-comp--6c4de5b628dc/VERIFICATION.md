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

The package contains `permutation_witnesses.json`, `make_cert.py`, `verify.py`, `poset_upper.py`, `verify_bitset_upper.py`, and `verification_output.txt`. All scripts use only Python 3 standard-library modules and exact integers. To replay from the same directory:

```
python3 verify.py
python3 poset_upper.py
python3 verify_bitset_upper.py
```

`verify.py` independently enumerates the entire permutation concept class for each order from two through seven and traverses all levels of every explicit adaptive decision tree. It checks query pair ranges and orientation, both child restrictions, leaf permutations, agreement with every path answer, no repeated leaf witness, and the exact number of leaves. It also uses the hypothesis-count bound to close the upper cases through six elements. The seven-item witness is a complete tree of depth eleven with 2,048 distinct leaf orders and 2,047 internal pair queries.

`poset_upper.py` checks an independently represented seven-item problem via transitive-closure predecessor masks and an exhaustive dynamic program for the exact number of linear extensions of each partial-order state. It tests all incomparable comparisons and both possible replies. One depth-eleven continuation of a single fixed initial comparison is impossible. Permutation-label symmetry turns this into a universal depth-twelve obstruction.

`verify_bitset_upper.py` independently enumerates all 5,040 permutations, represents restrictions as bitsets, and searches every pair query recursively. It confirms depth eleven is possible and depth twelve impossible. The computations returned 16,587 memoized search states for the conditioned poset checker, 37,565 linear-extension-count states, and 74,797 bitset search states. These are state counts of complete algorithms, not random samples or infinite statements.

The theorem's extension to arbitrary multiples of six is proved deductively by grafting the finite depth-nine six-element witness into pairwise disjoint label groups; no numerical extrapolation is involved.

Scope: no independent scientific audit was performed. Verification does not establish novelty against inaccessible or unsearched literature. The included plain-text output records successful runs of these exact files.
