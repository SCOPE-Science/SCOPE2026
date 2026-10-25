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

# Reproducible verification

Run `python verify.py` in the same directory as `requirements.txt`. The routine uses exact rational symbolic integration to evaluate the polynomial coefficient \(I=-5/96\), compares the closed logarithmic formula with two independent adaptive integrals for nine odd side counts, checks all nonthreshold discrete grid counts for odd orders from three through forty-three, and checks the strict central-rectangle inequality on a rational grid. It checks independent direct density-convolution integrations for four side counts and compares the scaled signed discrepancies with the predicted \(5\pi^4/192\) limit.

During preparation, the script executed successfully and ended with `PASS: exact convolution coefficient, phase counts, independent quadrature and limits`.

The full mathematical argument is in `RESULT.md`. Checks at finitely many numerical side counts do not establish claims for all integers; the exact symbolic coefficient check does not establish the rectangle inequality over its full continuous domain. Both unlimited steps are proved analytically in `RESULT.md`. No independent audit has been conducted.
