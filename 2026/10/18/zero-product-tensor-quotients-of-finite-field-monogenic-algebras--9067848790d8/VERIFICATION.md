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

Use `python3 verify.py`. The checker exhaustively enumerates every ordered pair of elements of each stated small prime-field quotient; it forms zero-product pure tensors, computes their span over the prime field, and compares the quotient dimension with the predicted sum of quadratic jet lengths. The script is included unchanged with this report.

Observed result: `VERIFY_OK 14 exhaustive configurations` (all configurations passed). Tested polynomial degrees range from one to four; prime characteristics are two, three, and five. The characteristic-two configurations validate only the zero-product tensor quotient, not the zero-Jordan-product interpretation. The nontrivial quadratic residue extension and repeated quadratic factor tests are included.

The general proof uses a separable coefficient-field lift, valuation of product in truncated polynomial local rings, and finite-field Galois decomposition. None of these infinite assertions is inferred from exhaustive checks of small cases. Source novelty search cannot prove absence of unindexed equivalent results. Independent validation has not been performed.
