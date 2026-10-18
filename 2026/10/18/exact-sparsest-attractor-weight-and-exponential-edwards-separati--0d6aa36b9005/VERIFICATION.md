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

## Reproduction

Run `python3 CHECKER.py` (no third-party packages). The checker derives static coefficients from the cited bivariate generating-function recurrence and checks the initial published counts through length 80, exhaustively tests jammed states for length 4, 8, 12 and 16, and independently enumerates every first-visit order for 4 and 8 sites. It checks exact basin weights 4 and 1120, the uniform-priority probability 1/6 per four-site block, and the exponent/comparator relationship. Actual completed execution: `PASS: 1560 exact finite assertions; permutation weights N=4 and N=8 are 4 and 1120.`

## Logical proof obligations

The analytically required infinite claims are: (a) the published static generating function applies to the padded-zero open-boundary rule, (b) its substitution has no negative occupancy-defect powers and has zero-degree coefficient `1/(1-z^4)`, (c) each target vacancy is rejected if and only if its associated middle pair was visited earlier, and (d) independent within-block priority events factor. The unweighted recurrence with nonnegative coefficients gives the global \((3/2)^n\) comparison by induction. Every step is reconstructed in `RESULT.md`.

## Limits

Finite testing does not establish all-length correctness, priority over the research literature, a full density large-deviation principle, or an independent audit. Published static results and the two smallest dynamical examples remain clearly attributed.
