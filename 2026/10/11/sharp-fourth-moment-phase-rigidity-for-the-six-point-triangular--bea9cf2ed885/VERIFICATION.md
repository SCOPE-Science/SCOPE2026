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

Run `python3 checker.py` with Python 3, requiring only its standard library. The program checks all support differences, confirms six single-pair and three triple-pair shift types, verifies the exact fourth-moment formula by independent pairwise convolution over \(\mathbb Z[\omega]\), exhausts 8 binary and 27 ternary normalized triples, checks the complete equality lists, and tests finite-grid difference injectivity. Direct sampled Fourier sums at grid sizes \((5,5)\), \((5,7)\), and \((7,5)\) provide additional numerical cross-checks; the printed PASS confirms completion.

Exact computation does not prove any assertion for arbitrary continuous phases; that proof is contained in the autocorrelation identity and elementary complex geometry in RESULT.md. The q-phase reachability criterion is algebraic, not an enumeration of every \(q\). All finite grids below order five are outside the theorem. Independent audit has not been performed.
