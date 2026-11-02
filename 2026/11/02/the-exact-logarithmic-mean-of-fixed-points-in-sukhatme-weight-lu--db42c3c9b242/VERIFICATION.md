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

Run `python verify.py` from the directory containing the files. The script uses Python standard-library rational arithmetic to enumerate all draw-order probabilities and a separate exceedance-polynomial integral, checking exact equality for sizes \(1\) through \(7\). It also compares two finite formulas for the Bernoulli integrand at four positive time points for sizes \(1\) through \(8\). The included `verification-output.txt` records **39 passing finite checks** and seeded Monte Carlo diagnostic averages; those averages are not confidence intervals or a proof.

The infinite statement is established in the written proof by Fourier smoothing and dominated convergence. The script does not certify asymptotics, uniqueness, historical priority, or any distributional limit.
