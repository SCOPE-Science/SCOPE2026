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

# Verification scope

The analytic proof in `RESULT.md` establishes every claimed statement for all finite positive group sizes and all stated real parameters. The accompanying `verify_contextual.py` can be run from the same directory after installing NumPy and SciPy.

Executed command: `python verify_contextual.py`

Observed output: `VERIFY_OK cases=72 coalitional_constraints=2376 simplex_vertices=360 min_norm_cases=4`

The program checks the least-core excess exactly by rational coalition enumeration, computes optimal excess independently through a full proper-coalition linear program, derives the Shapley value from its factorial-weighted subset formula using rational arithmetic, checks every claimed product-simplex vertex in its tested cases, and compares projected minimum-norm solutions to separate numerical constrained optimization in four cases.

**Boundaries:** LP and minimum-norm optimization use floating-point numerical methods with explicit tolerances; the complete finite sample is not a proof of the universal theorem. No independent scientific audit or external certification is claimed.
