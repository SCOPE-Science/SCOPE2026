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

# Reproducibility notes

Run `python greenwood_max_check.py` using Python 3 and its standard library. The checker evaluates exact rational beta integrals from inclusion–exclusion, moment identities and the closed covariance for all integers \(m=2,\ldots,160\). No sample simulation is used to establish the all-dimension theorem. The complete analytical proof is in `RESULT.md`.

The program should print `PASS: 159 exact rational checks, m=2,...,160`. The included `verification_output.txt` is the output from an actual execution of the embedded script. An independent normalized-exponential Monte Carlo experiment, using seed `20261023`, checked \(m=2,5,10,30\) and found discrepancies within two estimated Monte Carlo standard errors; this experiment is supplementary and is not an exhaustive proof.

Historical priority has not undergone independent assessment. Publisher access to one relevant 1965 survey was unavailable. No independent audit or external proof certification is asserted.
