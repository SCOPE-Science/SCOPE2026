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
# Reproducibility and limits

Run `python3 verify.py` using Python 3 and the standard library. The script checks seventeen specified intensities between \(0.01\) and \(100\). For each, it obtains \(a\) and \(b\) from independent Poisson-mass convolutions, verifies the strict inequalities \(b>\lambda c^3\), \(c<(1+2\lambda)^{-1/2}\), and \(Q_\lambda(c^2)>0\), and checks the exact dispersion-index expression against independently computed minimum/maximum mass functions and their moments. Successful execution ends with `VERIFIED 17 intensity points`.

The analytic proof, not the finite numerical checks, establishes all positive intensities. It uses exact Poisson size bias, the standard Skellam formula, strict conditional Jensen for a beta-gamma factorization, modified-Bessel derivative recurrences, and the impossibility of a first zero with positive derivative. The endpoint claims follow from Bessel series and standard large-argument expansions. There is no claim of independent verification or external certification.
