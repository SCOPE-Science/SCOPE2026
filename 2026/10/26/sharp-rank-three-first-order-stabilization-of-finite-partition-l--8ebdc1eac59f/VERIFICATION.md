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

# Reproducibility and scientific verification

Run `python3 verify_partition_lattices.py` in a directory containing the embedded script. It requires only the Python standard library. The captured successful run is `verification_output.txt`.

The program enumerates all partitions for ground-set sizes 1 through 8 as canonical restricted-growth words. It reconstructs refinement directly from equivalence-pair masks, independently produces the structural two-point extension table, and compares each predicted comparison pattern with actually realized third-partition patterns for **every** ordered pair through size seven. It performs a fixed-seed sample of 50,000 ordered pairs at size eight. It then computes all one-variable rank-two logical types via exact sets of comparison patterns for each integer-partition shape at every size through eight, obtaining exactly seven sentence-level rank-three types, stabilizing from seven to eight. A separate parameter-set calculation agrees with the seven saturated pairs up to 300 ground points.

The mathematical proof in `RESULT.md` covers all ground-set sizes and supplies complete separating rank-three formulas. The checker corroborates rather than replaces the infinite proof. It does **not** exhaustively check all 17,139,600 ordered pairs at size eight, and the tests up to size 300 alone do not establish infinite stabilization. No formal mechanized proof or independent external mathematical audit is claimed.
