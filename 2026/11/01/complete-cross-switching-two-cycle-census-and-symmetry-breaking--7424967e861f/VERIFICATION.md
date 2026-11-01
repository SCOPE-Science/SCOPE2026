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

The executable `check.py` is embedded in the same record. With Python and SymPy installed, execute `python check.py` to reproduce exact symbolic identities, root intervals over rational sample parameters, critical-parameter algebra, orbit substitutions, and local-stability examples. The executed program printed `SYMBOLIC_IDENTITIES_OK`, `EXACT_RATIONAL_ROOT_COUNTS_OK`, `LOCAL_STABILITY_SAMPLES_OK`, and `NONSYMMETRIC_CYCLE_IDENTITIES_AND_COUNTS_OK`. Mathematical statements quantified over real parameters are established by the analytical monotonicity proof in RESULT.md; rational sample tests are not exhaustive verification. Independent audit is not yet performed.
