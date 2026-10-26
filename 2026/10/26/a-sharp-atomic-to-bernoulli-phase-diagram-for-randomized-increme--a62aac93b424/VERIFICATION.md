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

Run `python verify_clipped_ripm.py` with a standard Python 3 interpreter. The standalone program uses only built-in `fractions`, `itertools`, and `random`; no network or external package is required. It compares independent subgradient proximal constructions to the stated clipped formulas over rational parameter grids, checks their interval invariance and contraction, the least constant-sign reset length, the infinite alternating orbit formula through finite prefixes, and exact finite Bernoulli-sum moments. Seeded bounded simulations supply additional regression coverage. Expected successful output: `PASS: 131832 exact-rational and finite numerical assertions`.

The proof in RESULT.md establishes the infinite claims using synchronous coupling, almost-sure occurrence of finite sign words in a bi-infinite independent sequence, and a maximum-atom contradiction. Numerical testing does not certify absence of atoms, Hausdorff dimension, or bibliographic originality. Independent verification has not been performed.
