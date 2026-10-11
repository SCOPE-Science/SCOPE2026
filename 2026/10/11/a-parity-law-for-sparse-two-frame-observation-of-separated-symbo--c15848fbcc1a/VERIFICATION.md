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

# Proof and computation checks

The theorem concerns all integer sensor separations \(d\geq1\). Its proof is analytic and uses the exact equivalence of winning schedules with translates covering the integers, two separate lower bounds, and two explicit matching periodic constructions.

Execute `python3 check_observation.py` using standard Python 3. It checks exact residue coverage, rational densities, and the finite local two-incidence inequality for \(1\leq d\leq500\). The checker is not a proof beyond the tested range; Steps 1–4 of `RESULT.md` supply the universal argument. No external solver, third-party data, or stochastic experiment is needed.

The publication comparison was based on accessible abstracts and the detailed public introduction of the motivating source; its remaining full-body novelty risk is recorded in `REVIEW.md` and `AUDIT.json`. There has been no independent audit.
