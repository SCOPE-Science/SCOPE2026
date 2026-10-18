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
# Reproducibility and verification

Run `python3 rook_2_independence_verify.py` to rebuild all six complexes, check all 9,216 Hasse covers for the last case, construct exactly 1,120 matched pairs there, prove acyclicity, count all critical cells and evaluate exact signed integral Morse differentials. Its complete expected output is `rook_2_independence_verify.out`.

Run `python3 rook_homology_crosscheck.py` to rebuild faces separately using row/column population tests and reduce all mod-two boundary matrices in every one of the six cases. Its complete expected output is `rook_homology_crosscheck.out`. Both programs use the Python standard library only and have no file dependencies beyond their own source text.

The critical step not established by a field computation alone is the integral vanishing of every Morse differential, including seven degree-four-to-degree-three boundaries in the last case. The first program performs that step using only exact signed integers and the explicit full matching. Hurewicz then upgrades the vanishing degrees to null attaching maps in the relevant dimensions. The finite enumeration proves nothing about board widths greater than six. Publication or independent review is not implied.
