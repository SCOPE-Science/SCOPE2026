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

`python3 check.py` uses only the Python standard library and performs exact rational arithmetic. It checks 108 basic finite-field overlap identities and the construction of 12 lines in four mutually unbiased bases. It verifies the exact ranks and spectra at degrees zero through two, checks the three rational spectral projectors and their ranks, and reproduces every eigenvalue and condition-number entry and the sharp global frame endpoints for degrees three through sixteen. Its JSON output is recorded in `exact_table.json`.

The proof's infinite step is independent of the computation: the Legendre integral bound implies that for every degree \(q\ge17\), the normalized three-sector eigenvalues lie within \(31/[2(q+1)]\) of one; thus the Gram condition number is at most \(67/5\), strictly below the degree-five extremum. The finite exact table together with this analytic tail covers every nonnegative integer degree.

These checks do not establish independent mathematical validation, independent verification of publication priority, or applicability to sampling designs other than the stated twelve rays.
