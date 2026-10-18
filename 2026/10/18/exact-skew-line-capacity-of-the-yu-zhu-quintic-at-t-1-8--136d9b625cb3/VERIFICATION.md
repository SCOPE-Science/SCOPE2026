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

# Reproducible exact checks

Execute `python3 artifacts/verify_skew_capacity.py` with Python 3 and only its standard library, from the directory containing this file. The checker constructs the complete stated list of 85 projective lines in the explicit 32-dimensional rational coefficient basis, rather than importing an adjacency matrix or relying on floating-point zero decisions. It verifies 3,570 determinant tests, the 850-edge 20-regular incidence graph, the 530/320 adjacent-pair common-neighbor census, the 18-line witness, a 19-clique cover of all 85 vertices, and a 65,536-choice eight-block obstruction to any 19-line skew family. A separate exhaustive bitset branch-and-color search excludes a skew set of 19, using 2,575 recursive nodes.

Successful output ends with `YU_ZHU_85_SKEW_MAXIMUM_EXACT_OK`. No third-party software or paper data download is needed to run the checker. All arithmetic identities are exact in the displayed algebraic field, contingent on the stated field-basis justification. The source's theorem that the 85 listed lines are all lines on the named smooth quintic is relied upon, not independently certified by the checker. Neither the proof nor the computational verification addresses other parameter values, and no independent audit has been performed.
