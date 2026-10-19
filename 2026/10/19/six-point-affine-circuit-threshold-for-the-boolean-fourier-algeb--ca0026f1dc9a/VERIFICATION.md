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

# Reproducibility and limits
The file `checker.cpp` is a standalone C++17 program. From the directory containing it, run `g++ -O2 -std=c++17 checker.cpp -o checker` and `./checker`. It calculates exact integer Walsh coefficients and binary affine ranks for **all** subsets with sizes one to six in dimensions three, four, and five. The checker compares every instance to the closed classification and independently counts all six-element cases. It prints `CHECK_PASS` on success. There are no random inputs, floating-point tolerances, external data, or undocumented dependencies.

For dimensions three, four, and five respectively, the six-element histograms with norms ordered \(3/2,7/4,15/8,9/4\) are \((28,0,0,0)\), \((840,6720,0,448)\), and \((17360,416640,444416,27776)\). These are finite exhaustions, **not** a proof that every dimension is covered. The dimension-general result instead follows from exhaustive affine-dependence alternatives, four explicit Walsh histogram identities, and symbolic counts of affine flats and independent tuples; those arguments are written out in `RESULT.md`.

The review is same-model only. No independent examination or broader exhaustive historical-table search is claimed.
