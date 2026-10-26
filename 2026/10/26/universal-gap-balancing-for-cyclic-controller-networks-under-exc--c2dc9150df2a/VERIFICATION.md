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

The bundled `check_cycle.py` builds connected components directly after deletion, independently of the theorem's gap-count calculation, and tests all controller sets and fixed-cardinality failure sets for cycles with 3 through 9 vertices. It checks equality of exact total unserved-vertex counts with the binomial gap formula for every tested instance, checks globally minimal expected losses for balanced gaps, and verifies that fixed failure counts smaller than the controller count have only balanced-gap optimizers. It also verifies the closed discrete-second-difference identity and the two-failure specialization by integer arithmetic through 31 vertices.

Command: `python3 check_cycle.py` from the directory containing this file and the script.

The executable checks provide finite corroboration; they do not prove the theorem for arbitrary cycle order or cardinality. The mathematical proof in `RESULT.md` supplies the general argument. No claims of independently conducted audit or certification are made.
