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

Execute `python3 verify_ut5_square_fibers.py` using Python 3.10 or later and no third-party modules. The finite field implementation uses bit-polynomial representations of \(\mathbb F_2,\mathbb F_4,\mathbb F_8\), with irreducible moduli `0b11`, `0b111`, and `0b1011`, respectively. The routine `matrix_square` literally multiplies each relevant pair of entries in the five-by-five matrix instead of calling the prediction function. The independent `predicted` function implements the proved target rules.

Complete enumeration for \(q=2\) and \(q=4\) checks all \(q^6\) targets and all \(q^9\) nontrivial input coordinates, including the multiplicity \(q\) of the free top-corner coordinate. The checker compares the complete distribution with the five-size histogram, the image polynomial and the group-size checksum. The \(q=8\) tests use an independent seven-coordinate enumeration at nine representative prescribed targets, together with 2,000 seeded sample squares.

Observed output:
```
GF 2 EXHAUSTIVE_OK group_size 1024 image 52 histogram [(8, 24), (16, 22), (48, 4), (96, 1), (192, 1)]
GF 4 EXHAUSTIVE_OK group_size 1048576 image 3376 histogram [(192, 2880), (768, 468), (3840, 24), (9216, 3), (16384, 1)]
GF 8 POINTWISE_OK 9 targets + 2000 direct-square samples
ALL_EXACT_CHECKS_PASSED
```

These tests are finite checks; correctness at arbitrary \(q=2^f\) follows from the rank-factorization and elimination proof, not extrapolation. Independent mathematical validation has not been performed. Historical-priority uncertainty remains as described in the manuscript.
