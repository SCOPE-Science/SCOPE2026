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

The analytic proof in `RESULT.md` establishes the claim for every \(0<p<1/2\) and integer \(m\ge1\). The computational check is supplementary.

`verify.py` solves, by exact rational Gaussian elimination, the finite first-hit and mean-duration recurrences for several rational \(p\) values and thresholds. For cases where \(\sqrt{p(1-p)}\) is rational, it also solves the stopped-record coherence recurrence exactly and compares it with \(2\sqrt{p_m(1-p_m)}\). The script checks the induced disturbance/frontier identity and prints `VERIFY_OK`.

The computation samples parameters and therefore is not an infinite proof. The general proof uses the exact gambler's-ruin equations and proportionality of all terminal-path Kraus operators. No claim is made for asymmetric detectors, noncommuting measurement steps, or arbitrary stopping regions.
