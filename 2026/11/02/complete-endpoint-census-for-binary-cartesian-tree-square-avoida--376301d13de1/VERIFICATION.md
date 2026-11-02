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

# Exact finite verification

Run the included, standalone Python 3 programs:

```
python3 cartesian_enumerate.py
python3 parent_distance_check.py
```

The first implements the recursive leftmost-minimum tree definition; the second uses the separate monotone-stack parent-distance representation and the equivalence theorem of Park et al. Both independently enumerate all binary prefixes satisfying avoidance of Cartesian-tree-matching adjacent halves of length at least \(3\). Both printed the same counts at every length \(1\) through \(30\), finishing with \(56,20,0\) at lengths \(28,29,30\). Both printed the identical SHA-256 of the ordered list of \(20\) maximum-length words:

```
fa7a68bf7155a80ca632847616541706160392ee2d4492e90c3310f1787da79a
```

The two end-of-run markers are `CARTESIAN_ENUMERATION_OK` and `PARENT_DISTANCE_CHECK_OK`. The recorded outputs are `tree_run.txt` and `pd_run.txt`. The certificate `extremal_words.txt` contains the \(20\) words (one per physical line) and `variable_patterns.txt` records their eight variable positions under the fixed template. No sampling, external package, or precomputed lookup table is used by either enumerator.

**Limits.** These checks prove an exact finite statement by exhaustive recursive exploration, conditional on standard Python execution and the Cartesian-tree definition. They do not certify claims about alphabets larger than two or about generalized squares with a different minimum half-length, and they do not constitute independent external mathematical review or priority certification.
