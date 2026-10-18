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

# Reproducible verification

Two complete independent replays were run: `python3 verify_t8.py` and `c++ -std=c++17 -O3 verify_t8.cpp -o verify_t8 && ./verify_t8`. Both returned `VERIFY_OK`, generated all \(6880\) tournament classes, and agreed on all \(26\) Betti profiles with the frequencies in `spectrum.csv`. Generation proceeds recursively from a one-vertex tournament, not from an imported table. Integer chain reductions use unimodular unit-pivot Schur complements and check every final residual is zero. A six-vertex projective-plane triangulation positive control was detected as nonunit/torsion-bearing by the Python implementation.

The use of exact integer arithmetic proves the finite integral homology calculations once the transparent algorithms are replayed; it does not prove any infinite-order extension. The reported results have not undergone an independent mathematical audit. Code and counts are supplied as reproducibility materials, not as claims of external certification.
