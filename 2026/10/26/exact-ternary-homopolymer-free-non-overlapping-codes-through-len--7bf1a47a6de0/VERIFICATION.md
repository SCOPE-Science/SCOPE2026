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
# Reproducibility

Execute `python3 check.py` in the directory containing this file. The script uses only the Python standard library. It independently performs an ordered bitset exhaustive clique search and a pivoted Bron–Kerbosch enumeration, compares all maximizing codebook sets, verifies every ordered prefix/suffix pairing in all optima, and computes global-alphabet-permutation/reversal orbits. The final line must be `TERNARY_RUN_ONE_NONOVERLAP_PASS`.

It verifies the optimum sequence at lengths two through nine as `2 2 2 4 5 8 16 24`, with exactly 12 maximum length-nine codebooks split into two orbits of size six. The independent maximal-clique algorithm enumerates 121728 maximal cliques at length nine. Explicit representatives are available in `OPTIMA_N9.txt`. The strict upper-bound pruning rule cannot remove a tied or improved optimum, and the independent search verifies exhaustive coverage.

This is an exact finite computational proof, not evidence that the same pattern persists beyond length nine. There is no proof or experiment here for larger alphabets, longer codes, or different maximum run length. Bibliographic originality remains subject to external verification.
