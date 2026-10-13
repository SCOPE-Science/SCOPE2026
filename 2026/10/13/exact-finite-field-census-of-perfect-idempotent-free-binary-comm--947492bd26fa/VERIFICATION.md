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

# Reproducible checks

The included `verify.py` exhaustively tests every symmetric multiplication table of dimension two over prime fields of orders 3 and 5, evaluates all rational projective eigendirections, counts the idempotent-free rank-two tables by cubic-factorization stratum, and checks the general count. Execute `python3 verify.py`. Verified output: `F_3 perfect=624, ... 144,72,16` and `F_5 perfect=14880, ... 4000,1200,96`; final `VERIFY_OK`. The infinite family follows from the self-contained proof, not these experiments. Independent audit has not been performed.
