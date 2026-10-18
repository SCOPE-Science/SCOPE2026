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

# Verification

Run `python3 verify.py` with Python 3 and the standard library. The script constructs exact factorial-weight low-tail polynomials from ordered vectors of independent Poisson observations, for every sample size from three to six and all interior retained ranks. It verifies the closed-form low tails, the signed ultra-log-concavity defect, and local ordinary-log-concavity signs at seven rational intensities. It separately checks the published maximum-rank ultra-log-concavity inequalities for finitely many rational intensities and indices.

Observed execution: `PASS: 346 exact checks on polynomial coefficients, ULC defects, and local LC signs`. The finite enumerations do not prove the unbounded sample-size or intensity statements. Those follow from the exact combinatorial event partition and analytic root argument in RESULT.md. The maximum endpoint relies on the cited independent published mathematical theorem. No external independent audit is claimed.
