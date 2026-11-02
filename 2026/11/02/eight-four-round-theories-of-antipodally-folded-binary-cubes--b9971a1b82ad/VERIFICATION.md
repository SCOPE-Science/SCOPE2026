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

# Verification procedures and limits

Execute `python3 folded_rank4_verify.py` from the directory containing the script. The code is standalone Python 3 and uses standard-library `functools` and `itertools`. Its output should match `folded_rank4_verify.out` byte-for-byte. The symbolic stage enumerates **every** profile extension and computes all pair equality/adjacency relations for every ordered four-tuple profile; it covers all dimensions from two to sixteen inclusive. A logically independent direct graph-vertex recursion confirms the exact root types for dimensions two to seven inclusive. The final status strings are `EIGHT_CLASSES_AND_FINITE_BOUNDARY_OK` and `VERIFY_OK`.

The infinite upper tail is **not** established by a finite run. It is established in the proof by the exact cellwise binary splitting lemma: truncated-at-sixteen one-cell profiles yield a four-round Duplicator strategy. The finite program is needed only for the boundary and sharp separation. No exhaustive test of higher quantifier rank, counting-logic extensions, independent peer review, or historical uniqueness has been undertaken.
