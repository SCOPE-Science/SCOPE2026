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
# Verification of the binary dimension-five three-read construction

Run `python3 verify_code.py` using Python 3.8 or later. All data needed to reproduce the result, including the ordered twenty columns, are in `RESULT.md` and in the standalone script.

The script enumerates all \(2^5=32\) messages, verifies full rank using distinct outputs, computes all \(31\) nonzero three-window weights, checks the exact weight distribution, checks the twenty sets of nonzero messages annihilating each consecutive three-column block, and tests equality in both bounds. Output on the checked source: `VERIFY_OK binary_linear=[20,5] min_3_symbol_distance=18 zero_triple_distribution= {0: 1, 2: 30} total_zero_triples= 60 all_cyclic_column_triplets_rank=3 Griesmer=140=7*20`.

The mathematical upper bound for **all** codes in the stated class is given by a separate universal double-counting proof in `RESULT.md`, not extrapolated from the enumerated finite witness. No statement about generator uniqueness, nonlinear codes, or independent certification follows from these checks.
