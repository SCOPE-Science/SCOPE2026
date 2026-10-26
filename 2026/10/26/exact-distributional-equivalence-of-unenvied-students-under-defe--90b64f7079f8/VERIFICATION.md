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

# Reproducibility and limitations

Run the accompanying standalone `verify.py` using Python 3 and only the standard library. It enumerates all independent uniform student-preference profiles under serial dictatorship for \(n=1,2,3,4\), and all independent uniform preferences and school-priority profiles under student-proposing deferred acceptance for \(n=1,2,3\). It checks those distributions against an independent exact-rational dynamic program for the coupon-collector singleton law, and checks every joint indicator subset and the telescoping product formula through \(n=8\).

On the completed execution, 331,997 RSD profiles and 46,673 DA profiles were examined across the respective ranges, with 551 additional exact-rational assertions passing. At \(n=3\) the common count probabilities for counts 1,2,3 are \(7/18,7/18,2/9\). At \(n=4\), RSD and coupon singleton count probabilities for counts 1,2,3,4 are \(97/288,97/288,67/288,3/32\).

The finite checks are independent corroboration, not an infinite proof. The theorem for all positive \(n\) is established by the analytic joint-inclusion argument in RESULT.md. No independent audit was conducted. Generalization to correlated or nonuniform preferences, unequal quotas, or fixed-profile equality is neither tested nor asserted.
