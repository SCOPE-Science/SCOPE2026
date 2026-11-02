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

# Verification and reproducibility

Run with a standard Python 3 interpreter in a directory containing all three `.py` files:

```
python alt_rank2_types.py > alt_partition_table.tsv
python alt_rank2_fast.py 5 6 7 8 9 > alt_fast_output.txt
python alt_rank2_direct.py 5 6 7 8 > alt_direct_output.txt
```

`alt_rank2_types.py` enumerates cycle partitions, decides permutation parity, the existence of an even square root, and the order-three centralizer condition. This produces the stated category profile for degrees 3–40 and exactly seven signatures in degrees 5–40. The proof of the infinite formula is symbolic in RESULT.md; checking 40 parameters alone would not prove it.

`alt_rank2_fast.py` explicitly enumerates every even permutation for the degrees 5–9, groups first moves by symmetric-cycle conjugacy (valid since conjugation by any symmetric permutation induces an automorphism of the alternating group), and independently tests second-move multiplication patterns for each first move. The last recorded run reports `PASS` for each of those five degrees and a size-7 pointed-type spectrum at degree 9. `alt_rank2_direct.py` independently enumerates all 27 multiplication atoms on the three named elements (identity and two selected group elements) for degrees 5–8. Its results agree exactly with the nine-category reduction wherever those types occur.

The direct computations use no precomputed database, package downloads or external network data. They verify finite cases only; the complete rank-two classification follows from the mathematical group and game lemmas, not from extrapolation. Higher-rank fragments, nonstandard signatures, full external source comparison, and independent validation are not verified.
