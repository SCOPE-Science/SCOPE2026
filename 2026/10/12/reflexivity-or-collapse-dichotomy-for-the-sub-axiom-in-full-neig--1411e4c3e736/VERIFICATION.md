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

# Verification details

The finite verifier `verify_sub_dichotomy.py` implements the full three-modal semantic clauses directly on every valuation and product world. Its input sets are every principal normal filter on a labeled finite carrier, including improper filters. It compares direct sub validity to the global T/T-or-improper/improper prediction. Complete rows checked:

| Carrier sizes | Frame pairs | Valid sub pairs | T/T pairs | Improper/improper pairs |
| --- | ---: | ---: | ---: | ---: |
| \((1,1)\) | 4 | 2 | 1 | 1 |
| \((1,2)\) | 32 | 5 | 4 | 1 |
| \((2,2)\) | 256 | 17 | 16 | 1 |
| \((2,3)\) | 8192 | 257 | 256 | 1 |

Reproduce with `python verify_sub_dichotomy.py`; the run terminates with `VERIFY_OK` and no assertion failures. A code-free proof covers arbitrary infinite and finite factors: improper/proper separation by the empty valuation, nonreflexivity separation by rectangle witnesses, propagation across coordinate pairs, and counting of finite principal generators. No extrapolation from finite tests is used.

An external independent audit has not been performed; no third-party certification is asserted.
