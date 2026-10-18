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

The self-contained `verify.py` program uses exact rational arithmetic to exhaustively enumerate positive-implicativity evaluations on all finite standard BCK chains of orders 2 through 50. It returns `VERIFY_OK`, verifies the smallest violating chain has order 3 and precisely one violating pair, and checks the quantified lower bound on every sampled violating chain. The proof for arbitrary chains and arbitrary equations is the interval-counting argument in `RESULT.md`, not the finite computation. No external independent audit or certification has been performed.
