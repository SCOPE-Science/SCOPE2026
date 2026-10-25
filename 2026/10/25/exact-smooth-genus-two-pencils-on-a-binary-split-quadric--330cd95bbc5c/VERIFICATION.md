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

The symbolic criterion uses four affine charts of the split quadric. For each of the 4095 nonzero binary (2,3)-forms, the local polynomial and two partial derivatives generate the unit ideal if and only if the corresponding chart has no geometric singular point. `gf2_ideal.py` implements exact GF(2) Buchberger reduction and yields 1116 smooth sections. An independently written SymPy Gröbner implementation agreed mask-by-mask across the entire space.

`enumerate_pencils.py` enumerates all triples of distinct nonzero forms arising from two-dimensional vector subspaces, tests all three for geometric smoothness, computes all nine rational point evaluations, and partitions the 44070 qualifying pencils under all 36 ruling-preserving projective transformations. Its output agrees with `COUNTS.json`; the deterministic `ORBIT_REPRESENTATIVES.csv` has 1242 representatives whose orbit sizes sum to 44070.

`verify_walsh.py` recomputes all smoothness flags and uses additive Fourier transforms to count satisfying triples. Summing over prescribed rational base-point subsets of sizes 0 through 4 yields binomial moments 44070, 62820, 28512, 3696, and 0. Inversion independently reproduces all four rational-base distributions and proves that the fourth and higher strata are empty.

No calculation enumerates arbitrary algebraic extension fields as a surrogate for geometric smoothness. The computation does not determine multiplicity partitions of the full degree-12 geometric base scheme, and the orbit catalogue is relative to the polarized split quadric rather than abstract curve moduli.
