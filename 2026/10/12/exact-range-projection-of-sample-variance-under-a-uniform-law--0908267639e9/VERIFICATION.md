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

The theorem is proved for every integer \(n\ge2\) by conditioning on the minimum and maximum, reducing the symmetric variance calculation to independent uniform interior points, and then applying exact beta moments for the normalized range.

`checker.py` uses only the Python standard library and exact rational arithmetic. For every integer \(2\le n\le250\), it checks the normalized conditional moment calculation, the four beta moments needed in the proof, unbiasedness of the range projection, the exact range variance, the exact sample-variance variance, the covariance, the squared correlation, the projected-estimator variance, the variance ratio, and the strict-improvement factorization.

`CHECKER_OUTPUT.txt` records successful completion of 3,486 exact assertions. These finite checks are consistency tests; they are not used to infer the all-\(n\) theorem.

The verification does not establish UMVU status, admissibility among all estimators, or any extension beyond iid continuous-uniform sampling.
