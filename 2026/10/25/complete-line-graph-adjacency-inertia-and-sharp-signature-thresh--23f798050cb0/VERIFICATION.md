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

# Verification record

The supplied `verify.py` is a standalone, Python 3 standard-library program. Run `python3 verify.py` in the directory containing this file. It constructs the two-cycle dumbbell for every \(3\le a,b\le10\) and \(1\le d\le8\), forms the complete ordinary adjacency matrix of the line graph, and uses independent exact `fractions.Fraction` arithmetic and symmetric \(1\times1\)/\(2\times2\) pivots to obtain all three inertia indices. There are exactly 512 sampled parameter triples, and the largest graph has 28 line-graph vertices. All triples, their dimensions and the separate closed signature table matched. The checker also asserts explicit endpoint and singular examples.

Expected stdout (also stored verbatim in `verify_output.txt`):

```text
VERIFY_OK exact_line_graphs=512 maximum_edges=28 residue_and_singular_branches=all
```

Exact rational finite checks are corroboration only. The infinite-family statement depends on the congruence proof in `RESULT.md`. This record makes no claim of independent external audit or formal proof assistant certification.
