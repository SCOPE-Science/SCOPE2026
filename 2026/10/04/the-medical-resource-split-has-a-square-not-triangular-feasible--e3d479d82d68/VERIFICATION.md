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

`verifier.py` uses `fractions.Fraction` only. It checks the two reported within-stratum ratios exactly as terminating decimals, verifies that their first coordinates sum to \\(1.4399>1\\), and verifies that each pair sums to one. It then inserts each orientation of the reported top-level pair \\(0.4479:0.5521\\) into the four-share allocation map; all four shares are nonnegative and sum exactly to one.

The general identity
\[
\\sigma\\alpha_1+\\sigma(1-\\alpha_1)+(1-\\sigma)\\alpha_2+(1-\\sigma)(1-\\alpha_2)=1
\]
is proved symbolically in `RESULT.md`; the finite exact replay only checks the source's numerical witness. The minimax identity on \\([0,1]^2\\) is likewise proved by a lower-bound-and-attainment argument, not by enumeration.

Limits: the verification does not recompute the source's epidemiological parameter fitting, does not optimize an endogenous \\(\\sigma\\), and does not claim global optimality for a state-coupled control horizon.
