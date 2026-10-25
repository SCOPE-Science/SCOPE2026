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

The attached `verify.py` tests the theorem with Python's standard library alone. Run `python verify.py` from the directory containing that file. It enumerates every binary factor and evaluates closedness by an independent occurrence-count definition, compares the entire resulting closed-factor set with the explicit family classification for all 3125 positive parameter five-tuples having entries at most five, checks the exact construction for 500 scales, and separately enumerates small-length extrema. The recorded successful output was:

`VERIFY_OK parameter_tuples= 3125 scaled_witnesses= 500 M5_n5_to_n14= [7, 8, 11, 14, 16, 20, 23, 26, 31, 34]`

The checked sets are finite. The general exact formula, asymptotic bound, and rigidity are established by the run/border argument and the algebraic defect identity in RESULT.md. No independent audit was performed.
