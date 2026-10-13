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
# Reproducibility

Execute `python3 geometric_verify.py` in a folder containing the accompanying `geometric_verify.py` and this result. Python 3 standard-library exact rational arithmetic is sufficient. Reproduced output:

`VERIFY_OK log_coeff_exact=16830 generating_coeff_exact=144 positive_cubic_certificate=True`

The finite grid includes positive rational \(q\) and integer sample sizes, independently computes the first coefficients of the order-statistic distribution, and checks the exact cubic-polynomial identity. It is a consistency test only. The theorem for all \(0<q<1\) and all positive integers \(m\) follows from the analytic proof and the count-law Lévy–Khintchine criterion, not from the finite program.
