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

# Reproducibility and certification boundaries

The included `verify_weighted_path.py` uses exact rational arithmetic and the Python standard library only. Run `python verify_weighted_path.py`; it checks sample intertwining identities, the characteristic polynomial, opposite strict signs of the switching function at rational endpoints, a certified exponential remainder, and an upper bound forcing the middle-edge time derivative negative at the switch. The three-exponential zero-count argument, Perron analysis and positive-matrix equality cases are proved in `RESULT.md`, not delegated to finite testing. The numerically displayed peak times are illustrative. The self-review passed; independent audit has not been performed.
