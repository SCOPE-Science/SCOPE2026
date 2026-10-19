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

# Verification and limitations

The proof covers all real \(\alpha>\beta>0\) and all integers \(m\ge1\). It uses only binomial conditioning, beta-integral identities, and dominated convergence. The even-increment formula has a strictly positive coefficient \(m(\alpha-\beta)+\alpha+2m+1\); the density-reflection argument proves the limit exceeds individual accuracy. Exact summation gives the first strict-even improvement at ten free voters for \((\alpha,\beta)=(2,1)\).

Run `python verify.py` in the extracted directory using Python 3 standard library; the finite rational checks cover six integral parameter pairs and up to 28 free voters, plus exact transition and cutoff checks. Expected output: `PASS: 444 exact rational checks; A8=2/3, A10=15/22`. This is a finite consistency check, not an exhaustion of continuous parameters or an independent audit. No external validation is asserted.

The result depends on the **strict** majority convention and the beta-binomial stationary mixture. A randomly awarded tied vote would change the even-size formulas. The related 1993 Berg original was not fully accessible for priority inspection; its odd-size result is credited and no claim that its full text excludes an even-size theorem is made.
