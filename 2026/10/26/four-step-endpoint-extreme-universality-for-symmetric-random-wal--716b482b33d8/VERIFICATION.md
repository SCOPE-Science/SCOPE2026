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

Run `python3 verify.py` from the directory containing the extracted files. The standard-library script checks eight generic ordered rational magnitude configurations by enumerating every one of the \(384\) equiprobable signed orders, testing the strict partial-sum inequalities with exact fractions and comparing each sign-pattern count against the analytic formulas. It reported: `PASS: 48 exact-rational assertions across 8 magnitude configurations; each of 384 signed orders directly enumerated.`

These finite checks are corroboration. The all-laws theorem follows from conditional uniformity of signed orders, explicit counting in the four possible sign words, and cancellation of the two magnitude regimes. No computation for \(n\ge5\) or proof of the all-horizon conjecture is asserted. No external independent audit has been performed.
