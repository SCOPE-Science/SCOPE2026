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

## Reproducibility

Run `python3 verify_skew_prism.py` with a standard Python 3 interpreter. The program independently generates prism adjacency, computes skew forcing closure from every two-vertex seed for each odd length from five through nineteen, and constructs both reconfiguration graphs directly from exchanges or slides. It checks precise component-size distributions, connectedness, orders, edge counts and degrees. It also verifies every individual force in the two-front construction for odd lengths five through 299. The required terminal markers are `VERIFY_OK` and `CONSTRUCTIVE_CERTIFICATES_OK`.

## Limits

These experiments independently stress-test the statement only over finite ranges; the infinite conclusions rest on the fully written proof in RESULT.md. No external or independent audit is represented by the tests.
