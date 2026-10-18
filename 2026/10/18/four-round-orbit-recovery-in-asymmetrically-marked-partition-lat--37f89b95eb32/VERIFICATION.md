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

Two standalone scripts, `verify_refinement.py` and `verify_orbit_formula.py`, require Python 3 only. Run each script directly; neither uses external datasets.

`verify_refinement.py`: 9 asymmetric two-block anchors for total sizes 3 through 7, involving 3,161 partition-vertex instances, all matching stabilizer-orbit profiles, with maximum stabilization round 3 in the tested cases. Expected final marker: `VERIFY_REFINEMENT_OK 9 3161 3`.

`verify_orbit_formula.py`: 12 asymmetric anchors for total sizes 3 through 8, involving 15,581 partition-vertex instances, matching exact orbit counts, class sizes, and Bell totals; all tested binomial-moment signatures were injective. Expected marker: `VERIFY_ORBIT_FORMULA_OK 12 15581`. Additional computed orbit counts: \(N(6,4)=323\), \(N(7,3)=257\), \(N(8,2)=181\), \(N(9,1)=97\), \(N(7,4)=522\).

The scripts verify finite instances and formulas; they do not serve as an exhaustive verification of the infinite-domain theorem. The mathematical derivation is in RESULT.md. No independent scientific audit has been performed.
