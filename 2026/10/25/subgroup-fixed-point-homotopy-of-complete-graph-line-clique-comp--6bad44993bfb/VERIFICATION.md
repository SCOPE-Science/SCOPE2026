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

The theorem is proved combinatorially in `RESULT.md`: orbit-simplex realization, classification of pairwise-intersecting edges, homotopy nerve and attaching-loop arguments, then a spanning-tree calculation of circle summands. The proof holds for every integer \(n\ge4\) and every subgroup \(H\le S_n\).

Run `python3 verify_fixed_line.py` to independently reconstruct geometric fixed-point complexes for 190 tested subgroup-generator configurations. The checker constructs the generated finite group, partitions label and edge sets into orbits, filters orbit-vertices to pairwise-intersecting edge families, enumerates the resulting flag complex, and computes every mod-two boundary rank using binary elimination. It checks reduced Betti numbers, including the empty-space case. This finite verification is neither an infinite-parameter proof nor an independent external audit.

Primary literature comparison: Goyal–Shukla–Singh, arXiv:2009.12130, Section 3, provides ordinary homotopy equivalence for line-clique complexes, but the fixed-point statement proved here requires additional orbit-level arguments.
