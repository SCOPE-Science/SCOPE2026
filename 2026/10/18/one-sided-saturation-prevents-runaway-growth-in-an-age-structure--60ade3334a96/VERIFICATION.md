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
# Verification and scope

The file `verify.py` runs with Python 3 and no external dependencies. Execute `python verify.py` from the directory containing that file. Its exact-rational tests cover the cancellation \(bc-qK=bc/2\) and the scalar dissipative inequality on a finite grid; randomized parameter tests check the derived aggregate differential estimates for admissible positive parameters.

The analytic proof in `RESULT.md`, not these finite checks, establishes the theorem for all stated initial conditions and parameters. The critical non-computational steps are the characteristic survival inequality over one maturation interval, comparison-based prey bound, and globally dissipative functional \(x+qP\). No numerical simulation can replace these inequalities. Global bounded age mortality and positive starvation mortality are substantive premises; neither is inferred from computations. Independent audit and independent validation have not been performed.
