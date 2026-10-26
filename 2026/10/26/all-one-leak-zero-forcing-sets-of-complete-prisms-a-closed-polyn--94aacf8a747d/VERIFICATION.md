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

# Reproducibility and mathematical verification

The Python 3 standard-library script `verify_leaky_prisms.py` is included in the same package. Run it as `python verify_leaky_prisms.py` from the directory containing that file. It constructs all edges of \(K_n\square K_2\) explicitly from adjacency, checks every subset as a possible starting blue set, and runs the usual unique-white-neighbor color change with each possible vertex independently forbidden from forcing. It then independently computes the full success histogram and inclusion-minimal histogram and compares them to the formulas.

The actual execution returned `ALL_PASS subsets= 21824` for \(n=3,4,5,6,7\); successful complete distributions (listed as cardinality:count) were, respectively: `{3: 2, 4: 15, 5: 6, 6: 1}`; `{4: 2, 5: 32, 6: 28, 7: 8, 8: 1}`; `{5: 2, 6: 70, 7: 120, 8: 45, 9: 10, 10: 1}`; `{6: 2, 7: 132, 8: 270, 9: 220, 10: 66, 11: 12, 12: 1}`; `{7: 2, 8: 224, 9: 532, 10: 560, 11: 364, 12: 91, 13: 14, 14: 1}`. Inclusion-minimal histograms were `{3: 2, 4: 9}`; `{4: 2, 5: 24}`; `{5: 2, 6: 60}`; `{6: 2, 7: 120}`; `{7: 2, 8: 210}`.

The script exhausts precisely those finite instances. It is not evidence for infinitely many graph orders. The general proof derives the necessary initial-force threshold, constructs forcing sequences robust to every single leak, partitions the count into disjoint cases, and confirms minimality with explicit single-deletion obstructions. Literature priority beyond the sources discussed in the result remains uncertain.
