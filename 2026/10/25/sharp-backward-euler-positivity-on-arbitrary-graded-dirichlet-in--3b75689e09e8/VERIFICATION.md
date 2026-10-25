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

# Reproducible checks and limits

Run `python verify_graded_mesh.py` with a standard Python 3 interpreter. The test uses `fractions.Fraction` for all cell lengths, timesteps, assembly and Gaussian elimination. It checks entrywise signs, positivity of every adjacent update coefficient for each positive step, the iff threshold, and explicit two-hop negative witnesses at subthreshold steps.

The script passed 618 exact configurations with 3 through 8 interior nodes. Sampling is not exhaustive and does not prove the general claim; the complete proof appears in `RESULT.md`. Scientific comparisons were conducted against primary literature and public research records, with the missing full 2008 primary text recorded as a residual originality risk.

Independent audit: not performed.
