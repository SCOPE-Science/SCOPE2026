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

`python3 verify.py` checks the explicit word-graph adjacency, all three conditions (selected weight, outside domination, and one-limitedness), four local boundary states, all 64 assignments of four local states across the three order-four blocks, and seeded higher-order products. It also tests balanced-state/matching counts. Successful replay: `BASEWISE_EXHAUSTIVE 2 4`, `BASEWISE_EXHAUSTIVE 3 8`, `FOUR_BOUNDARY_STATES_OK 4`, `BLOCK_PRODUCTS_OK 3 4`, `BLOCK_PRODUCTS_OK 4 64`, `RANDOM_BLOCK_PRODUCTS_OK 5 25`, `RANDOM_BLOCK_PRODUCTS_OK 6 10`, `FOUR_STATE_VERIFY_OK`. These are finite checks. The proof of the all-order theorem appears in `RESULT.md`. Historical priority and independent external validation remain open.
