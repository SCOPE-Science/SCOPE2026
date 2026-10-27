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

# Reproducibility and boundaries

The accompanying `verify.py` is a complete Python 3 standard-library verification program; run `python3 verify.py`. All 65,536 possible orientations of the 16 binary BWT blocks are checked. For each orientation whose LF permutation has a single orbit of length 32, the reconstructed length-32 cyclic word is tested for exactly 32 different length-five factors and for complete BWT agreement.

A distinct graph-based engine recursively enumerates every rooted Eulerian circuit of the binary order-four de Bruijn graph and computes each BWT from sorted full rotations. The two engines agree as complete maps from 2,048 canonical words to run counts. The histogram is `20:38, 22:426, 24:840, 26:608, 28:130, 30:6` (total 2,048). The independent rooted-circuit engine also checks lower orders: `2: {4:1}`, `3: {6:2}`, `4: {10:4,12:4,14:8}`.

All computations use exact integer comparisons. Enumeration is exhaustive because every cycle corresponds to one of the enumerated BWT block orientations, as proved in `RESULT.md`. There is no proof or claim for all higher orders. Independent mathematical auditing has not been performed, and historical priority beyond inspected sources remains open.
